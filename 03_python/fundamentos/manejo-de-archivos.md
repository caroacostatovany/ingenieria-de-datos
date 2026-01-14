# Manejo de archivos en Python

Aprende a leer y escribir diferentes formatos de archivos comunes en Data Engineering: CSV, Parquet, JSON, Excel y más.

> 💡 **Usa los archivos de ejemplo**: `../data/ventas.csv` y `../data/ventas.parquet` para practicar estos conceptos.

---

## 📄 CSV

### Leer CSV

```python
import pandas as pd

# Cargar datos de ejemplo
df = pd.read_csv('../data/ventas.csv')
print(f"✅ Datos cargados: {len(df)} registros")
df.head()

# Con opciones avanzadas
df = pd.read_csv(
    '../data/ventas.csv',
    sep=',',                    # Separador
    encoding='utf-8',          # Codificación
    header=0,                   # Fila de encabezados
    # skiprows=1,               # Saltar filas (si fuera necesario)
    # nrows=1000,               # Leer solo N filas
    usecols=['producto', 'precio', 'total'],  # Solo estas columnas
    dtype={'precio': 'float32'},  # Tipos específicos
    na_values=['NULL', 'N/A']   # Valores a tratar como nulos
)
print(f"Columnas seleccionadas: {df.columns.tolist()}")
```

### Escribir CSV

```python
# Básico
df.to_csv('../data/ventas_copia.csv', index=False)

# Con opciones
df.to_csv(
    '../data/ventas_formateado.csv',
    index=False,                # No incluir índice
    sep=',',                    # Separador
    encoding='utf-8',           # Codificación
    float_format='%.2f',        # Formato de números (2 decimales)
    columns=['producto', 'precio', 'total']  # Solo estas columnas
)

print("✅ CSV guardado exitosamente")
```

---

## 📋 JSON

JSON es común para APIs y intercambio de datos web.

### Leer JSON

```python
# Cargar CSV y convertir a JSON primero (para el ejemplo)
df = pd.read_csv('../data/ventas.csv')
df.to_json('../data/ventas.json', orient='records', index=False)

# Leer JSON desde archivo
df_json = pd.read_json('../data/ventas.json')
print(f"✅ JSON cargado: {len(df_json)} registros")
df_json.head()

# Desde string (si tienes JSON como string)
import json
with open('../data/ventas.json', 'r') as f:
    data = json.load(f)
df_from_string = pd.DataFrame(data)

# JSON anidado (si fuera necesario)
# df = pd.json_normalize(data)  # Aplana estructuras anidadas
```

### Escribir JSON

```python
# Cargar datos
df = pd.read_csv('../data/ventas.csv')

# Escribir JSON con diferentes orientaciones
df.to_json('../data/ventas_records.json', orient='records', index=False)  # Lista de objetos
df.to_json('../data/ventas_index.json', orient='index', index=True)      # Índice como clave
df.to_json('../data/ventas_values.json', orient='values', index=False)    # Solo valores

print("✅ JSONs guardados con diferentes orientaciones")

# Comparar tamaños
import os
size_records = os.path.getsize('../data/ventas_records.json')
print(f"Tamaño (records): {size_records:,} bytes ({size_records/1024:.2f} KB)")
```

---

## 🗄️ Parquet

Parquet es un formato columnar optimizado para analytics. Es el formato preferido para datos procesados en Data Engineering.

> 💡 **Instalación**: Necesitas `pyarrow` o `fastparquet`: `pip install pyarrow`

### Leer Parquet

```python
import pandas as pd
import time

# Cargar datos de ejemplo en Parquet
start = time.time()
df_parquet = pd.read_parquet('../data/ventas.parquet')
time_parquet = time.time() - start

print(f"✅ Parquet cargado: {len(df_parquet)} registros en {time_parquet:.4f}s")
df_parquet.head()

# Comparar velocidad con CSV
start = time.time()
df_csv = pd.read_csv('../data/ventas.csv')
time_csv = time.time() - start

print(f"\n📊 Comparación de velocidad:")
print(f"CSV: {time_csv:.4f}s")
print(f"Parquet: {time_parquet:.4f}s")
print(f"Parquet es {time_csv/time_parquet:.2f}x más rápido")

# Con opciones avanzadas
df = pd.read_parquet(
    '../data/ventas.parquet',
    engine='pyarrow',           # o 'fastparquet'
    columns=['producto', 'precio', 'total'],  # Solo estas columnas
    # filters=[('fecha', '>=', '2024-01-01')]  # Filtros pushdown (si fecha fuera columna)
)
```

