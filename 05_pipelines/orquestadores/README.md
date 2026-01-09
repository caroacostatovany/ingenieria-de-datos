# Orquestadores de Pipelines

Los orquestadores gestionan la ejecución, programación y monitoreo de pipelines de datos. Aprende cuándo y cómo usar cada uno.

---

## 📖 Contenido

### 🏠 Orquestadores locales (empezar aquí)

* **[Prefect](prefect.md)**
  * Orquestador moderno y Python-first
  * Fácil de empezar localmente
  * Excelente para desarrollo

* **[Dagster](dagster.md)**
  * Enfoque en data assets
  * Gran para desarrollo local
  * UI moderna

### ☁️ Orquestadores cloud/enterprise

* **[Apache Airflow](airflow.md)**
  * El más popular
  * Maduro y estable
  * Gran ecosistema

* **[Luigi](luigi.md)**
  * Desarrollado por Spotify
  * Simple y directo
  * Bueno para pipelines Python

* **[AWS Step Functions](step-functions.md)**
  * Nativo de AWS
  * Serverless
  * Integración con servicios AWS

* **[Google Cloud Composer](composer.md)**
  * Airflow gestionado en GCP
  * Sin infraestructura propia
  * Integración con GCP

* **[Azure Data Factory](data-factory.md)**
  * Nativo de Azure
  * UI visual
  * Integración con Azure

---

## 🎯 ¿Cuándo usar cada uno?

### Para empezar (local)

**Recomendado: Prefect o Dagster**

* ✅ Fácil instalación local
* ✅ Excelente para desarrollo
* ✅ Puede escalar a producción
* ✅ Menos overhead que Airflow

### Para producción (cloud/enterprise)

**Recomendado: Airflow o servicios cloud**

* ✅ Maduro y probado
* ✅ Gran comunidad
* ✅ Integración con servicios cloud
* ✅ Monitoreo avanzado

---

## 🔄 Comparación rápida

| Característica | Prefect | Dagster | Airflow | Luigi |
|----------------|---------|---------|---------|-------|
| **Complejidad** | Baja | Media | Alta | Baja |
| **Setup local** | Muy fácil | Fácil | Medio | Fácil |
| **UI** | Moderna | Excelente | Buena | Básica |
| **Python-first** | ✅ | ✅ | ⚠️ | ✅ |
| **Madurez** | Media | Media | Alta | Alta |
| **Comunidad** | Creciente | Creciente | Muy grande | Grande |

---

## 🚀 Recomendación de aprendizaje

1. **Empieza con Prefect** para entender conceptos
2. **Prueba Dagster** para ver alternativas
3. **Aprende Airflow** si necesitas estándar de industria
4. **Explora cloud** cuando necesites escalar

---

## 💡 Tips

* **No necesitas orquestador** para pipelines simples
* **Empieza local** antes de ir a cloud
* **Elige según tu stack**: Python-first vs. multi-lenguaje
* **Considera costos**: Local vs. Cloud gestionado

---

## 🎯 Próximo paso

Empieza con **[Prefect](prefect.md)** para un orquestador moderno y fácil de usar.

---

> **Recuerda**: El mejor orquestador es el que resuelve tu problema. Empieza simple y escala cuando sea necesario.
