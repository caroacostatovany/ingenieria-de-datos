# Dagster: Orquestador enfocado en Data Assets

Dagster es un orquestador que enfatiza los "data assets" (activos de datos) en lugar de solo tareas.

---

## 🧠 ¿Qué es Dagster?

Dagster es un orquestador que:
* **Enfoca en data assets**: Piensa en datos, no solo en tareas
* **Tiene UI excelente**: Interfaz moderna y clara
* **Es Python-first**: Diseñado para Python
* **Facilita desarrollo local**: Fácil de empezar

> Dagster te ayuda a pensar en qué datos produces, no solo en qué código ejecutas.

---

## 🚀 Instalación

```bash
# Instalación básica
pip install dagster dagit

# Con dependencias adicionales
pip install dagster[postgres,pandas]
```

---

## 📊 Conceptos clave

### Asset (Activo de datos)

Un asset es un dato que produces o consumes.

```python
from dagster import asset

@asset
def ventas_diarias():
    """Asset: ventas agregadas por día."""
    # Tu lógica aquí
    return df
```

### Op (Operación)

Una operación es una unidad de trabajo.

```python
from dagster import op

@op
def extraer_ventas():
    return "datos extraídos"
```

---

## 🎯 Primer Asset

```python
from dagster import asset, AssetExecutionContext
import pandas as pd

@asset
def ventas_raw(context: AssetExecutionContext):
    """Asset: datos de ventas sin procesar."""
    context.log.info("Extrayendo ventas...")
    df = pd.read_csv('data/raw/ventas.csv')
    context.log.info(f"Extraídas {len(df)} ventas")
    return df

@asset
def ventas_procesadas(context: AssetExecutionContext, ventas_raw):
    """Asset: ventas procesadas (depende de ventas_raw)."""
    context.log.info("Procesando ventas...")
    df = ventas_raw.copy()
    df = df.dropna()
    df['total'] = df['precio'] * df['cantidad']
    return df

@asset
def ventas_por_categoria(context: AssetExecutionContext, ventas_procesadas):
    """Asset: ventas agregadas por categoría."""
    context.log.info("Agregando por categoría...")
    return ventas_procesadas.groupby('categoria')['total'].sum()
```

---

## 🔄 Dependencias automáticas

Dagster detecta dependencias automáticamente por parámetros.

```python
@asset
def usuarios():
    return pd.read_csv('usuarios.csv')

@asset
def ventas():
    return pd.read_csv('ventas.csv')

@asset
def ventas_completas(usuarios, ventas):
    # Dagster sabe que ventas_completas depende de usuarios y ventas
    return pd.merge(ventas, usuarios, on='usuario_id')
```

---

## 🖥️ UI (Dagit)

Dagster incluye una UI excelente llamada Dagit.

```bash
# Iniciar Dagit
dagster dev

# Abrir en navegador
# http://localhost:3000
```

**Características de la UI:**
* Visualización de assets y dependencias
* Materialización de assets
* Logs y monitoreo
* Búsqueda y filtrado

---

## 📅 Programación

```python
from dagster import (
    asset,
    ScheduleDefinition,
    define_asset_job,
    AssetSelection
)

@asset
def ventas_diarias():
    # Tu lógica
    pass

# Definir job
ventas_job = define_asset_job(
    "procesar_ventas",
    selection=AssetSelection.assets(ventas_diarias)
)

# Definir schedule
ventas_schedule = ScheduleDefinition(
    job=ventas_job,
    cron_schedule="0 0 * * *"  # Diario
)
```

---

## 💡 Ventajas de Dagster

### 1. Enfoque en datos

```python
# Piensas en qué datos produces
@asset
def ventas_por_mes():
    # Este asset produce ventas_por_mes
    return df
```

### 2. UI excelente

* Visualización clara de dependencias
* Materialización de assets
* Historial de cambios

### 3. Desarrollo local fácil

```bash
# Iniciar y desarrollar
dagster dev
```

---

## 🎯 Ejercicios

1. Instala Dagster y crea tu primer asset
2. Define dependencias entre assets
3. Explora la UI de Dagster
4. Programa un job para ejecutarse regularmente

---

## 🚀 Próximos pasos

* **Materializaciones**: Ver qué assets están actualizados
* **Partitions**: Procesar datos por particiones
* **Resources**: Configuración reutilizable
* **I/O Managers**: Gestionar almacenamiento

---

> **Recuerda**: Dagster es excelente si piensas en términos de "qué datos produzco" en lugar de "qué código ejecuto".
