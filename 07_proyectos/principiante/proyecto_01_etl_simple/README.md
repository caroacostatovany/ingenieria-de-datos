# Proyecto 1: Pipeline ETL Simple

Construye tu primer pipeline ETL completo: extrae datos de CSV, transforma y limpia, y carga a archivos de salida.

> ✅ **Este proyecto incluye código funcional y un dataset de ejemplo listo para usar**

---

## 🎯 Objetivo

Aprender los fundamentos de un pipeline ETL:
* **Extract**: Leer datos de archivos CSV
* **Transform**: Limpiar y transformar datos
* **Load**: Guardar datos transformados en diferentes formatos

---

## 📋 Requisitos previos

* Python 3.8+
* Conocimientos básicos de Python y Pandas

---

## 🚀 Inicio Rápido

### 1. Preparar entorno

```bash
# Navegar al proyecto
cd 07_proyectos/principiante/proyecto_01_etl_simple

# Crear entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Ejecutar el pipeline

```bash
# Ejecutar el pipeline
python pipeline.py
```

**¡Eso es todo!** El pipeline:
- ✅ Lee el archivo `data/ventas.csv`
- ✅ Transforma y limpia los datos
- ✅ Guarda los resultados en `output/`

---

## 📁 Estructura del proyecto

```
proyecto_01_etl_simple/
├── README.md                 # Este archivo
├── requirements.txt          # Dependencias Python
├── pipeline.py              # Pipeline ETL completo y funcional
├── data/
│   └── ventas.csv          # Dataset de ejemplo (15 registros)
└── output/                  # Directorio de salida (se crea automáticamente)
    ├── ventas_transformadas_YYYYMMDD_HHMMSS.csv
    ├── ventas_transformadas_YYYYMMDD_HHMMSS.parquet
    └── resumen_ventas_YYYYMMDD_HHMMSS.csv
```

---

## 📊 Dataset de ejemplo

El archivo `data/ventas.csv` contiene datos de ventas con las siguientes columnas:

| Columna | Tipo | Descripción |
|---------|------|-------------|
| fecha | string | Fecha de la venta (YYYY-MM-DD) |
| producto | string | Nombre del producto |
| cantidad | int | Cantidad vendida |
| precio | float | Precio unitario |
| cliente | string | Nombre del cliente |
| ciudad | string | Ciudad donde se realizó la venta |

**Ejemplo de datos:**
```csv
fecha,producto,cantidad,precio,cliente,ciudad
2024-01-15,Producto A,5,10.50,Cliente 1,Madrid
2024-01-16,Producto B,3,25.00,Cliente 2,Barcelona
...
```

---

## 🔍 ¿Qué hace el pipeline?

### Extract (Extracción)
- Lee el archivo CSV `data/ventas.csv`
- Valida que el archivo existe
- Muestra estadísticas básicas

### Transform (Transformación)
1. **Convierte fechas** a formato datetime
2. **Calcula total** por venta (precio × cantidad)
3. **Agrega columna de mes** para análisis
4. **Elimina duplicados**
5. **Elimina registros con valores nulos** en columnas críticas
6. **Filtra registros válidos** (total > 0)
7. **Ordena por fecha**

### Load (Carga)
Guarda los datos en 3 archivos:
1. **CSV**: `ventas_transformadas_*.csv` - Formato legible
2. **Parquet**: `ventas_transformadas_*.parquet` - Formato eficiente
3. **Resumen**: `resumen_ventas_*.csv` - Agregaciones por producto

---

## 📝 Ejemplo de salida

Después de ejecutar el pipeline, verás algo como:

```
============================================================
🚀 Pipeline ETL Simple - Ejecutando...
============================================================
📥 Extrayendo datos de data/ventas.csv...
✅ Extraídos 15 registros
   Columnas: fecha, producto, cantidad, precio, cliente, ciudad
