# Proyecto 3: Pipeline con Airflow Local

Configura Apache Airflow localmente y crea tu primer DAG.

---

## 🎯 Objetivo

Aprender a:
* Instalar y configurar Airflow localmente
* Crear DAGs
* Programar ejecuciones
* Monitorear pipelines

---

## 📋 Requisitos previos

* Python 3.8+
* Docker (opcional pero recomendado)

---

## 🚀 Pasos del proyecto

### 1. Instalar Airflow

```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate

# Instalar Airflow
pip install apache-airflow

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
```

### 2. Crear DAG

`dags/pipeline_etl.py`:

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def extract():
    print("Extrayendo datos...")

def transform():
    print("Transformando datos...")

def load():
    print("Cargando datos...")

default_args = {
    'owner': 'data_engineer',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'pipeline_etl',
    default_args=default_args,
    description='Pipeline ETL simple',
    schedule_interval=timedelta(days=1),
    catchup=False,
)

extract_task = PythonOperator(
    task_id='extract',
    python_callable=extract,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform',
    python_callable=transform,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load',
    python_callable=load,
    dag=dag,
)

extract_task >> transform_task >> load_task
```

### 3. Ejecutar Airflow

```bash
# Iniciar scheduler
airflow scheduler

# En otra terminal, iniciar webserver
airflow webserver
```

Accede a `http://localhost:8080` con usuario `admin` y password `admin`.

---

## ✅ Checklist

- [ ] Airflow instalado y configurado
- [ ] DAG creado y funcionando
- [ ] Tareas ejecutándose correctamente
- [ ] Monitoreo funcionando

---

## 🚀 Próximo paso

Avanza a **[Proyecto 4: Pipeline con IA como Copiloto](../proyecto_04_ia_copiloto/)**.
