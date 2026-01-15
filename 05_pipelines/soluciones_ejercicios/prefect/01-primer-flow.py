from prefect import flow, task
import pandas as pd
from pathlib import Path

# Obtener la ruta base del proyecto (3 niveles arriba desde este archivo)
BASE_DIR = Path(__file__).parent.parent.parent.parent

@task
def extraer(ruta):
    """Extrae datos."""
    return pd.read_csv(ruta)

@task
def transformar(df):
    """Transforma datos."""
    df = df.dropna()
    df['total'] = df['precio'] * df['cantidad']
    return df

@task
def cargar(df, ruta):
    """Carga datos."""
    df.to_parquet(ruta, index=False)

@flow
def pipeline_etl(ruta_entrada, ruta_salida):
    """Pipeline ETL completo."""
    df = extraer(ruta_entrada)
    df = transformar(df)
    cargar(df, ruta_salida)
    print("✅ Pipeline completado")

# Ejecutar
if __name__ == '__main__':
    # Rutas relativas desde la raíz del proyecto
    ruta_entrada = BASE_DIR / '03_python' / 'data' / 'ventas.csv'
    # Outputs se guardan en 05_pipelines/data/output para mejor organización
    ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'ventas_processed.parquet'
    
    # Asegurar que el directorio de salida existe
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    
    pipeline_etl(str(ruta_entrada), str(ruta_salida))
