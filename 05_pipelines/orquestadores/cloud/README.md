# ☁️ Orquestadores y Servicios Cloud para Data Engineering

Esta sección cubre orquestadores cloud y servicios principales de los proveedores cloud más importantes para Data Engineering.

---

## 🧠 ¿Qué son los orquestadores cloud?

Los orquestadores cloud son servicios gestionados que te permiten orquestar pipelines de datos sin gestionar infraestructura. Son ideales para producción cuando ya estás usando servicios cloud.

---

## 🎯 Orquestadores Cloud por Proveedor

### AWS: Step Functions

**[Ver documentación completa →](step-functions.md)**

**¿Qué es?**
- Orquestación serverless nativa de AWS
- Define workflows con JSON o UI visual
- Integración profunda con servicios AWS

**Ventajas:**
- ✅ Serverless (sin gestión de infraestructura)
- ✅ Integración nativa con Lambda, Glue, EMR, S3
- ✅ Escala automáticamente
- ✅ Pago por uso

**Cuándo usar:**
- ✅ Ya estás en AWS
- ✅ Quieres serverless
- ✅ Necesitas integración con servicios AWS
- ❌ No estás en AWS
- ❌ Necesitas portabilidad entre clouds

---

### GCP: Cloud Composer

**[Ver documentación completa →](composer.md)**

**¿Qué es?**
- Airflow gestionado en GCP
- Sin necesidad de gestionar infraestructura
- Integración nativa con servicios GCP

**Ventajas:**
- ✅ Airflow sin el dolor de gestionar servidores
- ✅ Integración con BigQuery, Cloud Storage, Dataflow
- ✅ Monitoreo y logging integrados
- ✅ Actualizaciones automáticas

**Cuándo usar:**
- ✅ Estás en GCP
- ✅ Quieres Airflow sin gestión
- ✅ Necesitas integración con GCP
- ❌ No estás en GCP
- ❌ Presupuesto limitado (tiene costos base)

---

### Azure: Data Factory

**[Ver documentación completa →](data-factory.md)**

**¿Qué es?**
- Servicio de orquestación nativo de Azure
- UI visual para diseñar pipelines
- Code-first opcional (también soporta código)

**Ventajas:**
- ✅ UI visual muy intuitiva
- ✅ Integración profunda con servicios Azure
- ✅ Sin gestión de infraestructura
- ✅ Ideal para equipos no técnicos

**Cuándo usar:**
- ✅ Estás en Azure
- ✅ Prefieres UI visual
- ✅ Necesitas integración con servicios Azure
- ❌ No estás en Azure
- ❌ Prefieres código sobre UI

---

## 📊 Comparación de Orquestadores Cloud

| Característica | Step Functions | Cloud Composer | Data Factory |
|----------------|---------------|----------------|--------------|
| **Proveedor** | AWS | GCP | Azure |
| **Tipo** | Serverless | Airflow gestionado | ETL/Orquestación |
| **UI** | Visual (JSON) | Airflow UI | Visual (drag & drop) |
| **Código** | JSON/YAML | Python (DAGs) | JSON/Visual |
| **Integración** | AWS nativa | GCP nativa | Azure nativa |
| **Costo** | Pago por uso | Costo base + uso | Pago por uso |
| **Complejidad** | Media | Media-Alta | Baja-Media |
| **Vendor Lock-in** | Alto | Alto | Alto |

---

## 🎯 ¿Cuál elegir?

### Si estás en AWS → **Step Functions**
- Serverless y escalable
- Excelente para workflows con Lambda
- Integración perfecta con servicios AWS

### Si estás en GCP → **Cloud Composer**
- Si ya conoces Airflow, es la opción natural
- Integración excelente con BigQuery
- Ideal para equipos que prefieren código (Python)

### Si estás en Azure → **Data Factory**
- UI visual muy amigable
- Excelente para equipos no técnicos
- Integración profunda con servicios Azure

### Si no estás en ningún cloud → **Empieza local**
- Aprende primero con [Prefect](../prefect.md) o [Dagster](../dagster.md) localmente
- Luego considera servicios cloud cuando necesites escalar

