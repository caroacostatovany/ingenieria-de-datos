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

> ⚠️ **Importante**: Antes de instalar o ejecutar cualquier comando, asegúrate de activar tu entorno virtual de pyenv:
> ```bash
> pyenv activate ingenieria-de-datos
> ```
> O si usas `pyenv-virtualenv`:
> ```bash
> pyenv shell ingenieria-de-datos
> ```

```bash
# Instalación básica
pip install luigi
```

---

## 📁 Dónde crear tus archivos

**Crea todos tus ejercicios y tasks de Luigi en esta carpeta:**

```
05_pipelines/ejercicios/luigi/
```

### Estructura recomendada

```
05_pipelines/ejercicios/luigi/
├── 01-primera-tarea.py       # Tu primera tarea simple
├── 02-pipeline-etl.py        # Pipeline ETL completo
├── 03-dependencias.py        # Tasks con dependencias complejas
└── README.md                  # (opcional) Notas personales
```

> 💡 **Importante**: Los archivos de salida (outputs) se guardan en `05_pipelines/data/output/` para mejor organización.

### Cómo crear un archivo

#### Opción A: Usando Cursor (Recomendado)

1. **Abre la carpeta en Cursor:**
   - En Cursor, navega a `05_pipelines/ejercicios/luigi/`
   - O usa `Cmd+P` (Mac) / `Ctrl+P` (Windows/Linux) y escribe: `ejercicios/luigi`

2. **Crea un nuevo archivo:**
   - Click derecho en la carpeta `luigi` → "New File"
   - O usa `Cmd+N` (Mac) / `Ctrl+N` (Windows/Linux)
   - Guarda como `01-primera-tarea.py` en la carpeta `luigi`

3. **Escribe tu código** (ver ejemplos abajo)

4. **Ejecuta el archivo:**
   - Abre la terminal integrada en Cursor (`Ctrl+`` ` o `View → Terminal`)
   - Navega a la carpeta si es necesario:
     ```bash
     cd 05_pipelines/ejercicios/luigi
     ```
   - Ejecuta:
     ```bash
     python 01-primera-tarea.py CargarDatos --local-scheduler
     ```

#### Opción B: Desde terminal/Bash

1. **Navega a la carpeta de ejercicios:**
   ```bash
   cd 05_pipelines/ejercicios/luigi
   ```

2. **Crea un nuevo archivo:**
   ```bash
   touch 01-primera-tarea.py
   ```

3. **Abre el archivo en Cursor o tu editor:**
   ```bash
   # Si estás en la raíz del proyecto:
   cursor 05_pipelines/ejercicios/luigi/01-primera-tarea.py
   ```

4. **Escribe tu código** y guarda

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

## 🔄 Filosofía de Ejecución: Backward Dependency Resolution

### ⚠️ Diferencia clave con Airflow/Dagster

Luigi funciona de forma **"al revés"** comparado con Airflow o Dagster. Esta es una diferencia filosófica importante:

#### Luigi: Resolución hacia atrás (Backward)

**En Luigi, ejecutas el task FINAL y Luigi resuelve las dependencias hacia atrás:**

```python
# Ejecutas el task final
python pipeline.py CargarDatos

# Luigi internamente hace:
# 1. "¿Qué necesita CargarDatos?" → TransformarDatos
# 2. "¿Qué necesita TransformarDatos?" → ExtraerDatos
# 3. "¿Qué necesita ExtraerDatos?" → Nada (es el inicio)
# 4. Ejecuta: ExtraerDatos → TransformarDatos → CargarDatos
```

**Flujo de ejecución:**
```
Tú ejecutas: CargarDatos
    ↓
Luigi resuelve: "Necesito TransformarDatos"
    ↓
Luigi resuelve: "TransformarDatos necesita ExtraerDatos"
    ↓
Luigi ejecuta: ExtraerDatos → TransformarDatos → CargarDatos
```

#### Airflow/Dagster: Resolución hacia adelante (Forward)

**En Airflow/Dagster, defines el DAG completo y el scheduler ejecuta desde el principio:**

