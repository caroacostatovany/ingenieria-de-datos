# Proyecto 1: Pipeline SQL + Python

Construye un pipeline híbrido que combina SQL para transformaciones y Python para orquestación.

---

## 🎯 Objetivo

Aprender a:
* Combinar SQL y Python en un pipeline
* Usar SQL para transformaciones complejas
* Orquestar con Python
* Manejar errores y logging

---

## 📋 Requisitos previos

* Python 3.8+
* PostgreSQL
* Conocimientos de SQL y Python

---

## 🚀 Pasos del proyecto

### 1. Estructura del proyecto

```
proyecto_01_sql_python/
├── README.md
├── requirements.txt
├── sql/
│   ├── 01_extract.sql
│   ├── 02_transform.sql
│   └── 03_load.sql
├── src/
│   ├── pipeline.py
│   ├── db_connection.py
│   └── sql_executor.py
└── config/
    └── .env
```

### 2. SQL para transformaciones

`sql/02_transform.sql`:

```sql
-- Crear tabla de staging
CREATE TABLE IF NOT EXISTS staging_ventas AS
SELECT 
    fecha,
    producto,
    cantidad,
    precio,
    cantidad * precio AS total,
    cliente
FROM raw_ventas
WHERE fecha >= CURRENT_DATE - INTERVAL '30 days'
  AND cantidad > 0
  AND precio > 0;

-- Agregar datos transformados
INSERT INTO ventas_agregadas
SELECT 
    DATE_TRUNC('month', fecha) AS mes,
    producto,
    SUM(cantidad) AS total_cantidad,
    SUM(total) AS total_ingresos,
    COUNT(*) AS num_ventas
FROM staging_ventas
GROUP BY DATE_TRUNC('month', fecha), producto;
```

### 3. Orquestación con Python

`src/pipeline.py`:

```python
import logging
from db_connection import get_connection
from sql_executor import execute_sql_file

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_pipeline():
    """Ejecuta pipeline SQL + Python."""
    logger.info("🚀 Iniciando pipeline SQL + Python")
    
    conn = get_connection()
    
    try:
        # 1. Extract (SQL)
        logger.info("📥 Fase 1: Extract (SQL)")
        execute_sql_file(conn, 'sql/01_extract.sql')
        
        # 2. Transform (SQL)
        logger.info("🔄 Fase 2: Transform (SQL)")
        execute_sql_file(conn, 'sql/02_transform.sql')
        
        # 3. Validación (Python)
        logger.info("✅ Fase 3: Validación (Python)")
        validate_data(conn)
        
        # 4. Load (SQL)
        logger.info("📤 Fase 4: Load (SQL)")
        execute_sql_file(conn, 'sql/03_load.sql')
        
        logger.info("✅ Pipeline completado")
        
    except Exception as e:
        logger.error(f"❌ Error en pipeline: {e}")
        raise
    finally:
        conn.close()

def validate_data(conn):
    """Valida datos con Python."""
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM staging_ventas")
    count = cursor.fetchone()[0]
    
    if count == 0:
        raise ValueError("No hay datos para procesar")
    
    logger.info(f"✅ Validación: {count} registros en staging")
    cursor.close()

if __name__ == "__main__":
    run_pipeline()
```

---

## ✅ Checklist

- [ ] SQL para transformaciones implementado
- [ ] Orquestación Python funcionando
- [ ] Manejo de errores robusto
- [ ] Logging implementado
- [ ] Pipeline ejecutándose correctamente

---

## 🚀 Próximo paso

Avanza a **[Proyecto 2: Pipeline con Validaciones](../proyecto_02_validaciones/)**.
