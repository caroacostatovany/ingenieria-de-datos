# Prefect: Orquestador Moderno

Prefect es un orquestador moderno diseñado para Data Engineering, con enfoque en Python y facilidad de uso.

---

## 🧠 ¿Qué es Prefect?

Prefect es un orquestador que:
* **Es Python-first**: Diseñado para Python desde el inicio
* **Es fácil de empezar**: Funciona localmente sin configuración compleja
* **Escala a producción**: Puede usar Prefect Cloud o servidor propio
* **Tiene UI moderna**: Interfaz web intuitiva

> Prefect es como Airflow, pero más fácil de usar y más Python-friendly.

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
pip install prefect

# Con dependencias adicionales
pip install prefect[sql,aws,gcp,azure]
```

---

## 📁 Dónde crear tus archivos

**Crea todos tus ejercicios y flows de Prefect en esta carpeta:**

```
05_pipelines/ejercicios/prefect/
```

### Estructura recomendada

```
05_pipelines/ejercicios/prefect/
├── 01-primer-flow.py          # Tu primer flow simple
├── 02-pipeline-etl.py         # Pipeline ETL completo
├── 03-dependencias.py         # Flows con dependencias
├── 04-programacion.py        # Flows con scheduling
└── README.md                  # (opcional) Notas personales
```

### Cómo crear un archivo

#### Opción A: Usando Cursor (Recomendado)

1. **Abre la carpeta en Cursor:**
   - En Cursor, navega a `05_pipelines/ejercicios/prefect/`
   - O usa `Cmd+P` (Mac) / `Ctrl+P` (Windows/Linux) y escribe: `ejercicios/prefect`

2. **Crea un nuevo archivo:**
   - Click derecho en la carpeta `prefect` → "New File"
   - O usa `Cmd+N` (Mac) / `Ctrl+N` (Windows/Linux)
   - Guarda como `01-primer-flow.py` en la carpeta `prefect`

3. **Escribe tu código** (ver ejemplos abajo)

4. **Ejecuta el archivo:**
   - Abre la terminal integrada en Cursor (`Ctrl+`` ` o `View → Terminal`)
   - Navega a la carpeta si es necesario:
     ```bash
     cd 05_pipelines/ejercicios/prefect
     ```
   - Ejecuta:
     ```bash
     python 01-primer-flow.py
     ```

#### Opción B: Desde terminal/Bash

1. **Navega a la carpeta de ejercicios:**
   ```bash
   cd 05_pipelines/ejercicios/prefect
   ```

2. **Crea un nuevo archivo:**
   ```bash
   touch 01-primer-flow.py
   ```

3. **Abre el archivo en Cursor o tu editor:**
   ```bash
   # Si estás en la raíz del proyecto:
   cursor 05_pipelines/ejercicios/prefect/01-primer-flow.py
   # O simplemente:
   code 05_pipelines/ejercicios/prefect/01-primer-flow.py
   ```

4. **Escribe tu código** y guarda

5. **Ejecuta el archivo:**
   ```bash
   python 01-primer-flow.py
   ```

---

## 📊 Conceptos clave

### Flow (Flujo)

Un flow es tu pipeline. Es una función Python decorada.

```python
from prefect import flow

@flow
def mi_pipeline():
    print("Ejecutando pipeline...")
    # Tu lógica aquí
    return "completado"
```

### Task (Tarea)

Una tarea es una unidad de trabajo dentro del flow.

```python
from prefect import task

@task
def extraer_datos():
    return "datos extraídos"

@task
def transformar_datos(datos):
    return f"{datos} transformados"

@flow
def pipeline_etl():
    datos = extraer_datos()
    resultado = transformar_datos(datos)
    return resultado
```

---

## 🎯 Primer Flow

### Paso 1: Crear el archivo

**En Cursor:**
1. Navega a `05_pipelines/ejercicios/prefect/` en el explorador de archivos
2. Click derecho → "New File"
3. Nombra el archivo: `01-primer-flow.py`

**O desde terminal:**
```bash
cd 05_pipelines/ejercicios/prefect
touch 01-primer-flow.py
```

### Paso 2: Escribir el código

Abre `01-primer-flow.py` en Cursor y copia este código:

```python
from prefect import flow, task
import pandas as pd
from pathlib import Path

# Obtener la ruta base del proyecto (3 niveles arriba desde este archivo)
BASE_DIR = Path(__file__).parent.parent.parent.parent

@task
def extraer(ruta):
    """Extrae datos."""
    return pd.read_csv(ruta)

@task
def transformar(df):
    """Transforma datos."""
    df = df.dropna()
    df['total'] = df['precio'] * df['cantidad']
    return df

@task
def cargar(df, ruta):
    """Carga datos."""
    df.to_parquet(ruta, index=False)

@flow
def pipeline_etl(ruta_entrada, ruta_salida):
    """Pipeline ETL completo."""
    df = extraer(ruta_entrada)
    df = transformar(df)
    cargar(df, ruta_salida)
    print("✅ Pipeline completado")

