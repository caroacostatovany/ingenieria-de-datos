#!/bin/bash
# Script para configurar Airflow desde cero
# Uso: bash setup-airflow.sh

set -e

echo "🚀 Configurando Airflow desde cero..."
echo ""

# 1. Obtener ruta absoluta del proyecto
PROJECT_DIR=$(cd "$(dirname "$0")/../../.." && pwd)
AIRFLOW_HOME_ABS="$PROJECT_DIR/05_pipelines/orquestadores/.airflow"

# 2. Configurar variables de entorno (usar ruta absoluta)
export AIRFLOW_HOME="$AIRFLOW_HOME_ABS"
export AIRFLOW__CORE__LOAD_EXAMPLES=False

echo "✅ Variables configuradas:"
echo "   AIRFLOW_HOME=$AIRFLOW_HOME"
echo "   AIRFLOW__CORE__LOAD_EXAMPLES=False"
echo ""

# 3. Crear directorio de Airflow
mkdir -p "$AIRFLOW_HOME"
echo "✅ Directorio creado: $AIRFLOW_HOME"
echo ""

# 4. Crear carpeta dags y symlinks
mkdir -p "$AIRFLOW_HOME/dags"
echo "✅ Carpeta dags creada"
echo ""

# 5. Crear symlinks de los DAGs
echo "📁 Creando symlinks de DAGs..."
ln -sf "$PROJECT_DIR/05_pipelines/ejercicios/airflow"/*.py "$AIRFLOW_HOME/dags/"
echo "✅ Symlinks creados:"
ls -la "$AIRFLOW_HOME/dags"/*.py 2>/dev/null | awk '{print "   " $9 " -> " $11}' || echo "   (No hay archivos .py aún)"
echo ""

# 5. Mostrar instrucciones
echo "🎯 Próximos pasos:"
echo ""
echo "1. Inicia Airflow (usa ruta absoluta):"
echo "   export AIRFLOW_HOME=\"$AIRFLOW_HOME\""
echo "   export AIRFLOW__CORE__LOAD_EXAMPLES=False"
echo "   # macOS: Necesario para evitar errores de fork"
echo "   export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES"
echo "   airflow standalone"
echo ""
echo "   O desde la raíz del proyecto:"
echo "   export AIRFLOW_HOME=\$(pwd)/05_pipelines/orquestadores/.airflow"
echo "   export AIRFLOW__CORE__LOAD_EXAMPLES=False"
echo "   # macOS: Necesario para evitar errores de fork"
echo "   export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES"
echo "   airflow standalone"
echo ""
echo "2. Busca la contraseña en la terminal cuando Airflow inicie"
echo "   (Aparecerá en un mensaje como: 'Login with username: admin | password: ...')"
echo ""
echo "3. O encuentra la contraseña en:"
echo "   cat \"$AIRFLOW_HOME/simple_auth_manager_passwords.json.generated\""
echo ""
echo "4. Accede a: http://localhost:8080"
echo ""
echo "✅ Configuración completada!"
