"""
Primer DAG de Airflow: Pipeline ETL simple
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

# Obtener la ruta base del proyecto (3 niveles arriba desde este archivo)
BASE_DIR = Path(__file__).parent.parent.parent.parent

# Argumentos por defecto para el DAG
default_args = {
    'owner': 'data_engineer',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Definir el DAG
dag = DAG(
    'primer_pipeline_etl',
    default_args=default_args,
    description='Primer pipeline ETL con Airflow',
    schedule='@daily',  # Ejecutar diariamente (Airflow 3.0+ usa 'schedule' en lugar de 'schedule_interval')
    catchup=False,  # No ejecutar fechas pasadas
    tags=['etl', 'principiante'],
)

# Función para extraer datos
def extraer(**context):
    """Extrae datos del CSV de ventas."""
    print("📥 Extrayendo datos...")
    ruta_entrada = BASE_DIR / '03_python' / 'data' / 'ventas.csv'
    df = pd.read_csv(ruta_entrada)
    print(f"✅ Extraídas {len(df)} filas")
    return df.to_dict('records')  # Retornar como lista de diccionarios para XCom

# Función para transformar datos
def transformar(**context):
    """Transforma los datos extraídos."""
    print("🔄 Transformando datos...")
    
    # Obtener datos de la tarea anterior usando XCom
    ti = context['ti']
    datos = ti.xcom_pull(task_ids='extraer')
    
    # Convertir de vuelta a DataFrame
    df = pd.DataFrame(datos)
    
    # Transformaciones
    df = df.dropna()
    df['total'] = df['precio'] * df['cantidad']
    
    print(f"✅ Transformadas {len(df)} filas")
    return df.to_dict('records')

# Función para cargar datos
def cargar(**context):
    """Carga los datos transformados."""
    print("💾 Cargando datos...")
    
    # Obtener datos de la tarea anterior
    ti = context['ti']
    datos = ti.xcom_pull(task_ids='transformar')
    
    # Convertir a DataFrame
    df = pd.DataFrame(datos)
    
    # Guardar output en 05_pipelines/data/output
    ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'ventas_airflow.parquet'
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(ruta_salida, index=False)
    
    print(f"✅ Datos guardados en {ruta_salida}")
    print(f"   Total de registros: {len(df)}")
    print(f"   Total ingresos: ${df['total'].sum():,.2f}")

# Definir las tareas
tarea_extraer = PythonOperator(
    task_id='extraer',
    python_callable=extraer,
    dag=dag,
)

tarea_transformar = PythonOperator(
    task_id='transformar',
    python_callable=transformar,
    dag=dag,
)

tarea_cargar = PythonOperator(
    task_id='cargar',
    python_callable=cargar,
    dag=dag,
)

# Definir dependencias: extraer -> transformar -> cargar
tarea_extraer >> tarea_transformar >> tarea_cargar
