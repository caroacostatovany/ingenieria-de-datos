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

## 🚀 Instalación y configuración

### Instalación

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

df = pd.read_csv('datos.csv')
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

# Celda 2: Cargar datos
df = pd.read_csv('ventas.csv')
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
```

### 3. Análisis

```python
# Celda 6: Agregaciones
ventas_por_categoria = df.groupby('categoria')['total'].sum()
ventas_por_categoria

# Celda 7: Visualización
ventas_por_categoria.plot(kind='bar')
plt.title('Ventas por Categoría')
plt.show()
```

### 4. Conclusiones

```markdown
## Conclusiones

- La categoría "Electrónica" tiene las mayores ventas
- Hay un crecimiento del 15% respecto al mes anterior
- Recomendación: Invertir más en marketing de electrónica
```

---

## 📊 Visualizaciones

### Matplotlib básico

```python
import matplotlib.pyplot as plt

# Gráfico de barras
df.groupby('categoria')['total'].sum().plot(kind='bar')
plt.title('Ventas por Categoría')
plt.xlabel('Categoría')
plt.ylabel('Total')
plt.show()

# Gráfico de líneas
df.groupby('mes')['total'].sum().plot(kind='line')
plt.show()

# Histograma
df['edad'].hist(bins=20)
plt.show()
```

### Seaborn (más bonito)

```python
import seaborn as sns

# Gráfico de barras
sns.barplot(data=df, x='categoria', y='total')

# Box plot
sns.boxplot(data=df, x='categoria', y='precio')

# Heatmap de correlación
sns.heatmap(df.corr(), annot=True)
```

---

## 🔗 Integración con SQL

### Conectar a base de datos

```python
from sqlalchemy import create_engine
import pandas as pd

# Conectar
engine = create_engine('postgresql://user:pass@localhost/db')

# Ejecutar query
query = """
SELECT 
    categoria,
    SUM(total) AS total_ventas
FROM ventas
GROUP BY categoria
"""

df = pd.read_sql(query, engine)
df
```

### Magic commands

```python
# Ejecutar SQL directamente (requiere extensión)
%load_ext sql
%sql postgresql://user:pass@localhost/db

%%sql
SELECT * FROM ventas LIMIT 10;
```

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
# Explora rápidamente
df.head()
df.describe()
df['columna'].value_counts()
df.plot()
```

### Análisis ad-hoc

```python
# Prueba diferentes enfoques
# Celda 1: Enfoque A
resultado_a = df.groupby('cat')['total'].sum()

# Celda 2: Enfoque B (modifica y ejecuta)
resultado_b = df.groupby(['cat', 'mes'])['total'].sum()
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

1. **Instala Jupyter**: `pip install jupyter pandas matplotlib`
2. **Crea tu primer notebook**: Explora un dataset
3. **Practica visualizaciones**: Gráficos comunes
4. **Documenta tu análisis**: Combina código y explicaciones

---

## 💡 Tips

* **Guarda frecuentemente**: Ctrl+S
* **Reinicia kernel** si algo se comporta raro
* **Limpia outputs** antes de compartir
* **Usa Markdown** para documentar
* **Organiza** con headers y secciones

---

> **Recuerda**: Notebooks son para explorar y analizar. Para producción, usa scripts Python organizados en módulos.
