from dagster import (
    asset,
    AssetExecutionContext,
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    AssetSelection
)
import pandas as pd
from pathlib import Path
from datetime import datetime

# Obtener la ruta base del proyecto (3 niveles arriba desde este archivo)
BASE_DIR = Path(__file__).parent.parent.parent.parent

# ============================================
# ASSETS
# ============================================

@asset
def ventas_diarias(context: AssetExecutionContext):
    """Asset: ventas procesadas por día."""
    context.log.info("Procesando ventas diarias...")
    ruta = BASE_DIR / '03_python' / 'data' / 'ventas.csv'
    df = pd.read_csv(ruta)
    df = df.dropna()
    df['total'] = df['precio'] * df['cantidad']
    df['fecha'] = pd.to_datetime(datetime.now().date())
    
    # Guardar output
    ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'ventas_diarias.parquet'
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(ruta_salida, index=False)
    context.log.info(f"Ventas diarias guardadas en {ruta_salida}")
    
    return df

@asset
def reporte_ventas(context: AssetExecutionContext, ventas_diarias):
    """Asset: reporte agregado de ventas (depende de ventas_diarias)."""
    context.log.info("Generando reporte de ventas...")
    
    reporte = {
        'fecha': datetime.now().strftime('%Y-%m-%d'),
        'total_ventas': len(ventas_diarias),
        'total_ingresos': float(ventas_diarias['total'].sum()),
        'promedio_por_venta': float(ventas_diarias['total'].mean()),
        'ventas_por_categoria': ventas_diarias.groupby('categoria')['total'].sum().to_dict()
    }
    
    # Guardar output
    ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'reporte_ventas.json'
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    
    import json
    with open(ruta_salida, 'w') as f:
        json.dump(reporte, f, indent=2, default=str)
    
    context.log.info(f"Reporte guardado en {ruta_salida}")
    context.log.info(f"Total ingresos: ${reporte['total_ingresos']:,.2f}")
    
    return reporte

# ============================================
# JOBS
# ============================================

# Job 1: Procesar solo ventas diarias
procesar_ventas_job = define_asset_job(
    name="procesar_ventas",
    description="Job para procesar ventas diarias",
    selection=AssetSelection.assets(ventas_diarias)
)

# Job 2: Procesar ventas y generar reporte completo
reporte_completo_job = define_asset_job(
    name="reporte_completo",
    description="Job para procesar ventas y generar reporte completo",
    selection=AssetSelection.assets(ventas_diarias, reporte_ventas)
)

# ============================================
# SCHEDULES
# ============================================

# Schedule 1: Ejecutar diariamente a las 00:00 (medianoche)
schedule_diario = ScheduleDefinition(
    job=procesar_ventas_job,
    cron_schedule="0 0 * * *",  # Diario a medianoche
    name="procesar_ventas_diario"
)

# Schedule 2: Ejecutar cada hora
schedule_horario = ScheduleDefinition(
    job=procesar_ventas_job,
    cron_schedule="0 * * * *",  # Cada hora
    name="procesar_ventas_horario"
)

# Schedule 3: Ejecutar reporte completo diariamente a las 6:00 AM
schedule_reporte_diario = ScheduleDefinition(
    job=reporte_completo_job,
    cron_schedule="0 6 * * *",  # Diario a las 6 AM
    name="reporte_completo_diario"
)

# ============================================
# DEFINITIONS
# ============================================

defs = Definitions(
    assets=[ventas_diarias, reporte_ventas],
    jobs=[procesar_ventas_job, reporte_completo_job],
    schedules=[schedule_diario, schedule_horario, schedule_reporte_diario]
)
