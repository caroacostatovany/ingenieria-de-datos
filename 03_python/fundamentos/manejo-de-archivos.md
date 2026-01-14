# Manejo de archivos en Python

Aprende a leer y escribir diferentes formatos de archivos comunes en Data Engineering.

> 💡 **Trabajaremos con Jupyter Notebooks**: Todos los ejemplos de este documento están diseñados para ejecutarse en Jupyter Notebooks. Crea un nuevo notebook y ejecuta los ejemplos celda por celda.

---

## 📄 CSV

### Leer CSV

```python
import pandas as pd

# Básico
df = pd.read_csv('datos.csv')

# Con opciones
df = pd.read_csv(
    'datos.csv',
    sep=',',                    # Separador
    encoding='utf-8',          # Codificación
    header=0,                   # Fila de encabezados
    skiprows=1,                 # Saltar filas
    nrows=1000,                 # Leer solo N filas
    usecols=['col1', 'col2'],   # Solo estas columnas
    dtype={'col1': str},        # Tipos específicos
    na_values=['NULL', 'N/A']   # Valores a tratar como nulos
)
```

### Escribir CSV

```python
# Básico
df.to_csv('salida.csv', index=False)

# Con opciones
df.to_csv(
    'salida.csv',
    index=False,                # No incluir índice
    sep=',',                    # Separador
    encoding='utf-8',           # Codificación
    float_format='%.2f',        # Formato de números
    columns=['col1', 'col2']    # Solo estas columnas
)
```

---

## 📋 JSON

### Leer JSON

```python
# Desde archivo
df = pd.read_json('datos.json')

# Desde string
import json
with open('datos.json', 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data)

# JSON anidado
df = pd.json_normalize(data)  # Aplana estructuras anidadas
```

### Escribir JSON

```python
# Básico
df.to_json('salida.json', orient='records')

# Orientaciones comunes
df.to_json('salida.json', orient='records')      # Lista de objetos
df.to_json('salida.json', orient='index')        # Índice como clave
df.to_json('salida.json', orient='values')       # Solo valores
```

---

## 🗄️ Parquet

Parquet es un formato columnar optimizado para analytics.

### Leer Parquet

```python
# Básico
df = pd.read_parquet('datos.parquet')

# Con opciones
df = pd.read_parquet(
    'datos.parquet',
    engine='pyarrow',           # o 'fastparquet'
    columns=['col1', 'col2'],   # Solo estas columnas
    filters=[('fecha', '>=', '2024-01-01')]  # Filtros (pushdown)
)
```

### Escribir Parquet

```python
# Básico
df.to_parquet('salida.parquet', index=False)

# Con opciones
df.to_parquet(
    'salida.parquet',
    engine='pyarrow',
    compression='snappy',       # Compresión
    index=False,
    partition_cols=['fecha']    # Particionar por columna
)
```

**Ventajas de Parquet:**
* ✅ Más rápido que CSV
* ✅ Menor tamaño (compresión)
* ✅ Preserva tipos de datos
* ✅ Soporta particionamiento

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

1. Lee un CSV grande en chunks y procesa
2. Convierte datos de JSON a DataFrame
3. Lee datos de una API y guarda en Parquet
4. Escribe datos a múltiples formatos y compara tamaños

---

## 🚀 Próximo paso

Continúa con **[Scripts vs módulos](scripts-vs-modulos.md)**.
