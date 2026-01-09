# Pipelines con Python

Aprende a construir pipelines robustos usando Python puro, sin necesidad de orquestadores complejos al inicio.

---

## 🧠 ¿Por qué Python para pipelines?

**Ventajas:**
* **Flexibilidad**: Control total sobre el proceso
* **Librerías**: pandas, requests, sqlalchemy, etc.
* **Fácil de testear**: Tests unitarios estándar
* **Portable**: Funciona en cualquier entorno
* **Escalable**: Puede evolucionar a orquestadores

> Empieza simple con Python. Escala a orquestadores cuando lo necesites.

---

## 🏗️ Estructura básica de un pipeline

### Patrón ETL simple

```python
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract(ruta_entrada):
    """Extrae datos de una fuente."""
    logger.info(f"Extrayendo datos de {ruta_entrada}")
    try:
        df = pd.read_csv(ruta_entrada)
        logger.info(f"Extraídos {len(df)} registros")
        return df
    except Exception as e:
        logger.error(f"Error en extracción: {e}")
        raise

def transform(df):
    """Transforma los datos."""
    logger.info("Transformando datos...")
    try:
        # Limpiar
        df = df.dropna()
        df = df.drop_duplicates()
        
        # Transformar
        df['total'] = df['precio'] * df['cantidad']
        df['fecha'] = pd.to_datetime(df['fecha'])
        
        logger.info(f"Transformados {len(df)} registros")
        return df
    except Exception as e:
        logger.error(f"Error en transformación: {e}")
        raise

def load(df, ruta_salida):
    """Carga datos al destino."""
    logger.info(f"Cargando datos a {ruta_salida}")
    try:
        df.to_parquet(ruta_salida, index=False)
        logger.info("Carga completada exitosamente")
    except Exception as e:
        logger.error(f"Error en carga: {e}")
        raise

def run_pipeline(ruta_entrada, ruta_salida):
    """Ejecuta el pipeline completo."""
    logger.info("Iniciando pipeline...")
    try:
        df = extract(ruta_entrada)
        df = transform(df)
        load(df, ruta_salida)
        logger.info("✅ Pipeline completado exitosamente")
    except Exception as e:
        logger.error(f"❌ Pipeline falló: {e}")
        raise

if __name__ == '__main__':
    run_pipeline('data/raw/ventas.csv', 'data/processed/ventas.parquet')
```

---

## 🔄 Pipeline con múltiples fuentes

```python
def extract_multiple(fuentes):
    """Extrae datos de múltiples fuentes."""
    datos = {}
    
    for nombre, config in fuentes.items():
        tipo = config['tipo']
        ruta = config['ruta']
        
        if tipo == 'csv':
            datos[nombre] = pd.read_csv(ruta)
        elif tipo == 'json':
            datos[nombre] = pd.read_json(ruta)
        elif tipo == 'parquet':
            datos[nombre] = pd.read_parquet(ruta)
        elif tipo == 'api':
            import requests
            response = requests.get(ruta)
            datos[nombre] = pd.DataFrame(response.json())
    
    return datos

def transform_multiple(datos):
    """Transforma múltiples fuentes."""
    # Combinar datos
    df_ventas = datos['ventas']
    df_productos = datos['productos']
    
    # Merge
    df_completo = pd.merge(
        df_ventas,
        df_productos,
        on='producto_id',
        how='left'
    )
    
    # Transformar
    df_completo['total'] = df_completo['precio'] * df_completo['cantidad']
    
    return df_completo

def run_pipeline_multiple(fuentes, ruta_salida):
    """Pipeline con múltiples fuentes."""
    datos = extract_multiple(fuentes)
    df_final = transform_multiple(datos)
    load(df_final, ruta_salida)

# Uso
fuentes = {
    'ventas': {'tipo': 'csv', 'ruta': 'data/raw/ventas.csv'},
    'productos': {'tipo': 'json', 'ruta': 'data/raw/productos.json'}
}

run_pipeline_multiple(fuentes, 'data/processed/ventas_completas.parquet')
```

---

## 🛡️ Manejo de errores robusto

```python
import traceback
from datetime import datetime

def run_pipeline_with_error_handling(ruta_entrada, ruta_salida):
    """Pipeline con manejo robusto de errores."""
    inicio = datetime.now()
    
    try:
        # Extract
        try:
            df = extract(ruta_entrada)
        except FileNotFoundError:
            logger.error(f"Archivo no encontrado: {ruta_entrada}")
            raise
        except Exception as e:
            logger.error(f"Error en extracción: {e}")
            logger.error(traceback.format_exc())
            raise
        
        # Transform
        try:
            df = transform(df)
        except Exception as e:
            logger.error(f"Error en transformación: {e}")
            logger.error(traceback.format_exc())
            # Guardar datos parciales para debugging
            df.to_csv('data/error/partial_data.csv', index=False)
            raise
        
        # Load
        try:
            load(df, ruta_salida)
        except Exception as e:
            logger.error(f"Error en carga: {e}")
            logger.error(traceback.format_exc())
            raise
        
        # Éxito
        duracion = (datetime.now() - inicio).total_seconds()
        logger.info(f"Pipeline completado en {duracion:.2f} segundos")
        
    except Exception as e:
        # Notificar fallo
        logger.critical(f"Pipeline falló completamente: {e}")
        # Opcional: enviar alerta (email, Slack, etc.)
        raise
```

---

## 📊 Pipeline con validaciones

