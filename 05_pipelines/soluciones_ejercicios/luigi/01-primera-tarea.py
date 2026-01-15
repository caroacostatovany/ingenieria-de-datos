"""
Primer Task de Luigi: Pipeline ETL simple
"""
import luigi
import pandas as pd
from pathlib import Path

# Obtener la ruta base del proyecto (3 niveles arriba desde este archivo)
BASE_DIR = Path(__file__).parent.parent.parent.parent

class ExtraerDatos(luigi.Task):
    """Task para extraer datos del CSV de ventas."""
    
    def output(self):
        # Output se guarda en 05_pipelines/data/output para mejor organización
        ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'ventas_raw.csv'
        ruta_salida.parent.mkdir(parents=True, exist_ok=True)
        return luigi.LocalTarget(str(ruta_salida))
    
    def run(self):
        print("📥 Extrayendo datos...")
        # Leer el CSV de ejemplo del proyecto
        ruta_entrada = BASE_DIR / '03_python' / 'data' / 'ventas.csv'
        df = pd.read_csv(ruta_entrada)
        print(f"✅ Extraídas {len(df)} filas")
        
        # Guardar en output
        df.to_csv(self.output().path, index=False)
        print(f"✅ Guardado en {self.output().path}")

class TransformarDatos(luigi.Task):
    """Task para transformar datos (depende de ExtraerDatos)."""
    
    def requires(self):
        return ExtraerDatos()
    
    def output(self):
        ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'ventas_transformadas.parquet'
        ruta_salida.parent.mkdir(parents=True, exist_ok=True)
        return luigi.LocalTarget(str(ruta_salida))
    
    def run(self):
        print("🔄 Transformando datos...")
        df = pd.read_csv(self.input().path)
        df = df.dropna()
        df['total'] = df['precio'] * df['cantidad']
        print(f"✅ Transformadas {len(df)} filas")
        
        # Guardar en output
        df.to_parquet(self.output().path, index=False)
        print(f"✅ Guardado en {self.output().path}")

class CargarDatos(luigi.Task):
    """Task para cargar datos (depende de TransformarDatos)."""
    
    def requires(self):
        return TransformarDatos()
    
    def output(self):
        ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'pipeline_completado.txt'
        ruta_salida.parent.mkdir(parents=True, exist_ok=True)
        return luigi.LocalTarget(str(ruta_salida))
    
    def run(self):
        print("💾 Cargando datos...")
        # Leer datos transformados
        df = pd.read_parquet(self.input().path)
        print(f"✅ Datos listos para cargar: {len(df)} filas")
        
        # Marcar como completado
        with self.output().open('w') as f:
            f.write(f'Pipeline completado: {len(df)} filas procesadas')
        print(f"✅ Pipeline completado: {self.output().path}")

if __name__ == '__main__':
    # Ejecutar la tarea final (Luigi ejecutará las dependencias automáticamente)
    # Para ver el DAG en la UI: ejecuta sin --local-scheduler (y con luigid corriendo)
    # Para ejecución local rápida: agrega --local-scheduler
    import sys
    if '--local-scheduler' in sys.argv:
        luigi.run(['CargarDatos', '--local-scheduler'])
    else:
        luigi.run(['CargarDatos'])  # Usa el servidor central (luigid)
