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

## 🚀 Ruta de aprendizaje recomendada

> ⚠️ **Importante**: Antes de instalar o ejecutar cualquier orquestador, asegúrate de activar tu entorno virtual:
> ```bash
> pyenv activate ingenieria-de-datos
> ```
> O si usas `pyenv-virtualenv`:
> ```bash
> pyenv shell ingenieria-de-datos
> ```

Sigue este orden para aprender orquestadores de forma progresiva:

1. **[Prefect](prefect.md)** - Empieza aquí
   * Orquestador moderno y Python-first
   * Fácil de instalar y usar localmente
   * Excelente para entender conceptos básicos
   * Crea tus primeros flows y entiende tareas, dependencias y scheduling
   * **Recuerda**: Activa `pyenv activate ingenieria-de-datos` antes de instalar

2. **[Dagster](dagster.md)** - Siguiente paso
   * Enfoque en data assets y lineage
   * UI moderna y visual
   * Conceptos avanzados de orquestación
   * Compara con Prefect para entender diferentes enfoques
   * **Recuerda**: Activa `pyenv activate ingenieria-de-datos` antes de instalar

3. **[Apache Airflow](airflow.md)** - Estándar de industria
   * El orquestador más popular
   * Maduro y con gran comunidad
   * DAGs, operadores y conceptos enterprise
   * Necesario para muchos trabajos en Data Engineering
   * **Recuerda**: Activa `pyenv activate ingenieria-de-datos` antes de instalar

4. **[Luigi](luigi.md)** - Alternativa simple (opcional)
   * Para entender enfoques más simples
   * Bueno para pipelines Python puro
   * **Recuerda**: Activa `pyenv activate ingenieria-de-datos` antes de instalar

5. **Orquestadores cloud** - Cuando necesites escalar
   * **[AWS Step Functions](step-functions.md)** - Si usas AWS
   * **[Google Cloud Composer](composer.md)** - Si usas GCP
   * **[Azure Data Factory](data-factory.md)** - Si usas Azure
   * **Nota**: Estos son servicios cloud, no requieren instalación local

---

## 💡 Tips

* **No necesitas orquestador** para pipelines simples
* **Empieza local** antes de ir a cloud
* **Elige según tu stack**: Python-first vs. multi-lenguaje
* **Considera costos**: Local vs. Cloud gestionado
* **Siempre activa pyenv**: `pyenv activate ingenieria-de-datos` antes de instalar o ejecutar

---

## 🎯 Próximo paso

**👉 Empieza con [Prefect](prefect.md)** - El primer orquestador que debes aprender.

Después de dominar Prefect, continúa con **[Dagster](dagster.md)** para ver un enfoque diferente.

---

> **Recuerda**: El mejor orquestador es el que resuelve tu problema. Empieza simple y escala cuando sea necesario.
