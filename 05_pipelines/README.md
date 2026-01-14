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
  * **Orquestadores locales** (para desarrollo):
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

## 📚 Flujo de aprendizaje recomendado

1. **Empieza con [Pipelines básicos](pipelines-basicos/)** - Aprende conceptos y construye pipelines con Python puro
2. **Explora [Orquestadores](orquestadores/)** - Empieza con orquestadores locales (Prefect, Dagster) para desarrollo, luego escala a enterprise (Airflow) cuando necesites producción

---

## 🚀 ¿Qué sigue?

Según el roadmap, después de dominar pipelines:

**👉 Siguiente etapa: [06_inteligencia_artificial](../06_inteligencia_artificial/)** (Etapa 5 del roadmap)
* Usar AI como copiloto para aumentar productividad
* Generar código, documentación y tests con AI
* Aprender cuándo usar AI y cuándo no

**Después**: **[08_cloud](../08_cloud/)** (Etapa 6) para aplicar conocimientos en cloud, y finalmente **[07_proyectos](../07_proyectos/)** (Etapa 7) para proyectos end-to-end completos.

> 💡 **Tip**: Revisa el [Roadmap completo](../00_introduccion/roadmap-data-engineer.md) para ver la ruta completa.

---

## 💡 Tip

Un pipeline no es solo código. Piensa en orquestación, monitoreo, manejo de errores y mantenibilidad desde el diseño.