```python
# Defines el DAG completo
dag = DAG('mi_pipeline')
tarea_extraer = PythonOperator(...)
tarea_transformar = PythonOperator(...)
tarea_cargar = PythonOperator(...)

# Defines dependencias
tarea_extraer >> tarea_transformar >> tarea_cargar

# El scheduler ejecuta desde el principio:
# 1. Busca tasks sin dependencias → tarea_extraer
# 2. Ejecuta tarea_extraer
# 3. Cuando termina, ejecuta tarea_transformar
# 4. Cuando termina, ejecuta tarea_cargar
```

**Flujo de ejecución:**
```
Scheduler busca: "¿Qué tasks no tienen dependencias?"
    ↓
Encuentra: tarea_extraer
    ↓
Ejecuta: tarea_extraer
    ↓
Cuando termina, ejecuta: tarea_transformar
    ↓
Cuando termina, ejecuta: tarea_cargar
```

### ¿Por qué Luigi funciona así?

**Ventajas de la resolución hacia atrás:**

1. **Output-driven**: Luigi se enfoca en qué OUTPUT quieres, no en qué INPUT tienes
   - "Quiero `ventas_finales.parquet`" → Luigi resuelve cómo obtenerlo

2. **Idempotencia**: Luigi verifica si el output ya existe antes de ejecutar
   - Si `ventas_finales.parquet` ya existe, no ejecuta nada
   - Esto evita trabajo innecesario

3. **Simplicidad**: Solo necesitas especificar el objetivo final
   - No necesitas definir todo el DAG explícitamente
   - Luigi lo resuelve automáticamente

4. **Incremental**: Puedes ejecutar solo partes del pipeline
   - Si `TransformarDatos` ya tiene output, no lo re-ejecuta
   - Solo ejecuta lo que falta

**Ejemplo práctico:**

```python
# En Luigi:
python pipeline.py CargarDatos
# Luigi verifica:
# - ¿Existe pipeline_completado.txt? → No, necesito ejecutar
# - ¿Existe ventas_transformadas.parquet? → Sí, no necesito TransformarDatos
# - ¿Existe ventas_raw.csv? → Sí, no necesito ExtraerDatos
# Resultado: Solo ejecuta CargarDatos (eficiente!)

# En Airflow:
# El scheduler ejecuta todo el DAG desde el principio
# (a menos que configures skip o condiciones especiales)
```

### Comparación visual

| Aspecto | Luigi (Backward) | Airflow/Dagster (Forward) |
|---------|------------------|---------------------------|
| **Ejecutas** | Task final | Todo el DAG |
| **Resolución** | Hacia atrás (¿qué necesito?) | Hacia adelante (¿qué puedo ejecutar?) |
| **Enfoque** | Output-driven | Input-driven |
| **Idempotencia** | Automática (verifica outputs) | Manual (necesitas configurar) |
| **Flexibilidad** | Puedes ejecutar cualquier task | Ejecutas el DAG completo |

### ¿Cuándo usar cada enfoque?

**Luigi (Backward) es mejor cuando:**
- Quieres ejecutar solo lo necesario
- Los outputs son claros y verificables
- Prefieres simplicidad sobre control explícito
- Trabajas con pipelines incrementales

**Airflow/Dagster (Forward) es mejor cuando:**
- Necesitas control explícito del flujo
- Quieres programación compleja (cron, triggers)
- Necesitas monitoreo avanzado
- Trabajas con equipos grandes (más estructura)

> 💡 **Resumen**: Luigi piensa en "¿Qué quiero al final?" y resuelve hacia atrás. Airflow/Dagster piensan en "¿Qué puedo ejecutar ahora?" y avanzan hacia adelante. Ambos enfoques son válidos, solo son diferentes filosofías de diseño.

---

## 🎯 Primer Task

### Paso 1: Crear el archivo

**En Cursor:**
1. Navega a `05_pipelines/ejercicios/luigi/` en el explorador de archivos
2. Click derecho → "New File"
3. Nombra el archivo: `01-primera-tarea.py`

**O desde terminal:**
```bash
cd 05_pipelines/ejercicios/luigi
touch 01-primera-tarea.py
```

### Paso 2: Escribir el código

Abre `01-primera-tarea.py` en Cursor y copia este código:

```python
"""
Primer Task de Luigi: Pipeline ETL simple
"""
import luigi
import pandas as pd
from pathlib import Path

# Obtener la ruta base del proyecto (3 niveles arriba desde este archivo)
BASE_DIR = Path(__file__).parent.parent.parent.parent

class ExtraerDatos(luigi.Task):
    """Task para extraer datos del CSV de ventas."""
    
    def output(self):
        # Output se guarda en 05_pipelines/data/output para mejor organización
        ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'ventas_raw.csv'
        ruta_salida.parent.mkdir(parents=True, exist_ok=True)
        return luigi.LocalTarget(str(ruta_salida))
    
    def run(self):
        print("📥 Extrayendo datos...")
        # Leer el CSV de ejemplo del proyecto
        ruta_entrada = BASE_DIR / '03_python' / 'data' / 'ventas.csv'
        df = pd.read_csv(ruta_entrada)
        print(f"✅ Extraídas {len(df)} filas")
        
        # Guardar en output
        df.to_csv(self.output().path, index=False)
        print(f"✅ Guardado en {self.output().path}")

class TransformarDatos(luigi.Task):
    """Task para transformar datos (depende de ExtraerDatos)."""
    
    def requires(self):
        return ExtraerDatos()
    
    def output(self):
        ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'ventas_transformadas.parquet'
        ruta_salida.parent.mkdir(parents=True, exist_ok=True)
        return luigi.LocalTarget(str(ruta_salida))
    
    def run(self):
        print("🔄 Transformando datos...")
        df = pd.read_csv(self.input().path)
        df = df.dropna()
        df['total'] = df['precio'] * df['cantidad']
        print(f"✅ Transformadas {len(df)} filas")
        
        # Guardar en output
        df.to_parquet(self.output().path, index=False)
        print(f"✅ Guardado en {self.output().path}")

class CargarDatos(luigi.Task):
    """Task para cargar datos (depende de TransformarDatos)."""
    
    def requires(self):
        return TransformarDatos()
    
    def output(self):
        ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'pipeline_completado.txt'
        ruta_salida.parent.mkdir(parents=True, exist_ok=True)
        return luigi.LocalTarget(str(ruta_salida))
    
    def run(self):
        print("💾 Cargando datos...")
        # Leer datos transformados
        df = pd.read_parquet(self.input().path)
        print(f"✅ Datos listos para cargar: {len(df)} filas")
        
        # Marcar como completado
        with self.output().open('w') as f:
            f.write(f'Pipeline completado: {len(df)} filas procesadas')
        print(f"✅ Pipeline completado: {self.output().path}")

if __name__ == '__main__':
    # Ejecutar la tarea final (Luigi ejecutará las dependencias automáticamente)
    luigi.run(['CargarDatos', '--local-scheduler'])
```

> 💡 **Nota**: 
> - Usamos `pathlib.Path` para construir rutas de forma robusta
> - Los archivos de salida se guardan en `05_pipelines/data/output/`
> - Luigi ejecuta automáticamente las dependencias (ExtraerDatos → TransformarDatos → CargarDatos)

### Paso 3: Ejecutar el Task

> ⚠️ **Recuerda**: Activa tu entorno virtual antes de ejecutar:
> ```bash
> pyenv activate ingenieria-de-datos
> ```

**Desde la carpeta de ejercicios:**
```bash
cd 05_pipelines/ejercicios/luigi
python 01-primera-tarea.py CargarDatos --local-scheduler
```

**O desde la raíz del proyecto:**
```bash
python 05_pipelines/ejercicios/luigi/01-primera-tarea.py CargarDatos --local-scheduler
```

Luigi ejecutará automáticamente todas las dependencias en el orden correcto.

> 💬 **¿Necesitas ayuda?** Si encuentras algún error al ejecutar tu task, usa el chat de Cursor (`Cmd+L` en Mac o `Ctrl+L` en Windows/Linux) para pedir ayuda. Puedes:
> - Copiar y pegar el mensaje de error completo
> - Mencionar qué estabas intentando hacer
> - Preguntar sobre el error específico

---

## 🔄 Ejecución

### Modo Local (Recomendado para empezar)

```bash
# Ejecutar una tarea específica
python 01-primera-tarea.py CargarDatos --local-scheduler

# Ver ayuda
python 01-primera-tarea.py --help

# Ver todas las tareas disponibles
python 01-primera-tarea.py --module 01-primera-tarea
```

### Con parámetros

```python
class MiTask(luigi.Task):
    fecha = luigi.Parameter(default='2024-01-01')
    
    def output(self):
        return luigi.LocalTarget(f'output_{self.fecha}.txt')
```

