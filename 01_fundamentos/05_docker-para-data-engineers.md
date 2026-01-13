# Docker para Data Engineers

Docker es una herramienta que permite **empaquetar aplicaciones y sus dependencias en contenedores**, creando entornos consistentes y reproducibles. Para Data Engineers, Docker es esencial para crear pipelines portables y entornos de desarrollo aislados.

> 💡 **No te preocupes**: Este documento es **solo teórico**. No necesitas configurar ni ejecutar nada ahora. Solo lee para entender qué es Docker y cómo se usa en Data Engineering. Cuando llegue el momento de practicar, tendrás guías paso a paso.

---

## 🧠 ¿Por qué Docker es importante en Data Engineering?

En Data Engineering, Docker resuelve problemas comunes:

### Problema: "Funciona en mi máquina"
* Diferentes versiones de Python
* Librerías instaladas globalmente
* Configuraciones del sistema diferentes
* Dependencias conflictivas

### Solución: Contenedores Docker
* **Entorno consistente** en desarrollo, testing y producción
* **Aislamiento** de dependencias entre proyectos
* **Reproducibilidad** garantizada
* **Portabilidad** entre máquinas y servidores

> Docker hace que tu pipeline funcione igual en tu laptop, en CI/CD y en producción.

---

## 🔁 Conceptos fundamentales

### Imagen (Image)
Un **template** que define qué contiene tu aplicación:
* Sistema operativo base
* Librerías y dependencias
* Código de tu aplicación
* Configuraciones

### Contenedor (Container)
Una **instancia ejecutándose** de una imagen:
* Aislado del sistema host
* Tiene su propio sistema de archivos
* Puede tener red propia
* Se puede iniciar, detener y eliminar

### Dockerfile
Un **archivo de texto** que describe cómo construir una imagen:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "pipeline.py"]
```

---

## 📊 Docker en el flujo de Data Engineering

### Desarrollo local
```bash
# Construir imagen
docker build -t mi-pipeline .

# Ejecutar pipeline
docker run mi-pipeline
```

### Testing
```bash
# Ejecutar tests en contenedor
docker run mi-pipeline pytest tests/
```

### Producción
```bash
# Desplegar en servidor
docker run -d --name pipeline-prod mi-pipeline
```

---

## 🛠️ Casos de uso comunes

### 1. Pipeline Python aislado

**Dockerfile:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY src/ ./src/
COPY pipeline.py .

# Ejecutar pipeline
CMD ["python", "pipeline.py"]
```

**Uso:**
```bash
docker build -t data-pipeline .
docker run data-pipeline
```

### 2. Base de datos local para desarrollo

**docker-compose.yml:**
```yaml
version: '3.8'

services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: mydata
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

**Uso:**
```bash
docker-compose up -d  # Iniciar base de datos
docker-compose down   # Detener base de datos
```

### 3. Entorno de desarrollo completo

**docker-compose.yml:**
```yaml
version: '3.8'

services:
  pipeline:
    build: .
    volumes:
      - ./data:/app/data
      - ./src:/app/src
    depends_on:
      - postgres
  
  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: analytics
    ports:
      - "5432:5432"
  
  jupyter:
    image: jupyter/scipy-notebook
    ports:
      - "8888:8888"
    volumes:
      - ./notebooks:/home/jovyan/work
```

---

## 🎯 Comandos Docker esenciales

### Construir y ejecutar
```bash
# Construir imagen
docker build -t nombre-imagen .

# Ejecutar contenedor
docker run nombre-imagen

# Ejecutar con volúmenes (montar carpetas)
docker run -v $(pwd)/data:/app/data nombre-imagen

# Ejecutar en background
docker run -d nombre-imagen
```

### Gestión de contenedores
```bash
# Ver contenedores corriendo
docker ps

# Ver todos los contenedores
docker ps -a

# Detener contenedor
docker stop nombre-contenedor

