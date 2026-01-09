# Operaciones con DataFrames

Aprende a realizar operaciones avanzadas con pandas DataFrames.

---

## 🔄 Transformaciones

### Aplicar funciones

```python
# Aplicar función a columna
df['nombre_upper'] = df['nombre'].apply(str.upper)

# Aplicar función personalizada
def categorizar_edad(edad):
    if edad < 30:
        return 'Joven'
    elif edad < 50:
        return 'Adulto'
    else:
        return 'Senior'

df['categoria'] = df['edad'].apply(categorizar_edad)
```

### Map y replace

```python
# Mapear valores
mapeo = {'Madrid': 'Centro', 'Barcelona': 'Este'}
df['region'] = df['ciudad'].map(mapeo)

# Reemplazar valores
df['ciudad'] = df['ciudad'].replace('Madrid', 'MAD')
```

---

## 📊 Agrupaciones

### GROUP BY básico

```python
# Agrupar y agregar
df.groupby('ciudad')['edad'].mean()

# Múltiples agregaciones
df.groupby('ciudad').agg({
    'edad': ['mean', 'min', 'max'],
    'nombre': 'count'
})
```

### Transform y filter

```python
# Transform: mantiene forma original
df['edad_promedio_ciudad'] = df.groupby('ciudad')['edad'].transform('mean')

# Filter: filtra grupos
df_filtrado = df.groupby('ciudad').filter(lambda x: len(x) > 2)
```

---

## 🔗 Combinar DataFrames

### Concat

```python
# Concatenar verticalmente
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
df_combinado = pd.concat([df1, df2], ignore_index=True)
```

### Merge (JOIN)

```python
# Inner join
df_merged = pd.merge(df1, df2, on='id', how='inner')

# Left join
df_merged = pd.merge(df1, df2, on='id', how='left')

# Múltiples columnas
df_merged = pd.merge(df1, df2, on=['id', 'fecha'], how='inner')
```

---

## 🎯 Ejercicios

1. Agrupa datos por categoría y calcula estadísticas
2. Combina dos DataFrames con merge
3. Aplica transformaciones a múltiples columnas
4. Filtra grupos que cumplan ciertas condiciones

---

## 🚀 Siguiente paso

Continúa con **[Limpieza de datos](03-limpieza-datos.md)**.
