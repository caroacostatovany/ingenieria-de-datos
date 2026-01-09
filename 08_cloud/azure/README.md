# Microsoft Azure para Data Engineers

Microsoft Azure ofrece servicios integrados para Data Engineering, especialmente útil en entornos Microsoft y organizaciones que ya usan productos Microsoft (Office 365, Active Directory, etc.).

---

## 📖 Servicios principales para Data Engineering

### Almacenamiento

* **Azure Blob Storage**: Almacenamiento de objetos escalable
  * Ideal para: Data Lakes, archivos raw, backups
  * Características: Hot/Cool/Archive tiers, lifecycle management

* **Azure Data Lake Storage Gen2**: Optimizado para analytics
  * Ideal para: Big Data analytics, Data Lakes
  * Características: Compatible con HDFS, integrado con servicios analytics

### ETL y Procesamiento

* **Azure Data Factory**: ETL/ELT serverless
  * Ideal para: Orquestación de pipelines, integración de datos
  * Características: Visual interface, 90+ conectores, serverless

* **Azure Databricks**: Spark optimizado en Azure
  * Ideal para: Procesamiento de Big Data, ML, Spark jobs
  * Características: Optimizado para Azure, integrado con ML

* **Azure Functions**: Funciones serverless
  * Ideal para: Micro-ETL, triggers, procesamiento ligero
  * Características: Sin servidores, múltiples lenguajes

### Data Warehouse y Analytics

* **Azure Synapse Analytics**: Analytics unificado
  * Ideal para: Data warehousing, analytics, BI
  * Características: SQL y Spark en un solo servicio, integrado

* **Azure SQL Database**: Base de datos relacional gestionada
  * Ideal para: Aplicaciones, OLTP, bases de datos pequeñas/medianas

### Streaming

* **Event Hubs**: Streaming de eventos
  * Ideal para: Event streaming, telemetría, IoT
  * Características: Alta throughput, integrado con otros servicios

---

## 🎯 Objetivo de esta sección

Al finalizar, deberías poder:

* Configurar una cuenta Azure y usar el free tier
* Almacenar datos en Blob Storage o Data Lake
* Construir pipelines con Azure Data Factory
* Procesar datos con Azure Databricks
* Entender cuándo usar cada servicio
* Optimizar costos en Azure

---

## 🚀 Cómo empezar

### 1. Crear cuenta Azure

1. Ve a [azure.microsoft.com](https://azure.microsoft.com)
2. Crea una cuenta (requiere tarjeta, pero $200 de crédito gratis)
3. **Configura alertas de costo** desde el inicio
4. Activa MFA (autenticación de dos factores)

### 2. Explorar Azure Portal

* Familiarízate con la interfaz de Azure Portal
* Revisa los servicios disponibles
* Explora Azure Cloud Shell (terminal en el navegador)

### 3. Primeros pasos prácticos

**Ejercicio 1: Blob Storage**
1. Crea un Storage Account
2. Crea un container (bucket)
3. Sube un archivo CSV
4. Configura permisos y access tiers

**Ejercicio 2: Azure Data Factory**
1. Crea un Data Factory
2. Usa el visual interface para crear un pipeline simple
3. Copia datos de Blob Storage a otro destino

**Ejercicio 3: Azure Databricks**
1. Crea un workspace de Databricks
2. Crea un cluster
3. Ejecuta un notebook con Spark

---

## 💰 Free Tier y costos

### Free Tier (siempre gratis)

* **Blob Storage**: 5 GB LRS (Local Redundant Storage)
* **Azure Functions**: 1 millón de requests/mes
* **Event Hubs**: 1 unidad básica gratis

### Crédito inicial

* **$200 de crédito** gratis por 30 días (nuevas cuentas)

### Tips para ahorrar

* **Apaga recursos** cuando no los uses (Databricks, Synapse)
* **Usa Storage tiers** apropiados (Hot/Cool/Archive)
* **Configura alertas** de costo
* **Revisa regularmente** Azure Cost Management
* **Usa Azure Advisor** para recomendaciones de optimización

---

## 📚 Recursos de aprendizaje

### Documentación oficial

* [Azure Data Engineering](https://azure.microsoft.com/solutions/data-engineering/)
* [Azure Data Factory Documentation](https://docs.microsoft.com/azure/data-factory/)
* [Azure Databricks Documentation](https://docs.microsoft.com/azure/databricks/)

### Cursos y tutoriales

* Microsoft Learn (gratis, con certificaciones)
* Azure Data Factory tutorials
* Azure Databricks learning paths

### Certificaciones

* **Microsoft Certified: Azure Data Engineer Associate** (recomendado)
* **Microsoft Certified: Azure Solutions Architect Expert**

---

## 🌟 Ventajas de Azure para Data Engineering

* **Integración Microsoft**: Excelente si ya usas Office 365, Active Directory
* **Azure Data Factory**: Interface visual muy intuitiva
* **Azure Databricks**: Spark optimizado y potente
* **Azure Synapse**: Analytics unificado en un solo servicio

---

## 🔗 Relación con otros módulos

* Aplica conceptos de **[05_pipelines](../05_pipelines/)** en Azure
* Usa SQL de **[02_sql](../02_sql/)** con Azure Synapse
* Implementa calidad de **[04_modelado_y_calidad](../04_modelado_y_calidad/)** en Data Factory
* Python de **[03_python](../03_python/)** en Databricks y Functions

---

## 🚀 ¿Qué sigue?

Después de dominar Azure:

* **[AWS](aws/)** o **[GCP](gcp/)** para comparar con otros proveedores
* **[Multi-Cloud](multi-cloud/)** para estrategias avanzadas
* **[07_proyectos](../07_proyectos/)** para proyectos completos en Azure
* Profundizar en Azure Databricks o Synapse

> 💡 **Tip**: Azure es especialmente útil si trabajas en entornos Microsoft. Data Factory tiene una interface visual muy amigable para empezar.
