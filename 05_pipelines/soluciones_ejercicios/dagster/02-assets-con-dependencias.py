from dagster import asset, AssetExecutionContext, Definitions
import pandas as pd
from pathlib import Path
import time

# Obtener la ruta base del proyecto (3 niveles arriba desde este archivo)
BASE_DIR = Path(__file__).parent.parent.parent.parent

# ============================================
# ASSETS QUE SE EJECUTAN EN PARALELO
# ============================================

@asset
def productos_raw(context: AssetExecutionContext):
    """Asset: productos sin procesar (se ejecuta en paralelo con ventas_raw)."""
    context.log.info("Extrayendo productos...")
    time.sleep(1)  # Simular trabajo
    ruta = BASE_DIR / '03_python' / 'data' / 'productos.csv'
    df = pd.read_csv(ruta)
    context.log.info(f"Extraídos {len(df)} productos")
    return df

@asset
def ventas_raw(context: AssetExecutionContext):
    """Asset: ventas sin procesar (se ejecuta en paralelo con productos_raw)."""
    context.log.info("Extrayendo ventas...")
    time.sleep(1)  # Simular trabajo
    ruta = BASE_DIR / '03_python' / 'data' / 'ventas.csv'
    df = pd.read_csv(ruta)
    context.log.info(f"Extraídas {len(df)} ventas")
    return df

# ============================================
# ASSETS CON DEPENDENCIAS SECUENCIALES
# ============================================

@asset
def productos_procesados(context: AssetExecutionContext, productos_raw):
    """Asset: productos procesados (depende de productos_raw)."""
    context.log.info("Procesando productos...")
    df = productos_raw.copy()
    df = df.dropna()
    
    # Guardar output
    ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'productos_procesados.parquet'
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(ruta_salida, index=False)
    context.log.info(f"Guardado en {ruta_salida}")
    
    return df

@asset
def ventas_procesadas(context: AssetExecutionContext, ventas_raw):
    """Asset: ventas procesadas (depende de ventas_raw)."""
    context.log.info("Procesando ventas...")
    df = ventas_raw.copy()
    df = df.dropna()
    df['total'] = df['precio'] * df['cantidad']
    
    # Guardar output
    ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'ventas_procesadas.parquet'
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(ruta_salida, index=False)
    context.log.info(f"Guardado en {ruta_salida}")
    
    return df

# ============================================
# ASSET QUE DEPENDE DE MÚLTIPLES ASSETS
# ============================================

@asset
def ventas_completas(context: AssetExecutionContext, productos_procesados, ventas_procesadas):
    """Asset: ventas completas con información de productos (depende de ambos)."""
    context.log.info("Combinando ventas y productos...")
    
    # Merge de ventas y productos
    df_completo = pd.merge(
        ventas_procesadas,
        productos_procesados,
        left_on='producto_id',
        right_on='id',
        how='left',
        suffixes=('_venta', '_producto')
    )
    
    # Guardar output
    ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'ventas_completas.parquet'
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    df_completo.to_parquet(ruta_salida, index=False)
    context.log.info(f"Guardado en {ruta_salida}")
    context.log.info(f"Total de registros: {len(df_completo)}")
    
    return df_completo

@asset
def resumen_ventas(context: AssetExecutionContext, ventas_completas):
    """Asset: resumen de ventas (depende de ventas_completas)."""
    context.log.info("Generando resumen de ventas...")
    
    resumen = {
        'total_ventas': len(ventas_completas),
        'total_ingresos': ventas_completas['total'].sum(),
        'ventas_por_categoria': ventas_completas.groupby('categoria')['total'].sum().to_dict()
    }
    
    # Guardar output
    ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'resumen_ventas.json'
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    
    import json
    with open(ruta_salida, 'w') as f:
        json.dump(resumen, f, indent=2)
    
    context.log.info(f"Resumen guardado en {ruta_salida}")
    context.log.info(f"Total ingresos: ${resumen['total_ingresos']:,.2f}")
    
    return resumen

# Definiciones necesarias para que Dagster reconozca los assets
defs = Definitions(
    assets=[
        # Assets que se ejecutan en paralelo
        productos_raw,
        ventas_raw,
        # Assets con dependencias secuenciales
        productos_procesados,
        ventas_procesadas,
        # Assets que dependen de múltiples assets
        ventas_completas,
        resumen_ventas,
    ]
)
