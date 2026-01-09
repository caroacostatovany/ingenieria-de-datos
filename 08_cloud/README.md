# ☁️ Data Engineering en la Nube

Esta carpeta cubre Data Engineering usando servicios cloud de los principales proveedores.

---

## 📖 Contenido

### 📘 Proveedores Cloud

* **[AWS (Amazon Web Services)](aws/)**
  * S3 para almacenamiento
  * Glue para ETL
  * Redshift para data warehouse
  * EMR para procesamiento
  * Lambda para serverless

* **[Google Cloud Platform (GCP)](gcp/)**
  * Cloud Storage
  * BigQuery
  * Dataflow
  * Dataproc
  * Cloud Functions

* **[Microsoft Azure](azure/)**
  * Azure Blob Storage
  * Azure Data Factory
  * Azure Synapse
  * Azure Databricks
  * Azure Functions

* **[Multi-Cloud](multi-cloud/)**
  * Estrategias multi-cloud
  * Snowflake (multi-cloud)
  * Consideraciones y trade-offs

---

## 🎯 Objetivo de esta sección

Al finalizar esta sección, deberías poder:

* Entender los servicios cloud principales para Data Engineering
* Construir pipelines en al menos un proveedor cloud
* Decidir qué servicios usar según el caso
* Entender costos y optimización en cloud

---

## 🔗 Prerequisitos

Antes de empezar, asegúrate de dominar:

* **[01_fundamentos](../01_fundamentos/)**: Conceptos básicos
* **[02_sql](../02_sql/)**: SQL para transformaciones
* **[03_python](../03_python/)**: Python para automatización
* **[05_pipelines](../05_pipelines/)**: Conceptos de pipelines

Y especialmente:
* **[Data Engineering en la Nube](../01_fundamentos/08_data-engineering-en-la-nube.md)**: Conceptos fundamentales

---

## 🚀 Cómo empezar

1. **Lee primero** [Data Engineering en la Nube](../01_fundamentos/08_data-engineering-en-la-nube.md) en fundamentos
2. **Elige un proveedor** para empezar (recomendado: AWS o GCP)
3. **Crea una cuenta** y usa el free tier
4. **Sigue los tutoriales** del proveedor elegido
5. **Construye un pipeline simple** end-to-end

---

## 💰 Consideraciones de costo

* **Usa free tier** para aprender
* **Configura alertas** de costo desde el inicio
* **Apaga recursos** cuando no los uses
* **Monitorea** el uso regularmente

---

## 🧠 Filosofía

La nube es una herramienta poderosa, pero:

* **No reemplaza** entender los fundamentos
* **No es gratis** - monitorea costos
* **No es mágica** - sigue requiriendo buen diseño

> La nube facilita la infraestructura, pero la ingeniería de datos sigue siendo tu responsabilidad.

---

## 📚 Recursos adicionales

* Documentación oficial de cada proveedor
* Certificaciones cloud (opcional pero valiosas)
* Comunidades y foros específicos de cada plataforma

---

## 📚 Estructura del módulo

Este módulo está organizado por proveedor:

1. **[AWS](aws/)** - Amazon Web Services (el más popular)
2. **[GCP](gcp/)** - Google Cloud Platform (excelente para BigQuery)
3. **[Azure](azure/)** - Microsoft Azure (ideal para entornos Microsoft)
4. **[Multi-Cloud](multi-cloud/)** - Estrategias multi-proveedor

> 💡 **Recomendación**: Empieza con **un solo proveedor** (AWS o GCP son buenas opciones). Una vez que domines uno, será más fácil aprender otros.

---

## 🚀 ¿Qué sigue?

Según el roadmap, después de dominar cloud:

**👉 Siguiente etapa: [07_proyectos](../07_proyectos/)** (Etapa 7 del roadmap)
* Proyectos end-to-end completos
* Integrar todo lo aprendido
* Proyectos para tu portafolio

**También puedes:**
* Explorar servicios avanzados (streaming, ML, etc.)
* Considerar arquitecturas multi-cloud
* Profundizar en un proveedor específico
* Obtener certificaciones cloud (AWS, GCP, Azure)

> 💡 **Tip**: Revisa el [Roadmap completo](../00_introduccion/roadmap-data-engineer.md) para ver la ruta completa.
