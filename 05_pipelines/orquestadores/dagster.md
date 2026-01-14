# Dagster: Orquestador enfocado en Data Assets

Dagster es un orquestador que enfatiza los "data assets" (activos de datos) en lugar de solo tareas.

---

## 🧠 ¿Qué es Dagster?

Dagster es un orquestador que:
* **Enfoca en data assets**: Piensa en datos, no solo en tareas
* **Tiene UI excelente**: Interfaz moderna y clara
* **Es Python-first**: Diseñado para Python
* **Facilita desarrollo local**: Fácil de empezar

> Dagster te ayuda a pensar en qué datos produces, no solo en qué código ejecutas.

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
pip install dagster dagit

# Con dependencias adicionales
pip install dagster[postgres,pandas]
```

### Configurar DAGSTER_HOME (Opcional pero recomendado)

Dagster almacena metadatos, logs y configuración en un directorio. Por defecto, crea directorios temporales (`.tmp_dagster_home_*`). Para tener control sobre dónde se almacenan estos archivos:

1. **Agrega `DAGSTER_HOME` a tu `.env`** (ya está en `.env.example`):
   ```bash
   DAGSTER_HOME=./05_pipelines/data/.dagster
   ```

2. **O exporta la variable antes de ejecutar:**
   ```bash
   export DAGSTER_HOME=./05_pipelines/data/.dagster
   dagster dev -f 01-primer-asset.py
   ```

> 💡 **Nota**: Si no configuras `DAGSTER_HOME`, Dagster funcionará igual, pero creará directorios temporales. Configurarlo ayuda a mantener el proyecto organizado.

---

## 📁 Dónde crear tus archivos

**Crea todos tus ejercicios y assets de Dagster en esta carpeta:**

```
05_pipelines/ejercicios/dagster/
```

### Estructura recomendada

```
05_pipelines/ejercicios/dagster/
├── 01-primer-asset.py          # Tu primer asset simple
├── 02-assets-con-dependencias.py  # Assets con dependencias
├── 03-definitions.py           # Definiciones de jobs y schedules
└── README.md                   # (opcional) Notas personales
```

### Cómo crear un archivo

#### Opción A: Usando Cursor (Recomendado)

1. **Abre la carpeta en Cursor:**
   - En Cursor, navega a `05_pipelines/ejercicios/dagster/`
   - O usa `Cmd+P` (Mac) / `Ctrl+P` (Windows/Linux) y escribe: `ejercicios/dagster`

2. **Crea un nuevo archivo:**
   - Click derecho en la carpeta `dagster` → "New File"
   - O usa `Cmd+N` (Mac) / `Ctrl+N` (Windows/Linux)
   - Guarda como `01-primer-asset.py` en la carpeta `dagster`

3. **Escribe tu código** (ver ejemplos abajo)

4. **Ejecuta el archivo:**
   - Abre la terminal integrada en Cursor (`Ctrl+`` ` o `View → Terminal`)
   - Navega a la carpeta si es necesario:
     ```bash
     cd 05_pipelines/ejercicios/dagster
     ```
   - Ejecuta:
     ```bash
     dagster dev
     ```

#### Opción B: Desde terminal/Bash

1. **Navega a la carpeta de ejercicios:**
   ```bash
   cd 05_pipelines/ejercicios/dagster
   ```

2. **Crea un nuevo archivo:**
   ```bash
   touch 01-primer-asset.py
   ```

3. **Abre el archivo en Cursor o tu editor:**
   ```bash
   # Si estás en la raíz del proyecto:
   cursor 05_pipelines/ejercicios/dagster/01-primer-asset.py
   # O simplemente:
   code 05_pipelines/ejercicios/dagster/01-primer-asset.py
   ```

4. **Escribe tu código** y guarda

5. **Ejecuta:**
   ```bash
   dagster dev
   ```

---

## 📊 Conceptos clave

### Asset (Activo de datos)

Un asset es un dato que produces o consumes.

```python
from dagster import asset

@asset
def ventas_diarias():
    """Asset: ventas agregadas por día."""
    # Tu lógica aquí
    return df
```

### Op (Operación)

Una operación es una unidad de trabajo.

```python
from dagster import op

@op
def extraer_ventas():
    return "datos extraídos"
```

---

## 🎯 Primer Asset

### Paso 1: Crear el archivo

**En Cursor:**
1. Navega a `05_pipelines/ejercicios/dagster/` en el explorador de archivos
2. Click derecho → "New File"
3. Nombra el archivo: `01-primer-asset.py`

**O desde terminal:**
```bash
cd 05_pipelines/ejercicios/dagster
touch 01-primer-asset.py
```

### Paso 2: Escribir el código

Abre `01-primer-asset.py` en Cursor y copia este código:

```python
from dagster import asset, AssetExecutionContext, Definitions
import pandas as pd
from pathlib import Path

