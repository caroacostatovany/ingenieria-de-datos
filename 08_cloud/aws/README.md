# AWS para Data Engineers

Amazon Web Services (AWS) es el proveedor cloud más popular y ampliamente usado en la industria. Aprende a construir pipelines de datos escalables y robustos en AWS.

---

## 📖 Servicios principales para Data Engineering

### Almacenamiento

* **S3 (Simple Storage Service)**: Almacenamiento de objetos escalable
  * Ideal para: Data Lakes, archivos raw, backups
  * Características: Versionado, lifecycle policies, encriptación

### ETL y Procesamiento

* **AWS Glue**: ETL serverless y catalogado de datos
  * Ideal para: Transformaciones, catalogado, crawlers
  * Características: Sin servidores, pago por uso, integrado con otros servicios

* **EMR (Elastic MapReduce)**: Clusters Spark/Hadoop gestionados
  * Ideal para: Procesamiento de grandes volúmenes, Spark jobs
  * Características: Auto-scaling, múltiples frameworks

* **Lambda**: Funciones serverless
  * Ideal para: Micro-ETL, triggers, procesamiento ligero
  * Características: Sin servidores, pago por ejecución

### Data Warehouse y Analytics

* **Redshift**: Data warehouse columnar
  * Ideal para: Analytics, BI, queries complejas
  * Características: Escalable, optimizado para analytics

* **Athena**: Query SQL sobre S3 (serverless)
  * Ideal para: Análisis ad-hoc sobre Data Lakes
  * Características: Sin infraestructura, pago por query

### Streaming

* **Kinesis**: Streaming de datos en tiempo real
  * Ideal para: Procesamiento en tiempo real, event streaming
  * Características: Escalable, integrado con Lambda

---

## 🎯 Objetivo de esta sección

Al finalizar, deberías poder:

* Configurar una cuenta AWS y usar el free tier
* Almacenar datos en S3 de forma eficiente
* Construir pipelines ETL con AWS Glue
* Consultar datos con Athena
* Entender cuándo usar cada servicio
* Optimizar costos en AWS

---

## 🚀 Cómo empezar

### 1. Crear cuenta AWS

1. Ve a [aws.amazon.com](https://aws.amazon.com)
2. Crea una cuenta (requiere tarjeta, pero free tier es generoso)
3. **Configura alertas de costo** desde el inicio
4. Activa MFA (autenticación de dos factores)

### 2. Explorar la consola

* Familiarízate con la interfaz de AWS Console
* Revisa los servicios disponibles
* Explora la documentación oficial

### 3. Primeros pasos prácticos

**Ejercicio 1: S3 básico**
1. Crea un bucket S3
2. Sube un archivo CSV
3. Configura permisos y versionado

**Ejercicio 2: Athena sobre S3**
1. Crea una tabla en Athena apuntando a tu CSV en S3
2. Ejecuta queries SQL sobre los datos
3. Explora los resultados

**Ejercicio 3: Glue básico**
1. Crea un Glue Crawler para catalogar datos en S3
2. Revisa el Data Catalog generado
3. Crea un job ETL simple

---

## 💰 Free Tier y costos

### Free Tier (12 meses)

* **S3**: 5 GB de almacenamiento
* **Lambda**: 1 millón de requests gratis
* **Glue**: 10,000 objetos catalogados gratis
* **Athena**: 10 GB de datos escaneados gratis/mes

### Tips para ahorrar

* **Apaga recursos** cuando no los uses (Redshift, EMR)
* **Usa S3 Intelligent-Tiering** para almacenamiento
* **Configura alertas** de costo ($10, $50, $100)
* **Revisa regularmente** el AWS Cost Explorer
* **Usa tags** para organizar y monitorear costos

---

## 📚 Recursos de aprendizaje

### Documentación oficial

* [AWS Data Engineering](https://aws.amazon.com/data-engineering/)
* [AWS Glue Documentation](https://docs.aws.amazon.com/glue/)
* [S3 Best Practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html)

### Cursos y tutoriales

* AWS Training (gratis)
* AWS Well-Architected Framework
* AWS re:Invent videos (YouTube)

### Certificaciones

* **AWS Certified Data Analytics - Specialty** (recomendado)
* **AWS Certified Solutions Architect** (fundamental)

---

## 🔗 Relación con otros módulos

* Aplica conceptos de **[05_pipelines](../05_pipelines/)** en AWS
* Usa SQL de **[02_sql](../02_sql/)** con Redshift y Athena
* Implementa calidad de **[04_modelado_y_calidad](../04_modelado_y_calidad/)** en Glue
* Python de **[03_python](../03_python/)** en Lambda y Glue

---

## 🚀 ¿Qué sigue?

Después de dominar AWS:

* **[GCP](gcp/)** para comparar con otro proveedor
* **[Multi-Cloud](multi-cloud/)** para estrategias avanzadas
* **[07_proyectos](../07_proyectos/)** para proyectos completos en AWS
* Profundizar en servicios específicos (Kinesis, Redshift, etc.)

> 💡 **Tip**: No necesitas dominar todos los servicios. Enfócate en S3, Glue y Athena primero, luego expande según tus necesidades.
