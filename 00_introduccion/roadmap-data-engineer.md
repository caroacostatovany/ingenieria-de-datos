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

## 🟢 Etapa 0.5 — Cursor: Tu Copiloto de AI (PRIMERO)

**Objetivo:** Configurar Cursor para usar AI como copiloto desde el inicio.

**⚠️ IMPORTANTE:** Configura Cursor **ANTES** de empezar con SQL o Python. Te ayudará durante todo el aprendizaje.

Aprende:

* **Instalar y configurar Cursor**
* **Clonar este repositorio en Cursor**
* **Usar el chat de AI** para hacer preguntas sobre el contenido
* **Pedir explicaciones** adaptadas a tu nivel
* **Solicitar ayuda** para ejecutar comandos (Docker, etc.)

> 💡 **Tip**: Usa Cursor desde el día 1. Puedes preguntarle sobre cualquier archivo del repositorio, pedir explicaciones simples, o solicitar ayuda para ejecutar comandos.

📁 Contenido recomendado:

* **[Cursor para Data Engineers](../06_inteligencia_artificial/herramientas/cursor-para-data-engineers.md)** ⭐ **EMPIEZA AQUÍ**

---

## 🟢 Etapa 0.6 — Herramientas esenciales

**Objetivo:** Configurar tu entorno de trabajo.

Aprende:

* **Git y GitHub** para versionar código
* **Archivos .env** para gestionar configuraciones
* **Docker** para entornos reproducibles

Estas herramientas te acompañarán durante todo el camino.
Aprenderlas temprano te ahorrará tiempo después.

📁 Contenido recomendado:

* [Tipos de Datos](../01_fundamentos/00_tipos-de-datos.md)
* [¿Qué es un Pipeline?](../01_fundamentos/01_que-es-un-pipeline.md)
* [Batch vs Streaming](../01_fundamentos/02_batch-vs-streaming.md)
* [Git y GitHub para Data Engineers](../01_fundamentos/03_git-y-github-para-data-engineers.md)
* [Archivos .env para Data Engineers](../01_fundamentos/04_archivos-env-para-data-engineers.md)
* [Docker para Data Engineers](../01_fundamentos/05_docker-para-data-engineers.md)

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

* [Introducción a SQL](../01_fundamentos/06_introduccion-sql.md)
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

* [Fundamentos Python](../03_python/fundamentos/)
* [Pandas para Datos](../03_python/pandas/)
* [Storytelling con Datos](../03_python/storytelling/)
* [Ejemplos](../03_python/ejemplos/)

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

* [Modelado analítico](../04_modelado_y_calidad/modelado/)
* [Calidad de datos](../04_modelado_y_calidad/calidad/)
* [Validaciones](../04_modelado_y_calidad/calidad/validaciones/)
* [Testing de datos](../04_modelado_y_calidad/calidad/validaciones/testing-de-datos.md)
* [Herramientas](../04_modelado_y_calidad/calidad/herramientas/)
* [Ejemplos (Notebooks)](../04_modelado_y_calidad/ejemplos/)

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

* [¿Qué es un Pipeline?](../05_pipelines/pipelines-basicos/que-es-un-pipeline.md) *(conceptual)*
* [Batch vs Streaming](../01_fundamentos/02_batch-vs-streaming.md)
* [Pipelines básicos](../05_pipelines/pipelines-basicos/)
* [Pipelines con Python](../05_pipelines/pipelines-basicos/pipelines-con-python.md)
* [Introducción a Airflow](../05_pipelines/orquestadores/airflow.md)
* [Buenas Prácticas](../01_fundamentos/07_buenas-practicas.md)

---

## 🤖 Etapa 5 — AI como copiloto

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

* [Cursor para Data Engineers](../06_inteligencia_artificial/herramientas/cursor-para-data-engineers.md)
* [Cómo usar AI como DE](../06_inteligencia_artificial/uso-practico/como-usar-ai-como-de.md)
* [Ejemplos de Prompts](../06_inteligencia_artificial/uso-practico/ejemplos-prompts.md)
* [Documentación con AI](../06_inteligencia_artificial/uso-practico/documentacion-con-ai.md)
* [Límites de la AI](../06_inteligencia_artificial/limites-de-la-ai.md)
* [Buenas Prácticas de AI](../06_inteligencia_artificial/buenas-practicas-ai.md)

---

## 🔵 Etapa 6 — Data Engineering en la Nube

**Objetivo:** Aplicar conocimientos en entornos cloud.

Aprende:

* **Conceptos fundamentales**: Serverless, almacenamiento de objetos, servicios gestionados
* **Proveedores principales**: AWS, GCP, Azure
* **Servicios clave**: Almacenamiento, procesamiento, orquestación
* **Costos y optimización**: Free tier, monitoreo de costos
* **Arquitecturas cloud**: Data Warehouse vs Data Lake en cloud

> 💡 **Nota**: Puedes aprender cloud en paralelo con otras etapas. No es necesario esperar hasta aquí.

📁 Contenido recomendado:

* [Data Engineering en la Nube](../01_fundamentos/08_data-engineering-en-la-nube.md)
* [AWS](../08_cloud/aws/) *(próximo)*
* [Google Cloud Platform](../08_cloud/gcp/) *(próximo)*
* [Microsoft Azure](../08_cloud/azure/) *(próximo)*
* [Multi-Cloud](../08_cloud/multi-cloud/) *(próximo)*

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

* [Proyectos Principiantes](../07_proyectos/principiante/)
* [Proyectos Intermedios](../07_proyectos/intermedio/)
* [Proyectos Avanzados](../07_proyectos/avanzado/)

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
