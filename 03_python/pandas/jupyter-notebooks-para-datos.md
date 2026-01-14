# Jupyter Notebooks para Análisis de Datos

Jupyter Notebooks son excelentes para explorar datos, hacer análisis y documentar tu trabajo.

---

## 🧠 ¿Qué es Jupyter?

Jupyter Notebook es un entorno interactivo que combina:
* **Código ejecutable** (Python, SQL, etc.)
* **Resultados visuales** (gráficos, tablas)
* **Documentación** (Markdown, texto)
* **Todo en un solo lugar**

> Jupyter es perfecto para explorar datos, hacer análisis y compartir resultados.

---

## 🚀 Empezar con Jupyter Notebooks

> 💡 **Si ya instalaste Jupyter en Fundamentos**: Puedes saltar esta sección y ir directo a "Flujo de trabajo típico".

### Si estás usando Cursor

1. **Abre el notebook de ejemplo**: `03_python/ejemplos/00-notebook.ipynb`
2. **Selecciona el kernel de Python** en la parte superior
3. **¡Empieza a trabajar!**

### Si NO estás usando Cursor: Instalación

```bash
# Con pip
pip install jupyter pandas matplotlib seaborn

# O con conda
conda install jupyter pandas matplotlib seaborn
```

### Iniciar Jupyter

```bash
# Iniciar servidor
jupyter notebook

# O JupyterLab (interfaz moderna)
jupyter lab
```

Se abrirá en tu navegador en `http://localhost:8888`

---

## 📓 Estructura de un Notebook

Un notebook tiene **celdas** que pueden ser:

### Celda de código

```python
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos desde el CSV de ejemplo
df = pd.read_csv('../data/ventas.csv')
df.head()
```

### Celda de Markdown

```markdown
# Análisis de Ventas

Este notebook analiza las ventas del último trimestre.

## Objetivos
1. Calcular totales por categoría
2. Identificar tendencias
3. Generar visualizaciones
```

---

## 🔍 Flujo de trabajo típico

### 1. Cargar y explorar datos

```python
# Celda 1: Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Celda 2: Cargar datos desde el CSV de ejemplo
# El archivo está en 03_python/data/ventas.csv
df = pd.read_csv('../data/ventas.csv')
df.head()

# Celda 3: Explorar
df.info()
df.describe()

# Celda 4: Verificar nulos
df.isnull().sum()
```

### 2. Limpiar datos

```python
# Celda 5: Limpiar
df = df.dropna()
df = df.drop_duplicates()
df['fecha'] = pd.to_datetime(df['fecha'])

# Verificar que la limpieza funcionó
print(f"Registros después de limpieza: {len(df)}")
df.head()
```

### 3. Análisis

```python
# Celda 6: Agregaciones
ventas_por_categoria = df.groupby('categoria')['total'].sum()
print("Ventas por categoría:")
print(ventas_por_categoria)

# Celda 7: Visualización
ventas_por_categoria.plot(kind='bar', figsize=(10, 6))
plt.title('Ventas por Categoría')
plt.xlabel('Categoría')
plt.ylabel('Total de Ventas (€)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

### 4. Conclusiones

```markdown
## Conclusiones

- La categoría "Electrónica" tiene las mayores ventas
- Las ventas están distribuidas entre Madrid, Barcelona, Valencia y Sevilla
- Recomendación: Analizar tendencias por ciudad y mes
```

---

## 🔍 Exploración de Datos (EDA)

EDA (Exploratory Data Analysis) es el proceso de entender la estructura de tus datos, identificar patrones y detectar problemas de calidad.

> 💡 **Ejemplo práctico**: Usa el CSV de ejemplo `../data/ventas.csv` para practicar estos conceptos.

### Primeros pasos

```python
# Cargar datos
df = pd.read_csv('../data/ventas.csv')

# Primer vistazo
df.head()        # Primeras 5 filas
df.tail()        # Últimas 5 filas
df.sample(5)     # 5 filas aleatorias

