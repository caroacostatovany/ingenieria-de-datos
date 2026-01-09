"""
Ejemplo 1: Pipeline ETL simple

Este ejemplo muestra un pipeline ETL básico:
- Extract: Lee datos de CSV
- Transform: Limpia y transforma
- Load: Guarda en Parquet
"""

import pandas as pd
from datetime import datetime

def extract(ruta_entrada):
    """Extrae datos de un archivo CSV."""
    print(f"Extrayendo datos de {ruta_entrada}...")
    df = pd.read_csv(ruta_entrada)
    print(f"Extraídos {len(df)} registros")
    return df

def transform(df):
    """Transforma y limpia los datos."""
    print("Transformando datos...")
    
    # Limpiar
    df = df.dropna()
    df = df.drop_duplicates()
    
    # Transformar
    df['fecha'] = pd.to_datetime(df['fecha'])
    df['total'] = df['precio'] * df['cantidad']
    
    # Filtrar
    df = df[df['total'] > 0]
    
    print(f"Quedan {len(df)} registros después de transformación")
    return df

def load(df, ruta_salida):
    """Carga datos transformados."""
    print(f"Guardando en {ruta_salida}...")
    df.to_parquet(ruta_salida, index=False)
    print("Pipeline completado exitosamente")

def main():
    """Ejecuta el pipeline ETL."""
    ruta_entrada = 'data/raw/ventas.csv'
    ruta_salida = 'data/processed/ventas_limpias.parquet'
    
    # Pipeline
    df = extract(ruta_entrada)
    df = transform(df)
    load(df, ruta_salida)

if __name__ == '__main__':
    main()
