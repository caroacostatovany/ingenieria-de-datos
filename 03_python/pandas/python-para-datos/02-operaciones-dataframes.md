# Operaciones con DataFrames

Aprende a realizar operaciones avanzadas con pandas DataFrames: transformaciones, agrupaciones y combinación de DataFrames.

> 💡 **Usa el CSV de ejemplo**: `../data/ventas.csv` para practicar estos conceptos.

---

## 🔄 Transformaciones

### Aplicar funciones

```python
# Cargar datos
df = pd.read_csv('../data/ventas.csv')

# Aplicar función a columna (convertir a mayúsculas)
df['producto_upper'] = df['producto'].apply(str.upper)

# Aplicar función personalizada
def categorizar_precio(precio):
    if precio < 50:
        return 'Bajo'
    elif precio < 200:
        return 'Medio'
    else:
        return 'Alto'

df['categoria_precio'] = df['precio'].apply(categorizar_precio)
df[['producto', 'precio', 'categoria_precio']].head()
```

### Map y replace

```python
# Mapear valores (crear regiones desde ciudades)
mapeo_region = {
    'Madrid': 'Centro',
    'Barcelona': 'Este',
    'Valencia': 'Este',
    'Sevilla': 'Sur'
}
df['region'] = df['ciudad'].map(mapeo_region)
df[['ciudad', 'region']].head()

# Reemplazar valores específicos
df['categoria'] = df['categoria'].replace('Electrónica', 'Tecnología')
# O múltiples valores
df['categoria'] = df['categoria'].replace({
    'Tecnología': 'Electrónica',  # Revertir el cambio anterior
    'Ropa': 'Moda'
})
```

---

## 📊 Agrupaciones

### GROUP BY básico

```python
# Cargar datos
df = pd.read_csv('../data/ventas.csv')

# Agrupar y agregar (precio promedio por categoría)
df.groupby('categoria')['precio'].mean()

# Múltiples agregaciones
df.groupby('categoria').agg({
    'precio': ['mean', 'min', 'max'],
    'total': 'sum',
    'id': 'count'  # Número de productos
})

# Agrupar por múltiples columnas
df.groupby(['categoria', 'ciudad'])['total'].sum()
```

### Transform y filter

```python
# Transform: mantiene forma original (agrega columna con promedio por grupo)
df['precio_promedio_categoria'] = df.groupby('categoria')['precio'].transform('mean')
df[['producto', 'categoria', 'precio', 'precio_promedio_categoria']].head()

# Filter: filtra grupos (solo categorías con más de 5 productos)
df_filtrado = df.groupby('categoria').filter(lambda x: len(x) > 5)
print(f"Registros originales: {len(df)}")
print(f"Registros después de filtrar: {len(df_filtrado)}")
print(f"Categorías que quedaron: {df_filtrado['categoria'].unique()}")
```

---

## 🔗 Combinar DataFrames

### Concat

```python
# Cargar datos
df = pd.read_csv('../data/ventas.csv')

# Ejemplo: Dividir por categoría y luego concatenar
df_electronica = df[df['categoria'] == 'Electrónica'].copy()
df_ropa = df[df['categoria'] == 'Ropa'].copy()

# Concatenar verticalmente
df_combinado = pd.concat([df_electronica, df_ropa], ignore_index=True)
print(f"Total registros combinados: {len(df_combinado)}")

# Concatenar con diferentes columnas (rellena con NaN)
df1 = df[['id', 'producto', 'precio']].head(5)
df2 = df[['id', 'categoria', 'ciudad']].head(5)
df_concat = pd.concat([df1, df2], ignore_index=True)
df_concat
```

### Merge (JOIN)

