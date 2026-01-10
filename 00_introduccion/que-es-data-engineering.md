# ¿Qué es la Ingeniería de Datos?

La **Ingeniería de Datos (Data Engineering)** es la disciplina encargada de **diseñar, construir y mantener sistemas que mueven, transforman y preparan datos** para que puedan ser usados de forma confiable por analistas, científicos de datos y equipos de negocio.

En pocas palabras:

> Un/a Data Engineer convierte datos crudos en datos útiles.

---

## 🧠 ¿Por qué existe la Ingeniería de Datos?

En la práctica, los datos:

* vienen de muchas fuentes
* tienen distintos formatos
* llegan incompletos o con errores
* crecen en volumen con el tiempo

Sin Ingeniería de Datos:

* los reportes no cuadran
* los dashboards se rompen
* los modelos fallan
* el negocio pierde confianza en los datos

La Ingeniería de Datos existe para **evitar ese caos**.

---

## 🔁 Qué hace realmente un/a Data Engineer

Un/a Data Engineer trabaja en todo el **ciclo de vida del dato**:

1. **Ingesta**

   * APIs
   * Bases de datos
   * Archivos (CSV, JSON, Parquet, etc.)
2. **Transformación**

   * Limpieza
   * Normalización
   * Enriquecimiento
3. **Almacenamiento**

   * Data Warehouses
   * Data Lakes
4. **Exposición**

   * Tablas analíticas
   * Vistas
   * Data products
5. **Mantenimiento**

   * Calidad
   * Performance
   * Costos
   * Escalabilidad

---

## 🧰 Herramientas vs fundamentos

Las herramientas cambian.
Los **fundamentos permanecen**.

Un buen/a Data Engineer entiende:

* cómo funcionan los datos
* por qué una transformación es correcta
* cuándo un pipeline es frágil
* cómo detectar errores antes de que lleguen al negocio

Las herramientas (SQL engines, Airflow, Spark, cloud) son **medios**, no el objetivo.

---

## 🧱 Data Engineering no es solo escribir pipelines

Un error común es pensar que Data Engineering es solo:

* escribir scripts
* mover datos
* automatizar tareas

En realidad, también implica:

* diseño
* decisiones de arquitectura
* **trade-offs** (compromisos entre opciones)
* comunicación con otros equipos
* pensar en el impacto en el negocio

### 🤔 ¿Qué es un trade-off?

Un **trade-off** (compromiso o intercambio) es cuando eliges una opción sabiendo que estás renunciando a algo a cambio de otra cosa. En Data Engineering, esto es muy común:

**Ejemplos de trade-offs:**

* **Velocidad vs Costo**: 
  * Puedes procesar datos más rápido usando más recursos (más caro)
  * O procesar más lento usando menos recursos (más barato)
  * **Trade-off**: ¿Prefieres velocidad o ahorro?

* **Simplicidad vs Flexibilidad**:
  * Un pipeline simple es fácil de mantener pero menos flexible
  * Un pipeline complejo es más flexible pero más difícil de mantener
  * **Trade-off**: ¿Prefieres simplicidad o capacidad de adaptación?

* **Batch vs Streaming**:
  * Batch es más simple y barato, pero los datos llegan con retraso
  * Streaming es más complejo y costoso, pero los datos llegan en tiempo real
  * **Trade-off**: ¿Necesitas datos en tiempo real o puedes esperar?

* **Data Warehouse vs Data Lake**:
  * Data Warehouse: estructura fija, rápido para consultas, más caro
  * Data Lake: estructura flexible, más lento para consultas, más barato
  * **Trade-off**: ¿Prefieres estructura y velocidad o flexibilidad y costo?

* **Calidad vs Velocidad de entrega**:
  * Validaciones exhaustivas = datos más confiables pero tardan más en llegar
  * Validaciones mínimas = datos llegan rápido pero pueden tener errores
  * **Trade-off**: ¿Qué es más importante: calidad o velocidad?

> 💡 **En Data Engineering, no hay soluciones perfectas. Solo hay soluciones que equilibran diferentes necesidades según el contexto del negocio.**

---

## 🆚 Data Engineering vs otros roles

Data Engineering es parte de un ecosistema más amplio. Trabaja junto con:

* **Data Analysts**: Consumen y analizan los datos que tú preparas
* **Data Scientists**: Usan tus datos para construir modelos
* **Analytics Engineers**: Transforman datos en modelos analíticos

> 💡 **Para entender mejor las diferencias y cómo interactúan estos roles, lee:** [Roles en Datos](roles-en-datos.md)

> Sin Data Engineering, los otros roles no escalan.

---

## 🌱 ¿Qué aprenderás en este repositorio?

Aquí aprenderás:

* qué decisiones toma un/a Data Engineer
* cómo escribir SQL y Python de calidad
* cómo diseñar pipelines mantenibles
* cómo pensar en datos como producto
* cómo usar AI como **copiloto**, no como atajo

Este repositorio **no promete magia**, promete **fundamentos sólidos**.

---

## 🤖 Nota sobre AI

La AI puede:

* ayudarte a entender código
* acelerar documentación
* sugerir soluciones

Pero **no reemplaza el criterio técnico**.

Aquí aprenderás a usar AI:

* con intención
* con criterio
* con responsabilidad

---

## ➡️ ¿Qué sigue?

Continúa con:
📄 [Roles en Datos](roles-en-datos.md)


---

**La Ingeniería de Datos no empieza con herramientas.
Empieza con entender el problema.**
