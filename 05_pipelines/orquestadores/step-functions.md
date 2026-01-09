# AWS Step Functions: Orquestación Serverless

AWS Step Functions es un servicio serverless de AWS para orquestar workflows.

---

## 🧠 ¿Qué es Step Functions?

AWS Step Functions es:
* **Serverless**: No gestionas infraestructura
* **Nativo de AWS**: Integración profunda con servicios AWS
* **Visual**: Define workflows con JSON o UI visual
* **Escalable**: Escala automáticamente

> Step Functions es ideal si ya estás en AWS y quieres orquestación serverless.

---

## 🚀 Conceptos clave

### State Machine (Máquina de estados)

Un workflow se define como una máquina de estados.

```json
{
  "Comment": "Pipeline ETL",
  "StartAt": "ExtraerDatos",
  "States": {
    "ExtraerDatos": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:region:account:function:extraer",
      "Next": "TransformarDatos"
    },
    "TransformarDatos": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:region:account:function:transformar",
      "Next": "CargarDatos"
    },
    "CargarDatos": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:region:account:function:cargar",
      "End": true
    }
  }
}
```

### Estados

Tipos de estados:
* **Task**: Ejecuta una función Lambda o servicio
* **Choice**: Decisión condicional
* **Parallel**: Ejecución paralela
* **Wait**: Esperar tiempo
* **Succeed/Fail**: Terminar con éxito/error

---

## 🎯 Ejemplo con Lambda

```python
# lambda_extraer.py
import json

def lambda_handler(event, context):
    # Extraer datos
    datos = {"ventas": [1, 2, 3]}
    return {
        'statusCode': 200,
        'body': json.dumps(datos)
    }

# lambda_transformar.py
import json

def lambda_handler(event, context):
    # Transformar datos recibidos
    datos = json.loads(event['body'])
    # Transformar...
    return {
        'statusCode': 200,
        'body': json.dumps(datos)
    }
```

### State Machine

```json
{
  "StartAt": "Extraer",
  "States": {
    "Extraer": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:123456789:function:extraer",
      "Next": "Transformar"
    },
    "Transformar": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:123456789:function:transformar",
      "End": true
    }
  }
}
```

---

## 🔄 Integración con servicios AWS

### S3

```json
{
  "Type": "Task",
  "Resource": "arn:aws:states:::s3:getObject",
  "Parameters": {
    "Bucket": "mi-bucket",
    "Key": "data/raw/ventas.csv"
  }
}
```

### Glue

```json
{
  "Type": "Task",
  "Resource": "arn:aws:states:::glue:startJobRun.sync",
  "Parameters": {
    "JobName": "mi-job-etl"
  }
}
```

### EMR

```json
{
  "Type": "Task",
  "Resource": "arn:aws:states:::elasticmapreduce:createCluster.sync",
  "Parameters": {
    "Name": "Cluster ETL",
    "ReleaseLabel": "emr-6.0.0"
  }
}
```

---

## 💡 Ventajas de Step Functions

### 1. Serverless

* No gestionas servidores
* Escala automáticamente
* Paga por uso

### 2. Integración AWS

* Integración nativa con servicios AWS
* Fácil de usar con Lambda, Glue, EMR, etc.

### 3. Visual

* UI visual para diseñar workflows
* Fácil de entender y mantener

---

## ⚠️ Desventajas

### 1. Vendor lock-in

* Solo funciona en AWS
* Difícil migrar a otros clouds

### 2. Costos

* Puede ser caro con muchos estados
* Costos por transición de estado

---

## 🎯 Cuándo usar Step Functions

✅ **Usa Step Functions cuando:**
* Ya estás en AWS
* Quieres serverless
* Necesitas integración con servicios AWS
* Prefieres no gestionar infraestructura

❌ **No uses Step Functions cuando:**
* No estás en AWS
* Necesitas portabilidad
* Prefieres código sobre configuración JSON

---

## 🚀 Próximos pasos

* **CDK/CloudFormation**: Infraestructura como código
* **Error handling**: Manejo de errores avanzado
* **Parallel execution**: Ejecución paralela
* **Choice states**: Lógica condicional

---

> **Recuerda**: Step Functions es excelente para AWS, pero te ata a ese ecosistema.