# Obtener la ruta base del proyecto (3 niveles arriba desde este archivo)
BASE_DIR = Path(__file__).parent.parent.parent.parent

@asset
def ventas_raw(context: AssetExecutionContext):
    """Asset: datos de ventas sin procesar."""
    context.log.info("Extrayendo ventas...")
    ruta = BASE_DIR / '03_python' / 'data' / 'ventas.csv'
    df = pd.read_csv(ruta)
    context.log.info(f"Extraídas {len(df)} ventas")
    return df

@asset
def ventas_procesadas(context: AssetExecutionContext, ventas_raw):
    """Asset: ventas procesadas (depende de ventas_raw)."""
    context.log.info("Procesando ventas...")
    df = ventas_raw.copy()
    df = df.dropna()
    df['total'] = df['precio'] * df['cantidad']
    
    # Guardar output en 05_pipelines/data/output
    ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'ventas_procesadas.parquet'
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(ruta_salida, index=False)
    context.log.info(f"Guardado en {ruta_salida}")
    
    return df

@asset
def ventas_por_categoria(context: AssetExecutionContext, ventas_procesadas):
    """Asset: ventas agregadas por categoría."""
    context.log.info("Agregando por categoría...")
    resultado = ventas_procesadas.groupby('categoria')['total'].sum()
    
    # Guardar output
    ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'ventas_por_categoria.parquet'
    resultado.to_frame().to_parquet(ruta_salida)
    context.log.info(f"Guardado en {ruta_salida}")
    
    return resultado

# Definiciones necesarias para que Dagster reconozca los assets
defs = Definitions(assets=[ventas_raw, ventas_procesadas, ventas_por_categoria])
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
   cd 05_pipelines/ejercicios/dagster
   ```
4. Ejecuta (desde la carpeta `dagster`):
   ```bash
   dagster dev -f 01-primer-asset.py
   ```
   
   > 💡 **Nota**: Asegúrate de estar en la carpeta `05_pipelines/ejercicios/dagster/` antes de ejecutar. Si estás en otra ubicación, usa la ruta completa o relativa al archivo.

**O desde terminal externa (desde la raíz del proyecto):**
```bash
# Activa el entorno virtual primero:
pyenv activate ingenieria-de-datos

# Desde la raíz del proyecto, ejecuta con la ruta relativa:
dagster dev -f 05_pipelines/ejercicios/dagster/01-primer-asset.py

# O navega a la carpeta primero:
cd 05_pipelines/ejercicios/dagster
dagster dev -f 01-primer-asset.py
```

> ⚠️ **Importante**: Si ves el error "No such file or directory", asegúrate de:
> - Estar en el directorio correcto (`05_pipelines/ejercicios/dagster/`) si usas `-f 01-primer-asset.py`
> - O usar la ruta completa/relativa desde donde estés ejecutando el comando

### Paso 4: Verificar que funciona

Una vez que ejecutes `dagster dev -f 01-primer-asset.py` (desde la carpeta `dagster`) o `dagster dev -f 05_pipelines/ejercicios/dagster/01-primer-asset.py` (desde la raíz), deberías ver:

```
Serving on http://127.0.0.1:3000
```

**Verificación:**
1. ✅ **Servidor corriendo**: El mensaje "Serving on http://127.0.0.1:3000" confirma que Dagster está funcionando
2. ✅ **Abrir en el navegador**: Ve a **http://localhost:3000**
3. ✅ **Ver tus 3 assets**: Deberías ver `ventas_raw`, `ventas_procesadas`, y `ventas_por_categoria` en la UI
4. ✅ **Materializar assets**: Puedes hacer click en cada asset para materializarlo (ejecutarlo)

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

---

## 🔄 Dependencias automáticas

Dagster detecta dependencias automáticamente por parámetros.

```python
@asset
def usuarios():
    return pd.read_csv('usuarios.csv')

@asset
def ventas():
    return pd.read_csv('ventas.csv')

@asset
def ventas_completas(usuarios, ventas):
    # Dagster sabe que ventas_completas depende de usuarios y ventas
    return pd.merge(ventas, usuarios, on='usuario_id')
