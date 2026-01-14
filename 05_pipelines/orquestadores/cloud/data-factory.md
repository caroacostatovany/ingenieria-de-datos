# Azure Data Factory: Orquestación en Azure

Azure Data Factory es el servicio de orquestación nativo de Microsoft Azure.

> 📖 **Parte de**: [Orquestadores Cloud - README](README.md) | **Proveedor**: Azure

---

## 🧠 ¿Qué es Azure Data Factory?

Azure Data Factory es:
* **Nativo de Azure**: Integración profunda con servicios Azure
* **UI visual**: Diseño visual de pipelines
* **Code-first opcional**: También soporta código
* **Gestionado**: Sin gestión de infraestructura

> Data Factory es ideal si estás en el ecosistema Microsoft/Azure.

---

## 🚀 Conceptos clave

### Pipeline

Un pipeline es un grupo de actividades.

### Activities (Actividades)

Tareas dentro de un pipeline:
* **Copy**: Copiar datos
* **Transform**: Transformar con Databricks, HDInsight, etc.
* **Execute**: Ejecutar stored procedures, funciones, etc.

### Datasets

Definiciones de datos de entrada/salida.

### Linked Services

Conexiones a servicios externos.

---

## 🎯 Ejemplo visual

Data Factory se usa principalmente con UI visual:

1. **Crear pipeline** en Azure Portal
2. **Agregar actividades** visualmente
3. **Configurar conexiones**
4. **Programar ejecución**

También soporta código (JSON):

```json
{
  "name": "PipelineETL",
  "activities": [
    {
      "name": "CopyData",
      "type": "Copy",
      "inputs": [{"name": "InputDataset"}],
      "outputs": [{"name": "OutputDataset"}]
    }
  ]
}
```

---

## 💡 Ventajas

### 1. Integración Azure

* Azure Blob Storage
* Azure SQL Database
* Azure Synapse
* Azure Databricks

### 2. UI visual

* Fácil para no-programadores
* Visualización clara de pipelines

### 3. Gestionado

* Sin gestión de infraestructura
* Escalable automáticamente

---

## ⚠️ Desventajas

### 1. Vendor lock-in

* Solo funciona en Azure
* Difícil migrar

### 2. Menos flexible

* Menos control que Airflow
* UI puede ser limitante

---

## 🎯 Cuándo usar

✅ **Usa Data Factory cuando:**
* Estás en Azure
* Prefieres UI visual
* Necesitas integración con servicios Azure
* Equipo no técnico necesita crear pipelines

❌ **No uses Data Factory cuando:**
* No estás en Azure
* Prefieres código sobre UI
* Necesitas máxima flexibilidad

---

> **Recuerda**: Data Factory es excelente para Azure, especialmente si prefieres UI visual.
