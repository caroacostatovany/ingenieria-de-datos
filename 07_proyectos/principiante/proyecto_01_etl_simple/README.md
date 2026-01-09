# Proyecto 1: Pipeline ETL Simple

Construye tu primer pipeline ETL completo: extrae datos de CSV, transforma y limpia, y carga a una base de datos PostgreSQL.

---

## 🎯 Objetivo

Aprender los fundamentos de un pipeline ETL:
* **Extract**: Leer datos de archivos CSV
* **Transform**: Limpiar y transformar datos
* **Load**: Cargar datos a base de datos

---

## 📋 Requisitos previos

* Python 3.8+
* PostgreSQL (puedes usar Docker del módulo SQL)
* Conocimientos básicos de Python y SQL

---

## 🚀 Pasos del proyecto

### 1. Preparar entorno

```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install pandas psycopg2-binary python-dotenv
```

### 2. Estructura del proyecto

```
proyecto_01_etl_simple/
├── README.md
├── requirements.txt
├── .env.example
├── data/
│   └── ventas.csv
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── pipeline.py
└── tests/
    └── test_pipeline.py
```

### 3. Crear datos de ejemplo

Crea `data/ventas.csv`:

```csv
fecha,producto,cantidad,precio,cliente
2024-01-15,Producto A,5,10.50,Cliente 1
2024-01-16,Producto B,3,25.00,Cliente 2
2024-01-17,Producto A,2,10.50,Cliente 1
2024-01-18,Producto C,1,50.00,Cliente 3
```

### 4. Implementar Extract

`src/extract.py`:

```python
import pandas as pd
from pathlib import Path

def extract_csv(file_path: str) -> pd.DataFrame:
    """
    Extrae datos de un archivo CSV.
    
    Args:
        file_path: Ruta al archivo CSV
        
    Returns:
        DataFrame con los datos
    """
    try:
        df = pd.read_csv(file_path)
        print(f"✅ Extraídos {len(df)} registros de {file_path}")
        return df
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo {file_path}")
        raise
    except Exception as e:
        print(f"❌ Error al extraer datos: {e}")
        raise
```

### 5. Implementar Transform

`src/transform.py`:

```python
import pandas as pd
from datetime import datetime

def transform_ventas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforma y limpia datos de ventas.
    
    Args:
        df: DataFrame con datos de ventas
        
    Returns:
        DataFrame transformado
    """
    # Copiar para no modificar original
    df_clean = df.copy()
    
    # Convertir fecha a datetime
    df_clean['fecha'] = pd.to_datetime(df_clean['fecha'])
    
    # Calcular total
    df_clean['total'] = df_clean['cantidad'] * df_clean['precio']
    
    # Eliminar duplicados
    df_clean = df_clean.drop_duplicates()
    
    # Eliminar filas con valores nulos críticos
    df_clean = df_clean.dropna(subset=['fecha', 'producto', 'cantidad', 'precio'])
    
    # Validar que cantidad y precio sean positivos
    df_clean = df_clean[
        (df_clean['cantidad'] > 0) & 
        (df_clean['precio'] > 0)
    ]
    
    print(f"✅ Transformados {len(df_clean)} registros")
    return df_clean
```

### 6. Implementar Load

`src/load.py`:

```python
import psycopg2
from psycopg2.extras import execute_values
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

def create_table(conn):
    """Crea la tabla si no existe."""
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ventas (
            id SERIAL PRIMARY KEY,
            fecha DATE NOT NULL,
            producto VARCHAR(100) NOT NULL,
            cantidad INTEGER NOT NULL,
            precio DECIMAL(10, 2) NOT NULL,
            total DECIMAL(10, 2) NOT NULL,
            cliente VARCHAR(100),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cursor.close()
    print("✅ Tabla 'ventas' creada/verificada")

def load_to_postgres(df: pd.DataFrame):
    """
    Carga datos a PostgreSQL.
    
    Args:
        df: DataFrame con datos transformados
    """
    # Conectar a base de datos
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        port=os.getenv('DB_PORT', '5432'),
        database=os.getenv('DB_NAME', 'data_engineering'),
        user=os.getenv('DB_USER', 'de_user'),
        password=os.getenv('DB_PASSWORD', 'de_password')
    )
    
    try:
        # Crear tabla
        create_table(conn)
        
        # Insertar datos
        cursor = conn.cursor()
        execute_values(
            cursor,
            """
            INSERT INTO ventas (fecha, producto, cantidad, precio, total, cliente)
            VALUES %s
            ON CONFLICT DO NOTHING
            """,
            [
                (row['fecha'], row['producto'], row['cantidad'], 
                 row['precio'], row['total'], row['cliente'])
                for _, row in df.iterrows()
            ]
        )
        
        conn.commit()
        print(f"✅ Cargados {len(df)} registros a PostgreSQL")
        
    except Exception as e:
        conn.rollback()
        print(f"❌ Error al cargar datos: {e}")
        raise
    finally:
        cursor.close()
        conn.close()
```

### 7. Pipeline completo

`src/pipeline.py`:

```python
from extract import extract_csv
from transform import transform_ventas
from load import load_to_postgres

def run_pipeline(file_path: str):
    """
    Ejecuta el pipeline ETL completo.
    
    Args:
        file_path: Ruta al archivo CSV
    """
    print("🚀 Iniciando pipeline ETL...")
    
    # Extract
    print("\n📥 Fase 1: Extract")
    df = extract_csv(file_path)
    
    # Transform
    print("\n🔄 Fase 2: Transform")
    df_clean = transform_ventas(df)
    
    # Load
    print("\n📤 Fase 3: Load")
    load_to_postgres(df_clean)
    
    print("\n✅ Pipeline completado exitosamente!")

if __name__ == "__main__":
    run_pipeline("data/ventas.csv")
```

### 8. Archivo de configuración

`.env.example`:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=data_engineering
DB_USER=de_user
DB_PASSWORD=de_password
```

`requirements.txt`:

```
pandas==2.0.3
psycopg2-binary==2.9.9
python-dotenv==1.0.0
```

---

## ✅ Checklist de completado

- [ ] Entorno virtual creado y dependencias instaladas
- [ ] Archivo CSV con datos de ejemplo creado
- [ ] Función `extract_csv` implementada y probada
- [ ] Función `transform_ventas` implementada y probada
- [ ] Función `load_to_postgres` implementada y probada
- [ ] Pipeline completo ejecutado exitosamente
- [ ] Datos verificados en PostgreSQL
- [ ] Código documentado y limpio

---

## 🎓 Conceptos aprendidos

* ✅ Estructura de un pipeline ETL
* ✅ Separación de responsabilidades (extract, transform, load)
* ✅ Manejo de errores básico
* ✅ Uso de pandas para transformaciones
* ✅ Conexión a PostgreSQL desde Python
* ✅ Variables de entorno para configuración

---

## 🚀 Próximo paso

Después de completar este proyecto:
* Agrega validaciones más robustas
* Implementa logging
* Agrega tests unitarios
* Avanza a **[Proyecto 2: Análisis con Pandas](../proyecto_02_analisis_pandas/)**

---

> **Recuerda**: Este es tu primer pipeline. Tómate tu tiempo para entender cada paso.
