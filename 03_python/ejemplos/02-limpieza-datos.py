"""
Ejemplo 2: Limpieza de datos

Ejemplo de cómo limpiar un dataset común.
"""

import pandas as pd
import numpy as np

def limpiar_datos(df):
    """Limpia un DataFrame."""
    
    print(f"Datos originales: {len(df)} filas, {len(df.columns)} columnas")
    
    # 1. Eliminar duplicados
    df = df.drop_duplicates()
    print(f"Después de eliminar duplicados: {len(df)} filas")
    
    # 2. Manejar nulos
    # Eliminar columnas con >50% nulos
    umbral = len(df) * 0.5
    df = df.dropna(axis=1, thresh=umbral)
    
    # Rellenar nulos numéricos con mediana
    columnas_numericas = df.select_dtypes(include=[np.number]).columns
    for col in columnas_numericas:
        df[col].fillna(df[col].median(), inplace=True)
    
    # Rellenar nulos de texto con 'Desconocido'
    columnas_texto = df.select_dtypes(include=['object']).columns
    for col in columnas_texto:
        df[col].fillna('Desconocido', inplace=True)
    
    # 3. Normalizar texto
    if 'nombre' in df.columns:
        df['nombre'] = df['nombre'].str.strip().str.title()
    
    if 'email' in df.columns:
        df['email'] = df['email'].str.strip().str.lower()
    
    # 4. Convertir tipos
    if 'fecha' in df.columns:
        df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')
    
    # 5. Eliminar outliers (usando IQR)
    columnas_numericas = df.select_dtypes(include=[np.number]).columns
    for col in columnas_numericas:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR
        df = df[(df[col] >= limite_inferior) & (df[col] <= limite_superior)]
    
    print(f"Datos finales: {len(df)} filas, {len(df.columns)} columnas")
    return df

# Ejemplo de uso
if __name__ == '__main__':
    # Crear datos de ejemplo
    df = pd.DataFrame({
        'nombre': ['  Juan  ', 'María', None, 'Carlos'],
        'email': ['JUAN@EXAMPLE.COM', 'maria@example.com', None, 'carlos@example.com'],
        'edad': [28, 35, None, 150],  # 150 es outlier
        'fecha': ['2024-01-01', '2024-02-01', None, '2024-03-01']
    })
    
    df_limpio = limpiar_datos(df)
    print("\nDatos limpios:")
    print(df_limpio)
