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
df = pd.read_csv('datos.csv')
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

1. Crea un DataFrame con datos de usuarios
2. Filtra usuarios mayores de 30 años
3. Calcula la edad promedio por ciudad
4. Agrega una columna que indique si el usuario es "Mayor" o "Joven"

---

## 🚀 Siguiente paso

Continúa con **[Operaciones con DataFrames](02-operaciones-dataframes.md)**.