```python
def validar_entrada(df):
    """Valida datos de entrada."""
    errores = []
    
    # Verificar columnas
    columnas_requeridas = ['id', 'nombre', 'precio', 'cantidad']
    faltantes = set(columnas_requeridas) - set(df.columns)
    if faltantes:
        errores.append(f"Columnas faltantes: {faltantes}")
    
    # Verificar nulos en columnas críticas
    if 'id' in df.columns:
        nulos = df['id'].isnull().sum()
        if nulos > 0:
            errores.append(f"IDs nulos: {nulos}")
    
    # Verificar rangos
    if 'precio' in df.columns:
        negativos = df[df['precio'] < 0]
        if len(negativos) > 0:
            errores.append(f"Precios negativos: {len(negativos)}")
    
    if errores:
        raise ValueError("Errores de validación:\n" + "\n".join(errores))
    
    return True

def run_pipeline_con_validacion(ruta_entrada, ruta_salida):
    """Pipeline con validaciones."""
    df = extract(ruta_entrada)
    validar_entrada(df)  # Validar antes de procesar
    df = transform(df)
    load(df, ruta_salida)
```

---

## 🔄 Pipeline con dependencias

```python
def pipeline_con_dependencias():
    """Pipeline donde pasos dependen de anteriores."""
    
    # Paso 1: Extraer usuarios
    df_usuarios = extract('data/raw/usuarios.csv')
    
    # Paso 2: Extraer ventas (depende de usuarios para validar)
    df_ventas = extract('data/raw/ventas.csv')
    
    # Validar que usuarios de ventas existan
    usuarios_validos = set(df_usuarios['id'].unique())
    ventas_invalidas = df_ventas[~df_ventas['usuario_id'].isin(usuarios_validos)]
    
    if len(ventas_invalidas) > 0:
        logger.warning(f"Ventas con usuarios inválidos: {len(ventas_invalidas)}")
        df_ventas = df_ventas[df_ventas['usuario_id'].isin(usuarios_validos)]
    
    # Paso 3: Transformar (depende de ambos)
    df_completo = pd.merge(df_ventas, df_usuarios, on='id', how='left')
    df_completo = transform(df_completo)
    
    # Paso 4: Cargar
    load(df_completo, 'data/processed/ventas_completas.parquet')
```

---

## 📦 Estructura de proyecto

```
proyecto_pipeline/
├── src/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
├── data/
│   ├── raw/
│   └── processed/
├── logs/
├── config/
│   └── settings.py
├── main.py
└── requirements.txt
```

### Ejemplo modular

```python
# src/extract.py
def extract_csv(ruta):
    return pd.read_csv(ruta)

def extract_api(url):
    import requests
    response = requests.get(url)
    return pd.DataFrame(response.json())

# src/transform.py
def limpiar_datos(df):
    return df.dropna().drop_duplicates()

def calcular_totales(df):
    df['total'] = df['precio'] * df['cantidad']
    return df

# main.py
from src.extract import extract_csv
from src.transform import limpiar_datos, calcular_totales
from src.load import load_parquet

def run_pipeline():
    df = extract_csv('data/raw/ventas.csv')
    df = limpiar_datos(df)
    df = calcular_totales(df)
    load_parquet(df, 'data/processed/ventas.parquet')
```

---

## 🧪 Testing de pipelines

```python
import pytest
import pandas as pd

def test_extract():
    """Test de extracción."""
    df = extract('tests/fixtures/sample.csv')
    assert len(df) > 0
    assert 'id' in df.columns

def test_transform():
    """Test de transformación."""
    df = pd.DataFrame({
        'precio': [10, 20],
        'cantidad': [2, 3]
    })
    df = transform(df)
    assert 'total' in df.columns
    assert df['total'].tolist() == [20, 60]

def test_pipeline_completo():
    """Test end-to-end."""
    run_pipeline('tests/fixtures/sample.csv', 'tests/output/result.parquet')
    
    # Verificar que archivo existe
    import os
    assert os.path.exists('tests/output/result.parquet')
    
    # Verificar contenido
    df = pd.read_parquet('tests/output/result.parquet')
    assert len(df) > 0
```

---

## 💡 Buenas prácticas

### 1. Logging consistente

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/pipeline.log'),
        logging.StreamHandler()
    ]
)
```

### 2. Configuración externa

```python
# config/settings.py
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
API_KEY = os.getenv('API_KEY')
INPUT_PATH = os.getenv('INPUT_PATH', 'data/raw')
OUTPUT_PATH = os.getenv('OUTPUT_PATH', 'data/processed')
```

### 3. Idempotencia

```python
def load_idempotente(df, ruta_salida):
    """Carga que puede ejecutarse múltiples veces."""
    # Verificar si ya existe
    if os.path.exists(ruta_salida):
        logger.warning(f"Archivo {ruta_salida} ya existe. Sobrescribiendo...")
    
    df.to_parquet(ruta_salida, index=False)
```

---

## 🎯 Ejercicios

1. Crea un pipeline ETL simple con Python
2. Agrega validaciones y manejo de errores
3. Estructura un proyecto de pipeline modular
4. Escribe tests para tu pipeline

---

## 🚀 Próximo paso

Cuando tu pipeline crezca, considera usar un orquestador. Revisa **[Orquestadores](orquestadores/)** para opciones.

---

> **Recuerda**: Empieza simple con Python. Escala a orquestadores cuando necesites programación, monitoreo avanzado o dependencias complejas.
