# Limpieza de datos

La limpieza de datos es una tarea fundamental en Data Engineering. Aprende técnicas comunes.

---

## 🔍 Detectar problemas

### Valores nulos

```python
# Verificar nulos
df.isnull().sum()

# Porcentaje de nulos
(df.isnull().sum() / len(df)) * 100

# Filas con nulos
df[df.isnull().any(axis=1)]
```

### Duplicados

```python
# Detectar duplicados
df.duplicated()

# Contar duplicados
df.duplicated().sum()

# Ver duplicados
df[df.duplicated()]
```

### Valores atípicos

```python
# Usando IQR (Interquartile Range)
Q1 = df['edad'].quantile(0.25)
Q3 = df['edad'].quantile(0.75)
IQR = Q3 - Q1

outliers = df[(df['edad'] < Q1 - 1.5*IQR) | (df['edad'] > Q3 + 1.5*IQR)]
```

---

## 🧹 Limpiar datos

### Manejar nulos

```python
# Eliminar filas con nulos
df_limpio = df.dropna()

# Eliminar columnas con muchos nulos
df_limpio = df.dropna(axis=1, thresh=len(df)*0.5)  # Elimina si >50% nulos

# Rellenar nulos
df['edad'].fillna(df['edad'].mean())  # Con promedio
df['ciudad'].fillna('Desconocida')    # Con valor fijo
df.fillna(method='ffill')             # Forward fill
```

### Eliminar duplicados

```python
# Eliminar duplicados completos
df_limpio = df.drop_duplicates()

# Eliminar duplicados en columnas específicas
df_limpio = df.drop_duplicates(subset=['email'])
```

### Normalizar texto

```python
# Eliminar espacios
df['nombre'] = df['nombre'].str.strip()

# Convertir a mayúsculas/minúsculas
df['nombre'] = df['nombre'].str.upper()
df['email'] = df['email'].str.lower()

# Reemplazar caracteres
df['telefono'] = df['telefono'].str.replace('-', '')
```

### Convertir tipos

```python
# Convertir a numérico
df['precio'] = pd.to_numeric(df['precio'], errors='coerce')

# Convertir a fecha
df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d')

# Convertir a categoría (ahorra memoria)
df['ciudad'] = df['ciudad'].astype('category')
```

---

## 🎯 Ejercicios

1. Limpia un dataset con valores nulos y duplicados
2. Normaliza nombres y emails
3. Convierte tipos de datos apropiadamente
4. Detecta y maneja valores atípicos

---

## 🚀 Siguiente paso

Continúa con **[Agregaciones y agrupaciones](04-agregaciones.md)**.
