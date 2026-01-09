# 🛠️ Guía de Configuración Inicial

Esta guía te ayudará a configurar tu entorno de desarrollo para seguir el roadmap de Ingeniería de Datos.

---

## 📋 Requisitos Previos

### Software necesario

* **Python 3.8+** - [Descargar Python](https://www.python.org/downloads/)
* **Git** - [Descargar Git](https://git-scm.com/downloads)
* **Docker Desktop** (opcional pero recomendado) - [Descargar Docker](https://www.docker.com/products/docker-desktop)
* **Cursor IDE** (recomendado) - [Descargar Cursor](https://cursor.sh/)

### Verificar instalaciones

```bash
# Verificar Python
python --version  # Debe ser 3.8 o superior
# o
python3 --version

# Verificar Git
git --version

# Verificar Docker (opcional)
docker --version
docker-compose --version
```

---

## 🚀 Configuración Paso a Paso

### 1. Clonar el repositorio

```bash
# Clonar el repositorio
git clone https://github.com/USERNAME/REPO.git
cd ingenieria-de-datos

# O si ya lo tienes, actualiza
git pull origin main
```

### 2. Configurar Cursor (Recomendado - PRIMERO)

**⚠️ IMPORTANTE**: Configura Cursor ANTES de continuar. Te ayudará durante todo el aprendizaje.

Sigue la guía completa: **[Cursor para Data Engineers](06_inteligencia_artificial/herramientas/cursor-para-data-engineers.md)**

### 3. Configurar variables de entorno

```bash
# Copiar archivo de ejemplo
cp .env.example .env

# Editar con tus valores
nano .env  # o tu editor preferido
```

Lee más sobre `.env` en: **[Archivos .env para Data Engineers](01_fundamentos/04_archivos-env-para-data-engineers.md)**

### 4. Crear entorno virtual de Python (Recomendado)

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En macOS/Linux:
source venv/bin/activate

# En Windows:
venv\Scripts\activate
```

### 5. Instalar dependencias

```bash
# Instalar todas las dependencias principales
pip install -r requirements.txt

# O instalar solo lo que necesites según el módulo:
# Para SQL:
pip install psycopg2-binary python-dotenv sqlalchemy

# Para Python/Pandas:
pip install pandas numpy matplotlib seaborn python-dotenv

# Para Jupyter Notebooks:
pip install jupyter jupyterlab ipykernel

# Para Calidad de Datos:
pip install great-expectations pandera

# Para Pipelines:
pip install prefect  # o apache-airflow
```

### 6. Configurar base de datos local (Opcional)

Si vas a trabajar con SQL:

```bash
cd 02_sql

# Copiar configuración
cp ../.env.example .env

# Iniciar PostgreSQL con Docker
docker-compose up -d

# Verificar que está corriendo
docker-compose ps
```

Lee más en: **[README-DOCKER.md](02_sql/README-DOCKER.md)**

---

## ✅ Verificar que todo funciona

### Test 1: Python y dependencias

```bash
python -c "import pandas; import psycopg2; print('✅ Dependencias básicas OK')"
```

### Test 2: Docker (si lo instalaste)

```bash
docker ps
```

### Test 3: Jupyter (si lo instalaste)

```bash
jupyter --version
```

### Test 4: Base de datos (si configuraste Docker)

```bash
cd 02_sql
docker-compose ps
# Deberías ver PostgreSQL y pgAdmin corriendo
```

---

## 📚 Próximos Pasos

Una vez configurado todo:

1. **Lee** [¿Qué es Data Engineering?](00_introduccion/que-es-data-engineering.md)
2. **Revisa** el [Roadmap](00_introduccion/roadmap-data-engineer.md)
3. **Sigue** el orden sugerido en el roadmap
4. **Practica** con los ejercicios y proyectos

---

## 🐛 Problemas Comunes

### Error: "python: command not found"

**Solución**: Usa `python3` en lugar de `python`, o configura un alias.

### Error: "pip: command not found"

**Solución**: 
```bash
python -m pip install --upgrade pip
# o
python3 -m pip install --upgrade pip
```

### Error al conectar a PostgreSQL

**Solución**: 
1. Verifica que Docker esté corriendo: `docker ps`
2. Verifica que los contenedores estén activos: `cd 02_sql && docker-compose ps`
3. Revisa el archivo `.env` en `02_sql/`

### Error: "ModuleNotFoundError"

**Solución**: 
1. Asegúrate de tener el entorno virtual activado
2. Instala las dependencias: `pip install -r requirements.txt`
3. Verifica que estás en el directorio correcto

### Jupyter no inicia

**Solución**:
```bash
# Reinstalar Jupyter
pip install --upgrade jupyter jupyterlab

# O usar JupyterLab
jupyter lab
```

---

## 💡 Tips

* **Usa entornos virtuales** para cada proyecto
* **Lee los READMEs** de cada módulo antes de empezar
* **Configura Cursor primero** - te ahorrará mucho tiempo
* **Usa el chat de Cursor** para resolver dudas sobre el contenido

---

## 📞 ¿Necesitas ayuda?

* Revisa los READMEs de cada módulo
* Abre un Issue en GitHub
* Usa el chat de Cursor para preguntas sobre el contenido

---

> **Recuerda**: La configuración inicial puede tomar tiempo, pero una vez lista, todo será más fácil. ¡Vale la pena!