```

---

## 🖥️ UI (Dagit)

Dagster incluye una UI excelente llamada Dagit.

> ⚠️ **Recuerda**: Activa tu entorno virtual antes de ejecutar:
> ```bash
> pyenv activate ingenieria-de-datos
> ```

### Paso 1: Iniciar Dagit

**Opción A: Desde la carpeta `dagster`**
```bash
cd 05_pipelines/ejercicios/dagster
dagster dev -f 01-primer-asset.py
```

**Opción B: Desde la raíz del proyecto**
```bash
# Desde la raíz del proyecto
dagster dev -f 05_pipelines/ejercicios/dagster/01-primer-asset.py
```

Verás algo como:
```
Serving on http://127.0.0.1:3000
```

> 💡 **Nota**: 
> - `-f` especifica el archivo Python con tus assets
> - Si estás en la carpeta `dagster`, usa `-f 01-primer-asset.py`
> - Si estás en otra ubicación, usa la ruta completa o relativa al archivo
> - Los nombres de módulos Python no pueden empezar con números, por eso usamos `-f` en lugar de `-m`
> - Si ves "No such file or directory", verifica que estás en el directorio correcto o usa la ruta completa

### Paso 2: Abrir la UI

Abre tu navegador y ve a: **http://localhost:3000**

### Paso 3: Explorar

En la UI podrás:
- **Ver tus assets**: Lista de todos los assets definidos
- **Materializar assets**: Ejecutar y crear los datos
- **Ver dependencias**: Gráfico visual de cómo se relacionan los assets
- **Revisar logs**: Logs de cada ejecución
- **Explorar historial**: Ver ejecuciones anteriores

**Características de la UI:**
* Visualización de assets y dependencias
* Materialización de assets
* Logs y monitoreo
* Búsqueda y filtrado

> 💡 **Tip**: Deja `dagster dev` corriendo mientras trabajas. Puedes detenerlo con `Ctrl+C`.

---

## 📅 Programación

```python
from dagster import (
    asset,
    ScheduleDefinition,
    define_asset_job,
    AssetSelection
)

@asset
def ventas_diarias():
    # Tu lógica
    pass

# Definir job
ventas_job = define_asset_job(
    "procesar_ventas",
    selection=AssetSelection.assets(ventas_diarias)
)

# Definir schedule
ventas_schedule = ScheduleDefinition(
    job=ventas_job,
    cron_schedule="0 0 * * *"  # Diario
)
```

---

## 💡 Ventajas de Dagster

### 1. Enfoque en datos

```python
# Piensas en qué datos produces
@asset
def ventas_por_mes():
    # Este asset produce ventas_por_mes
    return df
```

### 2. UI excelente

* Visualización clara de dependencias
* Materialización de assets
* Historial de cambios

### 3. Desarrollo local fácil

```bash
# Iniciar y desarrollar
dagster dev
```

---

## 🎯 Ejercicios prácticos

Crea estos archivos en `05_pipelines/ejercicios/dagster/`:

### Ejercicio 1: Primer Asset
**Archivo:** `01-primer-asset.py`
- Crea assets simples que lean y procesen datos
- Usa el ejemplo de arriba como base
- Ejecuta `dagster dev` y materializa los assets en la UI

### Ejercicio 2: Assets con Dependencias
**Archivo:** `02-assets-con-dependencias.py`
- Crea múltiples assets que dependan unos de otros
- Algunos assets deben ejecutarse en paralelo
- Otros deben esperar a que terminen los anteriores
- Observa cómo Dagster detecta las dependencias automáticamente

### Ejercicio 3: Jobs y Schedules
**Archivo:** `03-definitions.py`
- Define jobs que agrupen assets
- Crea schedules para ejecutar jobs automáticamente
- Experimenta con diferentes frecuencias (diario, horario, etc.)

### Ejercicio 4: UI
- Inicia Dagit (`dagster dev`)
- Materializa tus assets desde la UI
- Explora el gráfico de dependencias
- Revisa logs y historial de ejecuciones

---

## 🚀 Próximos pasos

* **Materializaciones**: Ver qué assets están actualizados
* **Partitions**: Procesar datos por particiones
* **Resources**: Configuración reutilizable
* **I/O Managers**: Gestionar almacenamiento

---

## 💬 ¿Necesitas ayuda?

Si encuentras errores al ejecutar tus scripts de Dagster:

1. **Usa el chat de Cursor** (`Cmd+L` en Mac o `Ctrl+L` en Windows/Linux):
   - Copia y pega el mensaje de error completo
   - Explica qué estabas intentando hacer
   - Pregunta específicamente sobre el error

2. **El chat puede ayudarte con:**
   - Entender mensajes de error
   - Corregir problemas de sintaxis
   - Resolver importaciones faltantes
   - Ajustar rutas o configuraciones
   - Debugging de assets y dependencias

3. **Ejemplo de pregunta útil:**
   ```
   Tengo este error al ejecutar dagster dev:
   [pega el error completo aquí]
   
   ¿Qué significa y cómo lo soluciono?
   ```

---

> **Recuerda**: Dagster es excelente si piensas en términos de "qué datos produzco" en lugar de "qué código ejecuto". Si tienes dudas, usa el chat de Cursor para obtener ayuda rápida.