```bash
python pipeline.py MiTask --fecha 2024-01-15 --local-scheduler
```

### 🖥️ UI de Luigi: Ver tus DAGs visualmente

Luigi tiene una UI básica (`luigid`) que te permite ver tus DAGs (grafos de dependencias) de forma visual.

> ⚠️ **Recuerda**: Activa tu entorno virtual antes de ejecutar:
> ```bash
> pyenv activate ingenieria-de-datos
> ```

#### Paso 1: Iniciar el servidor de Luigi

En una terminal, inicia el servidor central de Luigi:

```bash
luigid
```

Verás algo como:
```
INFO: Starting server without password protection
INFO: Starting server at http://localhost:8082
```

> 💡 **Nota**: Deja esta terminal abierta mientras usas la UI. El servidor debe seguir corriendo.

#### Configurar Luigi con base de datos (Opcional - Mejora la visualización)

Luigi puede usar una base de datos para almacenar el estado de los tasks, lo que puede mejorar la visualización del DAG. Para configurarlo:

**Opción 1: Usar archivo de estado persistente**

```bash
# Iniciar luigid con un archivo de estado
luigid --state-path ./luigi-state.pickle
```

**Opción 2: Configurar con luigi.cfg**

Crea un archivo `luigi.cfg` en la raíz del proyecto o en `~/.luigi/`:

```ini
[scheduler]
record_task_history=True
state_path=/path/to/luigi-state.pickle

# Opcional: Usar base de datos (requiere luigi[mysql] o luigi[postgres])
# [database]
# connection=mysql://user:password@localhost/luigi
```

Luego instala el driver de base de datos (opcional):
```bash
# Para MySQL
pip install luigi[mysql]

# Para PostgreSQL  
pip install luigi[postgres]
```

> 💡 **Nota**: La configuración con base de datos puede mejorar la persistencia y visualización del historial de tasks, pero para empezar, el modo básico es suficiente.

#### Paso 2: Abrir la UI en el navegador

Abre tu navegador y ve a:
```
http://localhost:8082
```

#### Paso 3: Ver tus DAGs

1. **En la página principal** verás una lista de todos los tasks disponibles (Task Lists)
2. **Haz click en el nombre del task** (por ejemplo, `CargarDatos`) para ver su página de detalles
3. **⚠️ IMPORTANTE: Haz click en "Show upstream dependencies"** para ver el DAG completo
   - Inicialmente solo verás el task seleccionado (`CargarDatos`)
   - Al hacer click en "Show upstream dependencies" verás todo el DAG con:
     - `ExtraerDatos` → `TransformarDatos` → `CargarDatos`
     - Los tasks como nodos (círculos)
     - Las dependencias como flechas entre los nodos
     - El estado de cada task (PENDING, RUNNING, DONE, FAILED) con colores

> 💡 **Tip**: Si el task ya está completo (DONE), elimina los outputs para forzar re-ejecución y ver el DAG en tiempo real:
> ```bash
> rm 05_pipelines/data/output/ventas_raw.csv
> rm 05_pipelines/data/output/ventas_transformadas.parquet
> rm 05_pipelines/data/output/pipeline_completado.txt
> python 01-primera-tarea.py CargarDatos
> ```

#### Alternativa: Ver dependencias en la consola

Si el DAG visual no se muestra correctamente en la UI, puedes ver las dependencias desde la terminal:

```bash
# Ver el árbol de dependencias de un task
python 01-primera-tarea.py CargarDatos --tree

# O usar el comando luigi directamente
luigi --module 01-primera-tarea CargarDatos --tree
```

Esto mostrará algo como:
```
└─-- CargarDatos
    └─-- TransformarDatos
        └─-- ExtraerDatos
```

> ⚠️ **Nota importante sobre la UI de Luigi**: 
> - La visualización del DAG en la UI web de Luigi es **muy básica y limitada**
> - Puede que solo veas un punto verde (DONE) sin las conexiones visuales
> - Esto es una **limitación conocida** de Luigi comparado con Airflow o Dagster
> - El comando `--tree` es una alternativa confiable para ver las dependencias en texto
> - **Recomendación**: Si necesitas visualización rica de DAGs, considera usar Airflow o Dagster

