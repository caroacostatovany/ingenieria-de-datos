# Apache Airflow: El Estándar de la Industria

Apache Airflow es el orquestador de workflows más popular para Data Engineering. Aprende los conceptos básicos y cómo usarlo.

---

## 🧠 ¿Qué es Airflow?

Apache Airflow es una plataforma para:
* **Programar** workflows de datos
* **Orquestar** tareas complejas con dependencias
* **Monitorear** ejecuciones en tiempo real
* **Escalar** a múltiples workers

**Características:**
* **El más popular**: Estándar de la industria
* **Muy maduro**: Probado en producción a gran escala
* **Gran ecosistema**: Muchos plugins y integraciones
* **Comunidad grande**: Muchos recursos y soporte

> Airflow es como un cron job inteligente con dependencias, retry y monitoreo. Es la opción segura y probada para producción.

---

## 🚀 Instalación

```bash
# Instalación básica
pip install apache-airflow

# Con PostgreSQL
pip install apache-airflow[postgres]

# Con providers comunes
pip install apache-airflow-providers-postgres
pip install apache-airflow-providers-aws
```

### Setup inicial

```bash
# Inicializar base de datos
airflow db init

# Crear usuario admin
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com \
    --password admin

# Iniciar webserver
airflow webserver --port 8080

# Iniciar scheduler (en otra terminal)
airflow scheduler
```

---

## 📊 Conceptos clave

### DAG (Directed Acyclic Graph)

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

### Tasks y Operators

```python
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

def mi_funcion():
    print("Ejecutando tarea")

tarea = PythonOperator(
    task_id='mi_tarea',
    python_callable=mi_funcion,
    dag=dag
)
```

---

## 🎯 Ejemplo completo

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

default_args = {
    'owner': 'data_engineer',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'pipeline_etl',
    default_args=default_args,
    description='Pipeline ETL',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False
)

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

tarea_extraer >> tarea_transformar >> tarea_cargar
```

---

## 🔗 Dependencias

```python
# Sintaxis >>
tarea_a >> tarea_b >> tarea_c

# Múltiples
tarea_a >> [tarea_b, tarea_c] >> tarea_d
```

---

## 📅 Scheduling

```python
# Diario
schedule_interval='@daily'

# Cada hora
schedule_interval='@hourly'

# Cron
schedule_interval='0 0 * * *'  # Medianoche diario
```

---

## 💡 Ventajas de Airflow

### 1. Maduro y probado

* Usado en producción por miles de empresas
* Comunidad muy grande
* Muchos recursos disponibles

### 2. Gran ecosistema

* Muchos providers (AWS, GCP, Azure, etc.)
* Plugins para casi todo
* Integraciones con servicios comunes

### 3. UI completa

* Monitoreo en tiempo real
* Logs detallados
* Visualización de DAGs
* Gestión de conexiones y variables

---

## ⚠️ Desventajas

### 1. Curva de aprendizaje

* Conceptos nuevos (DAGs, Operators)
* Configuración inicial más compleja
* Requiere entender scheduling

### 2. Overhead

* Requiere base de datos
* Necesita scheduler corriendo
* Más recursos que soluciones simples

---

## 🎯 Cuándo usar Airflow

✅ **Usa Airflow cuando:**
* Necesitas orquestación compleja
* Tienes múltiples pipelines
* Necesitas programación avanzada
* Quieres estándar de industria

❌ **No uses Airflow cuando:**
* Pipeline muy simple
* Solo necesitas ejecutar ocasionalmente
* No tienes infraestructura para gestionarlo

---

## 🚀 Alternativas gestionadas

Si no quieres gestionar Airflow:

* **Google Cloud Composer**: Airflow gestionado en GCP
* **AWS MWAA**: Airflow gestionado en AWS
* **Astronomer**: Plataforma gestionada de Airflow

---

## 🎯 Ejercicios

1. Instala Airflow localmente
2. Crea tu primer DAG
3. Configura dependencias entre tareas
4. Explora la UI de Airflow

---

## 🎯 Ejercicios

1. Instala Airflow localmente
2. Crea tu primer DAG
3. Configura dependencias entre tareas
4. Explora la UI de Airflow

---

## 🚀 Próximos pasos

* **Operators avanzados**: DockerOperator, KubernetesPodOperator
* **XComs**: Pasar datos entre tareas
* **Hooks**: Conectar con servicios externos
* **Plugins**: Crear funcionalidad custom

---

> **Recuerda**: Airflow es poderoso pero tiene overhead. Úsalo cuando necesites sus capacidades avanzadas. Para empezar, considera primero **[Prefect](prefect.md)** o **[Dagster](dagster.md)** que son más simples.