---

## 📖 Servicios Cloud Principales (No Orquestadores)

Además de orquestadores, estos son los servicios principales de cada proveedor:

### AWS

**Almacenamiento:**
- **S3**: Almacenamiento de objetos escalable (equivalente a Data Lake)
- Ideal para: Data Lakes, archivos raw, backups

**ETL y Procesamiento:**
- **AWS Glue**: ETL serverless y catalogado de datos
- **EMR**: Clusters Spark/Hadoop gestionados
- **Lambda**: Funciones serverless para micro-ETL

**Data Warehouse:**
- **Redshift**: Data warehouse columnar
- **Athena**: Query SQL sobre S3 (serverless)

**Streaming:**
- **Kinesis**: Streaming de datos en tiempo real

### GCP

**Almacenamiento:**
- **Cloud Storage**: Almacenamiento de objetos (equivalente a S3)

**Data Warehouse:**
- **BigQuery**: Data warehouse serverless ⭐ (el servicio estrella de GCP)
  - Serverless, pago por query
  - Datasets públicos gratuitos para practicar
  - Excelente para analytics masivos

**ETL y Procesamiento:**
- **Dataflow**: Procesamiento stream/batch (Apache Beam)
- **Dataproc**: Clusters Spark/Hadoop gestionados
- **Cloud Functions**: Funciones serverless

**Streaming:**
- **Pub/Sub**: Messaging y streaming de eventos

### Azure

**Almacenamiento:**
- **Azure Blob Storage**: Almacenamiento de objetos
- **Azure Data Lake Storage Gen2**: Optimizado para analytics

**ETL y Procesamiento:**
- **Azure Databricks**: Spark optimizado en Azure
- **Azure Functions**: Funciones serverless

**Data Warehouse:**
- **Azure Synapse Analytics**: Analytics unificado (SQL + Spark)
- **Azure SQL Database**: Base de datos relacional gestionada

**Streaming:**
- **Event Hubs**: Streaming de eventos

---

## 💰 Consideraciones de Costo

### Free Tier

**AWS:**
- S3: 5 GB de almacenamiento (12 meses)
- Lambda: 1 millón de requests gratis
- Glue: 10,000 objetos catalogados gratis
- Athena: 10 GB de datos escaneados/mes

**GCP:**
- BigQuery: 10 GB almacenamiento, 1 TB queries/mes (siempre gratis)
- Cloud Storage: 5 GB (siempre gratis)
- Cloud Functions: 2 millones invocaciones/mes
- **$300 de crédito** gratis por 90 días (nuevas cuentas)

**Azure:**
- Blob Storage: 5 GB LRS (siempre gratis)
- Azure Functions: 1 millón requests/mes
- **$200 de crédito** gratis por 30 días (nuevas cuentas)

### Tips para ahorrar

- ✅ **Configura alertas de costo** desde el inicio
- ✅ **Apaga recursos** cuando no los uses (clusters, warehouses)
- ✅ **Usa free tier** para aprender
- ✅ **Monitorea regularmente** el uso y costos
- ✅ **Usa datasets públicos** (BigQuery tiene muchos gratuitos)

---

## 🚀 Cómo empezar

### 1. Elige un proveedor

**Recomendación para empezar:**
- **GCP** si quieres empezar rápido (BigQuery tiene datasets públicos)
- **AWS** si quieres el más popular y con más recursos
- **Azure** si ya estás en el ecosistema Microsoft

### 2. Crea una cuenta

1. Ve al sitio del proveedor (aws.amazon.com, cloud.google.com, azure.microsoft.com)
2. Crea una cuenta (requiere tarjeta, pero free tier es generoso)
3. **Configura alertas de costo** inmediatamente
4. Activa MFA (autenticación de dos factores)

### 3. Primeros pasos prácticos

**GCP (Recomendado para principiantes):**
1. Explora BigQuery y sus datasets públicos (gratis)
2. Ejecuta queries SQL sin costo
3. Crea un bucket en Cloud Storage
4. Prueba Cloud Composer (tiene costo, pero puedes probar)

