# Introducción a Apache Airflow

Apache Airflow es el orquestador de workflows más popular para Data Engineering. Aprende los conceptos básicos.

---

## 🧠 ¿Qué es Airflow?

Apache Airflow es una plataforma para:
* **Programar** workflows de datos
* **Orquestar** tareas complejas con dependencias
* **Monitorear** ejecuciones en tiempo real
* **Escalar** a múltiples workers

> Airflow es como un cron job inteligente con dependencias, retry y monitoreo.

---

## 📊 Conceptos clave

### DAG (Directed Acyclic Graph)

Un DAG es un workflow: conjunto de tareas con dependencias.

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

dag = DAG(
    'mi_pipeline',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily'
)
```

### Tasks (Tareas)

Cada paso del pipeline es una tarea.

```python
def extraer_datos():
    # Tu código aquí
    pass

tarea_extraer = PythonOperator(
    task_id='extraer_datos',
    python_callable=extraer_datos,
    dag=dag
)
```

### Operators (Operadores)

Tipos de tareas predefinidas.

* `PythonOperator`: Ejecuta función Python
* `BashOperator`: Ejecuta comando bash
* `SqlOperator`: Ejecuta SQL
* `DockerOperator`: Ejecuta contenedor Docker

---

## 🚀 Primer DAG

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def extraer():
    print("Extrayendo datos...")

def transformar():
    print("Transformando datos...")

def cargar():
    print("Cargando datos...")

# Definir DAG
default_args = {
    'owner': 'data_engineer',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'pipeline_etl',
    default_args=default_args,
    description='Pipeline ETL simple',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False
)

# Definir tareas
tarea_extraer = PythonOperator(
    task_id='extraer',
    python_callable=extraer,
    dag=dag
)

tarea_transformar = PythonOperator(
    task_id='transformar',
    python_callable=transformar,
    dag=dag
)

tarea_cargar = PythonOperator(
    task_id='cargar',
    python_callable=cargar,
    dag=dag
)

# Definir dependencias
tarea_extraer >> tarea_transformar >> tarea_cargar
```

---

## 🔗 Dependencias

### Sintaxis de dependencias

```python
# Usando >>
tarea_a >> tarea_b >> tarea_c

# Múltiples dependencias
tarea_a >> [tarea_b, tarea_c] >> tarea_d

# Usando set_downstream
tarea_a.set_downstream(tarea_b)
```

### Ejemplo complejo

```python
# Pipeline con ramificaciones
extraer_usuarios >> transformar_usuarios
extraer_ventas >> transformar_ventas

[transformar_usuarios, transformar_ventas] >> combinar_datos >> cargar
```

---

## 📅 Programación (Scheduling)

### Intervalos comunes

```python
# Diario
schedule_interval='@daily'

# Cada hora
schedule_interval='@hourly'

# Cada 15 minutos
schedule_interval='*/15 * * * *'

# Lunes a Viernes
schedule_interval='0 0 * * 1-5'

# Manual (solo ejecución manual)
schedule_interval=None
```

---

## 🔄 Retry y manejo de errores

```python
default_args = {
    'retries': 3,  # Reintentar 3 veces
    'retry_delay': timedelta(minutes=5),  # Esperar 5 min entre reintentos
    'email_on_failure': True,  # Enviar email si falla
    'email': ['team@example.com']
}

dag = DAG(
    'pipeline_robusto',
    default_args=default_args,
    # ...
)
```

---

## 💡 Buenas prácticas

### 1. Idempotencia

```python
def extraer_datos(**context):
    """Extrae datos de forma idempotente."""
    fecha = context['ds']  # Fecha de ejecución
    
    # Solo extraer si no existe
    ruta = f'data/raw/{fecha}.csv'
    if not os.path.exists(ruta):
        # Extraer datos
        pass
```

### 2. Variables y Connections

```python
from airflow.models import Variable
from airflow.hooks.base import BaseHook

# Variables
api_key = Variable.get("api_key")

# Connections
conn = BaseHook.get_connection('postgres_default')
db_url = f"postgresql://{conn.login}:{conn.password}@{conn.host}/{conn.schema}"
```

### 3. XComs para pasar datos

```python
def extraer(**context):
    datos = "datos extraídos"
    return datos  # Se guarda en XCom

def transformar(**context):
    ti = context['ti']
    datos = ti.xcom_pull(task_ids='extraer')  # Obtener datos
    # Transformar
    return "datos transformados"
```

---

## 🎯 Ejercicios

1. Crea tu primer DAG en Airflow
2. Define dependencias entre tareas
3. Configura retry y manejo de errores
4. Programa un DAG para ejecutarse diariamente

---

## 🚀 Próximos pasos

Para más detalles sobre Airflow, revisa:
* **[Orquestadores - Airflow](orquestadores/airflow.md)** para guía completa
* **[Orquestadores - Comparación](orquestadores/README.md)** para comparar opciones

---

> **Recuerda**: Airflow es poderoso pero tiene curva de aprendizaje. Empieza con DAGs simples y evoluciona gradualmente.
