# Introducción a Pandas

Pandas es la librería más importante de Python para Data Engineering. Te permite trabajar con datos estructurados de forma eficiente.

---

## 🧠 ¿Qué es Pandas?

Pandas proporciona estructuras de datos y herramientas para análisis de datos:

* **Series**: Array unidimensional etiquetado
* **DataFrame**: Tabla bidimensional (como Excel o SQL)
* **Operaciones eficientes**: Optimizado para grandes volúmenes

---

## 📊 Crear DataFrames

### Desde diccionario

```python
import pandas as pd

data = {
    'nombre': ['Juan', 'María', 'Carlos'],
    'edad': [28, 35, 42],
    'ciudad': ['Madrid', 'Barcelona', 'Valencia']
}

df = pd.DataFrame(data)
print(df)
```

### Desde lista de diccionarios

```python
usuarios = [
    {'nombre': 'Juan', 'edad': 28, 'ciudad': 'Madrid'},
    {'nombre': 'María', 'edad': 35, 'ciudad': 'Barcelona'},
    {'nombre': 'Carlos', 'edad': 42, 'ciudad': 'Valencia'}
]

df = pd.DataFrame(usuarios)
```

### Desde CSV

```python
# Cargar CSV de ejemplo del proyecto
df = pd.read_csv('../data/ventas.csv')

# O desde cualquier ruta
df = pd.read_csv('ruta/a/tu/archivo.csv')
```

---

## 🔍 Explorar datos

### Información básica

```python
# Primeras filas
df.head()        # 5 primeras (por defecto)
df.head(10)      # 10 primeras

# Últimas filas
df.tail()

# Información del DataFrame
df.info()        # Tipos, memoria, nulos

# Estadísticas descriptivas
df.describe()    # Solo columnas numéricas

# Forma del DataFrame
df.shape         # (filas, columnas)

# Nombres de columnas
df.columns

# Tipos de datos
df.dtypes
```

### Seleccionar columnas

```python
# Una columna (retorna Series)
df['nombre']

# Múltiples columnas (retorna DataFrame)
df[['nombre', 'edad']]

# Con punto (solo si el nombre no tiene espacios)
df.nombre
```

### Filtrar filas

```python
# Por condición
df[df['edad'] > 30]

# Múltiples condiciones
df[(df['edad'] > 30) & (df['ciudad'] == 'Madrid')]

# Con query (más legible)
df.query('edad > 30 and ciudad == "Madrid"')
```

---

## ✏️ Modificar datos

### Agregar columnas

```python
# Nueva columna
df['es_mayor'] = df['edad'] > 30

# Columna calculada
df['edad_doble'] = df['edad'] * 2

# Con apply
df['categoria_edad'] = df['edad'].apply(
    lambda x: 'Mayor' if x > 30 else 'Joven'
)
```

### Modificar valores

```python
# Cambiar valor específico
df.loc[0, 'nombre'] = 'Juan Pérez'

# Cambiar múltiples valores
df.loc[df['ciudad'] == 'Madrid', 'region'] = 'Centro'
```

### Eliminar columnas/filas

```python
# Eliminar columnas
df = df.drop('columna_no_necesaria', axis=1)
df = df.drop(['col1', 'col2'], axis=1)

# Eliminar filas
df = df.drop(0)  # Elimina fila con índice 0
df = df.drop([0, 1, 2])  # Elimina múltiples filas
```

---

## 📊 Operaciones básicas

### Ordenar

```python
# Por una columna
df.sort_values('edad')

# Descendente
df.sort_values('edad', ascending=False)

# Múltiples columnas
df.sort_values(['ciudad', 'edad'])
```

### Valores únicos

```python
# Valores únicos de una columna
df['ciudad'].unique()

# Contar valores únicos
df['ciudad'].nunique()

# Contar frecuencia
df['ciudad'].value_counts()
```

### Estadísticas básicas

```python
# Suma, promedio, etc.
df['edad'].sum()
df['edad'].mean()
df['edad'].median()
df['edad'].std()
df['edad'].min()
df['edad'].max()
```

---

## 💡 Buenas prácticas