# Información básica
print(f"Filas: {df.shape[0]}, Columnas: {df.shape[1]}")
df.info()        # Tipos, memoria, nulos
df.describe()    # Solo columnas numéricas
```

### Exploración de estructura

```python
# Ver todas las columnas
print("Columnas:", df.columns.tolist())

# Tipos de datos
print("\nTipos de datos:")
print(df.dtypes)

# Valores únicos por columna
for col in df.columns:
    print(f"\n{col}:")
    print(f"  Valores únicos: {df[col].nunique()}")
    if df[col].nunique() < 20:  # Si hay pocos valores únicos
        print(f"  Valores: {df[col].unique()}")
```

### Estadísticas descriptivas

```python
# Estadísticas básicas
df.describe()

# Estadísticas por columna numérica
df['precio'].describe()

# Estadísticas personalizadas
df.agg({
    'precio': ['mean', 'median', 'std', 'min', 'max'],
    'cantidad': ['sum', 'mean']
})

# Percentiles
df['precio'].quantile([0.25, 0.5, 0.75, 0.9, 0.95, 0.99])
```

### Detectar problemas

#### Valores nulos

```python
# Contar nulos por columna
print("Valores nulos:")
print(df.isnull().sum())

# Porcentaje de nulos
print("\nPorcentaje de nulos:")
print((df.isnull().sum() / len(df) * 100).sort_values(ascending=False))

# Filas con nulos
df[df.isnull().any(axis=1)]

# Visualizar nulos (si hay muchos)
import seaborn as sns
sns.heatmap(df.isnull(), cbar=True, yticklabels=False)
plt.title('Mapa de Valores Nulos')
plt.show()
```

#### Duplicados

```python
# Detectar duplicados completos
duplicados = df[df.duplicated()]
print(f"Duplicados completos: {len(duplicados)}")

# Duplicados en columnas específicas
duplicados_id = df[df.duplicated(subset=['id'])]
print(f"IDs duplicados: {len(duplicados_id)}")
```

#### Valores atípicos (Outliers)

```python
# Función para detectar outliers usando IQR
def detectar_outliers(df, columna):
    Q1 = df[columna].quantile(0.25)
    Q3 = df[columna].quantile(0.75)
    IQR = Q3 - Q1
    
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    
    outliers = df[(df[columna] < limite_inferior) | (df[columna] > limite_superior)]
    return outliers

# Detectar outliers en precio
outliers_precio = detectar_outliers(df, 'precio')
print(f"Outliers en precio: {len(outliers_precio)}")
if len(outliers_precio) > 0:
    print(outliers_precio[['id', 'producto', 'precio']])
```

### Análisis de relaciones

#### Correlaciones

```python
# Matriz de correlación (solo columnas numéricas)
columnas_numericas = df.select_dtypes(include=[np.number]).columns
correlaciones = df[columnas_numericas].corr()
print(correlaciones)

# Visualizar correlaciones
plt.figure(figsize=(8, 6))
sns.heatmap(correlaciones, annot=True, cmap='coolwarm', center=0)
plt.title('Matriz de Correlación')
plt.tight_layout()
plt.show()
```

#### Agrupaciones

```python
# Agrupar y analizar
df.groupby('categoria')['precio'].agg(['mean', 'median', 'std', 'count'])

