from prefect import flow, task
import pandas as pd
from pathlib import Path
import time

# Obtener la ruta base del proyecto
BASE_DIR = Path(__file__).parent.parent.parent.parent

@task
def extraer_usuarios():
    """Simula extracción de usuarios."""
    print("📥 Extrayendo usuarios...")
    time.sleep(1)  # Simula trabajo
    # En un caso real, esto vendría de una base de datos o API
    usuarios = pd.DataFrame({
        'usuario_id': [1, 2, 3],
        'nombre': ['Juan', 'María', 'Carlos'],
        'ciudad': ['Madrid', 'Barcelona', 'Valencia']
    })
    print("✅ Usuarios extraídos")
    return usuarios

@task
def extraer_productos():
    """Simula extracción de productos."""
    print("📥 Extrayendo productos...")
    time.sleep(1)  # Simula trabajo
    # En un caso real, esto vendría de otra fuente
    productos = pd.DataFrame({
        'producto_id': [101, 102, 103],
        'nombre': ['Laptop', 'Mouse', 'Teclado'],
        'precio': [899.99, 25.50, 45.00]
    })
    print("✅ Productos extraídos")
    return productos

@task
def combinar(usuarios, productos):
    """Combina usuarios y productos."""
    print("🔄 Combinando datos...")
    time.sleep(0.5)
    # Ejemplo: crear un DataFrame combinado
    resultado = pd.DataFrame({
        'usuario_id': [1, 2, 3],
        'producto_id': [101, 102, 103],
        'usuario': ['Juan', 'María', 'Carlos'],
        'producto': ['Laptop', 'Mouse', 'Teclado']
    })
    print("✅ Datos combinados")
    return resultado

@task
def cargar(resultado, ruta):
    """Carga el resultado."""
    print("💾 Cargando resultado...")
    ruta.parent.mkdir(parents=True, exist_ok=True)
    resultado.to_parquet(ruta, index=False)
    print("✅ Datos cargados")

@flow
def pipeline_con_dependencias():
    """Pipeline que demuestra dependencias entre tareas."""
    print("🚀 Iniciando pipeline con dependencias...")
    
    # Estas tareas se ejecutan en paralelo (no dependen una de otra)
    usuarios = extraer_usuarios()
    productos = extraer_productos()
    
    # Esta tarea espera a que ambas terminen (depende de ambas)
    resultado = combinar(usuarios, productos)
    
    # Esta tarea espera a combinar (depende de combinar)
    ruta_salida = BASE_DIR / '05_pipelines' / 'data' / 'output' / 'datos_combinados.parquet'
    cargar(resultado, ruta_salida)
    
    print("✅ Pipeline con dependencias completado")

# Ejecutar
if __name__ == '__main__':
    pipeline_con_dependencias()
