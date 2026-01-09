# Proyecto 2: Pipeline con Validaciones

Implementa validaciones robustas de calidad de datos en tu pipeline.

---

## 🎯 Objetivo

Aprender a:
* Implementar validaciones de datos
* Usar Great Expectations o Pandera
* Generar reportes de calidad
* Manejar datos inválidos

---

## 📋 Requisitos previos

* Python 3.8+
* Conocimientos de validación de datos

---

## 🚀 Pasos del proyecto

### 1. Estructura

```
proyecto_02_validaciones/
├── README.md
├── requirements.txt
├── src/
│   ├── pipeline.py
│   ├── validators.py
│   └── quality_report.py
└── expectations/  # Si usas Great Expectations
    └── expectations.json
```

### 2. Validaciones con Pandera

`src/validators.py`:

```python
import pandera as pa
from pandera import Column, Check

schema = pa.DataFrameSchema({
    "fecha": Column(pa.DateTime),
    "producto": Column(pa.String, Check.str_length(min_value=1)),
    "cantidad": Column(pa.Int, Check.greater_than(0)),
    "precio": Column(pa.Float, Check.greater_than(0)),
    "total": Column(pa.Float, Check.greater_than(0)),
})

def validate_data(df):
    """Valida DataFrame contra schema."""
    try:
        validated_df = schema.validate(df)
        return validated_df, True, None
    except pa.errors.SchemaError as e:
        return df, False, str(e)
```

### 3. Pipeline con validaciones

`src/pipeline.py`:

```python
from validators import validate_data
from quality_report import generate_report

def run_pipeline():
    # Extract
    df = extract_data()
    
    # Validate
    df_valid, is_valid, error = validate_data(df)
    
    if not is_valid:
        generate_report(df, error)
        raise ValueError(f"Datos inválidos: {error}")
    
    # Transform y Load
    # ...
```

---

## ✅ Checklist

- [ ] Validaciones implementadas
- [ ] Reportes de calidad generados
- [ ] Manejo de datos inválidos
- [ ] Tests de validación

---

## 🚀 Próximo paso

Avanza a **[Proyecto 3: Pipeline con Airflow Local](../proyecto_03_airflow_local/)**.
