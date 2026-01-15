"""
DAG con dependencias complejas: Tareas en paralelo y secuenciales
"""
from airflow import DAG
try:
    from airflow.providers.standard.operators.python import PythonOperator
except ImportError:
    # Fallback para versiones anteriores de Airflow
    from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd
import time

# Obtener la ruta base del proyecto
BASE_DIR = Path(__file__).parent.parent.parent.parent

default_args = {
    'owner': 'data_engineer',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'dependencias_complejas',
    default_args=default_args,
    description='DAG con tareas en paralelo y secuenciales',
    schedule=None,  # Sin programación, solo ejecución manual (Airflow 3.0+ usa 'schedule' en lugar de 'schedule_interval')
    catchup=False,
    tags=['dependencias', 'paralelo'],
)

# ============================================
# TAREAS QUE SE EJECUTAN EN PARALELO
# ============================================

def extraer_productos(**context):
    """Extrae productos (se ejecuta en paralelo con extraer_ventas)."""
    print("📥 Extrayendo productos...")
    time.sleep(2)  # Simular trabajo
    ruta = BASE_DIR / '03_python' / 'data' / 'productos.csv'
    df = pd.read_csv(ruta)
    print(f"✅ Extraídos {len(df)} productos")
    return df.to_dict('records')

def extraer_ventas(**context):
    """Extrae ventas (se ejecuta en paralelo con extraer_productos)."""
    print("📥 Extrayendo ventas...")
    time.sleep(2)  # Simular trabajo
    ruta = BASE_DIR / '03_python' / 'data' / 'ventas.csv'
    df = pd.read_csv(ruta)
    print(f"✅ Extraídas {len(df)} ventas")
    return df.to_dict('records')

# ============================================
# TAREAS SECUENCIALES
# ============================================

def procesar_productos(**context):
    """Procesa productos (depende de extraer_productos)."""
    print("🔄 Procesando productos...")
    ti = context['ti']
    datos = ti.xcom_pull(task_ids='extraer_productos')
    df = pd.DataFrame(datos)
    df = df.dropna()
    
    ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'productos_procesados_airflow.parquet'
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(ruta_salida, index=False)
    print(f"✅ Productos procesados guardados en {ruta_salida}")
    
    return df.to_dict('records')

def procesar_ventas(**context):
    """Procesa ventas (depende de extraer_ventas)."""
    print("🔄 Procesando ventas...")
    ti = context['ti']
    datos = ti.xcom_pull(task_ids='extraer_ventas')
    df = pd.DataFrame(datos)
    df = df.dropna()
    df['total'] = df['precio'] * df['cantidad']
    
    ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'ventas_procesadas_airflow.parquet'
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(ruta_salida, index=False)
    print(f"✅ Ventas procesadas guardadas en {ruta_salida}")
    
    return df.to_dict('records')

# ============================================
# TAREA QUE DEPENDE DE MÚLTIPLES TAREAS
# ============================================

def combinar_datos(**context):
    """Combina productos y ventas (depende de ambas tareas de procesamiento)."""
    print("🔗 Combinando productos y ventas...")
    ti = context['ti']
    
    productos = pd.DataFrame(ti.xcom_pull(task_ids='procesar_productos'))
    ventas = pd.DataFrame(ti.xcom_pull(task_ids='procesar_ventas'))
    
    # Merge
    df_completo = pd.merge(
        ventas,
        productos,
        left_on='producto_id',
        right_on='id',
        how='left',
        suffixes=('_venta', '_producto')
    )
    
    ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'datos_combinados_airflow.parquet'
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    df_completo.to_parquet(ruta_salida, index=False)
    
    print(f"✅ Datos combinados guardados en {ruta_salida}")
    print(f"   Total de registros: {len(df_completo)}")

# Definir tareas
tarea_extraer_productos = PythonOperator(
    task_id='extraer_productos',
    python_callable=extraer_productos,
    dag=dag,
)

tarea_extraer_ventas = PythonOperator(
    task_id='extraer_ventas',
    python_callable=extraer_ventas,
    dag=dag,
)

tarea_procesar_productos = PythonOperator(
    task_id='procesar_productos',
    python_callable=procesar_productos,
    dag=dag,
)

tarea_procesar_ventas = PythonOperator(
    task_id='procesar_ventas',
    python_callable=procesar_ventas,
    dag=dag,
)

tarea_combinar = PythonOperator(
    task_id='combinar_datos',
    python_callable=combinar_datos,
    dag=dag,
)

# Definir dependencias:
# - extraer_productos y extraer_ventas se ejecutan en paralelo
# - procesar_productos depende de extraer_productos
# - procesar_ventas depende de extraer_ventas
# - combinar_datos depende de ambas tareas de procesamiento
# Dependencias: extraer -> procesar -> combinar
try:
    from airflow.sdk.bases.operator import cross_downstream
except ImportError:
    # Fallback para versiones anteriores de Airflow
    from airflow.models.baseoperator import cross_downstream

# Todas las tareas de extraer deben completarse antes de procesar
cross_downstream([tarea_extraer_productos, tarea_extraer_ventas], [tarea_procesar_productos, tarea_procesar_ventas])

# Ambas tareas de procesar deben completarse antes de combinar
[tarea_procesar_productos, tarea_procesar_ventas] >> tarea_combinar
