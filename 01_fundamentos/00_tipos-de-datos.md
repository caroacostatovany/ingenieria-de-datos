# Tipos de datos en Ingeniería de Datos

En Ingeniería de Datos, **entender los tipos de datos es tan importante como saber procesarlos**.
No todos los datos se tratan igual, ni deberían viajar por los mismos pipelines.

Elegir mal cómo tratar un tipo de dato genera:

* pipelines innecesariamente complejos
* costos elevados
* errores difíciles de detectar

---

## 🧠 ¿Por qué importa clasificar los datos?

Porque el tipo de dato determina:

* cómo se ingiere
* cómo se almacena
* cómo se transforma
* cómo se consume
* cómo escala el sistema

> Antes de escribir código, hay que entender el dato.

---

## 📂 1. Datos estructurados

Son datos con un **esquema bien definido**.

Ejemplos:

* tablas relacionales
* archivos CSV bien formados
* tablas en un Data Warehouse

### Características

* filas y columnas
* tipos de datos claros
* fáciles de consultar con SQL

### Casos de uso

* reportes
* métricas
* análisis histórico

---

## 🧩 2. Datos semi-estructurados

Tienen estructura, pero **no rígida**.

Ejemplos:

* JSON
* XML
* logs
* eventos

### Características

* esquemas flexibles
* campos opcionales
* anidados

### Retos

* validación
* cambios de esquema
* normalización

---

## 📦 3. Datos no estructurados

No siguen un esquema tabular.

Ejemplos:

* texto libre
* imágenes
* audio
* video

### Características

* difíciles de analizar directamente
* requieren procesamiento adicional
* suelen almacenarse como archivos

En Data Engineering, normalmente se:

* almacenan
* indexan
* enriquecen con metadatos

---

## ⏱️ 4. Datos batch vs datos en tiempo real

Otra forma clave de clasificar datos es **cómo llegan**.

### Batch

* llegan en bloques
* se procesan por horarios
* más simples de operar

### Tiempo real (streaming)

* llegan de forma continua
* requieren baja latencia
* más complejos

👉 El tipo de llegada influye directamente en el diseño del pipeline.

---

## 📊 5. Datos transaccionales vs analíticos

### Datos transaccionales

* representan eventos individuales
* cambian constantemente
* normalizados

Ejemplo:

* órdenes
* pagos
* registros de usuarios

---

### Datos analíticos

* optimizados para lectura
* agregados
* históricos

Ejemplo:

* métricas
* KPIs
* tablas de hechos

> No todos los datos deben usarse directamente para análisis.

---

## 🧱 6. Datos crudos vs datos transformados

### Datos crudos (raw)

* tal como llegan de la fuente
* sin modificar
* sirven como respaldo

### Datos transformados

* limpios
* validados
* listos para consumo

Una buena práctica es **nunca perder los datos crudos**.

---

## 🧠 Errores comunes al tratar tipos de datos

* Tratar JSON como si fuera CSV
* Analizar datos transaccionales directamente
* Mezclar datos crudos y transformados
* Ignorar cambios de esquema

Estos errores escalan rápido.

---

## 🤖 ¿Dónde entra la AI?

La AI puede ayudarte a:

* inferir esquemas
* detectar anomalías
* clasificar datos
* generar documentación

Pero:

* no reemplaza el entendimiento del dato
* no define reglas de negocio

---

## ➡️ ¿Qué sigue?

Para continuar:
📄 [`01_que-es-un-pipeline.md`](01_que-es-un-pipeline.md)

---

**Los datos no son solo volumen.
Son contexto, forma y significado.**
