from dagster import asset, AssetExecutionContext, Definitions
import pandas as pd
from pathlib import Path

# Obtener la ruta base del proyecto (3 niveles arriba desde este archivo)
BASE_DIR = Path(__file__).parent.parent.parent.parent

@asset
def ventas_raw(context: AssetExecutionContext):
    """Asset: datos de ventas sin procesar."""
    context.log.info("Extrayendo ventas...")
    ruta = BASE_DIR / '03_python' / 'data' / 'ventas.csv'
    df = pd.read_csv(ruta)
    context.log.info(f"Extraídas {len(df)} ventas")
    return df

@asset
def ventas_procesadas(context: AssetExecutionContext, ventas_raw):
    """Asset: ventas procesadas (depende de ventas_raw)."""
    context.log.info("Procesando ventas...")
    df = ventas_raw.copy()
    df = df.dropna()
    df['total'] = df['precio'] * df['cantidad']
    
    # Guardar output en 05_pipelines/data/output
    ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'ventas_procesadas.parquet'
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(ruta_salida, index=False)
    context.log.info(f"Guardado en {ruta_salida}")
    
    return df

@asset
def ventas_por_categoria(context: AssetExecutionContext, ventas_procesadas):
    """Asset: ventas agregadas por categoría."""
    context.log.info("Agregando por categoría...")
    resultado = ventas_procesadas.groupby('categoria')['total'].sum()
    
    # Guardar output
    ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'ventas_por_categoria.parquet'
    resultado.to_frame().to_parquet(ruta_salida)
    context.log.info(f"Guardado en {ruta_salida}")
    
    return resultado

# Definiciones necesarias para que Dagster reconozca los assets
defs = Definitions(assets=[ventas_raw, ventas_procesadas, ventas_por_categoria])
