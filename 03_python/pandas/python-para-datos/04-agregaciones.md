# Agregaciones y agrupaciones

Aprende a resumir y agrupar datos con pandas usando agregaciones, groupby y pivot tables.

> 💡 **Usa el CSV de ejemplo**: `../data/ventas.csv` para practicar estos conceptos.

---

## 📊 Agregaciones básicas

```python
# Cargar datos
df = pd.read_csv('../data/ventas.csv')

# Agregaciones simples en una columna numérica
print(f"Total de ventas: €{df['total'].sum():,.2f}")
print(f"Precio promedio: €{df['precio'].mean():,.2f}")
print(f"Precio mediano: €{df['precio'].median():,.2f}")
print(f"Desviación estándar: €{df['precio'].std():,.2f}")
print(f"Precio mínimo: €{df['precio'].min():,.2f}")
print(f"Precio máximo: €{df['precio'].max():,.2f}")
print(f"Total de registros: {df['id'].count()}")
```

### Múltiples agregaciones

```python
# Todas las agregaciones numéricas automáticas
print("=== ESTADÍSTICAS DESCRIPTIVAS ===")
print(df.describe())

# Agregaciones personalizadas con agg()
print("\n=== AGREGACIONES PERSONALIZADAS ===")
agregaciones = df.agg({
    'precio': ['mean', 'min', 'max', 'std'],
    'total': ['sum', 'mean'],
    'cantidad': 'sum'
})
print(agregaciones)
```

---

## 📦 GROUP BY

### Agrupación básica

```python
# Cargar datos
df = pd.read_csv('../data/ventas.csv')

# Agrupar por ciudad y calcular promedio de precio
print("=== PRECIO PROMEDIO POR CIUDAD ===")
precio_por_ciudad = df.groupby('ciudad')['precio'].mean()
print(precio_por_ciudad)

# Agrupar por categoría y calcular total de ventas
print("\n=== TOTAL DE VENTAS POR CATEGORÍA ===")
total_por_categoria = df.groupby('categoria')['total'].sum()
print(total_por_categoria)

# Múltiples columnas: ciudad y categoría
print("\n=== PRECIO PROMEDIO POR CIUDAD Y CATEGORÍA ===")
precio_ciudad_cat = df.groupby(['ciudad', 'categoria'])['precio'].mean()
print(precio_ciudad_cat)
```

### Múltiples funciones

```python
# Diferentes funciones por columna
print("=== ESTADÍSTICAS POR CIUDAD ===")
estadisticas_ciudad = df.groupby('ciudad').agg({
    'precio': ['mean', 'min', 'max'],
    'total': 'sum',
    'id': 'count'  # Número de ventas
})
print(estadisticas_ciudad)

# Estadísticas por categoría
print("\n=== ESTADÍSTICAS POR CATEGORÍA ===")
estadisticas_categoria = df.groupby('categoria').agg({
    'precio': ['mean', 'min', 'max', 'std'],
    'total': ['sum', 'mean'],
    'cantidad': 'sum'
})
print(estadisticas_categoria)
```

### Named aggregations

```python
# Con nombres personalizados (más legible)
print("=== RESUMEN POR CIUDAD (NAMED AGGREGATIONS) ===")
resumen_ciudad = df.groupby('ciudad').agg(
    precio_promedio=('precio', 'mean'),
    total_ventas=('total', 'sum'),
    num_transacciones=('id', 'count'),
    cantidad_total=('cantidad', 'sum')
)
print(resumen_ciudad)

# Resumen por categoría
print("\n=== RESUMEN POR CATEGORÍA ===")
resumen_categoria = df.groupby('categoria').agg(
    precio_promedio=('precio', 'mean'),
    precio_maximo=('precio', 'max'),
    total_ingresos=('total', 'sum'),
    productos_unicos=('producto', 'nunique')
)
print(resumen_categoria)
```

---

## 🔄 Pivot tables

Las tablas pivot te permiten reorganizar y resumir datos de forma más visual.