# Ejecutar
if __name__ == '__main__':
    # Rutas relativas desde la raíz del proyecto usando pathlib
    ruta_entrada = BASE_DIR / '03_python' / 'data' / 'ventas.csv'
    # Outputs se guardan en 05_pipelines/data/output para mejor organización
    ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'ventas_processed.parquet'
    
    # Asegurar que el directorio de salida existe
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    
    pipeline_etl(str(ruta_entrada), str(ruta_salida))
```

> 💡 **Nota**: 
> - Usamos `pathlib.Path` para construir rutas de forma robusta, independientemente del sistema operativo.
> - Los archivos de salida se guardan en `05_pipelines/data/output/` para mantener una organización clara.
> - El código crea automáticamente el directorio si no existe.

### Paso 3: Ejecutar

> ⚠️ **Recuerda**: Activa tu entorno virtual antes de ejecutar:
> ```bash
> pyenv activate ingenieria-de-datos
> # O: pyenv shell ingenieria-de-datos
> ```

**En Cursor:**
1. Abre la terminal integrada (`Ctrl+`` ` o `View → Terminal`)
2. Activa el entorno virtual:
   ```bash
   pyenv activate ingenieria-de-datos
   ```
3. Si no estás en la carpeta correcta, navega:
   ```bash
   cd 05_pipelines/ejercicios/prefect
   ```
4. Ejecuta:
   ```bash
   python 01-primer-flow.py
   ```

**O desde terminal externa:**
```bash
# Activa el entorno virtual primero:
pyenv activate ingenieria-de-datos

# Desde la raíz del proyecto:
python 05_pipelines/ejercicios/prefect/01-primer-flow.py

# O navega primero:
cd 05_pipelines/ejercicios/prefect
python 01-primer-flow.py
```

> 💡 **Nota**: Asegúrate de que el archivo `ventas.csv` exista en `03_python/data/` o ajusta la ruta según tus datos.

> 💬 **¿Tienes errores?** Si encuentras algún error al ejecutar tu script, usa el chat de Cursor (`Cmd+L` en Mac o `Ctrl+L` en Windows/Linux) para pedir ayuda. Puedes:
> - Copiar y pegar el mensaje de error completo
> - Mencionar qué estabas intentando hacer
> - Preguntar sobre el error específico
> 
> El chat de Cursor puede ayudarte a:
> - Entender qué significa el error
> - Corregir problemas de sintaxis
> - Resolver problemas de importaciones
> - Ajustar rutas o configuraciones

> 💬 **¿Tienes errores?** Si encuentras algún error al ejecutar tu script, usa el chat de Cursor (`Cmd+L` o `Ctrl+L`) para pedir ayuda. Puedes:
> - Copiar y pegar el mensaje de error completo
> - Mencionar qué estabas intentando hacer
> - Preguntar sobre el error específico
> 
> El chat de Cursor puede ayudarte a:
> - Entender qué significa el error
> - Corregir problemas de sintaxis
> - Resolver problemas de importaciones
> - Ajustar rutas o configuraciones

---

## 🔄 Dependencias

Las dependencias se manejan automáticamente por el orden de llamadas.

```python
@flow
def pipeline_con_dependencias():
    # Estas tareas se ejecutan en paralelo
    usuarios = extraer_usuarios()
    productos = extraer_productos()
    
    # Esta tarea espera a que ambas terminen
    resultado = combinar(usuarios, productos)
    
    # Esta tarea espera a combinar
    cargar(resultado)
```

---

## 📅 Programación (Scheduling)

> ⚠️ **Nota**: En Prefect 3.x, el scheduling se configura al crear un **deployment**, no en el decorador `@flow`.

### Crear flows (sin schedule en el decorador)

```python
from prefect import flow

@flow
def pipeline_diario():
    # Tu pipeline
    pass

@flow
def pipeline_horario():
    # Tu pipeline
    pass
```

### Configurar scheduling con deployments

Una vez que tienes tus flows, configura el scheduling al crear deployments:

```bash
# Con cron (diario a medianoche)
prefect deploy --cron "0 0 * * *" pipeline_diario

# Con intervalo (cada hora)
prefect deploy --interval 3600 pipeline_horario

