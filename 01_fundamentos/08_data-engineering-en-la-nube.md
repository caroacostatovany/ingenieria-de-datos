# Data Engineering en la Nube

El Data Engineering en la nube ha transformado cómo construimos y escalamos sistemas de datos. Entender los conceptos de cloud es esencial para Data Engineers modernos.

---

## 🧠 ¿Qué es Data Engineering en la Nube?

Data Engineering en la nube significa:

* **Construir pipelines** usando servicios gestionados en la nube
* **Almacenar datos** en almacenamiento cloud (S3, Azure Blob, GCS)
* **Procesar datos** con servicios serverless o clusters gestionados
* **Escalar automáticamente** según la demanda
* **Pagar por uso** en lugar de mantener infraestructura propia

> La nube permite enfocarte en los datos, no en la infraestructura.

---

## ☁️ Principales proveedores de Cloud

### AWS (Amazon Web Services)

**Servicios clave para Data Engineering:**
* **S3**: Almacenamiento de objetos
* **Glue**: ETL serverless
* **Redshift**: Data warehouse
* **EMR**: Procesamiento con Spark/Hadoop
* **Lambda**: Funciones serverless
* **Athena**: Query SQL sobre S3

### Google Cloud Platform (GCP)

**Servicios clave:**
* **Cloud Storage**: Almacenamiento de objetos
* **BigQuery**: Data warehouse serverless
* **Dataflow**: Procesamiento stream/batch
* **Dataproc**: Clusters Spark/Hadoop
* **Cloud Functions**: Funciones serverless

### Microsoft Azure

**Servicios clave:**
* **Azure Blob Storage**: Almacenamiento
* **Azure Data Factory**: ETL/ELT
* **Azure Synapse**: Analytics
* **Azure Databricks**: Spark en Azure
* **Azure Functions**: Serverless

---

## 🎯 Ventajas del Cloud para Data Engineering

### 1. Escalabilidad automática

```python
# En la nube, escalas automáticamente
# No necesitas preocuparte por capacidad del servidor
```

**Ventajas:**
* Procesa petabytes sin preocuparte por hardware
* Escala hacia abajo cuando no hay carga
* Paga solo por lo que usas

### 2. Servicios gestionados

**En lugar de:**
* Instalar y mantener PostgreSQL
* Configurar clusters de Spark
* Gestionar servidores

**En la nube:**
* Usas Redshift/BigQuery (gestionados)
* Usas EMR/Dataproc (clusters gestionados)
* No gestionas servidores

### 3. Integración nativa

Los servicios cloud están diseñados para trabajar juntos:

```
S3 → Glue → Redshift → QuickSight
```

Todo integrado, sin configuración compleja.

### 4. Costo variable

**Tradicional:**
* Pagas servidores 24/7 aunque no los uses

**Cloud:**
* Pagas solo cuando procesas datos
* Puedes apagar recursos cuando no los necesitas

---

## 🔄 Conceptos clave de Cloud

### Serverless

Ejecuta código sin gestionar servidores:

```python
# AWS Lambda
def lambda_handler(event, context):
    # Tu código aquí
    # Se ejecuta cuando hay datos nuevos
    return result
```

**Ventajas:**
* No gestionas servidores
* Escala automáticamente
* Paga por ejecución

### Almacenamiento de objetos

Almacena datos como objetos (no como archivos en sistema de archivos):

* **AWS S3**: `s3://bucket-name/path/to/file.parquet`
* **GCS**: `gs://bucket-name/path/to/file.parquet`
* **Azure Blob**: `https://account.blob.core.windows.net/container/file.parquet`

**Ventajas:**
* Escalable a petabytes
* Durabilidad garantizada
* Acceso desde cualquier lugar

### Data Warehouses en la nube

Bases de datos optimizadas para analytics:

* **Redshift** (AWS): Data warehouse columnar
* **BigQuery** (GCP): Data warehouse serverless
* **Snowflake**: Data warehouse multi-cloud

**Características:**
* Escalan automáticamente
* Separación de compute y storage
* Optimizados para queries analíticas

---

## 📊 Arquitectura típica en la nube

### Patrón básico

```
Fuentes de datos
    ↓
Almacenamiento (S3/GCS/Blob)
    ↓
ETL/Transformación (Glue/Dataflow/ADF)
    ↓
Data Warehouse (Redshift/BigQuery/Synapse)
    ↓
Visualización (QuickSight/Data Studio/Power BI)
```

### Ejemplo: Pipeline en AWS

```
1. Datos llegan a S3 (bucket raw/)
2. AWS Glue cataloga los datos
3. Glue ETL transforma y carga a S3 (bucket processed/)
4. Redshift Spectrum consulta S3 directamente
5. QuickSight visualiza desde Redshift
```

---

## 💰 Modelo de costos

### Pago por uso (Pay-as-you-go)

**Ventajas:**
* Empiezas pequeño, escalas cuando creces
* No pagas por capacidad no usada
* Costos predecibles basados en uso

**Consideraciones:**
* Monitorea costos regularmente
* Usa tags para tracking
* Apaga recursos no usados

### Reservas y ahorros

* **Reserved Instances**: Descuentos por compromiso
* **Spot Instances**: Precios más bajos para trabajos flexibles
* **Savings Plans**: Descuentos por uso consistente

---

## 🔒 Seguridad en la nube

### Responsabilidad compartida

**El proveedor gestiona:**
* Infraestructura física
* Virtualización
* Redes

**Tú gestionas:**
* Acceso a datos
* Configuración de seguridad
* Encriptación de datos

### Mejores prácticas

* **IAM**: Control de acceso granular
* **Encriptación**: En tránsito y en reposo
* **VPCs**: Redes privadas virtuales
* **Logging**: Auditoría de accesos

---

## 🚀 Cuándo usar Cloud

### ✅ Usa Cloud cuando:

* Necesitas escalar rápidamente
* Tienes cargas de trabajo variables
* Quieres reducir tiempo de mantenimiento
* Necesitas servicios gestionados
* Trabajas con datos distribuidos

### ⚠️ Considera alternativas cuando:

* Tienes requisitos de compliance estrictos
* Los datos no pueden salir de cierta región
* Tienes costos fijos muy predecibles
* Necesitas latencia ultra-baja

---

## 🎓 Próximos pasos

Una vez que entiendas los conceptos básicos:

1. **Elige un proveedor**: AWS, GCP o Azure
2. **Aprende los servicios básicos**: Almacenamiento, compute, data warehouse
3. **Construye un pipeline simple**: De S3 a Redshift, por ejemplo
4. **Explora servicios avanzados**: Streaming, ML, etc.

📁 **Contenido avanzado**: Revisa **[Orquestadores Cloud](../05_pipelines/orquestadores/cloud/)** para profundizar en orquestadores cloud y servicios principales.

---

## 💡 Tips

* **Empieza con un proveedor**: No intentes aprender los tres a la vez
* **Usa free tier**: Todos los proveedores ofrecen tier gratuito para aprender
* **Monitorea costos**: Configura alertas desde el inicio
* **Lee documentación oficial**: Es excelente y actualizada

---

> **Recuerda**: La nube es una herramienta, no un fin. El objetivo sigue siendo construir pipelines confiables y escalables. La nube solo hace más fácil lograrlo.
