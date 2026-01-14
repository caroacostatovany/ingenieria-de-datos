# Scripts vs Módulos

Entender cuándo usar scripts simples y cuándo modularizar código es clave para escribir Python mantenible.

> 💡 **Nota**: Este documento es para referencia futura. Por ahora, trabajaremos solo con **Jupyter Notebooks** para aprender Python. Los scripts Python los veremos más adelante cuando construyamos pipelines automatizados.

---

## 📜 Scripts simples

Un **script** es un archivo Python que se ejecuta directamente.

### Cuándo usar scripts

✅ **Usa scripts cuando:**
* Tarea única y específica
* No necesitas reutilizar código
* Ejecución rápida y directa
* Prototipos o exploración

### Ejemplo de script

```python
# script_simple.py
import pandas as pd

# Leer datos
df = pd.read_csv('datos.csv')

# Procesar
df['total'] = df['precio'] * df['cantidad']

# Guardar
df.to_csv('resultado.csv', index=False)

print("Procesamiento completado")
```

**Ejecución:**
```bash
python script_simple.py
```

---

## 📦 Módulos

Un **módulo** es código organizado en funciones/clases reutilizables.

### Cuándo modularizar

✅ **Modulariza cuando:**
* Código se reutiliza en múltiples lugares
* Proyecto crece y necesita organización
* Múltiples personas trabajan en el código
* Necesitas testing

### Estructura de módulo

```python
# utils/data_processing.py
"""Utilidades para procesamiento de datos."""

import pandas as pd

def limpiar_datos(df):
    """Limpia un DataFrame."""
    df = df.dropna()
    df = df.drop_duplicates()
    return df

def calcular_totales(df):
    """Calcula totales por categoría."""
    return df.groupby('categoria')['precio'].sum()

def guardar_resultado(df, ruta):
    """Guarda DataFrame en Parquet."""
    df.to_parquet(ruta, index=False)
```

**Uso:**
```python
# main.py
from utils.data_processing import limpiar_datos, calcular_totales

df = pd.read_csv('datos.csv')
df_limpio = limpiar_datos(df)
totales = calcular_totales(df_limpio)
```

---

## 🏗️ Estructura de proyectos

### Estructura recomendada

```
proyecto/
├── src/
│   ├── __init__.py
│   ├── extract.py      # Extracción de datos
│   ├── transform.py    # Transformaciones
│   └── load.py         # Carga de datos
├── utils/
│   ├── __init__.py
│   └── helpers.py      # Funciones auxiliares
├── config/
│   └── settings.py     # Configuración
├── tests/
│   └── test_extract.py
├── data/
│   ├── raw/
│   └── processed/
├── main.py             # Script principal
└── requirements.txt
```

### Ejemplo completo

```python
# src/extract.py
"""Módulo para extraer datos."""
import pandas as pd
import requests

def extraer_de_csv(ruta):
    """Extrae datos de CSV."""
    return pd.read_csv(ruta)

def extraer_de_api(url):
    """Extrae datos de API."""
    response = requests.get(url)
    return pd.DataFrame(response.json())

# src/transform.py
"""Módulo para transformar datos."""
def limpiar_datos(df):
    """Limpia datos."""
    return df.dropna().drop_duplicates()

def calcular_metricas(df):
    """Calcula métricas."""
    return df.groupby('categoria').agg({
        'precio': ['mean', 'sum']
    })

# main.py
"""Script principal del pipeline."""
from src.extract import extraer_de_csv
from src.transform import limpiar_datos, calcular_metricas

# Pipeline
df = extraer_de_csv('data/raw/datos.csv')
df_limpio = limpiar_datos(df)
metricas = calcular_metricas(df_limpio)
metricas.to_csv('data/processed/metricas.csv')
```

---

## 🔄 Reutilización de código

### Funciones reutilizables

```python
# utils/validations.py
"""Validaciones de datos."""

def validar_schema(df, schema_esperado):
    """Valida que el DataFrame tenga el schema esperado."""
    columnas_esperadas = set(schema_esperado.keys())
    columnas_actuales = set(df.columns)
    
    if columnas_esperadas != columnas_actuales:
        raise ValueError(f"Columnas esperadas: {columnas_esperadas}, actuales: {columnas_actuales}")
    
    # Validar tipos
    for col, tipo in schema_esperado.items():
        if df[col].dtype != tipo:
            raise ValueError(f"Columna {col} debe ser {tipo}, es {df[col].dtype}")
    
    return True
```

### Clases para lógica compleja

```python
# src/pipeline.py
"""Clase para pipeline de datos."""

class DataPipeline:
    def __init__(self, config):
        self.config = config
    
    def extract(self):
        """Extrae datos."""
        # Lógica de extracción
        pass
    
    def transform(self, df):
        """Transforma datos."""
        # Lógica de transformación
        pass
    
    def load(self, df):
        """Carga datos."""
        # Lógica de carga
        pass
    
    def run(self):
        """Ejecuta el pipeline completo."""
        df = self.extract()
        df = self.transform(df)
        self.load(df)
```

---

## 💡 Buenas prácticas

### 1. Separa lógica de ejecución

```python
# ✅ Bueno: lógica en función
def procesar_datos(ruta_entrada, ruta_salida):
    df = pd.read_csv(ruta_entrada)
    df = limpiar_datos(df)
    df.to_csv(ruta_salida, index=False)

# Script solo llama la función
if __name__ == '__main__':
    procesar_datos('input.csv', 'output.csv')
```

### 2. Usa `if __name__ == '__main__'`

```python
# utils/helpers.py
def funcion_util():
    """Función reutilizable."""
    pass

# Solo se ejecuta si es el script principal
if __name__ == '__main__':
    # Código de prueba o ejecución
    funcion_util()
```

### 3. Documenta funciones

```python
def procesar_ventas(df, fecha_inicio, fecha_fin):
    """
    Procesa ventas en un rango de fechas.
    
    Args:
        df (pd.DataFrame): DataFrame con ventas
        fecha_inicio (str): Fecha inicio (YYYY-MM-DD)
        fecha_fin (str): Fecha fin (YYYY-MM-DD)
    
    Returns:
        pd.DataFrame: Ventas procesadas
    """
    # Código aquí
    pass
```

---

## 🎯 Ejercicios

1. Convierte un script simple en módulos reutilizables
2. Crea una estructura de proyecto para un pipeline ETL
3. Escribe funciones que puedan ser testeadas
4. Organiza código en clases cuando sea apropiado

---

## 🚀 Próximo paso

Revisa los **[Ejemplos](ejemplos/)** para ver patrones comunes.

---

> **Recuerda**: Empieza simple con scripts. Modulariza cuando el código crece o necesitas reutilización.
