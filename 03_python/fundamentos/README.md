# Fundamentos de Python

Esta sección cubre los fundamentos de Python necesarios para Data Engineering. **Trabajaremos con Jupyter Notebooks** para aprender de forma interactiva.

---

## 🚀 Empezar: Trabajar con Jupyter Notebooks

### Si estás usando Cursor

Si usas **Cursor**, es muy simple:

1. **Abre el notebook de ejemplo**:
   - Ve a `03_python/ejemplos/00-notebook.ipynb`
   - Ábrelo en Cursor (haz doble clic o click derecho → "Open with Cursor")

2. **Selecciona el kernel de Python**:
   - En la parte superior del notebook, verás un selector de kernel
   - Haz clic y selecciona tu entorno Python (el que configuraste con `pyenv` o tu Python global)
   - Si no aparece, Cursor te pedirá instalar la extensión de Jupyter (acepta)

3. **¡Empieza a escribir código!**:
   - El notebook está vacío para que agregues tus propias celdas
   - Presiona `Shift + Enter` para ejecutar una celda
   - Agrega nuevas celdas con el botón `+` o `Cmd/Ctrl + B`

> 💡 **Tip**: Cursor tiene soporte nativo para Jupyter Notebooks. No necesitas instalar nada adicional, solo abrir el archivo `.ipynb` y seleccionar el kernel.

---

### Si NO estás usando Cursor: Instalar Jupyter Notebook

Si prefieres usar Jupyter Notebook tradicional, sigue estos pasos:

### Paso 1: Verificar Python

Asegúrate de tener Python instalado:

```bash
python3 --version
# Debería mostrar Python 3.8 o superior
```

> 💡 **Si usas `pyenv`**: Asegúrate de tener un entorno virtual activado. Revisa [SETUP.md](../../SETUP.md) para más detalles.

### Paso 2: Instalar Jupyter Notebook

```bash
# Instalar Jupyter y librerías básicas
pip install jupyter pandas matplotlib seaborn

# O si usas pyenv-virtualenv:
# pyenv virtualenv 3.11.0 python-fundamentos
# pyenv activate python-fundamentos
# pip install jupyter pandas matplotlib seaborn
```

### Paso 3: Iniciar Jupyter Notebook

```bash
# Desde la carpeta donde quieres trabajar
jupyter notebook

# O usar JupyterLab (interfaz más moderna)
jupyter lab
```

Se abrirá en tu navegador en `http://localhost:8888`

### Paso 4: Abrir el notebook de ejemplo

1. En la interfaz de Jupyter, navega a `03_python/ejemplos/`
2. Abre el archivo **`00-notebook.ipynb`** (está vacío para que empieces desde cero)
3. O crea un nuevo notebook: haz clic en **"New"** → **"Python 3"**
4. Escribe tu primer código:
   ```python
   print("¡Hola, Data Engineering!")
   ```
5. Presiona **Shift + Enter** para ejecutar la celda

> 💡 **Tip**: El notebook `00-notebook.ipynb` está vacío intencionalmente. Úsalo como punto de partida para tus ejercicios.

---

## 📖 Contenido

* ✅ **[Fundamentos Python para DE](fundamentos-python.md)**
  * Sintaxis esencial
  * Estructuras de datos
  * Control de flujo
  * Funciones
  * Librerías clave

* ✅ **[Manejo de archivos](manejo-de-archivos.md)**
  * Leer/escribir CSV, JSON, Parquet, Excel
  * Trabajar con APIs
  * Conexión a bases de datos
  * Procesar archivos grandes

* ✅ **[Scripts vs Módulos](scripts-vs-modulos.md)**
  * Cuándo usar scripts simples
  * Cuándo modularizar código
  * Estructura de proyectos
  * Reutilización de código
  
  > 💡 **Nota**: Por ahora trabajaremos principalmente con Jupyter Notebooks. Los scripts Python los veremos más adelante cuando construyamos pipelines. Sin embargo, entender estos conceptos te ayudará a organizar mejor tu código.

* ✅ **[Storytelling con Datos](storytelling-con-datos.md)**
  * Comunicar hallazgos a personas de negocios
  * Principios de visualización efectiva
  * Estructura de historias con datos
  * Lenguaje de negocio vs técnico
  
  > 💡 **Importante**: En Data Engineering no solo construyes pipelines, también necesitas comunicar resultados a ejecutivos y stakeholders. El storytelling es tu puente entre datos técnicos y decisiones de negocio.

---

## 🎯 Objetivo

Al finalizar esta sección, deberías poder:

* **Trabajar con Jupyter Notebooks** para escribir y ejecutar código Python
* Escribir código Python claro y mantenible en notebooks
* Leer y escribir diferentes formatos de archivos (CSV, JSON, Parquet, Excel)
* Procesar archivos grandes usando técnicas de chunking
* Organizar código en scripts y módulos cuando sea apropiado
* **Comunicar hallazgos efectivamente** a personas de negocios usando storytelling con datos

---

## 🚀 Próximo paso

Ahora que sabes los fundamentos de Python, continúa con:

1. **[Pandas](../pandas/)** - Manipulación y análisis de datos con pandas
2. **[Jupyter Notebooks para Datos](../pandas/jupyter-notebooks-para-datos.md)** - Exploración de datos (EDA) y análisis interactivo

**Flujo completo de Fundamentos:**
1. Fundamentos Python → 2. Manejo de archivos → 3. Scripts vs Módulos → 4. Storytelling con Datos

---

> **Recuerda**: Los fundamentos sólidos te permitirán escribir código Python efectivo en Data Engineering.