### Escribir Parquet

```python
# Leer CSV primero
df = pd.read_csv('../data/ventas.csv')

# Convertir a Parquet (básico)
df.to_parquet('../data/ventas_convertido.parquet', index=False)

# Con opciones avanzadas
df.to_parquet(
    '../data/ventas_optimizado.parquet',
    engine='pyarrow',
    compression='snappy',       # Compresión (snappy, gzip, brotli)
    index=False,
    # partition_cols=['categoria']  # Particionar por columna (para datasets grandes)
)

print("✅ Parquet guardado exitosamente")

# Comparar tamaños
import os
size_csv = os.path.getsize('../data/ventas.csv')
size_parquet = os.path.getsize('../data/ventas_optimizado.parquet')

print(f"\n📊 Comparación de tamaños:")
print(f"CSV: {size_csv:,} bytes ({size_csv/1024:.2f} KB)")
print(f"Parquet: {size_parquet:,} bytes ({size_parquet/1024:.2f} KB)")
print(f"Parquet es {size_csv/size_parquet:.2f}x más pequeño")
```

**Ventajas de Parquet:**
* ✅ **Más rápido** que CSV (formato columnar)
* ✅ **Menor tamaño** (compresión eficiente)
* ✅ **Preserva tipos de datos** automáticamente
* ✅ **Soporta particionamiento** (ideal para datasets grandes)
* ✅ **Filtros pushdown** (lee solo lo necesario)

---

## 🗃️ Excel

### Leer Excel

```python
# Básico
df = pd.read_excel('datos.xlsx')

# Múltiples hojas
df1 = pd.read_excel('datos.xlsx', sheet_name='Hoja1')
df2 = pd.read_excel('datos.xlsx', sheet_name='Hoja2')

# Todas las hojas
all_sheets = pd.read_excel('datos.xlsx', sheet_name=None)
# Retorna diccionario: {'Hoja1': df1, 'Hoja2': df2}
```

### Escribir Excel

```python
# Básico
df.to_excel('salida.xlsx', index=False)

# Múltiples hojas
with pd.ExcelWriter('salida.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Hoja1', index=False)
    df2.to_excel(writer, sheet_name='Hoja2', index=False)
```

---

## 🌐 APIs

### requests básico

```python
import requests
import pandas as pd

# GET request
response = requests.get('https://api.ejemplo.com/datos')
data = response.json()
df = pd.DataFrame(data)

# Con autenticación
headers = {'Authorization': 'Bearer token'}
response = requests.get('https://api.ejemplo.com/datos', headers=headers)

# POST request
payload = {'param1': 'value1', 'param2': 'value2'}
response = requests.post('https://api.ejemplo.com/datos', json=payload)
```

### Paginación

```python
def obtener_todos_los_datos(url):
    """Obtiene todos los datos de una API paginada."""
    todos_datos = []
    pagina = 1
    
    while True:
        response = requests.get(f'{url}?page={pagina}')
        datos = response.json()
        
        if not datos:  # No hay más datos
            break
            
        todos_datos.extend(datos)
        pagina += 1
    
    return pd.DataFrame(todos_datos)
```

---

## 💾 Bases de datos

### SQL con pandas

```python
from sqlalchemy import create_engine
import pandas as pd

# Conectar
engine = create_engine('postgresql://user:pass@localhost/db')

# Leer
df = pd.read_sql('SELECT * FROM usuarios', engine)

# Leer con parámetros
df = pd.read_sql(
    'SELECT * FROM ventas WHERE fecha >= :fecha',
    engine,
    params={'fecha': '2024-01-01'}
)

# Escribir
df.to_sql(
    'usuarios_nuevos',
    engine,
    if_exists='append',  # 'replace', 'append', 'fail'
    index=False
)
```

---

## 🔄 Procesar archivos grandes

### Chunking (procesar por partes)

