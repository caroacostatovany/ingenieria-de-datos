# ¿Qué es un pipeline de datos?

Un **pipeline de datos** es un sistema que **orquesta, ejecuta y monitorea** una serie de pasos para mover y transformar datos de forma **confiable y repetible**.

Un pipeline no es solo código.
Es una **pieza de ingeniería**.

---

## 🧠 Pipeline ≠ Script

Un error común es pensar que un pipeline es simplemente:

* un script largo
* un cron job
* una secuencia de comandos

Eso puede funcionar al inicio, pero **no escala**.

### Diferencia clave

| Script              | Pipeline                  |
| ------------------- | ------------------------- |
| Ejecuta tareas      | Orquesta procesos         |
| Poco control        | Manejo de dependencias    |
| Difícil de observar | Monitoreable              |
| Frágil              | Diseñado para fallar bien |

---

## 🧱 Elementos fundamentales de un pipeline

Un pipeline bien diseñado incluye:

### 1️⃣ Tareas

Unidades pequeñas y claras de trabajo:

* extraer datos
* transformar datos
* cargar resultados

Cada tarea hace **una sola cosa**.

---

### 2️⃣ Dependencias

Definen el orden correcto de ejecución.

Ejemplo:

```text
Extraer → Transformar → Cargar
```

**DAG (Directed Acyclic Graph)**: En orquestadores, las dependencias se representan como un DAG (grafo acíclico dirigido). Un DAG es una estructura que define tareas y sus dependencias sin ciclos, asegurando que las tareas se ejecuten en el orden correcto. Por ejemplo, en Airflow, cada pipeline es un DAG donde las tareas tienen dependencias claras.

Sin dependencias claras:

* hay datos incompletos
* los resultados son inconsistentes

---

### 3️⃣ Manejo de errores

Los errores **van a ocurrir**.

Un pipeline debe:

* detectar fallos
* detenerse si es necesario
* permitir reintentos
* no corromper datos

---

### 4️⃣ Observabilidad

Saber qué está pasando.

Incluye:

* logs
* estados de ejecución
* tiempos
* alertas

Un pipeline invisible es un pipeline peligroso.

---

## 🔄 Tipos de pipelines

### 📦 Pipelines batch

* Procesan datos en bloques
* Se ejecutan por horarios
* Son los más comunes

Ejemplo:

* cargas diarias
* reportes semanales

---

### ⚡ Pipelines streaming

* Procesan datos en tiempo real
* Manejan eventos continuos
* Más complejos de operar

Ejemplo:

* eventos de usuario
* sensores

> La mayoría de sistemas empiezan en batch.

---

## 🧭 Pipelines como parte de un sistema mayor

Los pipelines no viven solos.

Normalmente forman parte de:

* Data Warehouses
* Data Lakes
* Plataformas analíticas

Por eso deben diseñarse pensando en:

* escalabilidad
* mantenimiento
* impacto en otros equipos

---

## 🧠 Buen diseño de pipelines

Algunas preguntas clave antes de construir uno:

* ¿Qué pasa si falla?
* ¿Se puede reejecutar?
* ¿Qué datos produce?
* ¿Quién los consume?
* ¿Cómo se valida la calidad?

Un pipeline bien pensado evita problemas futuros.

---

## 🤖 ¿Dónde entra la AI?

La AI puede ayudar a:

* documentar pipelines
* generar plantillas
* revisar lógica básica
* sugerir mejoras

Pero:

* no entiende tu contexto de negocio
* no asume la responsabilidad del resultado

---

## ➡️ ¿Qué sigue?

Para profundizar:
* **[Pipelines con Python](pipelines-con-python.md)** - Cómo construir pipelines prácticos
* **[Orquestadores](../orquestadores/)** - Herramientas para orquestar pipelines
* **[Batch vs Streaming](../../01_fundamentos/batch-vs-streaming.md)** - Tipos de procesamiento

O aplica todo con:
* **[Proyectos](../../07_proyectos/)** - Proyectos end-to-end

---

**Un pipeline no se mide por lo complejo que es,
sino por lo confiable que resulta.**