```python
# Cargar datos
df = pd.read_csv('../data/ventas.csv')

# Crear tabla pivot: precio promedio por ciudad y categoría
print("=== PRECIO PROMEDIO: CIUDAD (filas) × CATEGORÍA (columnas) ===")
pivot_precio = df.pivot_table(
    values='precio',
    index='ciudad',
    columns='categoria',
    aggfunc='mean'
)
print(pivot_precio)

# Tabla pivot con total de ventas
print("\n=== TOTAL DE VENTAS: CIUDAD × CATEGORÍA ===")
pivot_total = df.pivot_table(
    values='total',
    index='ciudad',
    columns='categoria',
    aggfunc='sum',
    fill_value=0  # Rellenar con 0 si no hay datos
)
print(pivot_total)

# Tabla pivot con múltiples funciones
print("\n=== MÚLTIPLES FUNCIONES: CIUDAD × CATEGORÍA ===")
pivot_multi = df.pivot_table(
    values='total',
    index='ciudad',
    columns='categoria',
    aggfunc=['sum', 'mean', 'count'],
    fill_value=0
)
print(pivot_multi)

# Tabla pivot con fechas (agrupar por mes)
df['fecha'] = pd.to_datetime(df['fecha'])
df['mes'] = df['fecha'].dt.to_period('M')
print("\n=== VENTAS POR MES Y CATEGORÍA ===")
pivot_mes = df.pivot_table(
    values='total',
    index='mes',
    columns='categoria',
    aggfunc='sum',
    fill_value=0
)
print(pivot_mes)
```

---

## 🎯 Ejercicios

> 💡 **Usa el CSV de ejemplo**: `../data/ventas.csv` para practicar estos ejercicios.

### Ejercicio 1: Agregaciones básicas

```python
# 1. Carga el CSV de ventas
df = pd.read_csv('../data/ventas.csv')

# 2. Calcula las siguientes métricas:
#    - Total de ingresos (suma de 'total')
#    - Precio promedio, mínimo y máximo
#    - Cantidad total de productos vendidos
#    - Número de transacciones
# Tu código aquí

# 3. Usa describe() para ver estadísticas de todas las columnas numéricas
# Tu código aquí
```

### Ejercicio 2: Agrupaciones básicas

```python
# 1. Agrupa por categoría y calcula:
#    - Precio promedio
#    - Total de ventas
#    - Número de productos únicos
# Tu código aquí

# 2. Agrupa por ciudad y calcula:
#    - Total de ingresos
#    - Número de transacciones
#    - Cantidad total vendida
# Tu código aquí

# 3. Agrupa por ciudad Y categoría, calcula el total de ventas
# Tu código aquí
```

### Ejercicio 3: Agregaciones múltiples y named aggregations

```python
# 1. Usa agg() para calcular por ciudad:
#    - Precio: mean, min, max
#    - Total: sum, mean
#    - Cantidad: sum
# Tu código aquí

# 2. Usa named aggregations para crear un resumen por categoría con nombres claros:
#    - precio_promedio
#    - total_ingresos
#    - num_productos
#    - cantidad_total
# Tu código aquí
```

### Ejercicio 4: Pivot tables

```python
# 1. Convierte 'fecha' a datetime y crea una columna 'mes'
# Tu código aquí

# 2. Crea una tabla pivot que muestre:
#    - Filas: mes
#    - Columnas: categoría
#    - Valores: total de ventas (suma)
# Tu código aquí

# 3. Crea otra tabla pivot:
#    - Filas: ciudad
#    - Columnas: categoría
#    - Valores: precio promedio
# Tu código aquí
```

### Ejercicio 5: Top N por categoría

```python
# 1. Encuentra los 3 productos más vendidos por categoría (usando cantidad)
#    Pista: groupby + sort_values + head()
# Tu código aquí

# 2. Encuentra las 3 ciudades con mayores ingresos
# Tu código aquí

# 3. Encuentra el mes con mayores ventas
# Tu código aquí
```

> 💡 **¿Quieres ver ejemplos de cómo resolver estos ejercicios?** Revisa el notebook de ejemplo: **[05-agregaciones.ipynb](../../ejemplos/05-agregaciones.ipynb)** que muestra estas técnicas aplicadas al CSV de ventas.

---

## 🚀 Siguiente paso

Continúa con **[Merge y Join](05-merge-join.md)**.