```python
# Procesar CSV grande en chunks
chunk_size = 10000
chunks = []

for chunk in pd.read_csv('datos_grandes.csv', chunksize=chunk_size):
    # Procesar cada chunk
    chunk_procesado = chunk[chunk['edad'] > 25]
    chunks.append(chunk_procesado)

# Combinar resultados
df_final = pd.concat(chunks, ignore_index=True)
```

### Filtros pushdown

```python
# Parquet permite filtros pushdown (más eficiente)
df = pd.read_parquet(
    'datos.parquet',
    filters=[('fecha', '>=', '2024-01-01')]
)
```

---

## 💡 Buenas prácticas

### 1. Especifica tipos al leer

```python
# ✅ Mejor rendimiento y memoria
df = pd.read_csv('datos.csv', dtype={
    'id': 'int32',
    'precio': 'float32',
    'nombre': 'string'
})
```

### 2. Usa Parquet para datos intermedios

```python
# ✅ Parquet es mejor para datos procesados
df.to_parquet('datos_procesados.parquet')

# ⚠️ CSV solo para intercambio
df.to_csv('datos_finales.csv')
```

### 3. Maneja errores

```python
def leer_archivo_seguro(ruta):
    """Lee un archivo con manejo de errores."""
    try:
        if ruta.endswith('.csv'):
            return pd.read_csv(ruta)
        elif ruta.endswith('.parquet'):
            return pd.read_parquet(ruta)
        elif ruta.endswith('.json'):
            return pd.read_json(ruta)
        else:
            raise ValueError(f"Formato no soportado: {ruta}")
    except FileNotFoundError:
        print(f"Archivo {ruta} no encontrado")
        return None
    except Exception as e:
        print(f"Error leyendo {ruta}: {e}")
        return None
```

---

## 🎯 Ejercicios

> 💡 **Usa los archivos de ejemplo**: `../data/ventas.csv` y `../data/ventas.parquet` para practicar estos ejercicios.

### Ejercicio 1: Leer y comparar CSV vs Parquet

```python
# 1. Lee el CSV de ventas
# Tu código aquí

# 2. Lee el Parquet de ventas
# Tu código aquí

# 3. Compara el tiempo de lectura de ambos
# Tu código aquí

# 4. Compara el tamaño en disco de ambos archivos
# Tu código aquí
```

### Ejercicio 2: Convertir entre formatos

```python
# 1. Lee el CSV de ventas
# Tu código aquí

# 2. Conviértelo a Parquet con compresión 'snappy'
# Tu código aquí

# 3. Conviértelo a JSON (orient='records')
# Tu código aquí

# 4. Compara los tamaños de los tres archivos
# Tu código aquí
```

### Ejercicio 3: Leer con opciones

```python
# 1. Lee solo las columnas 'producto', 'precio', 'total' del CSV
# Tu código aquí

# 2. Lee el Parquet especificando solo las columnas 'categoria' y 'ciudad'
# Tu código aquí

# 3. Lee el CSV especificando tipos de datos (precio como float32)
# Tu código aquí
```

### Ejercicio 4: Procesar archivos grandes (simulado)

```python
# 1. Lee el CSV en chunks de 10 filas (simulando archivo grande)
# Tu código aquí

# 2. Procesa cada chunk: filtra ventas con total > 500
# Tu código aquí

# 3. Combina todos los chunks procesados
# Tu código aquí

# 4. Guarda el resultado en Parquet
# Tu código aquí
```

### Ejercicio 5: Análisis completo

```python
# 1. Lee el CSV de ventas
# Tu código aquí

# 2. Realiza un análisis (ej: ventas por categoría)
# Tu código aquí

# 3. Guarda el resultado en múltiples formatos:
#    - CSV (para intercambio)
#    - Parquet (para uso interno)
#    - JSON (para APIs)
# Tu código aquí

# 4. Compara tamaños y tiempos de lectura de los tres formatos
# Tu código aquí
```

> 💡 **¿Quieres ver ejemplos de cómo resolver estos ejercicios?** Revisa el notebook de ejemplo: **[07-manejo-archivos.ipynb](../../ejemplos/07-manejo-archivos.ipynb)** que muestra estas técnicas aplicadas a los archivos de ejemplo.

---

## 🚀 Próximo paso

Continúa con **[Scripts vs Módulos](scripts-vs-modulos.md)** para aprender cuándo usar scripts simples y cuándo modularizar código para proyectos más grandes.