**AWS:**
1. Crea un bucket S3
2. Sube un archivo CSV
3. Consulta con Athena
4. Prueba Step Functions con Lambda

**Azure:**
1. Crea un Storage Account
2. Sube archivos a Blob Storage
3. Crea un pipeline simple en Data Factory
4. Explora Azure Databricks

---

## 🔗 Prerequisitos

Antes de empezar con servicios cloud, asegúrate de dominar:

* **[01_fundamentos](../01_fundamentos/)**: Conceptos básicos
* **[02_sql](../02_sql/)**: SQL para transformaciones
* **[03_python](../03_python/)**: Python para automatización
* **[05_pipelines](../README.md)**: Conceptos de pipelines
* **[Orquestadores locales](../README.md)**: Prefect, Dagster, Airflow (recomendado empezar local)

Y especialmente:
* **[Data Engineering en la Nube](../../01_fundamentos/08_data-engineering-en-la-nube.md)**: Conceptos fundamentales

---

## 🎯 Cuándo usar Cloud vs. Local

### Usa Cloud cuando:
- ✅ Necesitas escalar a producción
- ✅ Tienes presupuesto para servicios gestionados
- ✅ Necesitas integración con otros servicios cloud
- ✅ Quieres evitar gestionar infraestructura
- ✅ Tu equipo ya está en un cloud provider

### Usa Local cuando:
- ✅ Estás aprendiendo
- ✅ Desarrollando y probando
- ✅ Presupuesto limitado
- ✅ Necesitas control total
- ✅ Quieres evitar vendor lock-in

---

## 🧠 Filosofía

La nube es una herramienta poderosa, pero:

* **No reemplaza** entender los fundamentos
* **No es gratis** - monitorea costos cuidadosamente
* **No es mágica** - sigue requiriendo buen diseño
* **Vendor lock-in** es real - considera portabilidad

> La nube facilita la infraestructura, pero la ingeniería de datos sigue siendo tu responsabilidad.

---

## 📚 Recursos adicionales

### Documentación oficial

- **AWS**: [AWS Data Engineering](https://aws.amazon.com/data-engineering/)
- **GCP**: [GCP Data Engineering](https://cloud.google.com/solutions/data-engineering)
- **Azure**: [Azure Data Engineering](https://azure.microsoft.com/solutions/data-engineering/)

### Certificaciones (opcionales pero valiosas)

- **AWS**: AWS Certified Data Analytics - Specialty
- **GCP**: Google Cloud Professional Data Engineer
- **Azure**: Microsoft Certified: Azure Data Engineer Associate

---

## 🚀 ¿Qué sigue?

Después de dominar servicios cloud:

**👉 Siguiente etapa: [07_proyectos](../../07_proyectos/)**
* Proyectos end-to-end completos
* Integrar todo lo aprendido
* Proyectos para tu portafolio

**También puedes:**
* Profundizar en servicios específicos (BigQuery, Redshift, etc.)
* Explorar arquitecturas multi-cloud
* Obtener certificaciones cloud
* Explorar servicios avanzados (streaming, ML, etc.)

> 💡 **Tip**: No necesitas dominar todos los servicios. Enfócate en los servicios principales de un proveedor primero (almacenamiento, ETL, data warehouse), luego expande según tus necesidades.

---

## 📋 Referencias directas

### Orquestadores Cloud
- **[AWS Step Functions](step-functions.md)** - Orquestación serverless en AWS
- **[Google Cloud Composer](composer.md)** - Airflow gestionado en GCP
- **[Azure Data Factory](data-factory.md)** - Orquestación nativa de Azure

### Orquestadores Locales (recomendado empezar aquí)
- **[Prefect](../prefect.md)** - Orquestador moderno Python-first
- **[Dagster](../dagster.md)** - Enfoque en data assets
- **[Apache Airflow](../airflow.md)** - Estándar de industria
- **[Luigi](../luigi.md)** - Alternativa simple

### Conceptos fundamentales
- **[Data Engineering en la Nube](../../01_fundamentos/08_data-engineering-en-la-nube.md)** - Conceptos básicos de cloud
