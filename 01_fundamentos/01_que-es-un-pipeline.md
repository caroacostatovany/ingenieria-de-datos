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

## 🔄 Patrones de pipelines: ETL, ELT y más

Los pipelines siguen diferentes **patrones arquitectónicos** según dónde y cuándo se realizan las transformaciones.

### 📥 ETL: Extract, Transform, Load

**El patrón tradicional.**

```text
Fuente → Transformar → Cargar al destino
```

**Flujo:**
1. **Extract**: Extraer datos de la fuente
2. **Transform**: Transformar en un sistema intermedio
3. **Load**: Cargar datos transformados al destino

**Características:**
* Las transformaciones ocurren **antes** de cargar
* Requiere un sistema intermedio para procesar
* Los datos llegan ya transformados al destino

**Ventajas:**
* Datos listos para consumo inmediato
* Menor carga en el destino
* Bueno para Data Warehouses tradicionales

**Desventajas:**
* Requiere infraestructura intermedia
* Menos flexible para cambios de esquema
* Puede ser más lento

**Cuándo usar:**
* Data Warehouses tradicionales (Redshift, Snowflake clásico)
* Cuando el destino tiene capacidades limitadas de procesamiento
* Transformaciones complejas que requieren mucho cómputo

---

### 📤 ELT: Extract, Load, Transform

**El patrón moderno.**

```text
Fuente → Cargar al destino → Transformar en el destino
```

**Flujo:**
1. **Extract**: Extraer datos de la fuente
2. **Load**: Cargar datos crudos al destino
3. **Transform**: Transformar dentro del destino

**Características:**
* Los datos se cargan **primero** (crudos)
* Las transformaciones ocurren **en el destino**
* El destino debe ser capaz de procesar

**Ventajas:**
* Más flexible para cambios de esquema
* Menos infraestructura intermedia
* Datos crudos siempre disponibles
* Aprovecha el poder del destino (cloud warehouses)

**Desventajas:**
* Requiere un destino potente
* Puede ser más costoso en procesamiento
* Datos crudos ocupan más espacio

**Cuándo usar:**
* **Data Lakes** (S3, ADLS, GCS) - El patrón estándar para Data Lakes
* Data Warehouses modernos (BigQuery, Snowflake, Databricks)
* Cuando necesitas flexibilidad en transformaciones
* Cuando quieres mantener datos crudos

---

### 🔄 ETLT: Extract, Transform, Load, Transform

**Patrón híbrido.**

```text
Fuente → Transformar (básico) → Cargar → Transformar (avanzado)
```

**Flujo:**
1. **Extract**: Extraer datos
2. **Transform** (básico): Limpieza y normalización inicial
3. **Load**: Cargar al destino
4. **Transform** (avanzado): Transformaciones complejas en el destino

**Características:**
* Combina lo mejor de ETL y ELT
* Transformaciones básicas antes de cargar
* Transformaciones complejas después de cargar

**Cuándo usar:**
* Cuando necesitas limpieza inicial pero también flexibilidad
* Sistemas híbridos con múltiples capas

---

### ⬅️ Reverse ETL

**Llevar datos del warehouse a sistemas operacionales.**

```text
Data Warehouse → Transformar → Sistemas operacionales (CRM, Marketing, etc.)
```

**Flujo:**
1. Extraer datos del Data Warehouse
2. Transformar para el sistema destino
3. Cargar a sistemas operacionales (Salesforce, HubSpot, etc.)

**Propósito:**
* Activar datos analíticos en sistemas operacionales
* Enriquecer sistemas CRM con insights
* Sincronizar datos entre sistemas

**Ejemplo:**
* Llevar segmentos de clientes del warehouse a herramientas de marketing
* Enviar métricas calculadas a sistemas de ventas

---

### 📊 Comparación rápida

| Aspecto | ETL | ELT |
|---------|-----|-----|
| **Orden** | Transformar → Cargar | Cargar → Transformar |
| **Datos crudos** | No se guardan | Se guardan |
| **Infraestructura** | Requiere sistema intermedio | Menos infraestructura |
| **Flexibilidad** | Menor | Mayor |
| **Costo procesamiento** | En sistema intermedio | En destino |
| **Ideal para** | Warehouses tradicionales | **Data Lakes** y Warehouses modernos (cloud) |

