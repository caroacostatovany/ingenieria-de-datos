"""
Ejemplo 4: Procesar archivos grandes

Técnicas para procesar archivos que no caben en memoria.
"""

import pandas as pd

def procesar_csv_grande(ruta_entrada, ruta_salida, chunk_size=10000):
    """
    Procesa un CSV grande en chunks.
    
    Args:
        ruta_entrada: Ruta al CSV grande
        ruta_salida: Ruta donde guardar resultado
        chunk_size: Tamaño de cada chunk
    """
    chunks_procesados = []
    total_filas = 0
    
    print(f"Procesando {ruta_entrada} en chunks de {chunk_size}...")
    
    # Procesar por chunks
    for i, chunk in enumerate(pd.read_csv(ruta_entrada, chunksize=chunk_size)):
        print(f"Procesando chunk {i+1}...")
        
        # Transformar chunk
        chunk = chunk.dropna()
        chunk['total'] = chunk['precio'] * chunk['cantidad']
        chunk = chunk[chunk['total'] > 0]
        
        chunks_procesados.append(chunk)
        total_filas += len(chunk)
    
    # Combinar resultados
    print("Combinando chunks...")
    df_final = pd.concat(chunks_procesados, ignore_index=True)
    
    # Guardar
    print(f"Guardando {len(df_final)} filas en {ruta_salida}...")
    df_final.to_parquet(ruta_salida, index=False)
    
    print(f"Procesamiento completado. Total: {total_filas} filas procesadas")
    return df_final

def procesar_parquet_con_filtros(ruta_entrada, ruta_salida):
    """
    Procesa Parquet usando filtros pushdown (más eficiente).
    """
    # Parquet permite filtros pushdown
    df = pd.read_parquet(
        ruta_entrada,
        filters=[('fecha', '>=', '2024-01-01')]  # Solo lee datos relevantes
    )
    
    # Procesar
    df = df[df['total'] > 100]
    
    # Guardar
    df.to_parquet(ruta_salida, index=False)
    return df

# Ejemplo de uso
if __name__ == '__main__':
    # Procesar CSV grande
    # procesar_csv_grande('data/raw/ventas_grandes.csv', 'data/processed/ventas_procesadas.parquet')
    
    print("Este ejemplo muestra cómo procesar archivos grandes.")
    print("Ajusta las rutas según tus archivos.")
