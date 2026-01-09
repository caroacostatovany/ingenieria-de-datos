# Agregaciones y agrupaciones

Aprende a resumir y agrupar datos con pandas.

---

## 📊 Agregaciones básicas

```python
# Agregaciones simples
df['edad'].sum()
df['edad'].mean()
df['edad'].median()
df['edad'].std()
df['edad'].min()
df['edad'].max()
df['edad'].count()
```

### Múltiples agregaciones

```python
# Todas las agregaciones numéricas
df.describe()

# Agregaciones personalizadas
df.agg({
    'edad': ['mean', 'min', 'max'],
    'precio': ['sum', 'mean']
})
```

---

## 📦 GROUP BY

### Agrupación básica

```python
# Agrupar por ciudad y calcular promedio de edad
df.groupby('ciudad')['edad'].mean()

# Múltiples columnas
df.groupby(['ciudad', 'categoria'])['precio'].mean()
```

### Múltiples funciones

```python
# Diferentes funciones por columna
df.groupby('ciudad').agg({
    'edad': ['mean', 'min', 'max'],
    'precio': 'sum',
    'nombre': 'count'
})
```

### Named aggregations

```python
# Con nombres personalizados
df.groupby('ciudad').agg(
    edad_promedio=('edad', 'mean'),
    total_precio=('precio', 'sum'),
    total_usuarios=('nombre', 'count')
)
```

---

## 🔄 Pivot tables

```python
# Crear tabla pivot
df.pivot_table(
    values='precio',
    index='ciudad',
    columns='categoria',
    aggfunc='mean'
)
```

---

## 🎯 Ejercicios

1. Agrupa ventas por mes y calcula totales
2. Crea una tabla pivot de ventas por ciudad y categoría
3. Calcula estadísticas por múltiples dimensiones
4. Encuentra el top N por categoría

---

## 🚀 Siguiente paso

Continúa con **[Merge y Join](05-merge-join.md)**.
