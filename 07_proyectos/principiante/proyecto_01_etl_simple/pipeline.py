"""
Pipeline ETL Simple - Ejemplo Funcional

Este pipeline demuestra los conceptos básicos de ETL:
- Extract: Lee datos de un archivo CSV
- Transform: Limpia, transforma y calcula métricas
- Load: Guarda los datos transformados en CSV y Parquet

Uso:
    python pipeline.py
"""

import os
import pandas as pd
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# Cargar variables de entorno (opcional)
# Busca .env en la raíz del proyecto o usa valores por defecto
env_path = Path(__file__).parent.parent.parent.parent / '.env'
if env_path.exists():
    load_dotenv(env_path)

# Configuración de rutas
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / 'data'
OUTPUT_DIR = BASE_DIR / 'output'

# Crear directorio de salida si no existe
OUTPUT_DIR.mkdir(exist_ok=True)


def extract(file_path: str) -> pd.DataFrame:
    """
    Extrae datos de un archivo CSV.
    
    Args:
        file_path: Ruta al archivo CSV
        
    Returns:
        DataFrame con los datos extraídos
        
    Raises:
        FileNotFoundError: Si el archivo no existe
    """
    print(f"📥 Extrayendo datos de {file_path}...")
    
    try:
        df = pd.read_csv(file_path)
        print(f"✅ Extraídos {len(df)} registros")
        print(f"   Columnas: {', '.join(df.columns)}")
        return df
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo {file_path}")
        raise
    except Exception as e:
        print(f"❌ Error al extraer datos: {e}")
        raise


def transform(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforma y limpia los datos.
    
    Operaciones:
    - Convierte fechas a formato datetime
    - Calcula total por venta
    - Elimina duplicados
    - Elimina registros con valores nulos críticos
    - Agrega columna de mes para análisis
    
    Args:
        df: DataFrame con datos sin transformar
        
    Returns:
        DataFrame transformado y limpio
    """
    print("🔄 Transformando datos...")
    
    # Crear copia para no modificar el original
    df_transformed = df.copy()
    
    # 1. Convertir fecha a datetime
    df_transformed['fecha'] = pd.to_datetime(df_transformed['fecha'])
    
    # 2. Calcular total por venta
    df_transformed['total'] = df_transformed['precio'] * df_transformed['cantidad']
    
    # 3. Agregar columna de mes para análisis
    df_transformed['mes'] = df_transformed['fecha'].dt.to_period('M')
    
    # 4. Eliminar duplicados
    registros_antes = len(df_transformed)
    df_transformed = df_transformed.drop_duplicates()
    registros_despues = len(df_transformed)
    if registros_antes != registros_despues:
        print(f"   ⚠️  Eliminados {registros_antes - registros_despues} duplicados")
    
    # 5. Eliminar registros con valores nulos en columnas críticas
    columnas_criticas = ['fecha', 'producto', 'cantidad', 'precio']
    registros_antes = len(df_transformed)
    df_transformed = df_transformed.dropna(subset=columnas_criticas)
    registros_despues = len(df_transformed)
    if registros_antes != registros_despues:
        print(f"   ⚠️  Eliminados {registros_antes - registros_despues} registros con valores nulos")
    
    # 6. Filtrar registros con total válido (mayor a 0)
    df_transformed = df_transformed[df_transformed['total'] > 0]
    
    # 7. Ordenar por fecha
    df_transformed = df_transformed.sort_values('fecha')
    
    print(f"✅ Transformación completada: {len(df_transformed)} registros válidos")
    print(f"   Total de ventas: €{df_transformed['total'].sum():.2f}")
    
    return df_transformed


def load(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Guarda los datos transformados en diferentes formatos.
    
    Args:
        df: DataFrame con datos transformados
        output_dir: Directorio donde guardar los archivos
    """
    print("💾 Guardando datos transformados...")
    
    # Timestamp para nombres únicos
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # 1. Guardar en CSV
    csv_path = output_dir / f'ventas_transformadas_{timestamp}.csv'
    df.to_csv(csv_path, index=False)
    print(f"   ✅ CSV guardado: {csv_path}")
    
    # 2. Guardar en Parquet (formato más eficiente)
    parquet_path = output_dir / f'ventas_transformadas_{timestamp}.parquet'
    df.to_parquet(parquet_path, index=False)
    print(f"   ✅ Parquet guardado: {parquet_path}")
    
    # 3. Guardar resumen de ventas por producto
    resumen = df.groupby('producto').agg({
        'cantidad': 'sum',
        'total': 'sum',
        'precio': 'mean'
    }).round(2)
    resumen.columns = ['cantidad_total', 'ventas_totales', 'precio_promedio']
    resumen_path = output_dir / f'resumen_ventas_{timestamp}.csv'
    resumen.to_csv(resumen_path)
    print(f"   ✅ Resumen guardado: {resumen_path}")
    
    print("✅ Pipeline completado exitosamente!")


def main():
    """
    Función principal que ejecuta el pipeline ETL completo.
    """
    print("=" * 60)
    print("🚀 Pipeline ETL Simple - Ejecutando...")
    print("=" * 60)
    
    # Rutas de archivos
    input_file = DATA_DIR / 'ventas.csv'
    
    # Validar que existe el archivo de entrada
    if not input_file.exists():
        print(f"❌ Error: No se encontró el archivo {input_file}")
        print(f"   Asegúrate de que el archivo existe en: {DATA_DIR}")
        return
    
    try:
        # Extract
        df_raw = extract(str(input_file))
        
        # Transform
        df_transformed = transform(df_raw)
        
        # Load
        load(df_transformed, OUTPUT_DIR)
        
        print("\n" + "=" * 60)
        print("✨ Pipeline ejecutado exitosamente!")
        print(f"📁 Archivos de salida en: {OUTPUT_DIR}")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Error en el pipeline: {e}")
        raise


if __name__ == '__main__':
    main()
