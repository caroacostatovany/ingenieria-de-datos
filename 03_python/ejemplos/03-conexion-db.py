"""
Ejemplo 3: Conexión a base de datos

Ejemplo de cómo conectar Python con PostgreSQL y trabajar con datos.
"""

import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env en la raíz del proyecto
from pathlib import Path
env_path = Path(__file__).parent.parent.parent / '.env'
load_dotenv(env_path)

def conectar_db():
    """Crea conexión a la base de datos.
    
    Intenta usar DATABASE_URL si está disponible, 
    sino construye la connection string desde variables individuales.
    """
    # Opción 1: Usar DATABASE_URL si está disponible (más simple)
    database_url = os.getenv('DATABASE_URL')
    if database_url:
        engine = create_engine(database_url)
        return engine
    
    # Opción 2: Construir desde variables individuales (fallback)
    db_host = os.getenv('DB_HOST', 'localhost')
    db_port = os.getenv('DB_PORT', '5432')
    db_name = os.getenv('DB_NAME', 'data_engineering')
    db_user = os.getenv('DB_USER', 'de_user')
    db_password = os.getenv('DB_PASSWORD', 'de_password')
    
    connection_string = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    engine = create_engine(connection_string)
    return engine

def leer_datos(engine, query):
    """Lee datos de la base de datos."""
    df = pd.read_sql(query, engine)
    return df

def escribir_datos(engine, df, tabla, if_exists='append'):
    """Escribe datos a la base de datos."""
    df.to_sql(tabla, engine, if_exists=if_exists, index=False)
    print(f"Datos escritos en tabla {tabla}")

def ejemplo_completo():
    """Ejemplo completo de trabajo con base de datos."""
    # Conectar
    engine = conectar_db()
    
    # Leer datos
    query = """
    SELECT 
        u.nombre,
        u.ciudad,
        COUNT(v.id) AS total_ventas,
        SUM(v.total) AS ingresos_totales
    FROM usuarios u
    LEFT JOIN ventas v ON u.id = v.usuario_id
    GROUP BY u.id, u.nombre, u.ciudad
    ORDER BY ingresos_totales DESC
    """
    
    df = leer_datos(engine, query)
    print("Datos de la base de datos:")
    print(df)
    
    # Procesar en Python
    df['ticket_promedio'] = df['ingresos_totales'] / df['total_ventas']
    df['categoria'] = df['ingresos_totales'].apply(
        lambda x: 'Alto' if x > 1000 else 'Bajo'
    )
    
    # Guardar resultados (opcional)
    # escribir_datos(engine, df, 'resumen_ventas', if_exists='replace')
    
    return df

if __name__ == '__main__':
    try:
        df = ejemplo_completo()
        print("\nResultado procesado:")
        print(df)
    except Exception as e:
        print(f"Error: {e}")
        print("Asegúrate de que la base de datos esté corriendo (docker-compose up)")
