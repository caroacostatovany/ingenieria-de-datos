"""
Pipeline ETL completo con Luigi
"""
import luigi
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent.parent

class ExtraerVentas(luigi.Task):
    """Extrae datos de ventas."""
    
    def output(self):
        ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'ventas_extraidas.csv'
        ruta_salida.parent.mkdir(parents=True, exist_ok=True)
        return luigi.LocalTarget(str(ruta_salida))
    
    def run(self):
        print("📥 Extrayendo ventas...")
        ruta_entrada = BASE_DIR / '03_python' / 'data' / 'ventas.csv'
        df = pd.read_csv(ruta_entrada)
        df.to_csv(self.output().path, index=False)
        print(f"✅ Extraídas {len(df)} ventas")

class ExtraerProductos(luigi.Task):
    """Extrae datos de productos."""
    
    def output(self):
        ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'productos_extraidos.csv'
        ruta_salida.parent.mkdir(parents=True, exist_ok=True)
        return luigi.LocalTarget(str(ruta_salida))
    
    def run(self):
        print("📥 Extrayendo productos...")
        ruta_entrada = BASE_DIR / '03_python' / 'data' / 'productos.csv'
        df = pd.read_csv(ruta_entrada)
        df.to_csv(self.output().path, index=False)
        print(f"✅ Extraídos {len(df)} productos")

class TransformarDatos(luigi.Task):
    """Transforma y combina datos de ventas y productos."""
    
    def requires(self):
        return {
            'ventas': ExtraerVentas(),
            'productos': ExtraerProductos()
        }
    
    def output(self):
        ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'datos_transformados.parquet'
        ruta_salida.parent.mkdir(parents=True, exist_ok=True)
        return luigi.LocalTarget(str(ruta_salida))
    
    def run(self):
        print("🔄 Transformando y combinando datos...")
        df_ventas = pd.read_csv(self.input()['ventas'].path)
        df_productos = pd.read_csv(self.input()['productos'].path)
        
        # Merge por nombre de producto
        df = df_ventas.merge(df_productos, on='producto', how='left')
        
        # Transformaciones
        df = df.dropna()
        df['total'] = df['precio'] * df['cantidad']
        df['margen'] = df['precio'] - df['precio_base']
        
        print(f"✅ Transformadas {len(df)} filas")
        df.to_parquet(self.output().path, index=False)
        print(f"✅ Guardado en {self.output().path}")

class CargarDatos(luigi.Task):
    """Carga los datos transformados."""
    
    def requires(self):
        return TransformarDatos()
    
    def output(self):
        ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'etl_completado.txt'
        ruta_salida.parent.mkdir(parents=True, exist_ok=True)
        return luigi.LocalTarget(str(ruta_salida))
    
    def run(self):
        print("💾 Cargando datos...")
        df = pd.read_parquet(self.input().path)
        
        # Simular carga (aquí podrías cargar a una base de datos, etc.)
        with self.output().open('w') as f:
            f.write(f'ETL completado: {len(df)} filas procesadas\n')
            f.write(f'Total ventas: ${df["total"].sum():.2f}\n')
            f.write(f'Margen total: ${df["margen"].sum():.2f}')
        
        print(f"✅ ETL completado: {self.output().path}")

if __name__ == '__main__':
    # Para ver el DAG en la UI: ejecuta sin --local-scheduler (y con luigid corriendo)
    # Para ejecución local rápida: agrega --local-scheduler
    import sys
    if '--local-scheduler' in sys.argv:
        luigi.run(['CargarDatos', '--local-scheduler'])
    else:
        luigi.run(['CargarDatos'])  # Usa el servidor central (luigid)