# Múltiples agrupaciones
df['mes'] = pd.to_datetime(df['fecha']).dt.to_period('M')
df.groupby(['categoria', 'mes'])['total'].sum()
```

### Visualización para exploración

#### Histogramas

```python
# Histograma de precios
df['precio'].hist(bins=20, figsize=(10, 6))
plt.xlabel('Precio (€)')
plt.ylabel('Frecuencia')
plt.title('Distribución de Precios')
plt.tight_layout()
plt.show()
```

#### Box plots

```python
# Box plot para detectar outliers por categoría
df.boxplot(column='precio', by='categoria', figsize=(10, 6))
plt.title('Distribución de Precios por Categoría')
plt.suptitle('')  # Eliminar título automático
plt.xlabel('Categoría')
plt.ylabel('Precio (€)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

#### Scatter plots

```python
# Relación entre cantidad y precio
plt.figure(figsize=(10, 6))
plt.scatter(df['cantidad'], df['precio'], alpha=0.6)
plt.xlabel('Cantidad')
plt.ylabel('Precio (€)')
plt.title('Relación Cantidad vs Precio')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### Flujo de exploración completo

```python
# 1. Carga y primera inspección
df = pd.read_csv('../data/ventas.csv')
print(f"Shape: {df.shape}")
print(f"\nColumnas: {df.columns.tolist()}")
print(f"\nTipos:\n{df.dtypes}")
print(f"\nPrimeras filas:\n{df.head()}")

# 2. Estadísticas básicas
print("\n=== Estadísticas Numéricas ===")
print(df.describe())

print("\n=== Estadísticas Categóricas ===")
for col in df.select_dtypes(include=['object']).columns:
    print(f"\n{col}:")
    print(df[col].value_counts().head(10))

# 3. Detectar problemas
print("\n=== Problemas Detectados ===")
print("Valores nulos:")
print(df.isnull().sum())
print(f"\nDuplicados: {df.duplicated().sum()}")

# 4. Análisis de relaciones
print("\n=== Correlaciones ===")
columnas_numericas = df.select_dtypes(include=[np.number]).columns
correlaciones = df[columnas_numericas].corr()
print(correlaciones)

# 5. Agrupaciones interesantes
print("\n=== Ventas por Categoría ===")
print(df.groupby('categoria')['total'].agg(['sum', 'mean', 'count']))
```

### Tips para EDA efectivo

1. **Empieza con lo básico**: Siempre ejecuta `df.head()`, `df.info()`, `df.describe()`
2. **Documenta tus hallazgos**: En Jupyter Notebook, usa celdas Markdown para documentar
3. **Visualiza siempre**: Los números cuentan, las visualizaciones muestran
4. **Formula preguntas**: ¿Qué patrones veo? ¿Hay anomalías? ¿Qué relaciones existen?

---

## 📊 Visualizaciones

### Matplotlib básico

```python
import matplotlib.pyplot as plt

# Gráfico de barras
df.groupby('categoria')['total'].sum().plot(kind='bar', figsize=(10, 6))
plt.title('Ventas por Categoría')
plt.xlabel('Categoría')
plt.ylabel('Total (€)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico de líneas (ventas por mes)
df['mes'] = pd.to_datetime(df['fecha']).dt.to_period('M')
ventas_mes = df.groupby('mes')['total'].sum()
ventas_mes.plot(kind='line', figsize=(10, 6), marker='o')
plt.title('Ventas por Mes')
plt.xlabel('Mes')
plt.ylabel('Total (€)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Histograma de precios
df['precio'].hist(bins=20, figsize=(10, 6))
plt.title('Distribución de Precios')
plt.xlabel('Precio (€)')
plt.ylabel('Frecuencia')
plt.tight_layout()
plt.show()
```

### Seaborn (más bonito)

```python
import seaborn as sns

# Configurar estilo
sns.set_style("whitegrid")

# Gráfico de barras
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='categoria', y='total')
plt.title('Ventas por Categoría')
plt.xlabel('Categoría')
plt.ylabel('Total (€)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Box plot de precios por categoría
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='categoria', y='precio')
plt.title('Distribución de Precios por Categoría')
plt.xlabel('Categoría')
plt.ylabel('Precio (€)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Heatmap de correlación (solo columnas numéricas)
columnas_numericas = df.select_dtypes(include=['float64', 'int64']).columns
plt.figure(figsize=(8, 6))
sns.heatmap(df[columnas_numericas].corr(), annot=True, cmap='coolwarm', center=0)
plt.title('Correlación entre Variables Numéricas')
plt.tight_layout()
plt.show()
```

---

## 🔗 Integración con SQL

### Conectar a base de datos

> ⚠️ **Importante**: Antes de ejecutar este código, asegúrate de que **Docker esté corriendo** con la base de datos PostgreSQL. Si no lo has iniciado, ve a `02_sql/` y ejecuta `docker-compose up -d`.

```python
from sqlalchemy import create_engine
import pandas as pd
import os
from dotenv import load_dotenv
from pathlib import Path

# Cargar variables de entorno desde .env en la raíz del proyecto
env_path = Path().resolve().parent.parent / '.env'
load_dotenv(env_path)

def conectar_db():
    """Crea conexión a la base de datos usando variables del .env."""
    # Opción 1: Usar DATABASE_URL si está disponible (más simple)
    database_url = os.getenv('DATABASE_URL')
    if database_url:
        engine = create_engine(database_url)
        return engine
    
    # Opción 2: Construir desde variables individuales (fallback)
    db_host = os.getenv('DB_HOST', 'localhost')
    db_port = os.getenv('DB_PORT', '5432')
    db_name = os.getenv('DB_NAME', 'data_engineering')
    db_user = os.getenv('DB_USER', 'de_user')
    db_password = os.getenv('DB_PASSWORD', 'de_password')
    
    connection_string = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    engine = create_engine(connection_string)
    return engine

# Conectar a la base de datos
engine = conectar_db()

# Ejecutar query usando las tablas de ejemplo (usuarios, productos, ventas)
query = """
SELECT 
    p.categoria,
    COUNT(v.id) AS total_ventas,
    SUM(v.total) AS ingresos_totales
FROM productos p
LEFT JOIN ventas v ON p.id = v.producto_id
GROUP BY p.categoria
ORDER BY ingresos_totales DESC
"""

df = pd.read_sql(query, engine)
df
```

### Ejemplo completo: Análisis de ventas desde la base de datos

```python
# Cargar datos de la base de datos
query_ventas = """
SELECT 
    u.nombre,
    u.ciudad,
    p.categoria,
    p.nombre AS producto,
    v.cantidad,
    v.total,
    v.fecha_venta
FROM ventas v
JOIN usuarios u ON v.usuario_id = u.id
JOIN productos p ON v.producto_id = p.id
ORDER BY v.fecha_venta DESC
"""

df_ventas = pd.read_sql(query_ventas, engine)
print(f"Total de registros: {len(df_ventas)}")
df_ventas.head()

# Análisis con pandas
ventas_por_categoria = df_ventas.groupby('categoria')['total'].sum()
print("\nVentas por categoría:")
print(ventas_por_categoria)

# Visualización
ventas_por_categoria.plot(kind='bar', figsize=(10, 6))
plt.title('Ventas por Categoría (desde Base de Datos)')
plt.xlabel('Categoría')
plt.ylabel('Total (€)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

> 💡 **Tip**: Si tienes problemas de conexión, verifica que:
> 1. **Docker esté corriendo**: `docker ps` (deberías ver `ing-datos-db`)
> 2. El **`.env`** esté en la raíz del proyecto con las credenciales correctas
> 3. El **puerto** en `DB_PORT` o `POSTGRES_PORT` coincida con el que usa Docker (por defecto: 5432, o 15432 si cambiaste el puerto)
> 4. Si Docker no está corriendo, ve a `02_sql/` y ejecuta: `docker-compose up -d`

### Magic commands (Opcional)

Si prefieres ejecutar SQL directamente en el notebook sin pandas, puedes usar magic commands:

> ⚠️ **Importante**: Necesitas instalar la extensión `ipython-sql` primero: `pip install ipython-sql`

```python
# Cargar variables de entorno
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path().resolve().parent.parent / '.env'
load_dotenv(env_path)

# Construir connection string desde .env
db_host = os.getenv('DB_HOST', 'localhost')
db_port = os.getenv('DB_PORT', '5432')
db_name = os.getenv('DB_NAME', 'data_engineering')
db_user = os.getenv('DB_USER', 'de_user')
db_password = os.getenv('DB_PASSWORD', 'de_password')

# Cargar extensión SQL
%load_ext sql

# Conectar usando variables del .env
connection_string = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
%sql $connection_string

# Ejecutar queries SQL directamente
%%sql
SELECT 
    p.categoria,
    COUNT(v.id) AS total_ventas,
    SUM(v.total) AS ingresos_totales
FROM productos p
LEFT JOIN ventas v ON p.id = v.producto_id
GROUP BY p.categoria
ORDER BY ingresos_totales DESC
LIMIT 10;
```

> 💡 **Tip**: Los magic commands son útiles para ejecutar SQL rápido, pero para análisis más complejos es mejor usar `pandas.read_sql()` como en el ejemplo anterior.

---

## 💡 Buenas prácticas

### 1. Organiza tu notebook

```markdown
# 1. Introducción
# 2. Cargar datos
# 3. Exploración
# 4. Limpieza
# 5. Análisis
# 6. Visualizaciones
# 7. Conclusiones
```

### 2. Documenta tu proceso

```markdown
## Paso 1: Cargar datos

Cargamos los datos de ventas del último trimestre.
Nota: Los datos vienen de la API de ventas.
```

### 3. Limpia outputs antes de commitear

```bash
# Limpiar outputs
jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace notebook.ipynb
```

### 4. Convierte a otros formatos

```bash
# A HTML
jupyter nbconvert notebook.ipynb --to html

# A PDF
jupyter nbconvert notebook.ipynb --to pdf

# A Python script
jupyter nbconvert notebook.ipynb --to python
```

---

## 🎯 Casos de uso

### Exploración de datos

```python
# Cargar datos primero
df = pd.read_csv('../data/ventas.csv')

# Explora rápidamente
df.head()
df.describe()
df['categoria'].value_counts()
df['ciudad'].value_counts()

# Gráfico rápido
df.groupby('categoria')['total'].sum().plot(kind='bar')
plt.show()
```

### Análisis ad-hoc

```python
# Primero carga los datos
df = pd.read_csv('../data/ventas.csv')

# Prueba diferentes enfoques
# Celda 1: Enfoque A - Ventas por categoría
resultado_a = df.groupby('categoria')['total'].sum()
print("Ventas por categoría:")
print(resultado_a)

# Celda 2: Enfoque B - Ventas por categoría y ciudad (modifica y ejecuta)
resultado_b = df.groupby(['categoria', 'ciudad'])['total'].sum()
print("\nVentas por categoría y ciudad:")
print(resultado_b)
```

### Documentación de análisis

Combina código, resultados y explicaciones en un solo documento.

---

## ⚠️ Cuándo NO usar Notebooks

### ❌ No uses notebooks para:

* **Código de producción**: Usa scripts Python
* **Pipelines automatizados**: Usa scripts o Airflow
* **Código reutilizable**: Usa módulos Python
* **Testing**: Usa frameworks de testing

### ✅ Usa notebooks para:

* Exploración de datos
* Análisis ad-hoc
* Prototipado rápido
* Documentación de análisis
* Presentaciones interactivas

---

## 🔧 Extensiones útiles

### Instalar extensiones

```bash
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
```

### Extensiones recomendadas:

* **Table of Contents**: Índice automático
* **Variable Inspector**: Ver variables activas
* **Code Folding**: Plegar código
* **ExecuteTime**: Tiempo de ejecución

---

## 🎓 Próximos pasos

1. **Abre el notebook de ejemplo**: `03_python/ejemplos/00-notebook.ipynb`
2. **Carga el CSV de ejemplo**: `df = pd.read_csv('../data/ventas.csv')`
3. **Practica los ejemplos**: Ejecuta las celdas de este documento paso a paso
4. **Experimenta**: Modifica los ejemplos y crea tus propios análisis
5. **Continúa con Pandas**: Aprende los fundamentos de Pandas en [Introducción a Pandas](python-para-datos/01-introduccion-pandas.md)

---

## 💡 Tips

* **Guarda frecuentemente**: Ctrl+S
* **Reinicia kernel** si algo se comporta raro
* **Limpia outputs** antes de compartir
* **Usa Markdown** para documentar
* **Organiza** con headers y secciones

---

> **Recuerda**: Notebooks son para explorar y analizar. Para producción, usa scripts Python organizados en módulos.
