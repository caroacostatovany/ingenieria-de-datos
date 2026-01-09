# Proyecto 2: Pipeline en Producción Local

Aprende a configurar un entorno de producción local completo con CI/CD, monitoreo y alertas.

---

## 🎯 Objetivo

Aprender a:
* Configurar entorno de producción local
* Implementar CI/CD básico
* Configurar monitoreo y logging
* Implementar alertas
* Gestionar configuración de producción

---

## 📋 Requisitos previos

* Docker y Docker Compose
* Conocimientos de Git
* Conocimientos de Linux básico
* Entendimiento de conceptos de producción

---

## 🚀 Pasos del proyecto

### 1. Estructura del proyecto

```
proyecto_02_produccion_local/
├── README.md
├── docker-compose.prod.yml
├── .github/
│   └── workflows/
│       └── ci.yml
├── scripts/
│   ├── deploy.sh
│   └── health_check.sh
├── monitoring/
│   └── prometheus.yml
├── src/
│   └── pipeline.py
└── config/
    └── production.env
```

### 2. Docker Compose para producción

`docker-compose.prod.yml`:

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: ${DB_NAME}
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER}"]
      interval: 10s
      timeout: 5s
      retries: 5

  pipeline:
    build: .
    environment:
      - DB_HOST=postgres
      - ENV=production
      - LOG_LEVEL=INFO
    depends_on:
      postgres:
        condition: service_healthy
    restart: unless-stopped
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"

  prometheus:
    image: prom/prometheus
    volumes:
      - ./monitoring/prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus
    ports:
      - "9090:9090"
    restart: unless-stopped

volumes:
  postgres_data:
  prometheus_data:
```

### 3. Pipeline con logging robusto

`src/pipeline.py`:

```python
import logging
import os
from datetime import datetime
from pathlib import Path

# Configurar logging
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

logging.basicConfig(
    level=os.getenv('LOG_LEVEL', 'INFO'),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_dir / f"pipeline_{datetime.now().strftime('%Y%m%d')}.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def run_pipeline():
    logger.info("🚀 Iniciando pipeline en producción")
    
    try:
        # Tu lógica de pipeline aquí
        logger.info("✅ Pipeline completado exitosamente")
        return True
    except Exception as e:
        logger.error(f"❌ Error en pipeline: {e}", exc_info=True)
        # Enviar alerta (email, Slack, etc.)
        send_alert(f"Pipeline falló: {e}")
        return False

def send_alert(message: str):
    """Envía alerta (implementar según necesidad)."""
    logger.critical(f"ALERTA: {message}")
    # Aquí podrías integrar con:
    # - Email (SMTP)
    # - Slack webhook
    # - PagerDuty
    # - etc.

if __name__ == "__main__":
    success = run_pipeline()
    exit(0 if success else 1)
```

### 4. Script de deployment

`scripts/deploy.sh`:

```bash
#!/bin/bash

set -e  # Salir si hay error

echo "🚀 Iniciando deployment..."

# Verificar que estamos en la rama correcta
BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [ "$BRANCH" != "main" ]; then
    echo "❌ Error: Debes estar en la rama main"
    exit 1
fi

# Pull últimos cambios
git pull origin main

# Construir imágenes
docker-compose -f docker-compose.prod.yml build

# Detener servicios actuales
docker-compose -f docker-compose.prod.yml down

# Iniciar servicios
docker-compose -f docker-compose.prod.yml up -d

# Health check
./scripts/health_check.sh

echo "✅ Deployment completado"
```

### 5. Health check

`scripts/health_check.sh`:

```bash
#!/bin/bash

MAX_RETRIES=5
RETRY_COUNT=0

while [ $RETRY_COUNT -lt $MAX_RETRIES ]; do
    if docker-compose -f docker-compose.prod.yml ps | grep -q "Up"; then
        echo "✅ Servicios saludables"
        exit 0
    fi
    
    RETRY_COUNT=$((RETRY_COUNT + 1))
    echo "⏳ Esperando servicios... ($RETRY_COUNT/$MAX_RETRIES)"
    sleep 5
done

echo "❌ Health check falló"
exit 1
```

### 6. CI/CD con GitHub Actions

`.github/workflows/ci.yml`:

```yaml
name: CI Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pytest pytest-cov
    
    - name: Run tests
      run: pytest tests/ --cov=src --cov-report=xml
    
    - name: Lint
      run: |
        pip install flake8
        flake8 src/ --count --select=E9,F63,F7,F82 --show-source --statistics

  build:
    needs: test
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Build Docker image
      run: docker build -t pipeline:latest .
```

### 7. Monitoreo con Prometheus

`monitoring/prometheus.yml`:

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'pipeline'
    static_configs:
      - targets: ['pipeline:8000']
```

### 8. Configuración de producción

`config/production.env`:

```env
ENV=production
LOG_LEVEL=INFO
DB_HOST=postgres
DB_NAME=data_engineering
DB_USER=de_user
DB_PASSWORD=secure_password_here
```

---

## ✅ Checklist de completado

- [ ] Docker Compose para producción configurado
- [ ] Logging robusto implementado
- [ ] Scripts de deployment creados
- [ ] Health checks funcionando
- [ ] CI/CD configurado
- [ ] Monitoreo básico implementado
- [ ] Alertas configuradas
- [ ] Documentación de producción completa

---

## 🎓 Conceptos aprendidos

* ✅ Configuración de producción
* ✅ CI/CD básico
* ✅ Logging y monitoreo
* ✅ Health checks
* ✅ Deployment automatizado
* ✅ Gestión de configuración

---

## 🚀 Próximo paso

Después de completar este proyecto:
* Agrega más servicios de monitoreo (Grafana)
* Implementa rollback automático
* Avanza a **[Proyecto 3: Cloud Gratis](../proyecto_03_cloud_gratis/)**

---

> **Recuerda**: La producción requiere atención a detalles. Prueba todo antes de desplegar.