> 💡 **Data Lakes y ELT**: Los Data Lakes (S3, Azure Data Lake, Google Cloud Storage) **siempre usan ELT** porque están diseñados para almacenar datos crudos y aplicar transformaciones al leerlos (schema-on-read). Esto permite máxima flexibilidad y evita perder datos originales.

---

### 🎯 ¿Cuál elegir?

**Elige ETL si:**
* Tu destino tiene capacidades limitadas
* Necesitas datos listos para consumo inmediato
* Trabajas con Data Warehouses tradicionales

**Elige ELT si:**
* **Trabajas con Data Lakes** (S3, ADLS, GCS) - **ELT es el patrón estándar**
* Tienes un Data Warehouse moderno (cloud)
* Quieres mantener datos crudos
* Necesitas flexibilidad en transformaciones
* Quieres simplificar la arquitectura

**Elige Reverse ETL si:**
* Necesitas activar datos analíticos en sistemas operacionales
* Quieres enriquecer sistemas CRM/Marketing con insights

> 💡 **En la práctica**: La mayoría de sistemas modernos usan **ELT** porque los Data Warehouses cloud son muy potentes. ETL sigue siendo válido para casos específicos.

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

Las buenas prácticas en pipelines no son reglas rígidas. Son **principios que reducen errores, facilitan el mantenimiento y permiten escalar**.

### 1. Diseña antes de escribir código

Antes de programar, pregúntate:

* ¿Cuál es la fuente del dato?
* ¿Quién lo va a consumir?
* ¿Qué formato necesita?
* ¿Qué pasa si falla?
* ¿Se puede reejecutar?
* ¿Qué datos produce?
* ¿Cómo se valida la calidad?

Un pipeline pensado ahorra más tiempo que uno rápido.

### 2. Una responsabilidad por proceso

Cada tarea debe hacer **una sola cosa**:

* extraer
* transformar
* cargar

Evita:

* funciones "todopoderosas"
* scripts interminables
* lógica mezclada

> La claridad es una forma de escalabilidad.

### 3. Piensa en la reejecución

Un pipeline bien diseñado:

* puede ejecutarse más de una vez
* no duplica datos
* no corrompe resultados

Pregúntate:

* ¿puedo reejecutar este proceso sin miedo?

La reejecución segura es clave para operar.

### 4. Maneja errores explícitamente

Los errores no deben:

* esconderse
* ignorarse
* corregirse manualmente

Buenas prácticas:

* capturar excepciones
* fallar rápido
* registrar contexto
* alertar cuando es necesario

> Fallar bien es mejor que "parecer que funciona".

### 5. Agrega observabilidad desde el inicio

Incluso en pipelines simples:

* logs
* conteo de registros
* tiempos de ejecución

Si no sabes qué pasó:

* no puedes arreglarlo
* no puedes escalarlo

### 6. Valida la calidad de los datos

No asumas que los datos son correctos.

Valida:

* esquemas
* valores nulos
* rangos
* duplicados

La calidad no es opcional. Es parte del pipeline.

### 7. Estructura tu código

Evita:

* scripts sueltos
* lógica duplicada

Prefiere:

* funciones reutilizables
* módulos
* carpetas claras

El orden reduce errores.

### 8. Nombra bien las cosas

Nombres claros para:

* funciones
* tablas
* columnas
* archivos

Malos nombres generan:

* confusión
* errores
* dependencia de personas específicas

Si necesitas explicar un nombre, probablemente no es bueno.

### 9. Documenta decisiones, no solo código

Más importante que *qué hace* el código es:

* por qué existe
* qué problema resuelve
* qué trade-offs se tomaron

La documentación ahorra tiempo futuro.

---

## 🚫 Errores comunes que estas prácticas evitan

* pipelines frágiles
* procesos manuales
* dependencia de una sola persona
* datos inconsistentes
* deuda técnica innecesaria

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

Para continuar:
* **[Batch vs Streaming](02_batch-vs-streaming.md)** - Tipos de procesamiento

Para profundizar:
* **[Pipelines básicos](../05_pipelines/pipelines-basicos/)** - Cómo construir pipelines
* **[Orquestadores](../05_pipelines/orquestadores/)** - Herramientas para orquestar pipelines

---

**Un pipeline no se mide por lo complejo que es,
sino por lo confiable que resulta.**
