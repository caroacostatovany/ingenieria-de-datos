# Proyecto 2: Análisis de Datos con Pandas

Realiza un análisis exploratorio completo de datos usando Pandas y crea visualizaciones para comunicar tus hallazgos.

---

## 🎯 Objetivo

Aprender a:
* Explorar datos con Pandas
* Realizar análisis exploratorio de datos (EDA)
* Crear visualizaciones efectivas
* Comunicar insights de forma clara

---

## 📋 Requisitos previos

* Python 3.8+
* Conocimientos básicos de Pandas
* Jupyter Notebook (recomendado)

---

## 🚀 Pasos del proyecto

### 1. Preparar entorno

```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install pandas matplotlib seaborn jupyter
```

### 2. Estructura del proyecto

```
proyecto_02_analisis_pandas/
├── README.md
├── requirements.txt
├── data/
│   └── ecommerce_data.csv
├── notebooks/
│   └── 01_analisis_exploratorio.ipynb
├── src/
│   └── utils.py
└── reports/
    └── insights.md
```

### 3. Crear datos de ejemplo

Crea `data/ecommerce_data.csv` con datos de e-commerce:

```csv
order_id,date,customer_id,product_category,product_name,quantity,unit_price,total_price,region
1001,2024-01-15,101,Electronics,Smartphone,1,599.99,599.99,North
1002,2024-01-15,102,Clothing,T-Shirt,3,19.99,59.97,South
1003,2024-01-16,101,Electronics,Headphones,2,79.99,159.98,North
1004,2024-01-16,103,Books,Python Guide,1,29.99,29.99,East
1005,2024-01-17,102,Clothing,Jeans,1,49.99,49.99,South
```

### 4. Análisis exploratorio

Crea `notebooks/01_analisis_exploratorio.ipynb`:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar estilo
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Cargar datos
df = pd.read_csv('../data/ecommerce_data.csv')
df['date'] = pd.to_datetime(df['date'])

# 1. Primer vistazo
print("=== INFORMACIÓN BÁSICA ===")
print(f"Shape: {df.shape}")
print(f"\nColumnas: {df.columns.tolist()}")
print(f"\nTipos:\n{df.dtypes}")
print(f"\nPrimeras filas:")
df.head()

# 2. Estadísticas descriptivas
print("\n=== ESTADÍSTICAS DESCRIPTIVAS ===")
df.describe()

# 3. Valores nulos
print("\n=== VALORES NULOS ===")
print(df.isnull().sum())

# 4. Análisis por categoría
print("\n=== VENTAS POR CATEGORÍA ===")
ventas_categoria = df.groupby('product_category').agg({
    'total_price': ['sum', 'mean', 'count']
}).round(2)
print(ventas_categoria)

# Visualización
plt.figure(figsize=(10, 6))
df.groupby('product_category')['total_price'].sum().sort_values(ascending=True).plot(kind='barh')
plt.title('Ventas Totales por Categoría')
plt.xlabel('Ventas Totales (€)')
plt.tight_layout()
plt.show()

# 5. Análisis temporal
print("\n=== TENDENCIA TEMPORAL ===")
ventas_diarias = df.groupby('date')['total_price'].sum()
print(ventas_diarias)

plt.figure(figsize=(12, 6))
ventas_diarias.plot(marker='o')
plt.title('Ventas Diarias')
plt.xlabel('Fecha')
plt.ylabel('Ventas Totales (€)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6. Análisis por región
print("\n=== VENTAS POR REGIÓN ===")
ventas_region = df.groupby('region')['total_price'].sum().sort_values(ascending=False)
print(ventas_region)

plt.figure(figsize=(8, 6))
ventas_region.plot(kind='bar', color='steelblue')
plt.title('Ventas por Región')
plt.xlabel('Región')
plt.ylabel('Ventas Totales (€)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 7. Top productos
print("\n=== TOP 10 PRODUCTOS ===")
top_productos = df.groupby('product_name')['total_price'].sum().sort_values(ascending=False).head(10)
print(top_productos)

# 8. Insights
print("\n=== INSIGHTS ===")
print(f"1. Total de ventas: €{df['total_price'].sum():,.2f}")
print(f"2. Promedio por orden: €{df['total_price'].mean():,.2f}")
print(f"3. Categoría más vendida: {df.groupby('product_category')['total_price'].sum().idxmax()}")
print(f"4. Región con más ventas: {df.groupby('region')['total_price'].sum().idxmax()}")
print(f"5. Total de órdenes: {df['order_id'].nunique()}")
```

### 5. Documentar insights

Crea `reports/insights.md`:

```markdown
# Insights del Análisis de E-commerce

## Resumen Ejecutivo
- Total de ventas: €X
- Período analizado: [fecha inicio] - [fecha fin]
- Total de órdenes: X

## Hallazgos Principales

### 1. Ventas por Categoría
- [Categoría] es la más vendida con €X
- [Categoría] tiene potencial de crecimiento

### 2. Tendencia Temporal
- Las ventas [aumentan/disminuyen] en [período]
- Pico de ventas en [fecha]

### 3. Análisis Geográfico
- [Región] genera más ventas
- Oportunidad en [región]

## Recomendaciones
1. [Recomendación 1]
2. [Recomendación 2]
3. [Recomendación 3]
```

---

## ✅ Checklist de completado

- [ ] Entorno configurado con todas las dependencias
- [ ] Datos de ejemplo creados
- [ ] Análisis exploratorio completo realizado
- [ ] Visualizaciones creadas (mínimo 5 gráficos)
- [ ] Insights documentados
- [ ] Reporte ejecutivo creado
- [ ] Código limpio y documentado

---

## 🎓 Conceptos aprendidos

* ✅ Análisis exploratorio de datos (EDA)
* ✅ Estadísticas descriptivas
* ✅ Visualización de datos
* ✅ Agrupaciones y agregaciones
* ✅ Análisis temporal
* ✅ Comunicación de insights

---

## 🚀 Próximo paso

Después de completar este proyecto:
* Agrega más análisis (correlaciones, outliers)
* Crea dashboard interactivo
* Avanza a **[Proyecto 3: Pipeline con Docker](../proyecto_03_docker_pipeline/)**

---

> **Recuerda**: La visualización es clave para comunicar insights. Practica crear gráficos claros y efectivos.
