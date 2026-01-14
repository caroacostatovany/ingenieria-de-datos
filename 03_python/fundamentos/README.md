# Fundamentos de Python

Esta sección cubre los fundamentos de Python necesarios para Data Engineering. **Trabajaremos con Jupyter Notebooks** para aprender de forma interactiva.

---

## 🚀 Empezar: Instalar Jupyter Notebook

Antes de comenzar, necesitas instalar Jupyter Notebook para trabajar con Python de forma interactiva.

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

### Paso 4: Crear tu primer notebook

1. En la interfaz de Jupyter, haz clic en **"New"** → **"Python 3"**
2. Se abrirá un nuevo notebook
3. Escribe tu primer código:
   ```python
   print("¡Hola, Data Engineering!")
   ```
4. Presiona **Shift + Enter** para ejecutar la celda

> 💡 **Tip**: Guarda tu notebook con un nombre descriptivo (ej: `01-fundamentos-python.ipynb`)

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

* ✅ **[Scripts vs Módulos](scripts-vs-modulos.md)** *(Opcional - para más adelante)*
  * Cuándo usar scripts simples
  * Cuándo modularizar código
  * Estructura de proyectos
  * Reutilización de código
  
  > 💡 **Nota**: Por ahora trabajaremos solo con Jupyter Notebooks. Los scripts Python los veremos más adelante cuando construyamos pipelines.

---

## 🎯 Objetivo

Al finalizar esta sección, deberías poder:

* **Trabajar con Jupyter Notebooks** para escribir y ejecutar código Python
* Escribir código Python claro y mantenible en notebooks
* Leer y escribir diferentes formatos de archivos (CSV, JSON, Parquet)
* Conectar Python con bases de datos desde notebooks
* Usar notebooks para explorar y analizar datos de forma interactiva

---

## 🚀 Próximo paso

Continúa con **[Pandas](../pandas/)** para manipulación y análisis de datos.

---

> **Recuerda**: Los fundamentos sólidos te permitirán escribir código Python efectivo en Data Engineering.