# Eliminar contenedor
docker rm nombre-contenedor

# Ver logs
docker logs nombre-contenedor
```

### Gestión de imágenes
```bash
# Listar imágenes
docker images

# Eliminar imagen
docker rmi nombre-imagen

# Ver historial de imagen
docker history nombre-imagen
```

### Docker Compose
```bash
# Iniciar servicios
docker-compose up

# Iniciar en background
docker-compose up -d

# Detener servicios
docker-compose down

# Ver logs
docker-compose logs

# Reconstruir imágenes
docker-compose build
```

---

## 💡 Buenas prácticas para Data Engineers

### 1. Usa imágenes base pequeñas
```dockerfile
# ❌ Evita
FROM python:3.11

# ✅ Mejor
FROM python:3.11-slim
```

### 2. Cachea dependencias
```dockerfile
# Copiar requirements primero (capa que cambia menos)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar código después (capa que cambia más)
COPY . .
```

### 3. No incluyas datos en la imagen
```dockerfile
# ❌ No hagas esto
COPY data/ ./data/

# ✅ Usa volúmenes en runtime
docker run -v $(pwd)/data:/app/data mi-pipeline
```

### 4. Usa .dockerignore
Crea un archivo `.dockerignore`:
```
__pycache__/
*.pyc
.env
data/
.git/
*.md
```

### 5. Variables de entorno para configuración
```dockerfile
ENV DB_HOST=localhost
ENV DB_PORT=5432
```

```bash
docker run -e DB_HOST=prod-server mi-pipeline
```

---

## 🔗 Docker en pipelines de datos

### Pipeline con Airflow
```dockerfile
FROM apache/airflow:2.7.0

USER root
RUN pip install pandas sqlalchemy

USER airflow
COPY dags/ /opt/airflow/dags/
```

### Pipeline con Python + dependencias
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY . .

# Ejecutar
CMD ["python", "main.py"]
```

---

## 🚀 Integración con CI/CD

Docker es perfecto para CI/CD:

```yaml
# .github/workflows/pipeline.yml
name: Run Pipeline

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Build image
        run: docker build -t pipeline .
      - name: Run tests
        run: docker run pipeline pytest
      - name: Run pipeline
        run: docker run pipeline python main.py
```

---

## ⚠️ Consideraciones importantes

### Volúmenes para datos
* **No** incluyas datos grandes en imágenes
* **Usa volúmenes** para montar datos en runtime
* **Considera** volúmenes nombrados para persistencia

### Recursos
* Docker consume memoria y CPU
* Ajusta límites si es necesario:
  ```bash
  docker run --memory="512m" --cpus="1.0" mi-pipeline
  ```

### Seguridad
* No incluyas credenciales en imágenes
* Usa variables de entorno o secretos
* Escanea imágenes por vulnerabilidades

---

## ➡️ ¿Qué sigue?

Para continuar:
1. **Revisa [SETUP.md](../../SETUP.md)** y ejecuta la configuración si aún no lo has hecho
   - Incluye instrucciones para instalar Docker
   - Configuración de base de datos local con Docker Compose
   - Todo lo necesario para empezar a practicar
2. **[Introducción a SQL](06_introduccion-sql.md)** - Lenguaje para trabajar con datos estructurados

Para investigar:
1. **Aprende Docker Compose** para orquestar múltiples servicios
2. **Explora** imágenes oficiales (PostgreSQL, Redis, etc.)

---

## 📝 Recursos adicionales

* **Documentación oficial**: [docs.docker.com](https://docs.docker.com)
* **Docker Hub**: [hub.docker.com](https://hub.docker.com) - repositorio de imágenes
* **Best practices**: Revisa las mejores prácticas oficiales de Docker

---

> **Recuerda**: Docker no es solo para DevOps. Como Data Engineer, Docker te ayuda a crear pipelines más confiables, reproducibles y fáciles de desplegar.
