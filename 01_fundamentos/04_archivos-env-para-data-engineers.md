# Archivos .env para Data Engineers

Los archivos `.env` (environment variables) son una forma estándar de **gestionar configuraciones y secretos** en aplicaciones sin hardcodear valores sensibles en el código.

> 💡 **Este proyecto incluye un `.env.example` en la raíz** que puedes copiar y configurar. Los ejemplos y ejercicios del proyecto usan estas variables automáticamente. Ver más abajo cómo configurarlo.

---

## 🧠 ¿Por qué usar archivos .env?

### Problema: Configuración hardcodeada

```python
# ❌ MAL - Credenciales en el código
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="mi_db",
    user="admin",
    password="super_secret_password_123"  # ⚠️ Expuesto en el código
)
```

**Problemas:**
* Credenciales expuestas en el repositorio
* Diferentes configuraciones para dev/prod requieren cambiar código
* Riesgo de commitear secretos por error
* Dificulta colaboración en equipo

### Solución: Variables de entorno

```python
# ✅ BIEN - Usando variables de entorno
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()  # Carga variables del archivo .env

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")  # ✅ Seguro
)
```

**Ventajas:**
* Credenciales fuera del código
* Fácil cambiar entre entornos (dev, staging, prod)
* No se commitea al repositorio
* Cada desarrollador tiene su propia configuración

---

## 📝 Estructura de un archivo .env

Un archivo `.env` es un archivo de texto simple con formato `CLAVE=VALOR`:

```bash
# Comentarios empiezan con #
# Configuración de base de datos
DB_HOST=localhost
DB_PORT=5432
DB_NAME=data_engineering
DB_USER=de_user
DB_PASSWORD=mi_password_seguro

# Configuración de API
API_KEY=sk-1234567890abcdef
API_URL=https://api.ejemplo.com
API_TIMEOUT=30

# Configuración de entorno
ENVIRONMENT=development
DEBUG=True
LOG_LEVEL=INFO

# Rutas de archivos
DATA_PATH=/app/data
OUTPUT_PATH=/app/output
```

### Reglas básicas

* **Sin espacios** alrededor del `=`: `CLAVE=VALOR` (no `CLAVE = VALOR`)
* **Sin comillas** necesarias (a menos que el valor tenga espacios)
* **Comentarios** con `#`
* **Una variable por línea**

---

## 🐍 Usar .env en Python

### Instalación

```bash
# Asegúrate de tener tu entorno virtual activado (con pyenv)
pyenv activate ingenieria-de-datos

# Instalar python-dotenv
pip install python-dotenv
```

### Uso básico

```python
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

# Obtener una variable
db_host = os.getenv("DB_HOST")
db_password = os.getenv("DB_PASSWORD")

# Con valor por defecto
timeout = os.getenv("API_TIMEOUT", "30")  # Si no existe, usa "30"
```

### Ejemplo completo

```python
import os
from dotenv import load_dotenv
import psycopg2

# Cargar variables de entorno
load_dotenv()

def connect_to_database():
    """Conecta a la base de datos usando variables de entorno"""
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT", "5432"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        return conn
    except Exception as e:
        print(f"Error conectando a la base de datos: {e}")
        return None

# Uso
conn = connect_to_database()
```

---

## 🐳 Usar .env con Docker

Docker y Docker Compose pueden leer archivos `.env` automáticamente.

### docker-compose.yml

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    ports:
      - "${POSTGRES_PORT}:5432"
```

### .env

```bash
POSTGRES_DB=data_engineering
POSTGRES_USER=de_user
POSTGRES_PASSWORD=secure_password
POSTGRES_PORT=5432
```

Docker Compose **automáticamente** lee el archivo `.env` en el mismo directorio.

---

## 📋 Archivo .env.example

Este repositorio incluye un archivo **`.env.example`** en la raíz que muestra todas las variables de entorno necesarias para el proyecto.

### Usar el .env.example del proyecto

1. **Copia el archivo de ejemplo:**
   ```bash
   # Desde la raíz del proyecto
   cp .env.example .env
   ```

2. **Edita el archivo `.env`** con tus valores reales:
   ```bash
   # Abre .env en tu editor
   nano .env
   # o
   code .env
   ```

3. **Completa las variables necesarias** según lo que vayas a usar:
   - Si trabajas con SQL: configura `DB_HOST`, `DB_USER`, `DB_PASSWORD`, etc.
   - Si usas APIs: configura `API_KEY`, `API_URL`, etc.
   - Si procesas archivos: configura `DATA_SOURCE_PATH`, `DATA_OUTPUT_PATH`, etc.

### Estructura del .env.example

El archivo `.env.example` del proyecto está organizado en secciones:

```bash
# ============================================
# CONFIGURACIÓN DE BASE DE DATOS
# ============================================
DB_HOST=localhost
DB_PORT=5432
DB_NAME=data_engineering
DB_USER=de_user
DB_PASSWORD=tu_password_aqui