#### Ver dependencias en código (Alternativa más confiable)

La forma más confiable de entender las dependencias es ver el código directamente:

```python
# En 01-primera-tarea.py puedes ver:
class CargarDatos(luigi.Task):
    def requires(self):
        return TransformarDatos()  # ← Dependencia

class TransformarDatos(luigi.Task):
    def requires(self):
        return ExtraerDatos()  # ← Dependencia
```

**Estructura del DAG:**
```
CargarDatos
  └── TransformarDatos
      └── ExtraerDatos
```

> 💡 **Tip**: Luigi es excelente para simplicidad, pero si necesitas visualización rica de DAGs, considera [Airflow](airflow.md) o [Dagster](dagster.md) que tienen UIs mucho más avanzadas.

#### Paso 4: Ejecutar un task desde la UI

1. **Navega al task** que quieres ejecutar
2. **Haz click en "Run"** o ejecuta desde terminal:
   ```bash
   python 01-primera-tarea.py CargarDatos
   ```
   (Sin `--local-scheduler`, ahora usará el servidor central)
3. **Observa en tiempo real** cómo se ejecutan los tasks en el DAG

#### Ver el DAG de un ejemplo específico

**Ejemplo 1: Primera tarea**
```bash
# Terminal 1: Inicia el servidor
luigid

# Terminal 2: Ejecuta el task (sin --local-scheduler)
cd 05_pipelines/ejercicios/luigi
python 01-primera-tarea.py CargarDatos
```

Luego en http://localhost:8082 verás:
- `ExtraerDatos` → `TransformarDatos` → `CargarDatos`

**Ejemplo 2: Pipeline ETL**
```bash
python 02-pipeline-etl.py CargarDatos
```

Verás:
- `ExtraerVentas` y `ExtraerProductos` (en paralelo)
- `TransformarDatos` (depende de ambos)
- `CargarDatos` (depende de TransformarDatos)

**Ejemplo 3: Dependencias complejas**
```bash
python 03-dependencias.py CombinarDatos
```

Verás un DAG más complejo con:
- Tareas en paralelo
- Múltiples niveles de dependencias

> 💡 **Tip**: La UI es especialmente útil para entender dependencias complejas y monitorear ejecuciones en tiempo real.

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

## 🎯 Ejercicios prácticos

Crea estos archivos en `05_pipelines/ejercicios/luigi/`:

### Ejercicio 1: Primera tarea
**Archivo:** `01-primera-tarea.py`
- Crea un task simple que lea el CSV de ventas
- Transforma los datos (calcula total)
- Guarda el resultado en `05_pipelines/data/output/`
- Ejecuta con `--local-scheduler`

### Ejercicio 2: Pipeline ETL
**Archivo:** `02-pipeline-etl.py`
- Crea 3 tasks: ExtraerDatos, TransformarDatos, CargarDatos
- Define dependencias entre ellos
- Usa el CSV de ventas del proyecto
- Guarda outputs en `05_pipelines/data/output/`

### Ejercicio 3: Dependencias complejas
**Archivo:** `03-dependencias.py`
- Crea tasks que se ejecuten en paralelo
- Crea tasks que dependan de múltiples tasks anteriores
- Observa cómo Luigi maneja las dependencias

### Ejercicio 4: Ver DAGs en la UI
**Pasos:**
1. Inicia el servidor de Luigi:
   ```bash
   luigid
   ```
2. Abre http://localhost:8082 en tu navegador
3. Ejecuta un task (sin `--local-scheduler`):
   ```bash
   python 01-primera-tarea.py CargarDatos
   ```
4. Observa el DAG en la UI:
   - Verás `ExtraerDatos` → `TransformarDatos` → `CargarDatos`
   - Los tasks aparecen como nodos
   - Las dependencias como flechas
   - El estado de cada task se actualiza en tiempo real

> 💡 **Tip**: La UI es especialmente útil para entender dependencias complejas. Prueba con `03-dependencias.py` para ver un DAG más complejo con tareas en paralelo.

> ⚠️ **Recuerda**: Siempre activa tu entorno virtual antes de ejecutar:
> ```bash
> pyenv activate ingenieria-de-datos
> ```

---

> **Recuerda**: Luigi es simple y efectivo. Perfecto si prefieres código Python puro sobre configuración.
