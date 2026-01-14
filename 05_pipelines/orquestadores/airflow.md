# Apache Airflow: El Estándar de la Industria

Apache Airflow es el orquestador de workflows más popular para Data Engineering. Aprende los conceptos básicos y cómo usarlo.

---

## 🧠 ¿Qué es Airflow?

Apache Airflow es una plataforma para:
* **Programar** workflows de datos
* **Orquestar** tareas complejas con dependencias
* **Monitorear** ejecuciones en tiempo real
* **Escalar** a múltiples workers

**Características:**
* **El más popular**: Estándar de la industria
* **Muy maduro**: Probado en producción a gran escala
* **Gran ecosistema**: Muchos plugins y integraciones
* **Comunidad grande**: Muchos recursos y soporte

> Airflow es como un cron job inteligente con dependencias, retry y monitoreo. Es la opción segura y probada para producción.

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
pip install apache-airflow

# Con PostgreSQL (recomendado para producción)
pip install apache-airflow[postgres]

# Con providers comunes
pip install apache-airflow-providers-postgres
pip install apache-airflow-providers-aws
```

### Verificar versión instalada

Para saber qué versión de Airflow tienes instalada:

```bash
airflow version
```

Esto mostrará algo como:
```
Apache Airflow 3.1.6
```

> 💡 **Importante**: La versión de Airflow determina qué comandos están disponibles:
> - **Airflow 3.0+**: Usa `airflow standalone` (recomendado) o `airflow db migrate`
> - **Airflow 2.x**: Usa `airflow db migrate` y `airflow users create`
> - **Airflow 1.x**: Usa `airflow db init` (versiones muy antiguas)

### Configurar variables de entorno en .env

Airflow necesita algunas configuraciones. Agrégalas a tu `.env` (ya están en `.env.example`):

```bash
# Directorio donde se almacenan base de datos, logs y configuración
# NOTA: Airflow requiere ruta absoluta. Usa $(pwd)/05_pipelines/orquestadores/.airflow al exportar
# En .env puedes usar relativa, pero al exportar debe ser absoluta
AIRFLOW_HOME=./05_pipelines/orquestadores/.airflow

# Deshabilitar DAGs de ejemplo (para ver solo tus DAGs)
AIRFLOW__CORE__LOAD_EXAMPLES=False

