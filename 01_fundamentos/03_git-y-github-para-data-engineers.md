# Git y GitHub para Data Engineers

Git y GitHub no son solo herramientas para desarrolladores de software.
En Ingeniería de Datos son **fundamentales para construir pipelines confiables, auditables y mantenibles**.

Si tus datos cambian, tu código también debería estar versionado.

---

## 🧠 ¿Por qué Git es clave en Data Engineering?

En proyectos de datos:

* la lógica cambia
* las fuentes evolucionan
* los errores cuestan caro
* varias personas tocan el mismo pipeline

Sin control de versiones:

* no sabes qué cambió
* no sabes cuándo
* no sabes por qué

> Git es la memoria del sistema de datos.

---

## 🔁 Qué debería versionarse (y qué no)

### ✅ Versiona siempre

* código (SQL, Python)
* definiciones de pipelines
* validaciones
* documentación
* configuraciones (sin secretos)

### 🚫 NO versionar

* datos sensibles
* credenciales
* archivos enormes sin sentido
* outputs temporales

Usa `.gitignore` desde el inicio.

---

## 🌱 Flujo mínimo recomendado (simple y realista)

No necesitas flujos complejos.

Un flujo sano para Data Engineers:

1. `main`

   * código estable
2. `feature/*`

   * cambios pequeños y enfocados
3. Pull Request

   * descripción clara del cambio
4. Merge

   * cuando el pipeline sigue funcionando

> El objetivo es **control**, no burocracia.

---

## 📝 Commits que expliquen datos

Un buen commit debe responder:

* ¿qué cambió?
* ¿por qué cambió?

### ❌ Malos ejemplos

* `update`
* `fix`
* `changes`

### ✅ Buenos ejemplos

* `add null validation for orders pipeline`
* `change revenue aggregation to daily level`
* `fix date parsing from payments API`

Los commits también son documentación.

---

## 📂 Estructura clara del repositorio

Un repo de datos debería dejar claro:

* dónde vive el código
* dónde está la documentación
* dónde están los ejemplos

Ejemplo:

```text
pipelines/
docs/
examples/
```

El orden reduce errores.

---

## 🔍 Git como herramienta de auditoría

Con Git puedes responder:

* cuándo cambió un pipeline
* quién lo cambió
* qué lógica se modificó
* desde cuándo existe un error

Esto es **crítico** en entornos productivos.

---

## 🤝 GitHub como espacio de colaboración

GitHub no es solo para “subir código”.

Úsalo para:

* Pull Requests con contexto
* Issues para bugs de datos
* discusiones de diseño
* documentación viva

Un buen repo reduce dependencias entre personas.

---

## 🤖 AI + Git/GitHub

La AI puede ayudarte a:

* escribir mejores mensajes de commit
* resumir cambios en un PR
* generar README inicial
* revisar diffs simples

Pero:

* tú decides qué se acepta
* tú validas el impacto en datos

---

## 🚫 Errores comunes

* usar GitHub como backup
* commits gigantes
* no explicar cambios
* subir datos reales por error
* no revisar PRs

Estos errores escalan rápido en datos.

---

## ➡️ ¿Qué sigue?

Ahora que entiendes Git como fundamento, es momento de aplicarlo en:
🚀 `07_proyectos/proyecto_01_pipeline_simple`

Ahí usarás:

* branches
* commits claros
* estructura ordenada

---

**La Ingeniería de Datos sin control de versiones
no escala de forma segura.**
