# Roadmap para convertirte en Data Engineer

Este roadmap está diseñado para ayudarte a **convertirte en Data Engineer de forma progresiva**, construyendo **bases sólidas** antes de avanzar a sistemas más complejos.

No es una lista de herramientas.
Es una **forma de pensar**.

---

## 🧭 Principios del roadmap

Antes de empezar, algunas reglas importantes:

* No necesitas aprender todo a la vez
* Los fundamentos importan más que las herramientas
* Entender *por qué* es más importante que el *cómo*
* La experiencia se construye paso a paso

---

## 🟢 Etapa 0 — Fundamentos generales

**Objetivo:** Entender el ecosistema de datos.

Aprende:

* Qué es Data Engineering
* Cómo fluye un dato desde su origen hasta el negocio
* Diferencia entre:

  * Data Engineer
  * Data Analyst
  * Data Scientist

No necesitas escribir código todavía.
Necesitas **contexto**.

📁 Contenido recomendado:

* [¿Qué es Data Engineering?](que-es-data-engineering.md)
* [Roles en Datos](roles-en-datos.md)

---

## 🟢 Etapa 0.5 — Herramientas esenciales

**Objetivo:** Configurar tu entorno de trabajo.

Aprende:

* **Git y GitHub** para versionar código
* **Archivos .env** para gestionar configuraciones
* **Docker** para entornos reproducibles
* **Cursor** (o editor con AI) para trabajar eficientemente

Estas herramientas te acompañarán durante todo el camino.
Aprenderlas temprano te ahorrará tiempo después.

📁 Contenido recomendado:

* [Git y GitHub para Data Engineers](../01_fundamentos/git-y-github-para-data-engineers.md)
* [Archivos .env para Data Engineers](../01_fundamentos/archivos-env-para-data-engineers.md)
* [Docker para Data Engineers](../01_fundamentos/docker-para-data-engineers.md)
* [Cursor para Data Engineers](../06_ai_como_copiloto/cursor-para-data-engineers.md)

---

## 🟡 Etapa 1 — SQL (la base de todo)

**Objetivo:** Poder consultar y transformar datos con confianza.

Aprende:

* **Conceptos fundamentales**: SQL transaccional vs analítico
* **Básico**: SELECT, WHERE, JOIN, GROUP BY
* **Intermedio**: Subqueries, CTEs, Window functions
* **Avanzado**: Optimización, particionamiento, índices
* **Modelado relacional**: Diseño de esquemas, normalización

Buenas prácticas:

* Queries legibles
* Nombres claros
* Evitar lógica innecesaria
* Optimización para grandes volúmenes

👉 Si sabes SQL, siempre tendrás trabajo en datos.

📁 Contenido recomendado:

* [Introducción a SQL](../01_fundamentos/introduccion-sql.md)
* [SQL básico](../02_sql/sql-basico/) *(próximo)*
* [SQL intermedio](../02_sql/sql-intermedio/) *(próximo)*
* [SQL avanzado](../02_sql/sql-avanzado/) *(próximo)*
* [Modelado Relacional](../02_sql/modelado-relacional.md) *(próximo)*
* [Base de datos local con Docker](../02_sql/README-DOCKER.md) - Para practicar

---

## 🟡 Etapa 2 — Python para Data Engineering

**Objetivo:** Automatizar y estructurar procesos.

Aprende:

* **Fundamentos Python** para Data Engineering
* **Manejo de archivos**: CSV, JSON, Parquet
* **Pandas** para manipulación de datos
* **Scripts vs módulos**: Estructura de proyectos
* **Manejo de errores** y logging
* **Integración con SQL** y bases de datos

No se trata de "saber todo Python".
Se trata de **escribir código mantenible**.

📁 Contenido recomendado:

* [Fundamentos Python para DE](../03_python/fundamentos-python.md) *(próximo)*
* [Python para Datos](../03_python/python-para-datos/) *(próximo)*
* [Manejo de archivos](../03_python/manejo-de-archivos.md) *(próximo)*
* [Scripts vs módulos](../03_python/scripts-vs-modulos.md) *(próximo)*

---

## 🟠 Etapa 3 — Modelado y calidad de datos

**Objetivo:** Que los datos sean confiables.

Aprende:

* **Modelado analítico**: Star Schema, Snowflake, tablas de hechos y dimensiones
* **Calidad de datos**: Dimensiones de calidad, métricas, KPIs
* **Validaciones**: Checks de integridad, validación de esquemas
* **Testing de datos**: Tests unitarios, tests de integración
* **Detección de errores**: Alertas y notificaciones

Aquí pasas de "mover datos" a **ingeniería real**.

📁 Contenido recomendado:

