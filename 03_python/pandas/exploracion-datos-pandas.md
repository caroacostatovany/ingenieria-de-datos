# Exploración de Datos con Pandas

El análisis exploratorio de datos (EDA) es el primer paso para entender tus datos. Aprende a explorar datos efectivamente con pandas.

> 💡 **Ejemplo práctico**: Revisa el [notebook de exploración de datos](../ejemplos/01-exploracion-datos.ipynb) para ver estos conceptos en acción.

---

## 🧠 ¿Qué es EDA?

EDA (Exploratory Data Analysis) es el proceso de:
* **Entender** la estructura de tus datos
* **Identificar** patrones y anomalías
* **Detectar** problemas de calidad
* **Formular** hipótesis sobre los datos

> No puedes analizar lo que no entiendes. EDA es esencial antes de cualquier análisis.

---

## 📊 Primeros pasos

### Cargar y ver datos

```python
import pandas as pd
import numpy as np

# Cargar datos
df = pd.read_csv('datos.csv')

# Primer vistazo
df.head()        # Primeras 5 filas
df.tail()        # Últimas 5 filas
df.sample(5)     # 5 filas aleatorias
```

### Información básica

```python
# Forma del DataFrame
print(f"Filas: {df.shape[0]}, Columnas: {df.shape[1]}")

# Información del DataFrame
df.info()        # Tipos, memoria, nulos

# Estadísticas descriptivas
df.describe()    # Solo columnas numéricas

# Tipos de datos
df.dtypes
```

---

## 🔍 Exploración de estructura

### Columnas y tipos

```python
# Ver todas las columnas
df.columns.tolist()

# Tipos de datos
df.dtypes

# Verificar tipos esperados
for col in df.columns:
    print(f"{col}: {df[col].dtype}, Valores únicos: {df[col].nunique()}")
```

### Valores únicos

```python
# Valores únicos por columna
for col in df.columns:
    print(f"\n{col}:")
    print(f"  Valores únicos: {df[col].nunique()}")
    if df[col].nunique() < 20:  # Si hay pocos valores únicos
        print(f"  Valores: {df[col].unique()}")
```

---

## 📈 Estadísticas descriptivas

### Estadísticas numéricas

```python
# Estadísticas básicas
df.describe()

# Estadísticas por columna
df['precio'].describe()

# Estadísticas personalizadas
df.agg({
    'precio': ['mean', 'median', 'std', 'min', 'max'],
    'cantidad': ['sum', 'mean']
})
```

### Distribuciones

```python
# Histograma (usando pandas)
df['edad'].hist(bins=20)

# Percentiles
df['precio'].quantile([0.25, 0.5, 0.75, 0.9, 0.95, 0.99])

# Detectar outliers usando IQR
Q1 = df['precio'].quantile(0.25)
Q3 = df['precio'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['precio'] < Q1 - 1.5*IQR) | (df['precio'] > Q3 + 1.5*IQR)]
print(f"Outliers encontrados: {len(outliers)}")
```

---

## 🔎 Detectar problemas

### Valores nulos

```python
# Contar nulos por columna
df.isnull().sum()

# Porcentaje de nulos
(df.isnull().sum() / len(df) * 100).sort_values(ascending=False)

# Filas con nulos
df[df.isnull().any(axis=1)]

# Patrones de nulos
import seaborn as sns
sns.heatmap(df.isnull(), cbar=True)  # Visualizar nulos
```

### Duplicados

```python
# Detectar duplicados completos
duplicados = df[df.duplicated()]
print(f"Duplicados completos: {len(duplicados)}")

# Duplicados en columnas específicas
duplicados_id = df[df.duplicated(subset=['id'])]
print(f"IDs duplicados: {len(duplicados_id)}")
```

### Valores atípicos

```python
# Usando IQR
def detectar_outliers(df, columna):
    Q1 = df[columna].quantile(0.25)
    Q3 = df[columna].quantile(0.75)
    IQR = Q3 - Q1
    
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    
    outliers = df[(df[columna] < limite_inferior) | (df[columna] > limite_superior)]
    return outliers

outliers_precio = detectar_outliers(df, 'precio')
print(f"Outliers en precio: {len(outliers_precio)}")
```