🔄 Transformando datos...
✅ Transformación completada: 15 registros válidos
   Total de ventas: €450.00
💾 Guardando datos transformados...
   ✅ CSV guardado: output/ventas_transformadas_20240115_143022.csv
   ✅ Parquet guardado: output/ventas_transformadas_20240115_143022.parquet
   ✅ Resumen guardado: output/resumen_ventas_20240115_143022.csv
✅ Pipeline completado exitosamente!

============================================================
✨ Pipeline ejecutado exitosamente!
📁 Archivos de salida en: output
============================================================
```

---

## 🧪 Experimentar con el código

### Modificar el dataset

1. Edita `data/ventas.csv` y agrega más registros
2. Ejecuta el pipeline nuevamente: `python pipeline.py`
3. Observa cómo se procesan los nuevos datos

### Agregar nuevas transformaciones

Edita `pipeline.py` en la función `transform()`:

```python
def transform(df: pd.DataFrame) -> pd.DataFrame:
    # ... código existente ...
    
    # Agregar nueva transformación
    df_transformed['descuento'] = df_transformed['total'] * 0.1  # 10% descuento
    
    return df_transformed
```

### Cambiar el formato de salida

Modifica la función `load()` para guardar en otros formatos:

```python
# Guardar en JSON
df.to_json(output_dir / 'ventas.json', orient='records', indent=2)

# Guardar en Excel
df.to_excel(output_dir / 'ventas.xlsx', index=False)
```

---

## 📚 Conceptos aprendidos

Al completar este proyecto, habrás aprendido:

✅ **Extract**: Cómo leer datos de archivos CSV con Pandas  
✅ **Transform**: Técnicas de limpieza y transformación de datos  
✅ **Load**: Cómo guardar datos en diferentes formatos  
✅ **Manejo de errores**: Validación de archivos y datos  
✅ **Estructura de proyectos**: Organización de código en funciones  
✅ **Logging**: Mensajes informativos durante la ejecución  

---

## 🔗 Próximos pasos

Una vez que domines este pipeline básico:

1. **Proyecto 2**: [Análisis de Datos con Pandas](../proyecto_02_analisis_pandas/README.md)
   - Análisis exploratorio de datos (EDA)
   - Visualizaciones con Matplotlib/Seaborn

2. **Proyecto 3**: [Pipeline con Docker](../proyecto_03_docker_pipeline/README.md)
   - Containerizar el pipeline
   - Ejecutar en contenedores Docker

3. **Módulo SQL**: [02_sql](../../../02_sql/README.md)
   - Aprender a cargar datos a bases de datos
   - Usar SQL para transformaciones

---

## 🐛 Solución de problemas

### Error: "No se encontró el archivo"

**Solución**: Asegúrate de ejecutar el script desde el directorio del proyecto:
```bash
cd 07_proyectos/principiante/proyecto_01_etl_simple
python pipeline.py
```

### Error: "ModuleNotFoundError: No module named 'pandas'"

**Solución**: Instala las dependencias:
```bash
pip install -r requirements.txt
```

### Error al guardar Parquet

**Solución**: Instala pyarrow:
```bash
pip install pyarrow
```

---

## 💡 Tips

- **Revisa los archivos de salida** para entender qué datos se generaron
- **Experimenta modificando el código** para ver cómo cambian los resultados
- **Agrega más datos** al CSV para probar con datasets más grandes
- **Lee el código línea por línea** para entender cada transformación

---

## 📖 Recursos adicionales

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Python para Data Engineers](../../../03_python/fundamentos/fundamentos-python.md)
- [Manejo de Archivos](../../../03_python/fundamentos/manejo-de-archivos.md)
- [¿Qué es un Pipeline?](../../../01_fundamentos/01_que-es-un-pipeline.md)

---

> **💡 Recuerda**: Este es un ejemplo educativo. En producción, agrega más validaciones, logging estructurado, y manejo robusto de errores.
