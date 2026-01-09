# 📊 Ingenería de datos

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![Maintenance](https://img.shields.io/badge/maintained-yes-green.svg)
![Language](https://img.shields.io/badge/language-español-red.svg)
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)

<!-- Actualiza USERNAME y REPO con tu información de GitHub -->
[![GitHub stars](https://img.shields.io/github/stars/USERNAME/REPO.svg?style=social&label=Star)](https://github.com/USERNAME/REPO)
[![GitHub forks](https://img.shields.io/github/forks/USERNAME/REPO.svg?style=social&label=Fork)](https://github.com/USERNAME/REPO/fork)
[![GitHub issues](https://img.shields.io/github/issues/USERNAME/REPO.svg)](https://github.com/USERNAME/REPO/issues)
[![GitHub contributors](https://img.shields.io/github/contributors/USERNAME/REPO.svg)](https://github.com/USERNAME/REPO/graphs/contributors)

Este repositorio está diseñado para aprender **Ingeniería de Datos desde cero hasta un nivel profesional**, con **bases sólidas**, ejemplos prácticos y un enfoque moderno donde la **AI se usa como copiloto**, no como reemplazo.

Todo el contenido está en **español** y pensado para personas de **todos los niveles**.

---

## 🎯 Objetivo del repositorio

Ayudarte a:

* Entender **qué hace un/a Data Engineer**
* Construir **bases técnicas reales** (no solo herramientas)
* Aprender a escribir **SQL y Python de calidad**
* Diseñar **pipelines mantenibles**
* Prepararte para escalar hacia **arquitecturas como Data Lakes**

---

## 👥 ¿Para quién es?

* 👶 **Principiantes** que quieren entrar al mundo de datos
* 👩‍💻 **Perfiles intermedios** que ya usan SQL/Python pero quieren hacerlo mejor
* 🚀 **Perfiles avanzados** que buscan reforzar fundamentos y buenas prácticas

---

## 🚀 Cómo empezar

1. **⭐ PRIMERO:** [Configura Cursor](06_inteligencia_artificial/herramientas/cursor-para-data-engineers.md) - Tu copiloto de AI
2. **Configura tu entorno:** Sigue la [Guía de Configuración Inicial](SETUP.md) completa
3. **Lee** [¿Qué es Data Engineering?](00_introduccion/que-es-data-engineering.md)
4. **Revisa** el [Roadmap](00_introduccion/roadmap-data-engineer.md)
5. **Sigue** el orden sugerido en el roadmap
6. **Practica** con los ejercicios y proyectos
7. **Usa el chat de Cursor** para hacer preguntas sobre cualquier contenido

> 💡 **Nuevo**: Revisa [SETUP.md](SETUP.md) para una guía completa de configuración inicial con todos los requisitos y pasos detallados.

### ⚙️ Configuración de variables de entorno

Este proyecto usa archivos `.env` para gestionar configuraciones de forma segura. Lee **[Archivos .env para Data Engineers](01_fundamentos/04_archivos-env-para-data-engineers.md)** para más detalles.

**Configuración rápida:**
```bash
# 1. Copia el archivo de ejemplo desde la raíz del proyecto
cp .env.example .env

# 2. Edita .env con tus valores reales
nano .env  # o tu editor preferido

# 3. Para el módulo SQL con Docker (opcional)
cd 02_sql
cp ../.env.example .env  # o usa el .env.example específico del módulo
```

**Variables importantes a configurar:**
- **Base de datos**: `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`
- **Rutas**: `DATA_SOURCE_PATH`, `DATA_OUTPUT_PATH`
- **APIs**: `API_KEY`, `API_URL` (si usas APIs externas)

> 💡 **Nota**: El archivo `.env` está en `.gitignore` (no se commitea). Solo el `.env.example` está versionado. Los ejemplos y ejercicios del proyecto usan estas variables automáticamente.

---

## 🧭 Índice visual (ruta de aprendizaje)

**Elige tu punto de partida:**

* 👶 **Si vas empezando:** empieza por **Introducción → Fundamentos**
* 👩‍💻 **Si ya manejas SQL/Python:** salta a **Modelado, Calidad y Pipelines**
* 🚀 **Si buscas enfoque moderno:** revisa **AI como copiloto** y **Proyectos End-to-End**

---

### 🟩 Nivel 0 — Introducción

* ✅ [¿Qué es Data Engineering?](00_introduccion/que-es-data-engineering.md)
* ✅ [Roadmap para convertirte en Data Engineer](00_introduccion/roadmap-data-engineer.md)
* ✅ [Roles en datos](00_introduccion/roles-en-datos.md)

---

### 🟨 Nivel 1 — Fundamentos

* 📘 [Fundamentos (carpeta)](01_fundamentos/)
* ✅ [00. Tipos de Datos](01_fundamentos/00_tipos-de-datos.md)
* ✅ [01. ¿Qué es un Pipeline?](01_fundamentos/01_que-es-un-pipeline.md)
* ✅ [02. Batch vs Streaming](01_fundamentos/02_batch-vs-streaming.md)
* ✅ [03. Git y GitHub](01_fundamentos/03_git-y-github-para-data-engineers.md)
* ✅ [04. Archivos .env](01_fundamentos/04_archivos-env-para-data-engineers.md)
* ✅ [05. Docker](01_fundamentos/05_docker-para-data-engineers.md)
* ✅ [06. Introducción a SQL](01_fundamentos/06_introduccion-sql.md)
* ✅ [07. Buenas Prácticas](01_fundamentos/07_buenas-practicas.md)
* ✅ [08. Data Engineering en la Nube](01_fundamentos/08_data-engineering-en-la-nube.md)

---

### 🟧 Nivel 2 — SQL para Data Engineers

* 📘 [SQL (carpeta)](02_sql/)
* ✅ [SQL vs PostgreSQL](02_sql/sql-vs-postgresql.md) - ¿Por qué PostgreSQL?
* ✅ [Herramientas SQL](02_sql/herramientas/)
  * DBeaver (visualización y generación de queries)
  * Otras herramientas (pgAdmin, TablePlus, etc.)
* ✅ [SQL básico](02_sql/sql-basico/)
* ✅ [SQL intermedio](02_sql/sql-intermedio/)
* ✅ [SQL avanzado](02_sql/sql-avanzado/)
* ✅ [Modelado Relacional](02_sql/modelado-relacional.md)
* ✅ [Ejercicios](02_sql/ejercicios/)

---

### 🟦 Nivel 3 — Python aplicado

* 📘 [Python (carpeta)](03_python/)
* ✅ [Fundamentos](03_python/fundamentos/)
  * Sintaxis esencial, scripts vs módulos, manejo de archivos
* ✅ [Pandas](03_python/pandas/)
  * Manipulación de datos, exploración (EDA), Jupyter Notebooks
* ✅ [Storytelling con Datos](03_python/storytelling/)
  * Comunicar insights efectivamente, visualizaciones
* ✅ [Ejemplos](03_python/ejemplos/)

---

### 🟪 Nivel 4 — Modelado y calidad

* 📘 [Modelado y calidad (carpeta)](04_modelado_y_calidad/)
* ✅ [Modelado](04_modelado_y_calidad/modelado/)
  * Modelos dimensionales, Star Schema, Snowflake
* ✅ [Calidad de Datos](04_modelado_y_calidad/calidad/)
  * Métricas y KPIs de calidad
  * Validaciones y Testing
  * Herramientas (Great Expectations, Pandera)
* ✅ [Ejemplos (Notebooks)](04_modelado_y_calidad/ejemplos/)
  * Modelado Star Schema, Calidad, Validaciones, Testing, Great Expectations, Pandera

---

### 🟥 Nivel 5 — Pipelines y orquestación

* 📘 [Pipelines (carpeta)](05_pipelines/)
* ✅ [Pipelines básicos](05_pipelines/pipelines-basicos/)
  * Conceptos fundamentales
  * Pipelines con Python puro
* ✅ [Orquestadores](05_pipelines/orquestadores/)
  * Prefect, Dagster (local - empezar aquí)
  * Airflow, Luigi (enterprise)
  * Step Functions, Composer, Data Factory (cloud)

---

### 🤖 AI como copiloto

* 📘 [AI como Copiloto (carpeta)](06_inteligencia_artificial/)
* ✅ [Herramientas](06_inteligencia_artificial/herramientas/)
  * Cursor para Data Engineers
* ✅ [Uso Práctico](06_inteligencia_artificial/uso-practico/)
  * Cómo usar AI como DE
  * Ejemplos de Prompts
  * Documentación con AI
* ✅ [Límites de la AI](06_inteligencia_artificial/limites-de-la-ai.md)
* ✅ [Buenas Prácticas de AI](06_inteligencia_artificial/buenas-practicas-ai.md)

---

### 🚀 Proyectos End-to-End

* 📘 [Proyectos (carpeta)](07_proyectos/)
* ✅ [Nivel Principiante](07_proyectos/principiante/)
  * Pipeline ETL Simple, Análisis con Pandas, Docker
* ✅ [Nivel Intermedio](07_proyectos/intermedio/)
  * SQL+Python, Validaciones, Airflow, IA como Copiloto
* ✅ [Nivel Avanzado](07_proyectos/avanzado/)
  * Pipeline Completo, Producción Local, Cloud Gratis, IA Avanzada

---

### ☁️ Data Engineering en la Nube

* 📘 [Cloud (carpeta)](08_cloud/)
* ✅ [Conceptos fundamentales](01_fundamentos/08_data-engineering-en-la-nube.md)
* 📘 [AWS](08_cloud/aws/) *(próximo)*
* 📘 [Google Cloud Platform](08_cloud/gcp/) *(próximo)*
* 📘 [Microsoft Azure](08_cloud/azure/) *(próximo)*
* 📘 [Multi-Cloud](08_cloud/multi-cloud/) *(próximo)*

---

## ✅ Cómo contribuir / sugerir mejoras

¿Encontraste un error o quieres proponer un tema?

* Abre un **Issue** con sugerencias
* O manda un **Pull Request**
* Lee nuestra [Guía de Contribución](CONTRIBUTING.md) para más detalles
* Revisa nuestro [Código de Conducta](CODE_OF_CONDUCT.md)

⭐ Si este repo te ayuda, dale **Star** para apoyar el contenido en español.

---

## ❓ Preguntas Frecuentes

¿Tienes dudas? Revisa nuestro [FAQ](FAQ.md) con preguntas comunes sobre:
* Cómo empezar
* Configuración técnica
* Problemas comunes
* Sobre el aprendizaje
* Contribuciones

---

## 📚 Documentación Adicional

* **[SETUP.md](SETUP.md)** - Guía completa de configuración inicial
* **[FAQ.md](FAQ.md)** - Preguntas frecuentes
* **[CONTRIBUTING.md](CONTRIBUTING.md)** - Cómo contribuir
* **[requirements.txt](requirements.txt)** - Dependencias del proyecto

---

## 🤖 AI como copiloto

En este repositorio:

* Usamos AI para:

  * explicar código
  * generar ejemplos
  * documentar pipelines
  * crear tests
* **Nunca** para evitar entender los fundamentos.

> La AI potencia al Data Engineer que sabe lo que está haciendo.

---

## 🧠 Filosofía

* Menos magia, más fundamentos
* Código claro > código "ingenioso"
* Pensar en datos como **producto**
* Ingeniería antes que herramientas

---

## 📬 Contacto

* [LinkedIn](https://www.linkedin.com/in/carolina-acosta-tovany-1a6689275/)

---
