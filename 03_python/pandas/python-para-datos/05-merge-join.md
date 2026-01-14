# Merge y Join en Pandas

Combina múltiples DataFrames de forma similar a SQL JOINs. Aprende a enriquecer tus datos combinando información de diferentes fuentes.

> 💡 **Usa los CSVs de ejemplo**: `../data/ventas.csv` y `../data/productos.csv` para practicar estos conceptos.

---

## 🔗 Tipos de merge

### Inner join

```python
# Cargar datos
ventas = pd.read_csv('../data/ventas.csv')
productos = pd.read_csv('../data/productos.csv')

# Inner join: Solo filas que coinciden en ambas tablas
df_merged = pd.merge(ventas, productos, on='producto', how='inner')
print(f"Registros en ventas: {len(ventas)}")
print(f"Registros en productos: {len(productos)}")
print(f"Registros después de inner join: {len(df_merged)}")
df_merged.head()
```

### Left join

```python
# Left join: Todas las filas de la izquierda (ventas)
# Incluye ventas aunque no haya información del producto
df_left = pd.merge(ventas, productos, on='producto', how='left')
print(f"Registros después de left join: {len(df_left)}")
print(f"Ventas sin producto en catálogo: {df_left['stock'].isnull().sum()}")
df_left.head()
```

### Right join

```python
# Right join: Todas las filas de la derecha (productos)
# Incluye productos aunque no hayan tenido ventas
df_right = pd.merge(ventas, productos, on='producto', how='right')
print(f"Registros después de right join: {len(df_right)}")
print(f"Productos sin ventas: {df_right['id'].isnull().sum()}")
df_right.head()
```

### Outer join

```python
# Outer join: Todas las filas de ambas tablas
df_outer = pd.merge(ventas, productos, on='producto', how='outer')
print(f"Registros después de outer join: {len(df_outer)}")
print(f"Ventas sin producto: {df_outer['id'].notna() & df_outer['stock'].isna()}")
print(f"Productos sin ventas: {df_outer['id'].isna() & df_outer['stock'].notna()}")
```

---

## 🎯 Ejemplos prácticos

### Ejemplo 1: Combinar ventas con información de productos

```python
# Cargar datos
ventas = pd.read_csv('../data/ventas.csv')
productos = pd.read_csv('../data/productos.csv')

# Merge para enriquecer ventas con información de productos
ventas_completas = pd.merge(
    ventas, 
    productos[['producto', 'stock', 'proveedor', 'fecha_lanzamiento']], 
    on='producto', 
    how='left'
)

print("=== VENTAS CON INFORMACIÓN DE PRODUCTOS ===")
print(ventas_completas[['producto', 'total', 'stock', 'proveedor']].head())

# Análisis: productos con bajo stock y altas ventas
productos_riesgo = ventas_completas[
    (ventas_completas['stock'] < 20) & 
    (ventas_completas['total'] > 500)
]
print("\n=== PRODUCTOS CON BAJO STOCK Y ALTAS VENTAS ===")
print(productos_riesgo[['producto', 'total', 'stock', 'proveedor']])
```

### Ejemplo 2: Merge por múltiples columnas

```python
# Si necesitas combinar por producto Y categoría (aunque en este caso producto es único)
ventas = pd.read_csv('../data/ventas.csv')
productos = pd.read_csv('../data/productos.csv')

# Merge por múltiples columnas (útil cuando una sola columna no es única)
df_merged = pd.merge(
    ventas, 
    productos, 
    on=['producto', 'categoria'],  # Ambas deben coincidir
    how='inner'
)
print(f"Registros después de merge: {len(df_merged)}")
```

### Ejemplo 3: Sufijos para columnas duplicadas

```python
# Cuando hay columnas con el mismo nombre en ambas tablas
ventas = pd.read_csv('../data/ventas.csv')
productos = pd.read_csv('../data/productos.csv')

# Ambas tienen 'precio' y 'categoria', usamos sufijos
df_merged = pd.merge(
    ventas, 
    productos, 
    on='producto', 
    suffixes=('_venta', '_base'),  # precio_venta vs precio_base
    how='inner'
)

print("=== COLUMNAS CON SUFIJOS ===")
print(df_merged[['producto', 'precio_venta', 'precio_base', 'categoria_venta']].head())

# Comparar precio de venta vs precio base
df_merged['diferencia_precio'] = df_merged['precio_venta'] - df_merged['precio_base']
print("\n=== DIFERENCIA ENTRE PRECIO DE VENTA Y PRECIO BASE ===")
print(df_merged[['producto', 'precio_venta', 'precio_base', 'diferencia_precio']].head())
```

### Ejemplo 4: Merge con diferentes nombres de columnas

```python
# Cuando las columnas tienen nombres diferentes
ventas = pd.read_csv('../data/ventas.csv')
productos = pd.read_csv('../data/productos.csv')

# Si productos tuviera 'nombre_producto' en lugar de 'producto'
# productos.rename(columns={'nombre_producto': 'producto'}, inplace=True)

# O usar left_on y right_on
df_merged = pd.merge(
    ventas,
    productos,
    left_on='producto',      # Columna en ventas
    right_on='producto',     # Columna en productos (en este caso es igual)
    how='left'
)
```

---

## 💡 Buenas prácticas

### 1. Verifica antes de mergear

