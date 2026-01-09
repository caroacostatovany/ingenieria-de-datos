# Ejemplos de Python para Data Engineering

Esta carpeta contiene ejemplos prácticos en formato Jupyter Notebook para Data Engineering.

---

## 📖 Notebooks disponibles

### 📓 Jupyter Notebooks (Recomendado)

* ✅ **[01. Exploración de Datos](01-exploracion-datos.ipynb)**
  * Análisis exploratorio de datos (EDA)
  * Estadísticas descriptivas
  * Visualizaciones básicas
  * Detección de problemas
  * **Referencia:** [Exploración de Datos con Pandas](../pandas/exploracion-datos-pandas.md)

* ✅ **[02. Storytelling con Datos](02-storytelling-datos.ipynb)**
  * Principios de visualización efectiva
  * Crear historias con datos
  * Comparar visualizaciones buenas vs malas
  * **Referencia:** [Storytelling con Datos](../storytelling/storytelling-con-datos.md)

* ✅ **[03. Pipeline ETL](03-pipeline-etl.ipynb)**
  * Pipeline ETL completo
  * Extract, Transform, Load
  * Visualización de resultados
  * **Referencia:** [Fundamentos Python](../fundamentos/fundamentos-python.md)

* ✅ **[04. Limpieza de Datos](04-limpieza-datos.ipynb)**
  * Técnicas de limpieza
  * Manejo de valores nulos
  * Eliminación de duplicados
  * Corrección de tipos
  * **Referencia:** [Python para Datos - Limpieza](../pandas/python-para-datos/03-limpieza-datos.md)

### 📄 Scripts Python (Legacy)

Los siguientes scripts Python están disponibles pero se recomienda usar los notebooks arriba:

* ⚠️ [Pipeline ETL Simple](01-pipeline-etl-simple.py) - Ver [notebook equivalente](03-pipeline-etl.ipynb)
* ⚠️ [Limpieza de Datos](02-limpieza-datos.py) - Ver [notebook equivalente](04-limpieza-datos.ipynb)
* ✅ [Conexión a Base de Datos](03-conexion-db.py)
* ✅ [Procesar Archivos Grandes](04-archivos-grandes.py)

---

## ⚙️ Configuración inicial

Antes de ejecutar los ejemplos, configura tus variables de entorno:

1. **Copia el archivo `.env.example`** de la raíz del proyecto:
   ```bash
   # Desde la raíz del proyecto
   cp .env.example .env
   ```

2. **Edita `.env`** con tus valores reales:
   ```bash
   # Para conexión a base de datos
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=data_engineering
   DB_USER=de_user
   DB_PASSWORD=tu_password_aqui
   
   # Para rutas de archivos
   DATA_SOURCE_PATH=./data/raw
   DATA_OUTPUT_PATH=./data/processed
   ```

3. **Instala dependencias** si es necesario:
   ```bash
   pip install python-dotenv psycopg2-binary pandas
   ```

> 💡 **Nota**: Los ejemplos que usan base de datos requieren que tengas PostgreSQL corriendo (puedes usar el Docker setup de `02_sql/`).

---

## 🚀 Cómo usar estos ejemplos

### Opción 1: Jupyter Notebook (Recomendado)

```bash
# Instalar Jupyter
pip install jupyter

# Iniciar Jupyter
jupyter notebook

# O usar JupyterLab
pip install jupyterlab
jupyter lab
```

### Opción 2: VS Code

VS Code tiene soporte nativo para Jupyter Notebooks. Solo abre el archivo `.ipynb`.

### Opción 3: Google Colab

Sube los notebooks a Google Colab para ejecutarlos en la nube sin instalación.

---

## 💡 Tips

* **Ejecuta las celdas en orden** - Los notebooks están diseñados para ejecutarse secuencialmente
* **Experimenta** - Modifica los ejemplos para aprender
* **Lee las referencias** - Cada notebook referencia documentación detallada
* **Usa los notebooks como plantillas** - Adapta el código a tus necesidades

---

## 📚 Relación con documentación

Cada notebook está vinculado a documentación detallada en los módulos correspondientes:

* **Exploración de Datos** → [Pandas - Exploración](../pandas/exploracion-datos-pandas.md)
* **Storytelling** → [Storytelling con Datos](../storytelling/storytelling-con-datos.md)
* **Pipeline ETL** → [Fundamentos Python](../fundamentos/fundamentos-python.md)
* **Limpieza** → [Python para Datos](../pandas/python-para-datos/)

---

> **Recuerda**: Los notebooks son interactivos. Ejecuta, experimenta y aprende.