### 1. Usa copy() cuando modifiques

```python
# ✅ Crea copia
df_nuevo = df.copy()
df_nuevo['nueva_col'] = 1

# ⚠️ Modifica original
df_nuevo = df
df_nuevo['nueva_col'] = 1  # También modifica df
```

### 2. Verifica datos antes de procesar

```python
# Verifica forma
print(f"Filas: {df.shape[0]}, Columnas: {df.shape[1]}")

# Verifica nulos
print(df.isnull().sum())

# Verifica duplicados
print(df.duplicated().sum())
```

### 3. Usa métodos vectorizados

```python
# ✅ Rápido (vectorizado)
df['edad_doble'] = df['edad'] * 2

# ⚠️ Lento (iteración)
df['edad_doble'] = df['edad'].apply(lambda x: x * 2)
```

---

## 🎯 Ejercicios

> 💡 **Usa el CSV de ejemplo**: `../data/ventas.csv` para practicar estos ejercicios.

### Ejercicio 1: Cargar y explorar datos

```python
# 1. Carga el CSV de ventas
df = pd.read_csv('../data/ventas.csv')

# 2. Muestra las primeras 10 filas
# Tu código aquí

# 3. Muestra información del DataFrame (tipos, memoria, nulos)
# Tu código aquí

# 4. Muestra estadísticas descriptivas
# Tu código aquí
```

### Ejercicio 2: Seleccionar y filtrar

```python
# 1. Selecciona solo las columnas: 'categoria', 'producto', 'precio'
# Tu código aquí

# 2. Filtra productos de la categoría 'Electrónica'
# Tu código aquí

# 3. Filtra ventas con precio mayor a 100 euros
# Tu código aquí

# 4. Filtra ventas de 'Electrónica' con precio mayor a 100 (ambas condiciones)
# Tu código aquí
```

### Ejercicio 3: Modificar datos

```python
# 1. Agrega una columna 'precio_con_iva' que sea precio * 1.21
# Tu código aquí

# 2. Agrega una columna 'categoria_precio' que indique:
#    - 'Alto' si precio > 200
#    - 'Medio' si precio entre 50 y 200
#    - 'Bajo' si precio < 50
# Tu código aquí

# 3. Muestra las primeras filas para verificar tus cambios
# Tu código aquí
```

### Ejercicio 4: Estadísticas y agrupaciones

```python
# 1. Calcula el precio promedio por categoría
# Tu código aquí

# 2. Calcula el total de ventas (suma de 'total') por ciudad
# Tu código aquí

# 3. Encuentra el producto más caro y el más barato
# Tu código aquí

# 4. Cuenta cuántos productos hay por categoría
# Tu código aquí
```

### Ejercicio 5: Ordenar y valores únicos

```python
# 1. Ordena el DataFrame por precio descendente
# Tu código aquí

# 2. Muestra los 5 productos más caros
# Tu código aquí

# 3. Lista todas las ciudades únicas donde hay ventas
# Tu código aquí

# 4. Cuenta cuántas ventas hay por ciudad (value_counts)
# Tu código aquí
```

### Ejercicio 6: Análisis completo

```python
# 1. Carga los datos
df = pd.read_csv('../data/ventas.csv')

# 2. Crea un resumen que muestre:
#    - Total de registros
#    - Precio promedio
#    - Precio máximo y mínimo
#    - Total de ventas (suma de columna 'total')
#    - Número de categorías únicas
#    - Número de ciudades únicas
# Tu código aquí

# 3. Filtra las ventas de Madrid y calcula el total de ingresos
# Tu código aquí

# 4. Encuentra la categoría con mayor número de ventas
# Tu código aquí
```

> 💡 **¿Quieres ver ejemplos de cómo resolver estos ejercicios?** Revisa el notebook de ejemplo: **[01-exploracion-datos.ipynb](../../ejemplos/01-exploracion-datos.ipynb)** que muestra técnicas similares aplicadas al CSV de ventas.

---

## 🚀 Siguiente paso

Continúa con **[Operaciones con DataFrames](02-operaciones-dataframes.md)**.