# ============================================
# CONFIGURACIÓN DE API
# ============================================
API_KEY=tu_api_key_aqui
API_URL=https://api.ejemplo.com
API_TIMEOUT=30

# ... más secciones
```

**Ventajas:**
* Otros desarrolladores saben qué variables necesitan
* Documenta la configuración requerida
* Se puede commitear sin exponer secretos
* Organizado por categorías para fácil navegación

> 💡 **Nota**: El archivo `.env` (con tus valores reales) **NO se commitea** al repositorio. Solo el `.env.example` está versionado.

---

## 🔒 Seguridad: Qué NO hacer

### ❌ NO commitees el archivo .env

```bash
# .gitignore debe incluir:
.env
*.env
.env.local
.env.*.local
```

### ❌ NO uses valores por defecto inseguros

```bash
# ❌ MAL
DB_PASSWORD=password
API_KEY=12345
```

### ❌ NO compartas .env por email/chat

Usa gestores de secretos o variables de entorno del sistema.

### ✅ SÍ haz esto

* ✅ Commitea `.env.example` con valores de ejemplo
* ✅ Usa contraseñas fuertes y únicas
* ✅ Rota credenciales regularmente
* ✅ Usa gestores de secretos en producción (AWS Secrets Manager, Azure Key Vault, etc.)

---

## 🎯 Casos de uso comunes en Data Engineering

### 1. Conexión a bases de datos

```bash
# .env
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=analytics
POSTGRES_USER=analyst
POSTGRES_PASSWORD=secure_pass_123
```

```python
# pipeline.py
from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    database=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)
```

### 2. Credenciales de APIs

```bash
# .env
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
S3_BUCKET_NAME=mi-bucket-datos
```

```python
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)
```

### 3. Configuración de pipelines

```bash
# .env
DATA_SOURCE_PATH=/data/raw
DATA_OUTPUT_PATH=/data/processed
LOG_LEVEL=INFO
MAX_WORKERS=4
BATCH_SIZE=1000
```

```python
from dotenv import load_dotenv
import os

load_dotenv()

config = {
    "data_source": os.getenv("DATA_SOURCE_PATH"),
    "data_output": os.getenv("DATA_OUTPUT_PATH"),
    "log_level": os.getenv("LOG_LEVEL", "INFO"),
    "max_workers": int(os.getenv("MAX_WORKERS", "4")),
    "batch_size": int(os.getenv("BATCH_SIZE", "1000"))
}
```

### 4. Diferentes entornos

```bash
# .env.development
ENVIRONMENT=development
DB_HOST=localhost
DEBUG=True

# .env.production
ENVIRONMENT=production
DB_HOST=prod-db.example.com
DEBUG=False
```

```python
import os
from dotenv import load_dotenv

env = os.getenv("ENVIRONMENT", "development")
load_dotenv(f".env.{env}")

# Ahora carga las variables del entorno correcto
```

---

## 🛠️ Buenas prácticas

### 1. Valores por defecto sensatos

```python
# ✅ Con valor por defecto
timeout = int(os.getenv("API_TIMEOUT", "30"))
log_level = os.getenv("LOG_LEVEL", "INFO")
```

### 2. Validar variables críticas

```python
from dotenv import load_dotenv
import os
import sys

load_dotenv()

# Validar que las variables críticas existan
required_vars = ["DB_HOST", "DB_USER", "DB_PASSWORD"]
missing = [var for var in required_vars if not os.getenv(var)]

