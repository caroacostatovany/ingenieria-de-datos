# Limpieza de datos

La limpieza de datos es una tarea fundamental en Data Engineering. Aprende técnicas comunes para detectar y corregir problemas en tus datos.

> 💡 **Usa el CSV de ejemplo**: `../data/ventas.csv` para practicar estos conceptos. Aunque este CSV está limpio, aprenderás a detectar y limpiar problemas comunes.

---

## 🔍 Detectar problemas

### Valores nulos

```python
# Cargar datos
df = pd.read_csv('../data/ventas.csv')

# Verificar nulos
print("Valores nulos por columna:")
print(df.isnull().sum())

# Porcentaje de nulos
print("\nPorcentaje de nulos:")
print((df.isnull().sum() / len(df) * 100).round(2))

# Filas con nulos
filas_con_nulos = df[df.isnull().any(axis=1)]
print(f"\nFilas con al menos un nulo: {len(filas_con_nulos)}")
```

### Duplicados

```python
# Detectar duplicados completos
duplicados = df.duplicated()
print(f"Duplicados completos: {duplicados.sum()}")

# Contar duplicados
print(f"Total de duplicados: {df.duplicated().sum()}")

# Ver duplicados
if df.duplicated().sum() > 0:
    print("\nDuplicados encontrados:")
    print(df[df.duplicated()])
else:
    print("\n✅ No hay duplicados completos")

# Duplicados en columnas específicas (ej: mismo producto vendido el mismo día)
duplicados_producto_fecha = df.duplicated(subset=['producto', 'fecha'])
print(f"\nDuplicados en producto+fecha: {duplicados_producto_fecha.sum()}")
```

### Valores atípicos (Outliers)

```python
# Usando IQR (Interquartile Range) para detectar outliers en precio
Q1 = df['precio'].quantile(0.25)
Q3 = df['precio'].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers = df[(df['precio'] < limite_inferior) | (df['precio'] > limite_superior)]
print(f"Outliers en precio: {len(outliers)}")
if len(outliers) > 0:
    print(outliers[['producto', 'precio', 'categoria']])
```

---

## 🧹 Limpiar datos

### Manejar nulos

```python
# Cargar datos
df = pd.read_csv('../data/ventas.csv')

# Opción 1: Eliminar filas con nulos (si son pocos)
df_sin_nulos = df.dropna()
print(f"Registros originales: {len(df)}")
print(f"Registros después de dropna(): {len(df_sin_nulos)}")

# Opción 2: Eliminar columnas con muchos nulos (>50%)
df_limpio = df.dropna(axis=1, thresh=len(df)*0.5)
print(f"Columnas originales: {len(df.columns)}")
print(f"Columnas después de filtrar: {len(df_limpio.columns)}")

# Opción 3: Rellenar nulos
# Con promedio (para numéricos)
# df['precio'] = df['precio'].fillna(df['precio'].mean())

# Con valor fijo (para categóricos)
# df['ciudad'] = df['ciudad'].fillna('Desconocida')

# Con forward fill (rellena con valor anterior)
# df = df.fillna(method='ffill')  # Nota: method='ffill' está deprecado, usar ffill()
```

### Eliminar duplicados

```python
# Eliminar duplicados completos
df_limpio = df.drop_duplicates()
print(f"Registros originales: {len(df)}")
print(f"Registros después de eliminar duplicados: {len(df_limpio)}")

# Eliminar duplicados en columnas específicas (mantener el primero)
df_limpio = df.drop_duplicates(subset=['producto', 'fecha'], keep='first')
print(f"Registros después de eliminar duplicados en producto+fecha: {len(df_limpio)}")
```

### Normalizar texto

```python
# Crear copia para no modificar original
df_limpio = df.copy()

# Eliminar espacios al inicio y final
df_limpio['producto'] = df_limpio['producto'].str.strip()
df_limpio['categoria'] = df_limpio['categoria'].str.strip()

# Convertir a mayúsculas/minúsculas (si fuera necesario)
# df_limpio['producto'] = df_limpio['producto'].str.upper()
# df_limpio['categoria'] = df_limpio['categoria'].str.lower()

# Reemplazar caracteres (ejemplo: si hubiera guiones)
# df_limpio['producto'] = df_limpio['producto'].str.replace('-', ' ')

print("✅ Texto normalizado")
df_limpio[['producto', 'categoria']].head()
```

