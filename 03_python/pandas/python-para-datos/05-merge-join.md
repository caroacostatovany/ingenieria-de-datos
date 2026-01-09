# Merge y Join en Pandas

Combina múltiples DataFrames de forma similar a SQL JOINs.

---

## 🔗 Tipos de merge

### Inner join

```python
# Solo filas que coinciden en ambas tablas
df_merged = pd.merge(df1, df2, on='id', how='inner')
```

### Left join

```python
# Todas las filas de la izquierda
df_merged = pd.merge(df1, df2, on='id', how='left')
```

### Right join

```python
# Todas las filas de la derecha
df_merged = pd.merge(df1, df2, on='id', how='right')
```

### Outer join

```python
# Todas las filas de ambas tablas
df_merged = pd.merge(df1, df2, on='id', how='outer')
```

---

## 🎯 Ejemplos prácticos

### Ejemplo 1: Combinar usuarios y ventas

```python
# DataFrames
usuarios = pd.DataFrame({
    'id': [1, 2, 3],
    'nombre': ['Juan', 'María', 'Carlos']
})

ventas = pd.DataFrame({
    'usuario_id': [1, 1, 2],
    'total': [100, 200, 150]
})

# Merge
df_completo = pd.merge(usuarios, ventas, left_on='id', right_on='usuario_id', how='left')
```

### Ejemplo 2: Múltiples columnas

```python
# Merge por múltiples columnas
df_merged = pd.merge(
    df1, 
    df2, 
    on=['fecha', 'categoria'], 
    how='inner'
)
```

### Ejemplo 3: Sufijos para columnas duplicadas

```python
# Cuando hay columnas con el mismo nombre
df_merged = pd.merge(
    df1, 
    df2, 
    on='id', 
    suffixes=('_left', '_right')
)
```

---

## 💡 Buenas prácticas

### 1. Verifica antes de mergear

```python
# Verifica duplicados en la clave
print(df1['id'].duplicated().sum())
print(df2['id'].duplicated().sum())

# Verifica que las claves coincidan
print(df1['id'].isin(df2['id']).sum())
```

### 2. Usa índices cuando sea apropiado

```python
# Si las claves son índices
df1.set_index('id', inplace=True)
df2.set_index('id', inplace=True)
df_merged = df1.join(df2, how='left')
```

---

## 🎯 Ejercicios

1. Combina datos de usuarios y ventas
2. Realiza un left join y maneja valores nulos
3. Combina múltiples DataFrames
4. Verifica la integridad de los merges

---

## 🚀 Próximo paso

Continúa con **[Manejo de archivos](../manejo-de-archivos.md)**.