```python
# Crear dos DataFrames relacionados para demostrar merge
# DataFrame 1: Información de productos
df_productos = df[['id', 'producto', 'categoria', 'precio']].copy()
df_productos = df_productos.drop_duplicates(subset=['producto']).reset_index(drop=True)
df_productos['producto_id'] = range(1, len(df_productos) + 1)

# DataFrame 2: Información de ventas (simulando que tenemos IDs diferentes)
df_ventas = df[['id', 'fecha', 'cantidad', 'total', 'ciudad']].copy()
df_ventas['producto_id'] = (df_ventas['id'] % len(df_productos)) + 1

# Inner join: Solo productos que tienen ventas
df_merged = pd.merge(df_productos, df_ventas, on='producto_id', how='inner')
print(f"Registros después de merge: {len(df_merged)}")
df_merged.head()

# Left join: Todos los productos, incluso sin ventas
df_merged_left = pd.merge(df_productos, df_ventas, on='producto_id', how='left')
print(f"Registros con left join: {len(df_merged_left)}")
print(f"Productos sin ventas: {df_merged_left['total'].isnull().sum()}")

# Múltiples columnas (si tuvieras claves compuestas)
# df_merged = pd.merge(df1, df2, on=['id', 'fecha'], how='inner')
```

---

## 🎯 Ejercicios

> 💡 **Usa el CSV de ejemplo**: `../data/ventas.csv` para practicar estos ejercicios.

### Ejercicio 1: Transformaciones

```python
# 1. Carga el CSV de ventas
df = pd.read_csv('../data/ventas.csv')

# 2. Crea una columna 'precio_con_iva' aplicando una función que multiplique precio * 1.21
# Tu código aquí

# 3. Crea una columna 'tipo_producto' que categorice:
#    - 'Premium' si precio > 200
#    - 'Estándar' si precio entre 50 y 200
#    - 'Económico' si precio < 50
# Tu código aquí

# 4. Usa map() para crear una columna 'region' desde 'ciudad':
#    Madrid, Sevilla → 'Centro-Sur'
#    Barcelona, Valencia → 'Este'
# Tu código aquí
```

### Ejercicio 2: Agrupaciones

```python
# 1. Agrupa por categoría y calcula:
#    - Precio promedio
#    - Total de ventas (suma de 'total')
#    - Número de productos únicos
# Tu código aquí

# 2. Agrupa por ciudad y categoría, calcula el total de ventas
# Tu código aquí

# 3. Usa transform() para agregar una columna con el precio promedio por categoría
# Tu código aquí

# 4. Usa filter() para mantener solo ciudades con más de 3 ventas
# Tu código aquí
```

### Ejercicio 3: Combinar DataFrames

```python
# 1. Divide el DataFrame en dos:
#    - df1: productos de 'Electrónica'
#    - df2: productos de 'Ropa' y 'Hogar'
# Tu código aquí

# 2. Concatena ambos DataFrames
# Tu código aquí

# 3. Crea dos DataFrames relacionados:
#    - df_productos: id, producto, categoria, precio (sin duplicados)
#    - df_ventas: id, fecha, cantidad, total
# Tu código aquí

# 4. Haz un merge (left join) de df_productos con df_ventas
# Tu código aquí
```

### Ejercicio 4: Operaciones combinadas

```python
# 1. Carga los datos
df = pd.read_csv('../data/ventas.csv')

# 2. Crea un resumen que muestre:
#    - Por cada categoría:
#      * Precio promedio
#      * Precio máximo y mínimo
#      * Total de ventas
#      * Número de productos únicos
#      * Número de ciudades donde se vende
# Tu código aquí

# 3. Agrega una columna que indique si el precio está por encima o debajo del promedio de su categoría
# Tu código aquí

# 4. Filtra productos que:
#    - Están en la categoría con más ventas
#    - Y tienen precio mayor al promedio de esa categoría
# Tu código aquí
```

> 💡 **¿Quieres ver ejemplos de cómo resolver estos ejercicios?** Revisa el notebook de ejemplo: **[02-operaciones-dataframes.ipynb](../../ejemplos/02-operaciones-dataframes.ipynb)** que muestra estas técnicas aplicadas al CSV de ventas.

---

## 🚀 Siguiente paso

Continúa con **[Limpieza de datos](03-limpieza-datos.md)**.