# Contraseña para el usuario admin (solo para modo tradicional)
# En modo standalone, la contraseña se genera automáticamente
AIRFLOW_ADMIN_PASSWORD=admin
```

> ⚠️ **IMPORTANTE sobre rutas**: 
> - En el archivo `.env` puedes usar rutas relativas (`./05_pipelines/orquestadores/.airflow`)
> - Pero al exportar la variable, **debe ser absoluta**: `export AIRFLOW_HOME=$(pwd)/05_pipelines/orquestadores/.airflow`
> - O carga desde .env y convierte a absoluta: `export AIRFLOW_HOME=$(cd $(dirname .env) && pwd)/05_pipelines/orquestadores/.airflow`

**Para usar estas variables:**

1. **Carga el .env antes de ejecutar comandos de Airflow:**
   ```bash
   # Opción 1: Cargar manualmente (usar ruta absoluta)
   export AIRFLOW_HOME=$(pwd)/05_pipelines/orquestadores/.airflow
   export AIRFLOW__CORE__LOAD_EXAMPLES=False
   export AIRFLOW_ADMIN_PASSWORD=admin
   
   # Opción 2: Cargar desde .env y convertir a absoluta
   source <(python -c "from dotenv import load_dotenv; from pathlib import Path; load_dotenv(); import os; airflow_home = os.getenv('AIRFLOW_HOME', './05_pipelines/orquestadores/.airflow'); abs_path = str(Path(airflow_home).resolve()); print(f'export AIRFLOW_HOME={abs_path}'); [print(f'export {k}={v}') for k,v in os.environ.items() if k.startswith('AIRFLOW__')]")
   ```

2. **O exporta directamente (recomendado):**
   ```bash
   export AIRFLOW_HOME=$(pwd)/05_pipelines/orquestadores/.airflow
   export AIRFLOW__CORE__LOAD_EXAMPLES=False
   ```

> 💡 **Nota**: 
> - Si no configuras `AIRFLOW_HOME`, Airflow usará `~/airflow` por defecto
> - `AIRFLOW__CORE__LOAD_EXAMPLES=False` deshabilita los DAGs de ejemplo (recomendado para ver solo tus DAGs)
> - `AIRFLOW_ADMIN_PASSWORD` solo se usa en el modo tradicional (Opción B)
> - En modo `standalone`, la contraseña se genera automáticamente (no se puede configurar desde .env)
> - Si usas modo tradicional, puedes especificar la contraseña directamente en el comando o usar la variable del .env

### Setup inicial

> ⚠️ **Recuerda**: Activa tu entorno virtual antes de ejecutar:
> ```bash
> pyenv activate ingenieria-de-datos
> ```

#### Opción rápida: Script de configuración automática (Recomendado)

El proyecto incluye un script que configura todo automáticamente. **Esta es la forma más fácil y rápida de empezar:**

```bash
# 1. Ejecuta el script de setup desde la raíz del proyecto
bash 05_pipelines/ejercicios/airflow/setup-airflow.sh
```

**¿Qué hace el script?**
- ✅ Limpia cualquier configuración anterior de Airflow (si existe)
- ✅ Crea el directorio `AIRFLOW_HOME` con ruta absoluta (`$(pwd)/05_pipelines/orquestadores/.airflow`)
- ✅ Configura `AIRFLOW__CORE__LOAD_EXAMPLES=False` para ocultar DAGs de ejemplo
- ✅ Crea la carpeta `dags` dentro de `AIRFLOW_HOME`
- ✅ Crea symlinks de todos tus DAGs en `$AIRFLOW_HOME/dags/`
- ✅ Muestra las instrucciones exactas para iniciar Airflow

**Después de ejecutar el script, inicia Airflow:**

```bash
# El script te mostrará la ruta exacta, pero generalmente es:
export AIRFLOW_HOME=$(pwd)/05_pipelines/orquestadores/.airflow
export AIRFLOW__CORE__LOAD_EXAMPLES=False
airflow standalone
```

> 💡 **Tip**: El script muestra las instrucciones exactas al finalizar. Solo copia y pega los comandos que te muestre.

> ⚠️ **IMPORTANTE**: El script usa rutas absolutas automáticamente, así que no tendrás problemas con el error "Cannot use relative path" que puede aparecer si usas rutas relativas.

#### Opción manual: Configuración paso a paso

Si prefieres configurar todo manualmente (sin usar el script), sigue las instrucciones de abajo. **Nota**: El script automático hace todo esto por ti, así que solo necesitas esta opción si quieres entender cada paso o personalizar algo.

### Opción A: Modo Standalone (Recomendado para empezar - Airflow 3.0+)

El modo `standalone` inicia todo (webserver, scheduler, etc.) y crea un usuario admin automáticamente:

> ⚠️ **IMPORTANTE**: Siempre configura `AIRFLOW_HOME` antes de ejecutar `airflow standalone` para que todos los archivos (incluyendo el de contraseñas) se generen en el proyecto.

```bash
# 1. Configurar variables de entorno (OBLIGATORIO - usar ruta absoluta)
export AIRFLOW_HOME=$(pwd)/05_pipelines/orquestadores/.airflow
export AIRFLOW__CORE__LOAD_EXAMPLES=False  # Deshabilitar DAGs de ejemplo