# Con intervalo en formato legible
prefect deploy --interval "1 hour" pipeline_horario
```

> 💡 **Tip**: Primero inicia el servidor Prefect (`prefect server start`) antes de crear deployments.

---

## 🖥️ UI local

Prefect incluye una UI local para monitorear flows.

> ⚠️ **Recuerda**: Activa tu entorno virtual antes de ejecutar:
> ```bash
> pyenv activate ingenieria-de-datos
> ```

### Paso 1: Iniciar el servidor

En una terminal, desde cualquier carpeta del proyecto:

```bash
# Asegúrate de tener el entorno virtual activado
prefect server start
```

Verás algo como:
```
Starting Prefect server...
The Prefect UI is available at http://localhost:4200
```

### Paso 2: Abrir la UI

Abre tu navegador y ve a: **http://localhost:4200**

### Paso 3: Ejecutar tu flow

En otra terminal, ejecuta tu flow:

```bash
cd 05_pipelines/ejercicios/prefect
python 01-primer-flow.py
```

### Paso 4: Ver en la UI

Regresa a la UI en el navegador. Verás:
- Tu flow ejecutándose
- Estado de cada tarea
- Logs en tiempo real
- Historial de ejecuciones

> 💡 **Tip**: Deja el servidor corriendo mientras trabajas. Puedes detenerlo con `Ctrl+C`.

---

## 🔄 Retry y manejo de errores

```python
@task(retries=3, retry_delay_seconds=60)
def tarea_con_reintentos():
    # Esta tarea reintentará 3 veces si falla
    pass

@task
def tarea_que_puede_fallar():
    import random
    if random.random() < 0.5:
        raise Exception("Error aleatorio")
    return "éxito"
```

---

## 💾 Estado y resultados

Prefect guarda automáticamente el estado de cada ejecución.

```python
@flow
def pipeline_con_estado():
    resultado = procesar_datos()
    
    # Prefect guarda automáticamente:
    # - Estado de cada tarea
    # - Resultados
    # - Logs
    # - Tiempos de ejecución
    
    return resultado
```

---

## 🔗 Integración con servicios

### Base de datos

```python
from prefect_sqlalchemy import SqlAlchemyConnector

@task
def consultar_db():
    with SqlAlchemyConnector.load("postgres") as connector:
        df = pd.read_sql("SELECT * FROM ventas", connector.get_connection())
    return df
```

### Cloud Storage

```python
from prefect_aws import S3Bucket

@task
def leer_de_s3():
    s3_bucket = S3Bucket.load("my-bucket")
    return s3_bucket.read_path("data/raw/ventas.csv")
```

---

## 💡 Ventajas de Prefect

### 1. Python puro

```python
# No necesitas aprender DSL especial
# Es Python estándar
@flow
def mi_pipeline():
    # Código Python normal
    pass
```

### 2. Fácil de testear

```python
# Puedes testear flows como funciones normales
def test_pipeline():
    resultado = pipeline_etl('test_input.csv', 'test_output.parquet')
    assert resultado is not None
```

### 3. UI moderna

* Visualización de flows
* Monitoreo en tiempo real
* Logs integrados
* Historial de ejecuciones

---

## 🎯 Ejercicios prácticos

Crea estos archivos en `05_pipelines/ejercicios/prefect/`:

### Ejercicio 1: Primer Flow
**Archivo:** `01-primer-flow.py`
- Crea un flow simple que imprima "Hola Prefect"
- Ejecútalo y verifica que funciona

### Ejercicio 2: Pipeline ETL
**Archivo:** `02-pipeline-etl.py`
- Usa el ejemplo de pipeline ETL de arriba
- Ajusta las rutas a tus datos reales
- Ejecuta y verifica los resultados

### Ejercicio 3: Dependencias
**Archivo:** `03-dependencias.py`
- Crea un flow con múltiples tareas
- Algunas tareas deben ejecutarse en paralelo
- Otras deben esperar a que terminen las anteriores

### Ejercicio 4: Programación
**Archivo:** `04-programacion.py`
- Crea un flow con scheduling (cron o intervalo)
- Ejecuta el servidor Prefect y observa cómo se programa

### Ejercicio 5: UI
- Inicia el servidor Prefect (`prefect server start`)
- Ejecuta tus flows anteriores
- Explora la UI en http://localhost:4200
- Revisa logs, estados y tiempos de ejecución

---

## 🚀 Próximos pasos

* **Prefect Cloud**: Para producción sin gestionar servidor
* **Prefect Server**: Para auto-hospedaje
* **Blocks**: Para configuración reutilizable
* **Deployments**: Para desplegar flows a producción

---

## 💬 ¿Necesitas ayuda?

Si encuentras errores al ejecutar tus scripts de Prefect:

1. **Usa el chat de Cursor** (`Cmd+L` en Mac o `Ctrl+L` en Windows/Linux):
   - Copia y pega el mensaje de error completo
   - Explica qué estabas intentando hacer
   - Pregunta específicamente sobre el error

2. **El chat puede ayudarte con:**
   - Entender mensajes de error
   - Corregir problemas de sintaxis
   - Resolver importaciones faltantes
   - Ajustar rutas o configuraciones
   - Debugging de flows y tareas

3. **Ejemplo de pregunta útil:**
   ```
   Tengo este error al ejecutar 01-primer-flow.py:
   [pega el error completo aquí]
   
   ¿Qué significa y cómo lo soluciono?
   ```

---

> **Recuerda**: Prefect es excelente para empezar. Es simple localmente pero puede escalar a producción cuando lo necesites. Si tienes dudas, usa el chat de Cursor para obtener ayuda rápida.