### Convertir tipos

```python
# Verificar tipos actuales
print("Tipos antes de conversión:")
print(df.dtypes)

# Convertir fecha a datetime
df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d', errors='coerce')
print(f"\nFecha convertida. Tipo: {df['fecha'].dtype}")

# Convertir a numérico (si fuera necesario, aunque ya lo es)
# df['precio'] = pd.to_numeric(df['precio'], errors='coerce')

# Convertir a categoría (ahorra memoria para columnas con pocos valores únicos)
df['categoria'] = df['categoria'].astype('category')
df['ciudad'] = df['ciudad'].astype('category')

print("\nTipos después de conversión:")
print(df.dtypes)
print(f"\nMemoria ahorrada: {df.memory_usage(deep=True).sum() / 1024:.2f} KB")
```

### Manejar valores atípicos

```python
# Opción 1: Eliminar outliers
Q1 = df['precio'].quantile(0.25)
Q3 = df['precio'].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

df_sin_outliers = df[(df['precio'] >= limite_inferior) & (df['precio'] <= limite_superior)]
print(f"Registros originales: {len(df)}")
print(f"Registros sin outliers: {len(df_sin_outliers)}")
print(f"Outliers eliminados: {len(df) - len(df_sin_outliers)}")

# Opción 2: Capar outliers (limitar valores extremos)
df_capped = df.copy()
df_capped['precio'] = df_capped['precio'].clip(lower=limite_inferior, upper=limite_superior)
print(f"\nPrecios capados entre {limite_inferior:.2f} y {limite_superior:.2f}")
```

---

## 🎯 Ejercicios

> 💡 **Usa el CSV de ejemplo**: `../data/ventas.csv` para practicar estos ejercicios.

### Ejercicio 1: Detectar problemas

```python
# 1. Carga el CSV de ventas
df = pd.read_csv('../data/ventas.csv')

# 2. Verifica valores nulos en todas las columnas
# Tu código aquí

# 3. Verifica duplicados completos y en columnas específicas (producto + fecha)
# Tu código aquí

# 4. Detecta outliers en la columna 'precio' usando IQR
# Tu código aquí
```

### Ejercicio 2: Limpiar datos básicos

```python
# 1. Crea una copia del DataFrame para trabajar
# Tu código aquí

# 2. Convierte la columna 'fecha' a datetime
# Tu código aquí

# 3. Convierte 'categoria' y 'ciudad' a tipo 'category' para ahorrar memoria
# Tu código aquí

# 4. Normaliza el texto: elimina espacios en 'producto' y 'categoria'
# Tu código aquí
```

### Ejercicio 3: Manejar duplicados y outliers

```python
# 1. Elimina duplicados completos (si los hay)
# Tu código aquí

# 2. Elimina duplicados basados en 'producto' y 'fecha' (mantén el primero)
# Tu código aquí

# 3. Detecta outliers en 'precio' y muestra cuántos hay
# Tu código aquí

# 4. Crea un DataFrame sin outliers (elimina los valores extremos)
# Tu código aquí
```

### Ejercicio 4: Limpieza completa

```python
# 1. Carga los datos
df = pd.read_csv('../data/ventas.csv')

# 2. Realiza una limpieza completa:
#    - Convierte 'fecha' a datetime
#    - Convierte 'categoria' y 'ciudad' a category
#    - Normaliza texto (strip en producto y categoria)
#    - Elimina duplicados en producto+fecha
#    - Detecta y muestra outliers en precio
# Tu código aquí

# 3. Crea un resumen de la limpieza:
#    - Registros originales vs finales
#    - Duplicados eliminados
#    - Outliers detectados
#    - Tipos de datos corregidos
# Tu código aquí
```

> 💡 **¿Quieres ver ejemplos de cómo resolver estos ejercicios?** Revisa el notebook de ejemplo: **[04-limpieza-datos.ipynb](../../ejemplos/04-limpieza-datos.ipynb)** que muestra estas técnicas aplicadas paso a paso.

---

## 🚀 Siguiente paso

Continúa con **[Agregaciones y agrupaciones](04-agregaciones.md)**.
