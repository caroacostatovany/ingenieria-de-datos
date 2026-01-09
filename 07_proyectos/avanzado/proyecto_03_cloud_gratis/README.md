# Proyecto 3: Pipeline en Cloud (Sin Tarjeta)

Despliega un pipeline a la nube usando servicios gratuitos. Aprende cloud sin costo.

---

## 🎯 Objetivo

Aprender a:
* Desplegar pipelines en la nube
* Usar servicios gratuitos de cloud
* Configurar automatización en cloud
* Gestionar recursos cloud

---

## 📋 Requisitos previos

* Cuenta en al menos un proveedor cloud (Google Cloud, AWS, Azure)
* Conocimientos básicos de cloud
* Entendimiento de servicios gratuitos

---

## 🚀 Opciones de Cloud Gratis

### Opción 1: Google Cloud Platform (GCP)

**Servicios gratuitos disponibles:**
* Cloud Run (2 millones de requests/mes gratis)
* Cloud Functions (2 millones de invocaciones/mes)
* Cloud SQL (solo instancia pequeña, limitada)
* BigQuery (10 GB almacenamiento, 1 TB procesamiento/mes)

### Opción 2: AWS

**Servicios gratuitos disponibles:**
* Lambda (1 millón de requests/mes gratis)
* RDS (750 horas/mes de db.t2.micro)
* S3 (5 GB almacenamiento)
* Glue (limitado)

### Opción 3: Azure

**Servicios gratuitos disponibles:**
* Functions (1 millón de requests/mes)
* SQL Database (limitado)
* Storage (5 GB)
* Data Factory (limitado)

---

## 📖 Proyecto: Pipeline en GCP (Recomendado)

### 1. Estructura del proyecto

```
proyecto_03_cloud_gratis/
├── README.md
├── cloud/
│   ├── gcp/
│   │   ├── cloud_run/
│   │   │   └── Dockerfile
│   │   └── cloud_function/
│   │       └── main.py
│   └── aws/
│       └── lambda/
│           └── lambda_function.py
├── src/
│   └── pipeline.py
└── terraform/  # Opcional
    └── main.tf
```

### 2. Pipeline para Cloud Run (GCP)

`cloud/gcp/cloud_run/Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

CMD ["python", "src/pipeline.py"]
```

### 3. Desplegar a Cloud Run

```bash
# Instalar Google Cloud SDK
# https://cloud.google.com/sdk/docs/install

# Autenticar
gcloud auth login

# Configurar proyecto
gcloud config set project TU_PROJECT_ID

# Construir y desplegar
gcloud run deploy pipeline-etl \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated

# Configurar trigger (Cloud Scheduler para ejecución periódica)
gcloud scheduler jobs create http pipeline-daily \
  --schedule="0 2 * * *" \
  --uri="https://pipeline-etl-xxx.run.app" \
  --http-method=GET
```

### 4. Cloud Function (Alternativa más simple)

`cloud/gcp/cloud_function/main.py`:

```python
def pipeline_etl(request):
    """
    Cloud Function que ejecuta pipeline ETL.
    """
    import pandas as pd
    from google.cloud import bigquery
    
    # Tu lógica de pipeline aquí
    print("🚀 Ejecutando pipeline en Cloud Function")
    
    # Ejemplo: Cargar a BigQuery
    client = bigquery.Client()
    
    # Tu código de pipeline
    # ...
    
    return {"status": "success", "message": "Pipeline ejecutado"}
```

Desplegar:

```bash
gcloud functions deploy pipeline-etl \
  --runtime python311 \
  --trigger-http \
  --entry-point pipeline_etl \
  --memory 256MB \
  --timeout 540s
```

### 5. Usar Cloud Scheduler (Gratis)

```bash
# Crear job que ejecuta cada día a las 2 AM
gcloud scheduler jobs create http daily-pipeline \
  --schedule="0 2 * * *" \
  --uri="https://REGION-PROJECT.cloudfunctions.net/pipeline-etl" \
  --http-method=GET \
  --oidc-service-account-email=SERVICE_ACCOUNT@PROJECT.iam.gserviceaccount.com
```

---

## 📖 Alternativa: AWS Lambda

### Lambda Function

`cloud/aws/lambda/lambda_function.py`:

```python
import json

def lambda_handler(event, context):
    """
    Lambda function que ejecuta pipeline ETL.
    """
    print("🚀 Ejecutando pipeline en Lambda")
    
    # Tu lógica de pipeline aquí
    # ...
    
    return {
        'statusCode': 200,
        'body': json.dumps('Pipeline ejecutado exitosamente')
    }
```

Desplegar con AWS CLI:

```bash
# Crear package
zip function.zip lambda_function.py

# Crear función
aws lambda create-function \
  --function-name pipeline-etl \
  --runtime python3.11 \
  --role arn:aws:iam::ACCOUNT:role/lambda-role \
  --handler lambda_function.lambda_handler \
  --zip-file fileb://function.zip

# Configurar EventBridge (CloudWatch Events) para ejecución periódica
aws events put-rule \
  --name daily-pipeline \
  --schedule-expression "cron(0 2 * * ? *)"

aws lambda add-permission \
  --function-name pipeline-etl \
  --statement-id allow-eventbridge \
  --action lambda:InvokeFunction \
  --principal events.amazonaws.com
```

---

## 💡 Tips para mantenerte en el tier gratuito

### GCP
* ✅ Usa Cloud Run con mínimo de instancias = 0
* ✅ Usa Cloud Functions en lugar de Compute Engine
* ✅ Usa BigQuery solo para queries pequeñas
* ✅ Monitorea uso en Cloud Console

### AWS
* ✅ Usa Lambda con timeout corto
* ✅ Usa RDS solo cuando sea necesario
* ✅ Limpia recursos no usados
* ✅ Configura alertas de billing

### Azure
* ✅ Usa Functions en lugar de VMs
* ✅ Usa tier gratuito de servicios
* ✅ Monitorea uso en Azure Portal

---

## ✅ Checklist de completado

- [ ] Cuenta cloud creada (sin tarjeta si es posible)
- [ ] Pipeline desplegado a cloud
- [ ] Automatización configurada (scheduler)
- [ ] Pipeline ejecutándose periódicamente
- [ ] Monitoreo básico configurado
- [ ] Documentación de deployment completa
- [ ] Costos verificados (deben ser $0)

---

## 🎓 Conceptos aprendidos

* ✅ Deployment a cloud
* ✅ Servicios serverless
* ✅ Automatización en cloud
* ✅ Gestión de recursos cloud
* ✅ Monitoreo de costos

---

## 🚀 Próximo paso

Después de completar este proyecto:
* Explora más servicios cloud
* Implementa pipelines más complejos
* Considera multi-cloud

---

## ⚠️ Importante

* **Siempre monitorea tus costos** - Configura alertas
* **Limpia recursos no usados** - Evita cargos inesperados
* **Lee los términos del tier gratuito** - Cada proveedor tiene límites diferentes
* **Usa servicios serverless** - Generalmente más baratos

---

> **Recuerda**: El tier gratuito tiene límites. Monitorea tu uso y configura alertas de billing.
