# Datos de Ejemplo

Esta carpeta contiene archivos de datos de ejemplo para practicar con Python y Pandas.

## 📄 Archivos disponibles

### `ventas.csv`

Dataset de ejemplo con datos de ventas que incluye:

- **30 registros** de ventas
- **Columnas**:
  - `id`: Identificador único de la venta
  - `fecha`: Fecha de la venta (formato YYYY-MM-DD)
  - `categoria`: Categoría del producto (Electrónica, Ropa, Hogar)
  - `producto`: Nombre del producto
  - `precio`: Precio unitario del producto
  - `cantidad`: Cantidad vendida
  - `total`: Total de la venta (precio × cantidad)
  - `ciudad`: Ciudad donde se realizó la venta (Madrid, Barcelona, Valencia, Sevilla)

### `productos.csv`

Dataset de ejemplo con información de productos que incluye:

- **30 registros** de productos (coincide con los productos en `ventas.csv`)
- **Columnas**:
  - `producto`: Nombre del producto (clave para hacer merge con `ventas.csv`)
  - `categoria`: Categoría del producto (Electrónica, Ropa, Hogar)
  - `precio_base`: Precio base del producto
  - `stock`: Cantidad disponible en inventario
  - `proveedor`: Nombre del proveedor (TechCorp, FashionStore, HomeGoods)
  - `fecha_lanzamiento`: Fecha de lanzamiento del producto (formato YYYY-MM-DD)

> 💡 **Ideal para practicar merge/join**: Puedes combinar `ventas.csv` y `productos.csv` usando la columna `producto` para enriquecer los datos de ventas con información de inventario y proveedores.

### `ventas.parquet`

Versión en formato Parquet del dataset de ventas:

- **Mismo contenido** que `ventas.csv` pero en formato Parquet
- **Ventajas de Parquet**:
  - ✅ Más rápido de leer que CSV
  - ✅ Menor tamaño (compresión)
  - ✅ Preserva tipos de datos automáticamente
  - ✅ Ideal para datos procesados

> 💡 **Ideal para practicar manejo de archivos**: Compara el rendimiento y tamaño entre CSV y Parquet. Aprende a leer y escribir diferentes formatos.

## 🚀 Cómo usar

### Desde un notebook en `03_python/ejemplos/`:

```python
import pandas as pd

# Cargar el CSV
df = pd.read_csv('../data/ventas.csv')
df.head()
```

### Desde un notebook en `03_python/pandas/`:

```python
import pandas as pd

# Cargar el CSV
df = pd.read_csv('../data/ventas.csv')
df.head()
```

### Desde cualquier notebook en el proyecto:

```python
import pandas as pd
from pathlib import Path

# Ruta relativa desde la raíz del proyecto
data_path = Path('03_python/data/ventas.csv')
df = pd.read_csv(data_path)
df.head()
```

## 💡 Ejercicios sugeridos

### Con `ventas.csv`:
1. **Exploración básica**: Usa `df.head()`, `df.info()`, `df.describe()`
2. **Agregaciones**: Calcula ventas por categoría, ciudad o mes
3. **Visualizaciones**: Crea gráficos de barras, líneas, histogramas
4. **Limpieza**: Practica con `dropna()`, `drop_duplicates()`, conversión de tipos
5. **Análisis**: Encuentra patrones, tendencias, outliers

### Con `ventas.csv` y `productos.csv` (merge/join):
1. **Merge básico**: Combina ventas con información de productos
2. **Análisis enriquecido**: Analiza ventas considerando stock y proveedores
3. **Left/Right/Inner joins**: Práctica con diferentes tipos de merge
4. **Análisis de inventario**: Identifica productos con bajo stock y altas ventas

### Con `ventas.csv` y `ventas.parquet` (manejo de archivos):
1. **Comparar formatos**: Lee ambos y compara tamaño y velocidad
2. **Convertir formatos**: Convierte CSV a Parquet y viceversa
3. **Optimización**: Aprende cuándo usar cada formato
4. **Filtros pushdown**: Práctica con filtros en Parquet

---

> 💡 **Tip**: Este dataset es pequeño y simple, perfecto para aprender. En proyectos reales trabajarás con datasets mucho más grandes y complejos.