if missing:
    print(f"Error: Faltan variables de entorno: {', '.join(missing)}")
    sys.exit(1)
```

### 3. Tipos de datos correctos

```python
# Convertir a los tipos correctos
max_workers = int(os.getenv("MAX_WORKERS", "4"))
debug_mode = os.getenv("DEBUG", "False").lower() == "true"
timeout = float(os.getenv("TIMEOUT", "30.0"))
```

### 4. Organizar por secciones

```bash
# .env
# ============================================
# BASE DE DATOS
# ============================================
DB_HOST=localhost
DB_PORT=5432
DB_NAME=data_engineering

# ============================================
# API EXTERNA
# ============================================
API_URL=https://api.ejemplo.com
API_KEY=tu_key_aqui
```

---

## 📚 Integración con otras herramientas

### Airflow

```python
# En tu DAG
from airflow.models import Variable

db_host = Variable.get("DB_HOST")
db_password = Variable.get("DB_PASSWORD", deserialize_json=False)
```

O usa variables de entorno del sistema directamente.

### Docker

```yaml
# docker-compose.yml
services:
  app:
    environment:
      - DB_HOST=${DB_HOST}
      - DB_PASSWORD=${DB_PASSWORD}
    env_file:
      - .env  # Carga todo el archivo .env
```

---

## 🚀 Flujo de trabajo recomendado en este proyecto

### Paso 1: Configurar .env en la raíz

1. **Copia el `.env.example`** de la raíz del proyecto:
   ```bash
   # Desde la raíz del proyecto
   cp .env.example .env
   ```

2. **Edita `.env`** con tus valores reales:
   ```bash
   nano .env  # o tu editor preferido
   ```

3. **Configura las variables que necesites:**
   - Si trabajas con SQL: `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`
   - Si procesas archivos: `DATA_SOURCE_PATH`, `DATA_OUTPUT_PATH`
   - Si usas APIs: `API_KEY`, `API_URL`

### Paso 2: Configurar .env para módulos específicos (opcional)

Para módulos específicos como SQL con Docker, puedes usar el mismo `.env` o crear uno local:

```bash
# Opción 1: Usar el .env de la raíz (recomendado)
# Los scripts Python buscan el .env en la raíz automáticamente

# Opción 2: Crear .env específico para SQL
cd 02_sql
cp ../.env.example .env
# O usa el .env.example específico del módulo si existe
cp .env.example .env
```

### Paso 3: Verificar que funciona

Los ejemplos y scripts del proyecto cargan automáticamente el `.env` desde la raíz:

```python
# Los scripts en 03_python/ejemplos/ buscan automáticamente:
# - .env en la raíz del proyecto (3 niveles arriba)
# - Usan variables como DB_HOST, DB_NAME, DATA_SOURCE_PATH, etc.
```

**Ejemplo de uso en scripts:**
```python
# 03_python/ejemplos/03-conexion-db.py ya está configurado así:
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).parent.parent.parent / '.env'
load_dotenv(env_path)

# Ahora puedes usar:
db_host = os.getenv('DB_HOST', 'localhost')
```

### Importante

- ✅ **El archivo `.env` ya está en `.gitignore`** - no se commitea automáticamente
- ✅ **Solo el `.env.example` está versionado** - sin valores reales
- ✅ **En producción**, usa variables de entorno del sistema o gestores de secretos
- ✅ **Los ejemplos del proyecto** usan estas variables automáticamente

---

## 📝 Checklist

- [ ] Archivo `.env.example` creado y commiteado
- [ ] Archivo `.env` en `.gitignore`
- [ ] Variables documentadas en `.env.example`
- [ ] Valores por defecto sensatos en el código
- [ ] Validación de variables críticas
- [ ] No hay secretos hardcodeados en el código

---

## 🎓 Próximos pasos

* Revisa el ejemplo de Docker en **[02_sql/docker-compose.yml](../02_sql/docker-compose.yml)** que usa `.env`
* Aprende sobre **gestores de secretos** para producción
* Explora **variables de entorno del sistema** como alternativa

---

> **Recuerda**: Los archivos `.env` son para desarrollo local. En producción, usa gestores de secretos profesionales (AWS Secrets Manager, HashiCorp Vault, etc.) o variables de entorno del sistema operativo.