---

## 📊 Análisis de relaciones

### Correlaciones

```python
# Matriz de correlación
correlaciones = df.select_dtypes(include=[np.number]).corr()
print(correlaciones)

# Visualizar correlaciones
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 8))
sns.heatmap(correlaciones, annot=True, cmap='coolwarm', center=0)
plt.title('Matriz de Correlación')
plt.show()
```

### Agrupaciones

```python
# Agrupar y analizar
df.groupby('categoria')['precio'].agg(['mean', 'median', 'std', 'count'])

# Múltiples agrupaciones
df.groupby(['categoria', 'mes'])['total'].sum()
```

---

## 🎨 Visualización básica

### Histogramas

```python
# Histograma simple
df['edad'].hist(bins=20)
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.title('Distribución de Edades')
plt.show()
```

### Box plots

```python
# Box plot para detectar outliers
df.boxplot(column='precio', by='categoria')
plt.show()
```

### Scatter plots

```python
# Relación entre variables
plt.scatter(df['cantidad'], df['precio'])
plt.xlabel('Cantidad')
plt.ylabel('Precio')
plt.title('Relación Cantidad vs Precio')
plt.show()
```

---

## 🔄 Flujo de exploración típico

### 1. Carga y primera inspección

```python
# Cargar
df = pd.read_csv('datos.csv')

# Primer vistazo
print(f"Shape: {df.shape}")
print(f"\nColumnas: {df.columns.tolist()}")
print(f"\nTipos:\n{df.dtypes}")
print(f"\nPrimeras filas:\n{df.head()}")
```

### 2. Estadísticas básicas

```python
# Estadísticas numéricas
print(df.describe())

# Estadísticas categóricas
for col in df.select_dtypes(include=['object']).columns:
    print(f"\n{col}:")
    print(df[col].value_counts().head(10))
```

### 3. Detectar problemas

```python
# Nulos
print("Valores nulos:")
print(df.isnull().sum())

# Duplicados
print(f"\nDuplicados: {df.duplicated().sum()}")

# Outliers
for col in df.select_dtypes(include=[np.number]).columns:
    outliers = detectar_outliers(df, col)
    if len(outliers) > 0:
        print(f"\nOutliers en {col}: {len(outliers)}")
```

### 4. Análisis de relaciones

```python
# Correlaciones
correlaciones = df.select_dtypes(include=[np.number]).corr()
print(correlaciones)

# Agrupaciones interesantes
df.groupby('categoria')['precio'].agg(['mean', 'count'])
```

---

## 💡 Tips para EDA efectivo

### 1. Empieza con lo básico

```python
# Siempre empieza con:
df.head()
df.info()
df.describe()
```

### 2. Documenta tus hallazgos

```python
# En Jupyter Notebook, documenta:
"""
Hallazgos de exploración:
- 150 valores nulos en columna 'email' (15%)
- 5 duplicados completos
- Precio tiene outliers: 3 valores > 1000
- Correlación fuerte entre cantidad y total (0.95)
"""
```

### 3. Visualiza siempre que sea posible

```python
# Los números cuentan, las visualizaciones muestran
df['precio'].hist()  # Mejor que solo df['precio'].describe()
```

### 4. Formula preguntas

```python
# Durante EDA, pregunta:
# - ¿Qué patrones veo?
# - ¿Hay anomalías?
# - ¿Qué relaciones existen?
# - ¿Qué necesito investigar más?
```

---

## 🎯 Ejercicios

1. Carga un dataset y realiza EDA completo
2. Identifica todos los problemas de calidad
3. Visualiza distribuciones y relaciones
4. Documenta tus hallazgos
5. Formula 3 preguntas sobre los datos

---

## 🚀 Próximo paso

Después de explorar datos, aprende a **[contar la historia con datos](../storytelling/)** para comunicar tus hallazgos efectivamente.

---

> **Recuerda**: La exploración de datos no tiene un final claro. Explora hasta que entiendas tus datos lo suficiente para hacer análisis significativos.
