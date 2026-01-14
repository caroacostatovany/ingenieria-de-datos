# Ejemplos de Modelado y Calidad

Esta carpeta contiene notebooks Jupyter con ejemplos prácticos de modelado analítico y calidad de datos.

---

## 📖 Notebooks disponibles

### 📓 Jupyter Notebooks

* ✅ **[01. Modelado Star Schema](01-modelado-star-schema.ipynb)**
  * Crear tablas de hechos y dimensiones
  * Visualizar estructura del modelo
  * Consultar datos usando el modelo
  * **Referencia:** [Modelado Analítico](../modelado/modelado-analitico.md)

* ✅ **[02. Calidad de Datos](02-calidad-datos.ipynb)**
  * Calcular dimensiones de calidad
  * Completitud, Exactitud, Unicidad
  * Dashboard de calidad
  * **Referencia:** [Calidad de Datos](../calidad/calidad-de-datos.md)

* ✅ **[03. Great Expectations](03-great-expectations.ipynb)**
  * Crear expectativas sobre datos
  * Validar automáticamente
  * Generar reportes
  * **Referencia:** [Great Expectations](../calidad/herramientas/great-expectations-para-calidad.md)

* ✅ **[04. Pandera Validación](04-pandera-validacion.ipynb)**
  * Definir esquemas de validación
  * Validar DataFrames
  * Integrar en pipelines
  * **Referencia:** [Pandera](../calidad/herramientas/pandera-validacion-pandas.md)

* ✅ **[05. Testing de Datos](05-testing-datos.ipynb)**
  * Tests unitarios para transformaciones
  * Tests de integridad
  * Tests de calidad
  * Tests de reglas de negocio
  * **Referencia:** [Testing de Datos](../calidad/validaciones/testing-de-datos.md)

* ✅ **[06. Validaciones](06-validaciones.ipynb)**
  * Validación de esquema
  * Validación de rangos
  * Validación de completitud
  * Integración en pipelines
  * **Referencia:** [Validaciones](../calidad/validaciones/validaciones.md)

---

## 🚀 Cómo usar estos notebooks

### Opción 1: Jupyter Notebook

```bash
# Instalar Jupyter
pip install jupyter pandas matplotlib seaborn

# Iniciar Jupyter
jupyter notebook

# O JupyterLab
jupyter lab
```

### Opción 2: VS Code

VS Code tiene soporte nativo para Jupyter Notebooks. Solo abre el archivo `.ipynb`.

### Opción 3: Google Colab

Sube los notebooks a Google Colab para ejecutarlos en la nube.

---

## 💡 Tips

* **Ejecuta las celdas en orden** - Los notebooks están diseñados para ejecutarse secuencialmente
* **Experimenta** - Modifica los ejemplos para aprender
* **Lee las referencias** - Cada notebook referencia documentación detallada
* **Instala dependencias** - Algunos notebooks requieren librerías adicionales (Great Expectations, Pandera)

---


> **Recuerda**: Los notebooks son interactivos. Ejecuta, experimenta y aprende. Los conceptos aquí son fundamentales para Data Engineering.
