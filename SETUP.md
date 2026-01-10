# 🛠️ Guía de Configuración Inicial

Esta guía te ayudará a configurar tu entorno de desarrollo para seguir el roadmap de Ingeniería de Datos.

---

## 📋 Requisitos Previos

### Software necesario

* **pyenv** - Gestor de versiones de Python (recomendado) - [Instalar pyenv](https://github.com/pyenv/pyenv#installation)
* **Python 3.8+** - Se instalará con pyenv
* **Git** - [Descargar Git](https://git-scm.com/downloads)
* **Docker Desktop** (opcional pero recomendado) - [Descargar Docker](https://www.docker.com/products/docker-desktop)
* **Cursor IDE** (opcional) - [Descargar Cursor](https://cursor.sh/) - Para usar AI como copiloto

### Verificar instalaciones

```bash
# Verificar pyenv
pyenv --version

# Verificar Python instalado con pyenv
pyenv versions

# Verificar Git
git --version

# Verificar Docker (opcional)
docker --version
docker-compose --version
```

---

## 🚀 Configuración Paso a Paso

> ⚡ **Antes de instalar cosas con `pip`, asegúrate de tener la última versión de pip (opcional pero recomendado):**
```bash
python -m pip install --upgrade pip

[notice] To update, run: python -m pip install --upgrade pip
```

### 1. Clonar el repositorio

```bash
# Clonar el repositorio
git clone https://github.com/USERNAME/REPO.git
cd ingenieria-de-datos

# O si ya lo tienes, actualiza
git pull origin main
```

### 2. Configurar variables de entorno (Opcional para desarrollo local)

```bash
# Copiar archivo de ejemplo
cp .env.example .env
```

> 💡 **Para desarrollo local**: Los valores por defecto en `.env.example` funcionan perfectamente para trabajar localmente. **No necesitas editar nada** por ahora. Solo copia el archivo y ya está listo.

> 📝 **Más adelante**: Si necesitas configurar valores específicos (como credenciales de base de datos, APIs, etc.), puedes editar el archivo `.env`. Lee más sobre `.env` en: **[Archivos .env para Data Engineers](01_fundamentos/04_archivos-env-para-data-engineers.md)**

### 3. ⭐ Opcional: Configurar Cursor para uso de AI

Si quieres usar AI como copiloto durante tu aprendizaje, puedes configurar Cursor:

Sigue la guía completa: **[Cursor para Data Engineers](06_inteligencia_artificial/herramientas/cursor-para-data-engineers.md)**

> 💡 **Nota**: Cursor es completamente opcional. Puedes usar cualquier editor (VS Code, PyCharm, etc.). Si prefieres configurarlo más adelante, está bien.

### 4. Instalar Python con pyenv y crear entorno virtual (Recomendado)

#### 4.1. Instalar pyenv (si no lo tienes)

**macOS/Linux:**
```bash
# Instalar pyenv con Homebrew (macOS)
brew install pyenv

# O con el instalador automático
curl https://pyenv.run | bash

# Agregar a tu shell (agrega estas líneas a ~/.zshrc o ~/.bashrc)
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

# Recargar shell
exec $SHELL
```

**Windows:**
```bash
# Instalar pyenv-win
git clone https://github.com/pyenv-win/pyenv-win.git %USERPROFILE%\.pyenv
```

#### 4.2. Instalar Python con pyenv

```bash
# Ver versiones disponibles de Python
pyenv install --list

# Instalar Python 3.11 (o la versión que prefieras, mínimo 3.8)
pyenv install 3.11.0

# Establecer como versión global (opcional)
pyenv global 3.11.0
```

> 👇 **Antes de establecer la versión local, asegúrate de estar dentro de la carpeta del repositorio "ingenieria-de-datos".**

```bash
# Verifica tu ubicación actual
pwd  # Debería terminar en "ingenieria-de-datos"

# Si NO estás en el directorio correcto, navega primero:
cd ruta/al/directorio/ingenieria-de-datos
```

```bash
# Ahora sí puedes establecer la versión local de Python para este proyecto
pyenv local 3.11.0
```
> 💡 Si tienes dudas, usa `pwd` para confirmar que estás dentro de "ingenieria-de-datos" antes de correr `pyenv local`.

#### 4.3. Instalar pyenv-virtualenv (plugin para entornos virtuales)

**macOS/Linux:**
```bash
# Instalar el plugin
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv

# Agregar a tu shell (agrega esta línea a ~/.zshrc o ~/.bashrc)
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc

# Recargar shell
exec $SHELL
```

**Windows:**
```bash
# pyenv-win incluye virtualenv por defecto
```

#### 4.4. Crear entorno virtual con pyenv-virtualenv

```bash
# Crear entorno virtual (desde la raíz del proyecto)
pyenv virtualenv 3.11.0 ingenieria-de-datos

# Activar entorno virtual
pyenv activate ingenieria-de-datos

# O usar automáticamente cuando entres al directorio (recomendado)
# Crea un archivo .python-version en la raíz del proyecto
# pyenv activará automáticamente el entorno al entrar al directorio
echo "ingenieria-de-datos" > .python-version
```

> 💡 **Tip**: Con `pyenv-virtualenv`, el entorno se activa automáticamente cuando entras al directorio si tienes `.python-version` configurado.

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

# Iniciar PostgreSQL con Docker
docker-compose up -d

# Verificar que está corriendo
docker-compose ps
```

> 💡 **Nota**: Los valores por defecto funcionan perfectamente para desarrollo local. No necesitas editar el `.env` a menos que quieras cambiar puertos o credenciales.

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
3. Verifica que el archivo `.env` existe en la raíz del proyecto: `ls -la .env`

### Error: "ModuleNotFoundError"

**Solución**: 
1. Asegúrate de tener el entorno virtual activado: `pyenv activate ingenieria-de-datos`
2. Verifica que estás usando la versión correcta de Python: `pyenv version`
3. Instala las dependencias: `pip install -r requirements.txt`
4. Verifica que estás en el directorio correcto

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

* **Usa pyenv para gestionar versiones de Python** - facilita cambiar entre versiones
* **Usa pyenv-virtualenv para entornos virtuales** - se activan automáticamente
* **Lee los READMEs** de cada módulo antes de empezar
* **⭐ Opcional: Configura Cursor** - puede ayudarte con AI como copiloto
* **Usa el chat de Cursor** para resolver dudas sobre el contenido

---

## 📞 ¿Necesitas ayuda?

* Revisa los READMEs de cada módulo
* Abre un Issue en GitHub
* Usa el chat de Cursor para preguntas sobre el contenido

---

> **Recuerda**: La configuración inicial puede tomar tiempo, pero una vez lista, todo será más fácil. ¡Vale la pena!