```python
# Cargar datos
ventas = pd.read_csv('../data/ventas.csv')
productos = pd.read_csv('../data/productos.csv')

# Verifica duplicados en la clave
print("=== VERIFICACIÓN DE DUPLICADOS ===")
print(f"Duplicados en 'producto' (ventas): {ventas['producto'].duplicated().sum()}")
print(f"Duplicados en 'producto' (productos): {productos['producto'].duplicated().sum()}")

# Verifica que las claves coincidan
print("\n=== VERIFICACIÓN DE COINCIDENCIAS ===")
productos_en_ventas = ventas['producto'].isin(productos['producto']).sum()
print(f"Productos de ventas que están en catálogo: {productos_en_ventas} de {len(ventas)}")
print(f"Productos en catálogo que tienen ventas: {productos['producto'].isin(ventas['producto']).sum()} de {len(productos)}")

# Productos únicos
print("\n=== PRODUCTOS ÚNICOS ===")
print(f"Productos únicos en ventas: {ventas['producto'].nunique()}")
print(f"Productos únicos en catálogo: {productos['producto'].nunique()}")
```

### 2. Usa índices cuando sea apropiado

```python
# Si las claves son índices (más eficiente para merges repetidos)
ventas_indexed = ventas.set_index('producto')
productos_indexed = productos.set_index('producto')

# Usar join() en lugar de merge()
df_joined = ventas_indexed.join(productos_indexed[['stock', 'proveedor']], how='left')
print(f"Registros después de join: {len(df_joined)}")
df_joined.head()
```

### 3. Maneja valores nulos después del merge

```python
# Después de un left join, verifica nulos
ventas_completas = pd.merge(ventas, productos, on='producto', how='left')

print("=== VALORES NULOS DESPUÉS DE MERGE ===")
print(ventas_completas.isnull().sum())

# Opciones para manejar nulos:
# 1. Eliminar filas con nulos
# ventas_completas = ventas_completas.dropna(subset=['stock'])

# 2. Rellenar con valores por defecto
# ventas_completas['stock'] = ventas_completas['stock'].fillna(0)
# ventas_completas['proveedor'] = ventas_completas['proveedor'].fillna('Desconocido')
```

---

## 🎯 Ejercicios

> 💡 **Usa los CSVs de ejemplo**: `../data/ventas.csv` y `../data/productos.csv` para practicar estos ejercicios.

### Ejercicio 1: Merge básico

```python
# 1. Carga ambos CSVs
ventas = pd.read_csv('../data/ventas.csv')
productos = pd.read_csv('../data/productos.csv')

# 2. Realiza un inner join entre ventas y productos usando 'producto'
# Tu código aquí

# 3. Muestra las primeras filas del resultado
# Tu código aquí

# 4. Verifica cuántos registros tiene el resultado
# Tu código aquí
```

### Ejercicio 2: Left join y manejo de nulos

```python
# 1. Realiza un left join (todas las ventas, incluso sin producto en catálogo)
# Tu código aquí

# 2. Identifica cuántas ventas no tienen información del producto
# Tu código aquí

# 3. Muestra esas ventas sin información
# Tu código aquí

# 4. Rellena los nulos en 'stock' con 0 y 'proveedor' con 'Desconocido'
# Tu código aquí
```

### Ejercicio 3: Análisis con merge

```python
# 1. Combina ventas con productos usando left join
# Tu código aquí

# 2. Encuentra productos con bajo stock (< 20) que tienen ventas altas (> 500)
# Tu código aquí

# 3. Calcula el total de ventas por proveedor
# Tu código aquí

# 4. Encuentra el proveedor con mayores ingresos
# Tu código aquí
```

### Ejercicio 4: Múltiples merges

```python
# 1. Crea un DataFrame de resumen de ventas por producto
resumen_ventas = ventas.groupby('producto').agg({
    'total': 'sum',
    'cantidad': 'sum',
    'id': 'count'
}).reset_index()
resumen_ventas.columns = ['producto', 'total_ventas', 'cantidad_total', 'num_transacciones']

# 2. Combina este resumen con la información de productos
# Tu código aquí

# 3. Calcula el ratio de ventas vs stock (total_ventas / stock)
# Tu código aquí

# 4. Ordena por este ratio descendente para ver productos más demandados
# Tu código aquí
```

### Ejercicio 5: Verificación de integridad

```python
# 1. Verifica duplicados en 'producto' en ambos DataFrames
# Tu código aquí

# 2. Verifica qué productos de ventas no están en el catálogo
# Tu código aquí

# 3. Verifica qué productos del catálogo no tienen ventas
# Tu código aquí

# 4. Crea un reporte de integridad mostrando:
#    - Total de productos en ventas
#    - Total de productos en catálogo
#    - Productos que coinciden
#    - Productos solo en ventas
#    - Productos solo en catálogo
# Tu código aquí
```

> 💡 **¿Quieres ver ejemplos de cómo resolver estos ejercicios?** Revisa el notebook de ejemplo: **[06-merge-join.ipynb](../../ejemplos/06-merge-join.ipynb)** que muestra estas técnicas aplicadas a los CSVs de ejemplo.

---

## 🚀 Próximo paso

Continúa con **[Manejo de archivos](../../fundamentos/manejo-de-archivos.md)** para aprender a leer y escribir diferentes formatos (CSV, Parquet, JSON, Excel) y trabajar con archivos grandes.
