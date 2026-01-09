# Luigi: Orquestador Simple de Spotify

Luigi es un orquestador simple desarrollado por Spotify, ideal para pipelines Python.

---

## 🧠 ¿Qué es Luigi?

Luigi es:
* **Simple**: Diseñado para ser fácil de usar
* **Python puro**: Todo en Python, sin DSL
* **Desarrollado por Spotify**: Probado a gran escala
* **Ligero**: Menos overhead que Airflow

> Luigi es como Airflow pero más simple y Python-focused.

---

## 🚀 Instalación

```bash
pip install luigi
```

---

## 📊 Conceptos clave

### Task (Tarea)

Una tarea es una clase que hereda de `luigi.Task`.

```python
import luigi

class MiTarea(luigi.Task):
    def output(self):
        return luigi.LocalTarget('output.txt')
    
    def run(self):
        with self.output().open('w') as f:
            f.write('Hola mundo')
```

### Dependencias

Las dependencias se definen con `requires()`.

```python
class TareaA(luigi.Task):
    def output(self):
        return luigi.LocalTarget('a.txt')
    
    def run(self):
        with self.output().open('w') as f:
            f.write('A')

class TareaB(luigi.Task):
    def requires(self):
        return TareaA()
    
    def output(self):
        return luigi.LocalTarget('b.txt')
    
    def run(self):
        with self.output().open('w') as f:
            f.write('B')
```

---

## 🎯 Ejemplo completo

```python
import luigi
import pandas as pd

class ExtraerDatos(luigi.Task):
    def output(self):
        return luigi.LocalTarget('data/raw/ventas.csv')
    
    def run(self):
        # Simular extracción
        df = pd.DataFrame({
            'id': [1, 2, 3],
            'precio': [10, 20, 30],
            'cantidad': [2, 1, 3]
        })
        df.to_csv(self.output().path, index=False)

class TransformarDatos(luigi.Task):
    def requires(self):
        return ExtraerDatos()
    
    def output(self):
        return luigi.LocalTarget('data/processed/ventas.parquet')
    
    def run(self):
        df = pd.read_csv(self.input().path)
        df['total'] = df['precio'] * df['cantidad']
        df.to_parquet(self.output().path, index=False)

class CargarDatos(luigi.Task):
    def requires(self):
        return TransformarDatos()
    
    def output(self):
        return luigi.LocalTarget('data/final/completado.txt')
    
    def run(self):
        # Simular carga
        with self.output().open('w') as f:
            f.write('Carga completada')

if __name__ == '__main__':
    luigi.run(['CargarDatos', '--local-scheduler'])
```

---

## 🔄 Ejecución

```bash
# Ejecutar tarea
python pipeline.py CargarDatos --local-scheduler

# Con parámetros
python pipeline.py CargarDatos --date 2024-01-01 --local-scheduler
```

---

## 💡 Ventajas de Luigi

### 1. Simplicidad

* Todo en Python
* Sin conceptos complejos
* Fácil de entender

### 2. Ligero

* Menos overhead que Airflow
* No requiere base de datos
* Puede ejecutarse localmente

### 3. Probado

* Desarrollado por Spotify
* Usado en producción a gran escala

---

## ⚠️ Desventajas

### 1. UI limitada

* UI básica comparada con Airflow
* Menos visualización

### 2. Menos features

* Menos providers que Airflow
* Menos integraciones

---

## 🎯 Cuándo usar Luigi

✅ **Usa Luigi cuando:**
* Quieres simplicidad
* Pipeline principalmente Python
* No necesitas UI avanzada
* Prefieres código sobre configuración

❌ **No uses Luigi cuando:**
* Necesitas UI rica
* Necesitas muchas integraciones
* Prefieres estándar de industria (Airflow)

---

## 🎯 Ejercicios

1. Instala Luigi y crea tu primera tarea
2. Define dependencias entre tareas
3. Ejecuta un pipeline completo
4. Explora la UI básica de Luigi

---

> **Recuerda**: Luigi es simple y efectivo. Perfecto si prefieres código Python puro sobre configuración.
