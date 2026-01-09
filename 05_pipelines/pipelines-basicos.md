# Pipelines básicos de datos

Un **pipeline de datos** es una secuencia de pasos que permite mover y transformar datos desde una fuente hasta un destino de forma **repetible, confiable y automatizada**.

No es solo un script.
Es un **proceso con intención**.

---

## 🧠 ¿Por qué son importantes los pipelines?

Sin pipelines:

* los datos se mueven manualmente
* los errores pasan desapercibidos
* los procesos no escalan
* el negocio pierde confianza

Un buen pipeline:

* se puede ejecutar muchas veces
* falla de forma controlada
* produce resultados consistentes

---

## 🔁 Componentes básicos de un pipeline

Todo pipeline, por simple que sea, tiene:

1. **Fuente**

   * API
   * Base de datos
   * Archivo (CSV, JSON, etc.)
2. **Transformación**

   * Limpieza
   * Normalización
   * Cálculos
3. **Destino**

   * Tabla
   * Archivo procesado
   * Sistema analítico

---

## 🧱 Ejemplo conceptual de pipeline

```text
Fuente → Transformación → Destino
```

Ejemplo real:

```text
CSV de ventas → Limpieza + agregación → Tabla analítica
```

---

## 🛠️ Pipeline básico con Python (conceptual)

Un pipeline simple puede verse así:

1. Leer datos
2. Transformarlos
3. Guardar el resultado

```python
def read_data(path):
    pass

def transform_data(data):
    pass

def write_data(data, output_path):
    pass

def run_pipeline():
    data = read_data("input.csv")
    transformed = transform_data(data)
    write_data(transformed, "output.csv")

if __name__ == "__main__":
    run_pipeline()
```

👉 Lo importante no es el código, sino la **estructura**.

---

## ✅ Buenas prácticas desde el inicio

Incluso en pipelines simples:

* Separar responsabilidades
* Nombrar funciones claramente
* Manejar errores
* Registrar logs
* Evitar lógica “pegada”

> Un pipeline pequeño mal hecho crece mal.

---

## ❌ Errores comunes en pipelines básicos

* Todo en un solo script
* No manejar errores
* Sobrescribir datos sin control
* No documentar qué hace el proceso
* Depender de ejecuciones manuales

---

## 🔄 Pipelines manuales vs automatizados

| Manual              | Automatizado        |
| ------------------- | ------------------- |
| Depende de personas | Depende del sistema |
| Propenso a errores  | Repetible           |
| No escala           | Escala              |
| Difícil de auditar  | Trazable            |

La automatización es el objetivo natural.

---

## 🧭 De pipelines básicos a sistemas de datos

Los pipelines básicos son el **primer paso** hacia:

* orquestadores
* monitoreo
* Data Warehouses
* Data Lakes

Antes de escalar, hay que **entender lo básico**.

---

## 🤖 ¿Dónde entra la AI aquí?

La AI puede ayudarte a:

* generar plantillas
* explicar código
* documentar pipelines
* detectar errores simples

Pero:

* tú defines la lógica
* tú validas el resultado

---

## ➡️ ¿Qué sigue?

Continúa con:
📄 `batch-vs-streaming.md`
o
📄 `05_pipelines/que-es-un-pipeline.md`
o empieza con:
🚀 `07_proyectos/proyecto_01_pipeline_simple`

---

**Un buen pipeline no es complejo.
Es claro, confiable y mantenible.**