* [Modelado analítico](../04_modelado_y_calidad/modelado-analitico.md) *(próximo)*
* [Calidad de datos](../04_modelado_y_calidad/calidad-de-datos.md) *(próximo)*
* [Validaciones](../04_modelado_y_calidad/validaciones.md) *(próximo)*
* [Testing de datos](../04_modelado_y_calidad/testing-de-datos.md) *(próximo)*

---

## 🟠 Etapa 4 — Pipelines y orquestación

**Objetivo:** Automatizar procesos de forma robusta.

Aprende:

* **Conceptos**: Qué es un pipeline, diferencia con scripts
* **Componentes**: Tareas, dependencias, monitoreo
* **Batch vs Streaming**: Cuándo usar cada enfoque
* **Pipelines con Python**: Construir pipelines desde cero
* **Orquestadores**: Introducción a Airflow
* **Buenas prácticas**: Manejo de errores, logging, testing

El foco no es la herramienta.
Es la **orquestación correcta**.

📁 Contenido recomendado:

* [¿Qué es un Pipeline?](../01_fundamentos/que-es-un-pipeline.md) *(conceptual)*
* [Batch vs Streaming](../01_fundamentos/batch-vs-streaming.md)
* [Pipelines básicos](../05_pipelines/pipelines-basicos.md)
* [Pipelines con Python](../05_pipelines/pipelines-con-python.md) *(próximo)*
* [Introducción a Airflow](../05_pipelines/introduccion-airflow.md) *(próximo)*
* [Buenas Prácticas](../01_fundamentos/buenas-practicas.md)

---

## 🔵 Etapa 5 — Arquitectura de datos

**Objetivo:** Pensar en sistemas, no solo en tareas.

Aprende:

* Data Warehouse vs Data Lake
* Capas de datos
* Trade-offs de diseño
* Costos y escalabilidad

Aquí empiezas a pensar como **Data Engineer senior**.

---

## 🤖 Etapa 6 — AI como copiloto

**Objetivo:** Aumentar productividad sin perder criterio.

Aprende a usar AI para:

* **Entender código**: Explicar funciones complejas, SQL, pipelines
* **Generar código**: SQL queries, funciones Python, pipelines
* **Documentar**: Docstrings, READMEs, documentación técnica
* **Generar tests**: Tests unitarios, tests de integración
* **Debugging**: Identificar errores, sugerir soluciones
* **Refactorizar**: Mejorar código existente

Pero también aprende:

* **Cuándo NO usar AI**: Decisiones críticas, validaciones importantes
* **Cómo validar resultados**: Revisar siempre el código generado
* **Límites de la AI**: Qué puede y qué no puede hacer

La AI es una herramienta.
La responsabilidad sigue siendo tuya.

📁 Contenido recomendado:

* [Cursor para Data Engineers](../06_ai_como_copiloto/cursor-para-data-engineers.md)
* [Cómo usar AI como DE](../06_ai_como_copiloto/como-usar-ai-como-de.md) *(próximo)*
* [Ejemplos de Prompts](../06_ai_como_copiloto/ejemplos-prompts.md) *(próximo)*
* [Documentación con AI](../06_ai_como_copiloto/documentacion-con-ai.md) *(próximo)*
* [Límites de la AI](../06_ai_como_copiloto/limites-de-la-ai.md) *(próximo)*

---

## 🚀 Etapa 7 — Proyectos end-to-end

**Objetivo:** Integrar todo lo aprendido.

Construye proyectos que incluyan:

* **Ingesta**: Extraer datos de fuentes (APIs, bases de datos, archivos)
* **Transformación**: Limpiar, normalizar, enriquecer datos
* **Modelado**: Diseñar esquemas analíticos apropiados
* **Validación**: Tests de calidad, checks de integridad
* **Orquestación**: Pipelines automatizados y monitoreados
* **Documentación**: READMEs, comentarios, guías de uso

Un proyecto bien hecho vale más que 10 cursos.

📁 Contenido recomendado:

* [Proyecto 01: Pipeline Simple](../07_proyectos/proyecto_01_pipeline_simple/) *(próximo)*
* [Proyecto 02: SQL + Python](../07_proyectos/proyecto_02_pipeline_sql_python/) *(próximo)*

---

## 🧠 ¿Cuánto tiempo toma este roadmap?

Depende de:

* tu punto de partida
* tu constancia
* tu contexto profesional

Como referencia:

* 3–6 meses para bases sólidas
* 6–12 meses para nivel intermedio
* aprendizaje continuo para nivel senior

No hay atajos reales.

---

## ➡️ ¿Qué sigue después?

Una vez domines este roadmap, el siguiente paso natural es aplicar todo en un **Data Lake real**, donde:

* los datos escalan
* los errores cuestan
* las decisiones importan

👉 Repositorio complementario:
`data-lake-engineering-en-espanol` (próximamente)

---

**La Ingeniería de Datos no se aprende en línea recta.
Se construye con criterio, práctica y paciencia.**
