# Google Cloud Platform para Data Engineers

Google Cloud Platform (GCP) ofrece servicios potentes para Data Engineering, con **BigQuery** como su servicio estrella para analytics. GCP es especialmente fuerte en data analytics y machine learning.

---

## 📖 Servicios principales para Data Engineering

### Almacenamiento

* **Cloud Storage**: Almacenamiento de objetos (equivalente a S3)
  * Ideal para: Data Lakes, archivos raw, backups
  * Características: Lifecycle policies, versionado, multi-región

### Data Warehouse y Analytics

* **BigQuery**: Data warehouse serverless y escalable
  * Ideal para: Analytics masivos, BI, queries complejas
  * Características: **Serverless**, pago por query, datasets públicos
  * **Ventaja clave**: No necesitas gestionar infraestructura

### ETL y Procesamiento

* **Dataflow**: Procesamiento stream/batch (Apache Beam)
  * Ideal para: ETL complejos, streaming, transformaciones
  * Características: Auto-scaling, serverless, stream y batch

* **Dataproc**: Clusters Spark/Hadoop gestionados
  * Ideal para: Procesamiento de grandes volúmenes, Spark jobs
  * Características: Auto-scaling, múltiples frameworks

* **Cloud Functions**: Funciones serverless
  * Ideal para: Micro-ETL, triggers, procesamiento ligero
  * Características: Sin servidores, pago por ejecución

### Streaming y Messaging

* **Pub/Sub**: Messaging y streaming de eventos
  * Ideal para: Event-driven architectures, streaming
  * Características: Escalable, desacoplado, at-least-once delivery

---

## 🎯 Objetivo de esta sección

Al finalizar, deberías poder:

* Configurar una cuenta GCP y usar el free tier
* Almacenar datos en Cloud Storage
* Consultar datos con BigQuery (incluyendo datasets públicos)
* Construir pipelines con Dataflow
* Entender cuándo usar cada servicio
* Optimizar costos en GCP

---

## 🚀 Cómo empezar

### 1. Crear cuenta GCP

1. Ve a [cloud.google.com](https://cloud.google.com)
2. Crea una cuenta (requiere tarjeta, pero $300 de crédito gratis)
3. **Configura alertas de costo** desde el inicio
4. Activa MFA (autenticación de dos factores)

### 2. Explorar BigQuery (Recomendado - PRIMERO)

**BigQuery tiene datasets públicos gratuitos** - perfecto para practicar:

1. Ve a [BigQuery Console](https://console.cloud.google.com/bigquery)
2. Explora datasets públicos:
   * `bigquery-public-data`
   * `bigquery-samples`
3. Ejecuta queries SQL sin costo (hasta 1 TB/mes gratis)

**Ejemplo de query:**
```sql
SELECT 
  name,
  SUM(number) as total_births
FROM `bigquery-public-data.usa_names.usa_1910_2013`
WHERE state = 'CA'
GROUP BY name
ORDER BY total_births DESC
LIMIT 10
```

### 3. Primeros pasos prácticos

**Ejercicio 1: Cloud Storage**
1. Crea un bucket en Cloud Storage
2. Sube un archivo CSV
3. Configura permisos y lifecycle policies

**Ejercicio 2: BigQuery**
1. Crea un dataset en BigQuery
2. Carga datos desde Cloud Storage
3. Ejecuta queries SQL sobre los datos

**Ejercicio 3: Dataflow básico**
1. Crea un pipeline simple con Apache Beam
2. Procesa datos de Cloud Storage
3. Escribe resultados a BigQuery

---

## 💰 Free Tier y costos

### Free Tier (siempre gratis)

* **BigQuery**: 10 GB de almacenamiento, 1 TB de queries/mes
* **Cloud Storage**: 5 GB de almacenamiento
* **Cloud Functions**: 2 millones de invocaciones/mes
* **Pub/Sub**: 10 GB de mensajes/mes

### Crédito inicial

* **$300 de crédito** gratis por 90 días (nuevas cuentas)

### Tips para ahorrar

* **Usa BigQuery** para analytics (muy eficiente en costo)
* **Apaga Dataproc** cuando no lo uses
* **Configura alertas** de costo
* **Usa datasets públicos** de BigQuery para practicar (gratis)
* **Revisa regularmente** el GCP Cost Management

---

## 📚 Recursos de aprendizaje

### Documentación oficial

* [GCP Data Engineering](https://cloud.google.com/solutions/data-engineering)
* [BigQuery Documentation](https://cloud.google.com/bigquery/docs)
* [Dataflow Documentation](https://cloud.google.com/dataflow/docs)

### Cursos y tutoriales

* Google Cloud Training (gratis)
* BigQuery Public Datasets (para practicar)
* Qwiklabs (laboratorios prácticos)

### Certificaciones

* **Google Cloud Professional Data Engineer** (recomendado)
* **Google Cloud Professional Cloud Architect**

---

## 🌟 Ventajas de GCP para Data Engineering

* **BigQuery es excepcional**: Serverless, rápido, escalable
* **Excelente para ML**: Integración con TensorFlow, Vertex AI
* **Datasets públicos**: Perfectos para aprender y practicar
* **Precios competitivos**: Especialmente BigQuery

---


## 🚀 ¿Qué sigue?

Después de dominar GCP:

* **[AWS](aws/)** para comparar con otro proveedor
* **[Multi-Cloud](multi-cloud/)** para estrategias avanzadas
* **[07_proyectos](../07_proyectos/)** para proyectos completos en GCP
* Profundizar en BigQuery avanzado o Dataflow

> 💡 **Tip**: Empieza con BigQuery - es el servicio más fácil de usar y tiene datasets públicos gratuitos para practicar.
