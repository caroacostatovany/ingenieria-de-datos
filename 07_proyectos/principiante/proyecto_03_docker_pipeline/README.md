# Proyecto 3: Pipeline con Docker

Aprende a containerizar un pipeline ETL usando Docker y Docker Compose.

---

## 🎯 Objetivo

Aprender a:
* Crear Dockerfiles para pipelines
* Usar Docker Compose para orquestar servicios
* Containerizar aplicaciones Python
* Gestionar variables de entorno en contenedores

---

## 📋 Requisitos previos

* Docker instalado
* Docker Compose instalado
* Conocimientos básicos de Docker

---

## 🚀 Pasos del proyecto

### 1. Estructura del proyecto

```
proyecto_03_docker_pipeline/
├── README.md
├── docker-compose.yml
├── Dockerfile
├── .env.example
├── requirements.txt
├── src/
│   └── pipeline.py
├── data/
│   └── input/
│       └── datos.csv
└── output/
```

### 2. Crear Dockerfile

`Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copiar requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY src/ ./src/
COPY data/ ./data/

# Ejecutar pipeline
CMD ["python", "src/pipeline.py"]
```

### 3. Crear docker-compose.yml

`docker-compose.yml`:

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: ${DB_NAME}
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER}"]
      interval: 10s
      timeout: 5s
      retries: 5

  pipeline:
    build: .
    environment:
      DB_HOST: postgres
      DB_PORT: 5432
      DB_NAME: ${DB_NAME}
      DB_USER: ${DB_USER}
      DB_PASSWORD: ${DB_PASSWORD}
    depends_on:
      postgres:
        condition: service_healthy
    volumes:
      - ./output:/app/output
    command: python src/pipeline.py
```

### 4. Pipeline simple

`src/pipeline.py`:

```python
import os
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

def run_pipeline():
    print("🚀 Iniciando pipeline containerizado...")
    
    # Conectar a PostgreSQL
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        port=os.getenv('DB_PORT', '5432'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
    
    # Leer datos
    df = pd.read_csv('data/input/datos.csv')
    print(f"✅ Leídos {len(df)} registros")
    
    # Transformar (ejemplo simple)
    df['processed'] = True
    
    # Cargar a PostgreSQL
    cursor = conn.cursor()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS datos_procesados (
            id SERIAL PRIMARY KEY,
            columna1 VARCHAR(100),
            columna2 INTEGER,
            processed BOOLEAN,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    execute_values(
        cursor,
        "INSERT INTO datos_procesados (columna1, columna2, processed) VALUES %s",
        [(row['columna1'], row['columna2'], row['processed']) for _, row in df.iterrows()]
    )
    
    conn.commit()
    print("✅ Pipeline completado!")
    
    cursor.close()
    conn.close()

if __name__ == "__main__":
    run_pipeline()
```

### 5. Archivos de configuración

`.env.example`:

```env
DB_NAME=data_engineering
DB_USER=de_user
DB_PASSWORD=de_password
```

`requirements.txt`:

```
pandas==2.0.3
psycopg2-binary==2.9.9
python-dotenv==1.0.0
```

### 6. Ejecutar pipeline

```bash
# Copiar .env
cp .env.example .env

# Construir y ejecutar
docker-compose up --build

# Ver logs
docker-compose logs -f pipeline

# Detener servicios
docker-compose down
```

---

## ✅ Checklist de completado

- [ ] Dockerfile creado y funcionando
- [ ] docker-compose.yml configurado
- [ ] Pipeline containerizado ejecutándose
- [ ] Variables de entorno funcionando
- [ ] Volúmenes configurados correctamente
- [ ] Health checks implementados

---

## 🎓 Conceptos aprendidos

* ✅ Containerización de aplicaciones Python
* ✅ Docker Compose para orquestación
* ✅ Variables de entorno en contenedores
* ✅ Volúmenes para persistencia
* ✅ Health checks
* ✅ Dependencias entre servicios

---

## 🚀 Próximo paso

Después de completar este proyecto:
* Agrega más servicios (Redis, Airflow)
* Implementa logging en contenedores
* Avanza a **[Proyectos Intermedios](../../intermedio/)**

---

> **Recuerda**: Docker hace que tus pipelines sean reproducibles. Aprende a usarlo bien.
