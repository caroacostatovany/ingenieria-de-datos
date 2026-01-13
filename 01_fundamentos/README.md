# 🧱 Fundamentos de Data Engineering

Esta carpeta cubre los conceptos fundamentales que todo Data Engineer debe dominar antes de construir pipelines complejos.

---

## 📖 Contenido

### ✅ Documentos disponibles (en orden de aprendizaje)

**Conceptos Fundamentales:**
* **[00. Tipos de Datos](00_tipos-de-datos.md)**
  * Tipos de datos estructurados, semi-estructurados y no estructurados
  * Formatos comunes (CSV, JSON, Parquet, etc.)
  * Cuándo usar cada formato
  * Consideraciones de almacenamiento

* **[01. ¿Qué es un Pipeline?](01_que-es-un-pipeline.md)**
  * Concepto fundamental de pipelines de datos
  * Diferencia entre script y pipeline
  * Componentes de un pipeline
  * DAGs y dependencias

* **[02. Batch vs Streaming](02_batch-vs-streaming.md)**
  * Diferencias entre procesamiento batch y streaming
  * Cuándo usar cada enfoque
  * Trade-offs y consideraciones
  * Ejemplos prácticos

**Herramientas Esenciales (Etapa 0.5 del Roadmap):**
* **[03. Git y GitHub para Data Engineers](03_git-y-github-para-data-engineers.md)**
  * Control de versiones en proyectos de datos
  * Flujo de trabajo con Git
  * Colaboración en GitHub
  * Buenas prácticas para Data Engineers

* **[04. Archivos .env para Data Engineers](04_archivos-env-para-data-engineers.md)**
  * ¿Por qué usar archivos .env?
  * Estructura y sintaxis
  * Uso en Python y Docker
  * Seguridad y buenas prácticas
  * Casos de uso comunes
  * .env.example y flujo de trabajo

* **[05. Docker para Data Engineers](05_docker-para-data-engineers.md)**
  * ¿Por qué Docker es importante en Data Engineering?
  * Conceptos fundamentales (imágenes, contenedores, Dockerfile)
  * Docker en el flujo de datos
  * Casos de uso comunes
  * Comandos esenciales
  * Buenas prácticas

**Preparación para SQL (Etapa 1 del Roadmap):**
* **[06. Introducción a SQL](06_introduccion-sql.md)**
  * ¿Por qué SQL es esencial en Data Engineering?
  * SQL transaccional vs SQL analítico
  * Conceptos fundamentales
  * SQL en el flujo de datos (ETL)
  * Cuándo usar SQL vs otras herramientas

**Buenas Prácticas:**
* **[Buenas Prácticas de Pipelines](01_que-es-un-pipeline.md#-buen-diseño-de-pipelines)** (integrado en "¿Qué es un pipeline?")
  * Principios de diseño de pipelines
  * Manejo de errores
  * Versionado y documentación
  * Testing y validación

**Conceptos Avanzados:**
* **[08. Data Engineering en la Nube](08_data-engineering-en-la-nube.md)**
  * ¿Qué es Data Engineering en la nube?
  * Principales proveedores (AWS, GCP, Azure)
  * Ventajas del cloud
  * Conceptos clave (serverless, almacenamiento de objetos)
  * Arquitecturas típicas
  * Modelo de costos y seguridad

---

## 🎯 Objetivo de esta sección

Al finalizar esta sección, deberías poder:

* Entender los diferentes tipos de datos y formatos
* Comprender qué es un pipeline y cómo diseñarlo
* Decidir entre batch y streaming según el caso
* Aplicar buenas prácticas desde el inicio
* Usar Git y GitHub para versionar y colaborar en proyectos de datos
* Entender el rol de SQL en Data Engineering y cuándo usarlo
* Gestionar configuraciones y secretos con archivos .env de forma segura
* Usar Docker para crear entornos reproducibles y pipelines portables
* Entender conceptos de Data Engineering en la nube y cuándo usarlo

---

## 🔗 Relación con otras secciones

* Estos fundamentos se aplican en **[05_pipelines](../05_pipelines/)** cuando construyas pipelines reales
* La introducción a SQL te prepara para profundizar en **[02_sql](../02_sql/)**
* Los tipos de datos son relevantes para **[02_sql](../02_sql/)** y **[03_python](../03_python/)**
* Las buenas prácticas se refuerzan en **[04_modelado_y_calidad](../04_modelado_y_calidad/)**

---

## 📚 Flujo de aprendizaje recomendado

Sigue este orden para un aprendizaje progresivo:

1. **Conceptos fundamentales** (00-02): Entiende tipos de datos, pipelines y batch vs streaming
2. **Herramientas esenciales** (03-05): Configura tu entorno con Git, .env y Docker
3. **Preparación SQL** (06): Entiende el rol de SQL antes de profundizar
4. **Buenas prácticas** (07): Aplica principios desde el inicio
5. **Cloud** (08): Explora conceptos avanzados cuando estés listo

---

## 🚀 ¿Qué sigue?

Según el roadmap, después de dominar los fundamentos:

**👉 Siguiente etapa: [02_sql](../02_sql/)** (Etapa 1 del roadmap)
* SQL es la base de todo en Data Engineering
* Te recomendamos empezar con SQL antes de Python
* Aprende a consultar y transformar datos con confianza

**Alternativa**: Si prefieres empezar con programación, puedes ir a **[03_python](../03_python/)** (Etapa 2), pero SQL es más fundamental.

> 💡 **Tip**: Revisa el [Roadmap completo](../00_introduccion/roadmap-data-engineer.md) para ver la ruta completa.

---

## 💡 Tip

No saltes esta sección. Los fundamentos sólidos te ahorrarán tiempo y problemas más adelante.
