"""
Luigi: Tasks con dependencias complejas (paralelo y secuencial)
"""
import luigi
import pandas as pd
import time
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent.parent

class ExtraerProductos(luigi.Task):
    """Extrae productos (se ejecuta en paralelo con ExtraerVentas)."""
    
    def output(self):
        ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'productos_luigi.csv'
        ruta_salida.parent.mkdir(parents=True, exist_ok=True)
        return luigi.LocalTarget(str(ruta_salida))
    
    def run(self):
        print("📥 [PARALELO] Extrayendo productos...")
        time.sleep(1)  # Simular trabajo
        ruta_entrada = BASE_DIR / '03_python' / 'data' / 'productos.csv'
        df = pd.read_csv(ruta_entrada)
        df.to_csv(self.output().path, index=False)
        print(f"✅ Productos extraídos: {len(df)}")

class ExtraerVentas(luigi.Task):
    """Extrae ventas (se ejecuta en paralelo con ExtraerProductos)."""
    
    def output(self):
        ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'ventas_luigi.csv'
        ruta_salida.parent.mkdir(parents=True, exist_ok=True)
        return luigi.LocalTarget(str(ruta_salida))
    
    def run(self):
        print("📥 [PARALELO] Extrayendo ventas...")
        time.sleep(1)  # Simular trabajo
        ruta_entrada = BASE_DIR / '03_python' / 'data' / 'ventas.csv'
        df = pd.read_csv(ruta_entrada)
        df.to_csv(self.output().path, index=False)
        print(f"✅ Ventas extraídas: {len(df)}")

class ProcesarProductos(luigi.Task):
    """Procesa productos (depende de ExtraerProductos)."""
    
    def requires(self):
        return ExtraerProductos()
    
    def output(self):
        ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'productos_procesados.parquet'
        ruta_salida.parent.mkdir(parents=True, exist_ok=True)
        return luigi.LocalTarget(str(ruta_salida))
    
    def run(self):
        print("🔄 Procesando productos...")
        time.sleep(1)
        df = pd.read_csv(self.input().path)
        df['precio_final'] = df['precio_base'] * 1.1  # Aplicar margen
        df.to_parquet(self.output().path, index=False)
        print(f"✅ Productos procesados: {len(df)}")

class ProcesarVentas(luigi.Task):
    """Procesa ventas (depende de ExtraerVentas)."""
    
    def requires(self):
        return ExtraerVentas()
    
    def output(self):
        ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'ventas_procesadas.parquet'
        ruta_salida.parent.mkdir(parents=True, exist_ok=True)
        return luigi.LocalTarget(str(ruta_salida))
    
    def run(self):
        print("🔄 Procesando ventas...")
        time.sleep(1)
        df = pd.read_csv(self.input().path)
        df = df.dropna()
        df['total'] = df['precio'] * df['cantidad']
        df.to_parquet(self.output().path, index=False)
        print(f"✅ Ventas procesadas: {len(df)}")

class CombinarDatos(luigi.Task):
    """Combina datos procesados (depende de ProcesarProductos Y ProcesarVentas)."""
    
    def requires(self):
        return {
            'productos': ProcesarProductos(),
            'ventas': ProcesarVentas()
        }
    
    def output(self):
        ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'datos_combinados_luigi.parquet'
        ruta_salida.parent.mkdir(parents=True, exist_ok=True)
        return luigi.LocalTarget(str(ruta_salida))
    
    def run(self):
        print("🔗 Combinando datos...")
        df_productos = pd.read_parquet(self.input()['productos'].path)
        df_ventas = pd.read_parquet(self.input()['ventas'].path)
        
        # Merge por nombre de producto
        df = df_ventas.merge(df_productos, on='producto', how='left')
        df.to_parquet(self.output().path, index=False)
        print(f"✅ Datos combinados: {len(df)} filas")
        print(f"✅ Guardado en {self.output().path}")

if __name__ == '__main__':
    # Ejecutar la tarea final (Luigi ejecutará todas las dependencias)
    # Para ver el DAG en la UI: ejecuta sin --local-scheduler (y con luigid corriendo)
    # Para ejecución local rápida: agrega --local-scheduler
    import sys
    if '--local-scheduler' in sys.argv:
        luigi.run(['CombinarDatos', '--local-scheduler'])
    else:
        luigi.run(['CombinarDatos'])  # Usa el servidor central (luigid)
