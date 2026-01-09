# Prefect: Orquestador Moderno

Prefect es un orquestador moderno diseñado para Data Engineering, con enfoque en Python y facilidad de uso.

---

## 🧠 ¿Qué es Prefect?

Prefect es un orquestador que:
* **Es Python-first**: Diseñado para Python desde el inicio
* **Es fácil de empezar**: Funciona localmente sin configuración compleja
* **Escala a producción**: Puede usar Prefect Cloud o servidor propio
* **Tiene UI moderna**: Interfaz web intuitiva

> Prefect es como Airflow, pero más fácil de usar y más Python-friendly.

---

## 🚀 Instalación

```bash
# Instalación básica
pip install prefect

# Con dependencias adicionales
pip install prefect[sql,aws,gcp,azure]
```

---

## 📊 Conceptos clave

### Flow (Flujo)

Un flow es tu pipeline. Es una función Python decorada.

```python
from prefect import flow

@flow
def mi_pipeline():
    print("Ejecutando pipeline...")
    # Tu lógica aquí
    return "completado"
```

### Task (Tarea)

Una tarea es una unidad de trabajo dentro del flow.

```python
from prefect import task

@task
def extraer_datos():
    return "datos extraídos"

@task
def transformar_datos(datos):
    return f"{datos} transformados"

@flow
def pipeline_etl():
    datos = extraer_datos()
    resultado = transformar_datos(datos)
    return resultado
```

---

## 🎯 Primer Flow

```python
from prefect import flow, task
import pandas as pd

@task
def extraer(ruta):
    """Extrae datos."""
    return pd.read_csv(ruta)

@task
def transformar(df):
    """Transforma datos."""
    df = df.dropna()
    df['total'] = df['precio'] * df['cantidad']
    return df

@task
def cargar(df, ruta):
    """Carga datos."""
    df.to_parquet(ruta, index=False)

@flow
def pipeline_etl(ruta_entrada, ruta_salida):
    """Pipeline ETL completo."""
    df = extraer(ruta_entrada)
    df = transformar(df)
    cargar(df, ruta_salida)
    print("✅ Pipeline completado")

# Ejecutar
if __name__ == '__main__':
    pipeline_etl('data/raw/ventas.csv', 'data/processed/ventas.parquet')
```

---

## 🔄 Dependencias

Las dependencias se manejan automáticamente por el orden de llamadas.

```python
@flow
def pipeline_con_dependencias():
    # Estas tareas se ejecutan en paralelo
    usuarios = extraer_usuarios()
    productos = extraer_productos()
    
    # Esta tarea espera a que ambas terminen
    resultado = combinar(usuarios, productos)
    
    # Esta tarea espera a combinar
    cargar(resultado)
```

---

## 📅 Programación (Scheduling)

### Con cron

```python
from prefect import flow
from prefect.schedules import CronSchedule

@flow(schedule=CronSchedule(cron="0 0 * * *"))  # Diario a medianoche
def pipeline_diario():
    # Tu pipeline
    pass
```

### Con intervalos

```python
from prefect.schedules import IntervalSchedule
from datetime import timedelta

@flow(schedule=IntervalSchedule(interval=timedelta(hours=1)))
def pipeline_horario():
    # Tu pipeline
    pass
```

---

## 🖥️ UI local

Prefect incluye una UI local para monitorear flows.

```bash
# Iniciar servidor Prefect
prefect server start

# Abrir en navegador
# http://localhost:4200
```

---

## 🔄 Retry y manejo de errores

```python
@task(retries=3, retry_delay_seconds=60)
def tarea_con_reintentos():
    # Esta tarea reintentará 3 veces si falla
    pass

@task
def tarea_que_puede_fallar():
    import random
    if random.random() < 0.5:
        raise Exception("Error aleatorio")
    return "éxito"
```

---

## 💾 Estado y resultados

Prefect guarda automáticamente el estado de cada ejecución.

```python
@flow
def pipeline_con_estado():
    resultado = procesar_datos()
    
    # Prefect guarda automáticamente:
    # - Estado de cada tarea
    # - Resultados
    # - Logs
    # - Tiempos de ejecución
    
    return resultado
```

---

## 🔗 Integración con servicios

### Base de datos

```python
from prefect_sqlalchemy import SqlAlchemyConnector

@task
def consultar_db():
    with SqlAlchemyConnector.load("postgres") as connector:
        df = pd.read_sql("SELECT * FROM ventas", connector.get_connection())
    return df
```

### Cloud Storage

```python
from prefect_aws import S3Bucket

@task
def leer_de_s3():
    s3_bucket = S3Bucket.load("my-bucket")
    return s3_bucket.read_path("data/raw/ventas.csv")
```

---

## 💡 Ventajas de Prefect

### 1. Python puro

```python
# No necesitas aprender DSL especial
# Es Python estándar
@flow
def mi_pipeline():
    # Código Python normal
    pass
```

### 2. Fácil de testear

```python
# Puedes testear flows como funciones normales
def test_pipeline():
    resultado = pipeline_etl('test_input.csv', 'test_output.parquet')
    assert resultado is not None
```

### 3. UI moderna

* Visualización de flows
* Monitoreo en tiempo real
* Logs integrados
* Historial de ejecuciones

---

## 🎯 Ejercicios

1. Instala Prefect y crea tu primer flow
2. Convierte un pipeline Python en un flow de Prefect
3. Configura programación para un flow
4. Explora la UI de Prefect

---

## 🚀 Próximos pasos

* **Prefect Cloud**: Para producción sin gestionar servidor
* **Prefect Server**: Para auto-hospedaje
* **Blocks**: Para configuración reutilizable
* **Deployments**: Para desplegar flows a producción

---

> **Recuerda**: Prefect es excelente para empezar. Es simple localmente pero puede escalar a producción cuando lo necesites.
