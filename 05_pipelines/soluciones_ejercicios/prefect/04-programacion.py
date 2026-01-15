from prefect import flow, task
from prefect.schedules import Cron, Interval
from datetime import timedelta
import pandas as pd
from pathlib import Path

# Obtener la ruta base del proyecto
BASE_DIR = Path(__file__).parent.parent.parent.parent

@task
def procesar_datos():
    """Simula procesamiento de datos."""
    print("🔄 Procesando datos...")
    # En un caso real, aquí procesarías datos reales
    df = pd.DataFrame({
        'fecha': pd.date_range('2024-01-01', periods=10, freq='D'),
        'valor': [100, 200, 150, 300, 250, 400, 350, 500, 450, 600]
    })
    return df

@task
def guardar_resultado(df, ruta):
    """Guarda el resultado."""
    ruta.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(ruta, index=False)
    print(f"✅ Resultado guardado en {ruta}")

# Ejemplo 1: Flow que puede programarse con cron (diario a medianoche)
# Nota: En Prefect 3.x, el scheduling se configura al crear un deployment
# usando: prefect deploy --cron "0 0 * * *"
@flow
def pipeline_diario():
    """Pipeline que puede ejecutarse diariamente a medianoche."""
    print("📅 Ejecutando pipeline diario...")
    df = procesar_datos()
    ruta = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'datos_diarios.parquet'
    guardar_resultado(df, ruta)
    print("✅ Pipeline diario completado")

# Ejemplo 2: Flow que puede programarse con intervalo (cada hora)
# Nota: En Prefect 3.x, el scheduling se configura al crear un deployment
# usando: prefect deploy --interval 3600
@flow
def pipeline_horario():
    """Pipeline que puede ejecutarse cada hora."""
    print("⏰ Ejecutando pipeline horario...")
    df = procesar_datos()
    ruta = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'datos_horarios.parquet'
    guardar_resultado(df, ruta)
    print("✅ Pipeline horario completado")

# Ejemplo 3: Flow sin programación (ejecución manual)
@flow
def pipeline_manual():
    """Pipeline que se ejecuta manualmente."""
    print("👤 Ejecutando pipeline manual...")
    df = procesar_datos()
    ruta = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'datos_manuales.parquet'
    guardar_resultado(df, ruta)
    print("✅ Pipeline manual completado")

# Ejecutar
if __name__ == '__main__':
    # Para probar, ejecutamos el pipeline manual
    # Los pipelines con schedule se ejecutarán automáticamente cuando
    # el servidor Prefect esté corriendo y el flow esté registrado como deployment
    print("💡 Ejecutando pipeline manual para prueba...")
    print("💡 Para usar scheduling en Prefect 3.x:")
    print("   1. Inicia el servidor: prefect server start")
    print("   2. Crea un deployment con schedule:")
    print("      prefect deploy --cron '0 0 * * *' pipeline_diario")
    print("      prefect deploy --interval 3600 pipeline_horario")
    print()
    
    pipeline_manual()