# 2. Crear carpeta dags y symlinks de tus DAGs
mkdir -p $AIRFLOW_HOME/dags
ln -sf $(pwd)/05_pipelines/ejercicios/airflow/*.py $AIRFLOW_HOME/dags/

# 3. Verificar configuración
echo "AIRFLOW_HOME: $AIRFLOW_HOME"
echo "DAGs configurados:"
ls -la $AIRFLOW_HOME/dags/*.py 2>/dev/null || echo "  (Aún no hay DAGs)"

# 4. Iniciar Airflow en modo standalone
airflow standalone
```

> ⚠️ **IMPORTANTE**: Airflow requiere una **ruta absoluta** para `AIRFLOW_HOME`. Usa `$(pwd)/05_pipelines/orquestadores/.airflow` en lugar de `./05_pipelines/orquestadores/.airflow`.

> 💡 **Tip**: Si usaste el script `setup-airflow.sh`, ya tienes todo configurado. Solo ejecuta:
> ```bash
> export AIRFLOW_HOME=$(pwd)/05_pipelines/orquestadores/.airflow
> export AIRFLOW__CORE__LOAD_EXAMPLES=False
> airflow standalone
> ```

> 💡 **Nota**: Si ya ejecutaste `airflow standalone` sin configurar `AIRFLOW_HOME`, el archivo de contraseñas se generó en `~/airflow/`. Puedes moverlo:
> ```bash
> # Mover el archivo de contraseñas al directorio del proyecto
> mkdir -p ./05_pipelines/orquestadores/.airflow
> mv ~/airflow/simple_auth_manager_passwords.json.generated ./05_pipelines/orquestadores/.airflow/
> ```

Esto:
- ✅ Inicializa la base de datos automáticamente
- ✅ Crea un usuario admin (usuario: `admin`, contraseña: se genera automáticamente)
- ✅ Inicia webserver y scheduler en un solo proceso
- ✅ Abre la UI en http://localhost:8080

> ⚠️ **Problema común: "Invalid credentials" al iniciar sesión**
> 
> Si ves el error "401 Unauthorized" al intentar iniciar sesión, la contraseña se generó automáticamente cuando ejecutaste `airflow standalone`.
> 
> **Cómo encontrar la contraseña:**
> 
> 1. **Si es la primera vez que ejecutas `standalone`**, la contraseña aparece en la terminal:
>    ```
>    =================================================================
>    Airflow is ready!
>    =================================================================
>    Login with username: admin  |  password: [AQUÍ_ESTÁ_LA_CONTRASEÑA]
>    =================================================================
>    ```
> 
> 2. **Si ya ejecutaste `standalone` antes**, la contraseña está guardada en un archivo JSON:
>    ```bash
>    # Si configuraste AIRFLOW_HOME (recomendado - en el proyecto):
>    export AIRFLOW_HOME=$(pwd)/05_pipelines/orquestadores/.airflow
>    cat $AIRFLOW_HOME/simple_auth_manager_passwords.json.generated
>    
>    # O si no configuraste AIRFLOW_HOME (se generó en ~/airflow):
>    cat ~/airflow/simple_auth_manager_passwords.json.generated
>    ```
>    El archivo contiene algo como: `{"admin": "tu_contraseña_aqui"}`
>    
>    > 💡 **Para mover el archivo al proyecto**: Si el archivo está en `~/airflow/` y quieres que esté en el proyecto:
>    > ```bash
>    > export AIRFLOW_HOME=$(pwd)/05_pipelines/orquestadores/.airflow
>    > mkdir -p $AIRFLOW_HOME
>    > mv ~/airflow/simple_auth_manager_passwords.json.generated $AIRFLOW_HOME/
>    > # La próxima vez, configura AIRFLOW_HOME antes de ejecutar standalone
>    > ```
> 
> 3. **O busca el archivo automáticamente:**
>    ```bash
>    # Buscar el archivo de contraseñas
>    find ~/airflow $AIRFLOW_HOME -name "*password*.json*" 2>/dev/null
>    cat $(find ~/airflow $AIRFLOW_HOME -name "*password*.json*" 2>/dev/null | head -1)
>    ```
> 
> 4. **Si no encuentras el archivo**, elimina la base de datos y reinicia:
>    ```bash
>    export AIRFLOW_HOME=$(pwd)/05_pipelines/orquestadores/.airflow
>    rm -rf $AIRFLOW_HOME/airflow.db
>    rm -f $AIRFLOW_HOME/simple_auth_manager_passwords.json.generated
>    export AIRFLOW__CORE__LOAD_EXAMPLES=False
>    airflow standalone
>    # Ahora la contraseña aparecerá en la terminal
>    ```

### Opción B: Modo tradicional (Webserver + Scheduler separados)

Si prefieres tener más control, usar una contraseña personalizada, o usar Airflow 2.x:

```bash
# 1. Configurar AIRFLOW_HOME (si no está en .env)
export AIRFLOW_HOME=./05_pipelines/orquestadores/.airflow

# 2. Cargar variables del .env (opcional, para usar AIRFLOW_ADMIN_PASSWORD)
# Si tienes python-dotenv instalado:
source <(python -c "from dotenv import load_dotenv; load_dotenv(); import os; print('export AIRFLOW_ADMIN_PASSWORD=' + os.getenv('AIRFLOW_ADMIN_PASSWORD', 'admin'))")

# 3. Inicializar base de datos
airflow db migrate

# 4. Crear usuario admin con contraseña personalizada (Airflow 3.0+)
# En Airflow 3.0+, el comando 'users create' no existe, usa este script Python:
python << 'EOF'
from airflow.www.app import create_app
app = create_app()
with app.app_context():
    from airflow.auth.managers.fab.models import User
    import os
    password = os.getenv('AIRFLOW_ADMIN_PASSWORD', 'admin')
    if not User.find_user(username='admin'):
        User.create_user(
            username='admin',
            first_name='Admin',
            last_name='User',
            email='admin@example.com',
            role='Admin',
            password=password
        )
        print(f'✅ Usuario admin creado con contraseña: {password}')
    else:
        print('⚠️ Usuario admin ya existe')
EOF

# 5. Iniciar webserver (en una terminal)
export AIRFLOW_HOME=$(pwd)/05_pipelines/orquestadores/.airflow
airflow webserver --port 8080

# 6. Iniciar scheduler (en otra terminal)
export AIRFLOW_HOME=$(pwd)/05_pipelines/orquestadores/.airflow
airflow scheduler
```

> 💡 **Configurar contraseña en .env**:
> 1. Agrega `AIRFLOW_ADMIN_PASSWORD=tu_contraseña` a tu `.env` (ya está en `.env.example`)
> 2. Antes de crear el usuario, carga la variable: `export AIRFLOW_ADMIN_PASSWORD=$(grep AIRFLOW_ADMIN_PASSWORD .env | cut -d '=' -f2)`
> 3. O simplemente especifica la contraseña directamente en el comando `--password`

---

## 📁 Dónde crear tus archivos

**Crea todos tus ejercicios y DAGs de Airflow en esta carpeta:**

```
05_pipelines/ejercicios/airflow/
```

### Estructura recomendada

```
05_pipelines/ejercicios/airflow/
├── 01-primer-dag.py          # Tu primer DAG simple
├── 02-dependencias.py        # DAG con dependencias complejas
├── 03-programacion.py       # DAG con scheduling avanzado
└── README.md                 # (opcional) Notas personales
```

> 💡 **Importante**: Los DAGs de Airflow deben estar en la carpeta `dags/` dentro de `AIRFLOW_HOME`. Ver instrucciones abajo para configurar esto.

### Cómo crear un archivo

#### Opción A: Usando Cursor (Recomendado)

1. **Abre la carpeta en Cursor:**
   - En Cursor, navega a `05_pipelines/ejercicios/airflow/`
   - O usa `Cmd+P` (Mac) / `Ctrl+P` (Windows/Linux) y escribe: `ejercicios/airflow`

2. **Crea un nuevo archivo:**
   - Click derecho en la carpeta `airflow` → "New File"
   - O usa `Cmd+N` (Mac) / `Ctrl+N` (Windows/Linux)
   - Guarda como `01-primer-dag.py` en la carpeta `airflow`

3. **Escribe tu código** (ver ejemplos abajo)

4. **Copia el DAG a la carpeta de Airflow:**
   - Los DAGs deben estar en `AIRFLOW_HOME/dags/`
   - Puedes crear un symlink o copiar el archivo

#### Opción B: Desde terminal/Bash

1. **Navega a la carpeta de ejercicios:**
   ```bash
   cd 05_pipelines/ejercicios/airflow
   ```

2. **Crea un nuevo archivo:**
   ```bash
   touch 01-primer-dag.py
   ```

3. **Abre el archivo en Cursor o tu editor:**
   ```bash
   cursor 05_pipelines/ejercicios/airflow/01-primer-dag.py
   ```

4. **Escribe tu código** y guarda

---

## 📊 Conceptos clave

### DAG (Directed Acyclic Graph)

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

dag = DAG(
    'mi_pipeline',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily'
)
```

### Tasks y Operators

```python
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

def mi_funcion():
    print("Ejecutando tarea")

tarea = PythonOperator(
    task_id='mi_tarea',
    python_callable=mi_funcion,
    dag=dag
)
```

---

## 🎯 Primer DAG

### Paso 1: Crear el archivo

**En Cursor:**
1. Navega a `05_pipelines/ejercicios/airflow/` en el explorador de archivos
2. Click derecho → "New File"
3. Nombra el archivo: `01-primer-dag.py`

**O desde terminal:**
```bash
cd 05_pipelines/ejercicios/airflow
touch 01-primer-dag.py
```

### Paso 2: Escribir el código

Abre `01-primer-dag.py` en Cursor y copia este código (o usa el archivo de ejemplo que ya está creado):

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).parent.parent.parent.parent

default_args = {
    'owner': 'data_engineer',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'primer_pipeline_etl',
    default_args=default_args,
    description='Primer pipeline ETL con Airflow',
    schedule_interval='@daily',
    catchup=False,
)

def extraer(**context):
    """Extrae datos del CSV de ventas."""
    ruta_entrada = BASE_DIR / '03_python' / 'data' / 'ventas.csv'
    df = pd.read_csv(ruta_entrada)
    return df.to_dict('records')

def transformar(**context):
    """Transforma los datos extraídos."""
    ti = context['ti']
    datos = ti.xcom_pull(task_ids='extraer')
    df = pd.DataFrame(datos)
    df = df.dropna()
    df['total'] = df['precio'] * df['cantidad']
    return df.to_dict('records')

def cargar(**context):
    """Carga los datos transformados."""
    ti = context['ti']
    datos = ti.xcom_pull(task_ids='transformar')
    df = pd.DataFrame(datos)
    
    ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'ventas_airflow.parquet'
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(ruta_salida, index=False)
    print(f"✅ Datos guardados en {ruta_salida}")

tarea_extraer = PythonOperator(
    task_id='extraer',
    python_callable=extraer,
    dag=dag,
)

tarea_transformar = PythonOperator(
    task_id='transformar',
    python_callable=transformar,
    dag=dag,
)

tarea_cargar = PythonOperator(
    task_id='cargar',
    python_callable=cargar,
    dag=dag,
)

tarea_extraer >> tarea_transformar >> tarea_cargar
```

> 💡 **Nota**: 
> - Usamos `pathlib.Path` para construir rutas de forma robusta
> - Los archivos de salida se guardan en `05_pipelines/data/output/`
> - Usamos XCom para pasar datos entre tareas (ver `ti.xcom_pull`)

### Paso 3: Configurar Airflow para usar tus DAGs

Airflow busca DAGs en `AIRFLOW_HOME/dags/`. **Es importante hacer esto antes de iniciar Airflow**:

> ⚠️ **IMPORTANTE**: Si ya tienes `airflow standalone` corriendo, deténlo (Ctrl+C), configura los DAGs, y reinícialo.

**Opción A: Crear symlinks (Recomendado - los cambios se reflejan automáticamente)**
```bash
# 1. Asegúrate de que AIRFLOW_HOME esté configurado (ruta absoluta)
export AIRFLOW_HOME=$(pwd)/05_pipelines/orquestadores/.airflow

# 2. Crear carpeta dags si no existe
mkdir -p $AIRFLOW_HOME/dags

# 3. Crear symlinks de cada archivo DAG
ln -sf $(pwd)/05_pipelines/ejercicios/airflow/*.py $AIRFLOW_HOME/dags/

# 4. Verificar que los symlinks se crearon
ls -la $AIRFLOW_HOME/dags/
```

**Opción B: Copiar archivos (si prefieres copias estáticas)**
```bash
# Copiar DAGs a la carpeta de Airflow
export AIRFLOW_HOME=$(pwd)/05_pipelines/orquestadores/.airflow
mkdir -p $AIRFLOW_HOME/dags
cp 05_pipelines/ejercicios/airflow/*.py $AIRFLOW_HOME/dags/
```

> 💡 **Nota**: Con symlinks (Opción A), cualquier cambio que hagas en los archivos originales se reflejará automáticamente en Airflow. Con copias (Opción B), necesitarás copiar de nuevo después de cada cambio.

### Paso 4: Iniciar Airflow

> ⚠️ **Recuerda**: Activa tu entorno virtual antes de ejecutar:
> ```bash
> pyenv activate ingenieria-de-datos
> ```

**Opción A: Modo Standalone (Recomendado para Airflow 3.0+)**
```bash
# Configurar variables de entorno (usar ruta absoluta)
export AIRFLOW_HOME=$(pwd)/05_pipelines/orquestadores/.airflow
export AIRFLOW__CORE__LOAD_EXAMPLES=False  # Deshabilitar DAGs de ejemplo

airflow standalone
```

> ⚠️ **IMPORTANTE**: Airflow requiere una **ruta absoluta** para `AIRFLOW_HOME`. Usa `$(pwd)/05_pipelines/orquestadores/.airflow` en lugar de `./05_pipelines/orquestadores/.airflow`.

Esto inicia todo en un solo proceso. La contraseña del usuario admin se mostrará en la terminal.

> 💡 **Nota**: `AIRFLOW__CORE__LOAD_EXAMPLES=False` deshabilita los 80+ DAGs de ejemplo para que veas solo los tuyos. Ya está configurado en `.env.example`.

**Opción B: Modo tradicional (Solo si usas Airflow 2.x o necesitas más control)**

**Terminal 1 - Webserver:**
```bash
export AIRFLOW_HOME=./05_pipelines/orquestadores/.airflow
airflow webserver --port 8080
```

**Terminal 2 - Scheduler:**
```bash
export AIRFLOW_HOME=./05_pipelines/orquestadores/.airflow
airflow scheduler
```

> 💡 **Nota**: Si tienes Airflow 3.0+, usa la Opción A (`standalone`). La Opción B es para versiones anteriores o cuando necesitas más control sobre los procesos.

### Paso 5: Verificar que funciona

1. ✅ **Abrir UI**: Ve a **http://localhost:8080**
2. ✅ **Login**: Usa `admin` / contraseña del archivo JSON (o las credenciales que creaste)
3. ✅ **Ver tus DAGs**: Deberías ver `primer_pipeline_etl` y `dependencias_complejas` en la lista de DAGs

> ⚠️ **Si no ves tus DAGs**:
> - **Si acabas de configurar los symlinks**: Espera 30-60 segundos para que Airflow los detecte automáticamente, o reinicia `airflow standalone`
> - **Verifica que los symlinks estén correctos**: `ls -la $AIRFLOW_HOME/dags/` debe mostrar tus archivos `.py`
> - **Revisa los logs**: En la UI, ve a "Browse" → "Logs" para ver si hay errores en los DAGs
> - **Verifica la sintaxis**: Asegúrate de que tus archivos Python no tengan errores

4. ✅ **Ejecutar DAG**: Activa el toggle del DAG y luego haz click en "Trigger DAG"

> 💬 **¿Tienes errores?** Si encuentras algún error al ejecutar tu DAG, usa el chat de Cursor (`Cmd+L` en Mac o `Ctrl+L` en Windows/Linux) para pedir ayuda. Puedes:
> - Copiar y pegar el mensaje de error completo
> - Mencionar qué estabas intentando hacer
> - Preguntar sobre el error específico

---

## 🔗 Dependencias

```python
# Sintaxis >>
tarea_a >> tarea_b >> tarea_c

# Múltiples
tarea_a >> [tarea_b, tarea_c] >> tarea_d
```

---

## 📅 Scheduling

```python
# Diario
schedule_interval='@daily'

# Cada hora
schedule_interval='@hourly'

# Cron
schedule_interval='0 0 * * *'  # Medianoche diario
```

---

## 💡 Ventajas de Airflow

### 1. Maduro y probado

* Usado en producción por miles de empresas
* Comunidad muy grande
* Muchos recursos disponibles

### 2. Gran ecosistema

* Muchos providers (AWS, GCP, Azure, etc.)
* Plugins para casi todo
* Integraciones con servicios comunes

### 3. UI completa

* Monitoreo en tiempo real
* Logs detallados
* Visualización de DAGs
* Gestión de conexiones y variables

---

## ⚠️ Desventajas

### 1. Curva de aprendizaje

* Conceptos nuevos (DAGs, Operators)
* Configuración inicial más compleja
* Requiere entender scheduling

### 2. Overhead

* Requiere base de datos
* Necesita scheduler corriendo
* Más recursos que soluciones simples

---

## 🎯 Cuándo usar Airflow

✅ **Usa Airflow cuando:**
* Necesitas orquestación compleja
* Tienes múltiples pipelines
* Necesitas programación avanzada
* Quieres estándar de industria

❌ **No uses Airflow cuando:**
* Pipeline muy simple
* Solo necesitas ejecutar ocasionalmente
* No tienes infraestructura para gestionarlo

---

## 🚀 Alternativas gestionadas

Si no quieres gestionar Airflow:

* **Google Cloud Composer**: Airflow gestionado en GCP
* **AWS MWAA**: Airflow gestionado en AWS
* **Astronomer**: Plataforma gestionada de Airflow

---

## 🎯 Ejercicios prácticos

Crea estos archivos en `05_pipelines/ejercicios/airflow/`:

### Ejercicio 1: Primer DAG
**Archivo:** `01-primer-dag.py`
- Crea un DAG simple con 3 tareas: extraer, transformar, cargar
- Usa el ejemplo de arriba como base
- Ejecuta el DAG desde la UI de Airflow

### Ejercicio 2: Dependencias complejas
**Archivo:** `02-dependencias.py`
- Crea tareas que se ejecuten en paralelo
- Crea tareas que dependan de múltiples tareas anteriores
- Observa cómo Airflow maneja las dependencias

### Ejercicio 3: Scheduling
- Modifica `schedule_interval` en tus DAGs
- Prueba diferentes frecuencias: `@daily`, `@hourly`, `0 0 * * *`
- Observa cómo Airflow programa las ejecuciones

### Ejercicio 4: UI
- Explora la UI de Airflow
- Revisa logs de tareas ejecutadas
- Visualiza el gráfico de dependencias
- Monitorea ejecuciones en tiempo real

---

## 🚀 Próximos pasos

* **Operators avanzados**: DockerOperator, KubernetesPodOperator
* **XComs**: Pasar datos entre tareas
* **Hooks**: Conectar con servicios externos
* **Plugins**: Crear funcionalidad custom

---

> **Recuerda**: Airflow es poderoso pero tiene overhead. Úsalo cuando necesites sus capacidades avanzadas. Para empezar, considera primero **[Prefect](prefect.md)** o **[Dagster](dagster.md)** que son más simples.
