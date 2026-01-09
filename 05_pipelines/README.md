# 🔄 Pipelines y Orquestación

Esta carpeta cubre cómo construir, orquestar y monitorear pipelines de datos en producción.

---

## 📖 Contenido

### ✅ Documentos disponibles

* ✅ **[Pipelines básicos](pipelines-basicos/)**
  * Conceptos fundamentales de pipelines
  * Componentes básicos
  * Pipelines con Python puro
  * Estructura de proyectos
  * Testing de pipelines

* ✅ **[Orquestadores](orquestadores/)**
  * Comparación de orquestadores
  * **Orquestadores locales** (empezar aquí):
    * Prefect (moderno, Python-first)
    * Dagster (data assets, UI excelente)
  * **Orquestadores enterprise/cloud**:
    * Airflow (estándar industria, completo)
    * Luigi (simple, Python puro)
    * AWS Step Functions (serverless)
    * Google Cloud Composer (Airflow gestionado)
    * Azure Data Factory (Azure nativo)

---

## 🎯 Objetivo de esta sección

Al finalizar esta sección, deberías poder:

* Diseñar y construir pipelines ETL/ELT básicos
* Construir pipelines con Python puro (sin orquestadores)
* Elegir el orquestador apropiado para tu caso
* Orquestar pipelines con herramientas modernas
* Manejar errores y dependencias
* Monitorear y mantener pipelines en producción

---

## 🔗 Relación con otras secciones

* Aplica fundamentos de **[01_fundamentos](../01_fundamentos/)**
* Usa SQL de **[02_sql](../02_sql/)** para transformaciones
* Implementa con Python de **[03_python](../03_python/)**
* Aplica calidad de **[04_modelado_y_calidad](../04_modelado_y_calidad/)**

## 📚 Flujo de aprendizaje recomendado

1. **Empieza con [Pipelines básicos](pipelines-basicos/)** - Aprende conceptos y Python puro
2. **Prueba [Orquestadores locales](orquestadores/)** - Prefect o Dagster para desarrollo
3. **Escala a [Orquestadores enterprise](orquestadores/)** - Airflow u otros cuando necesites producción

---

## 🚀 Siguiente paso

Después de dominar pipelines:

* **[03_python/ejemplos/](../03_python/ejemplos/)** para ejemplos prácticos de pipelines con Python
* **[07_proyectos](../07_proyectos/)** para proyectos end-to-end completos
* **[06_ai_como_copiloto](../06_ai_como_copiloto/)** para usar AI en el desarrollo

---

## 💡 Tip

Un pipeline no es solo código. Piensa en orquestación, monitoreo, manejo de errores y mantenibilidad desde el diseño.

---

## 📚 Flujo de aprendizaje recomendado

1. **Empieza con [¿Qué es un pipeline?](pipelines-basicos/que-es-un-pipeline.md)** - Conceptos fundamentales
2. **Aprende [Pipelines con Python](pipelines-basicos/pipelines-con-python.md)** - Implementación práctica
3. **Prueba [Orquestadores locales](orquestadores/)** - Prefect o Dagster para desarrollo
4. **Escala a [Orquestadores enterprise](orquestadores/)** - Airflow u otros cuando necesites producción
