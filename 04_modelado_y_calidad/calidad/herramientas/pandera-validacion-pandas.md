# Pandera: Validación de Esquemas para Pandas

Pandera es una librería Python para validar esquemas de DataFrames de pandas de forma declarativa.

> 💡 **Ejemplo práctico**: Revisa el [notebook de Pandera](../ejemplos/04-pandera-validacion.ipynb) para ver cómo definir esquemas y validar DataFrames interactivamente.

---

## 🧠 ¿Qué es Pandera?

Pandera permite:
* **Validar esquemas** de DataFrames de forma declarativa
* **Type checking** de columnas
* **Validaciones personalizadas** con funciones
* **Integración** con pandas

> Pandera es como Great Expectations pero más simple y enfocado en pandas.

---

## 🚀 Instalación

```bash
pip install pandera
```

---

## 📊 Uso básico

### Definir esquema

```python
import pandera as pa
import pandas as pd

# Definir esquema
schema = pa.DataFrameSchema({
    "nombre": pa.Column(str),
    "edad": pa.Column(int, pa.Check.ge(0), pa.Check.le(120)),
    "email": pa.Column(str, pa.Check.str_matches(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')),
    "precio": pa.Column(float, pa.Check.gt(0)),
})

# Validar DataFrame
df = pd.DataFrame({
    'nombre': ['Juan', 'María'],
    'edad': [28, 35],
    'email': ['juan@example.com', 'maria@example.com'],
    'precio': [10.5, 20.0]
})

# Validar
schema.validate(df)
```

---

## 🔍 Validaciones comunes

### Rangos

```python
schema = pa.DataFrameSchema({
    "edad": pa.Column(int, pa.Check.between(0, 120)),
    "precio": pa.Column(float, pa.Check.gt(0)),
})
```

### Valores únicos

```python
schema = pa.DataFrameSchema({
    "id": pa.Column(int, unique=True),
})
```

### Valores en conjunto

```python
schema = pa.DataFrameSchema({
    "categoria": pa.Column(str, pa.Check.isin(["A", "B", "C"])),
})
```

---

## 💡 Integración en pipelines

```python
import pandera as pa

# Esquema de entrada
schema_entrada = pa.DataFrameSchema({
    "fecha": pa.Column("datetime64[ns]"),
    "producto_id": pa.Column(int),
    "cantidad": pa.Column(int, pa.Check.gt(0)),
    "precio": pa.Column(float, pa.Check.gt(0)),
})

# Esquema de salida
schema_salida = pa.DataFrameSchema({
    "fecha": pa.Column("datetime64[ns]"),
    "producto_id": pa.Column(int),
    "total": pa.Column(float, pa.Check.gt(0)),
})

def pipeline_con_validacion(df):
    # Validar entrada
    df = schema_entrada.validate(df)
    
    # Transformar
    df['total'] = df['cantidad'] * df['precio']
    df = df[['fecha', 'producto_id', 'total']]
    
    # Validar salida
    df = schema_salida.validate(df)
    
    return df
```

---

## 🎯 Cuándo usar Pandera

✅ **Usa Pandera cuando:**
* Trabajas principalmente con pandas
* Necesitas validación de esquemas simple
* Quieres type checking de columnas
* Prefieres algo más ligero que Great Expectations

❌ **No uses Pandera cuando:**
* Necesitas validaciones muy complejas
* Quieres documentación automática
* Necesitas profiling automático

---

## 🚀 Próximo paso

Compara con **[Great Expectations](great-expectations-para-calidad.md)** para decidir cuál usar.

---

> **Recuerda**: Pandera es excelente para validaciones simples de pandas. Para validaciones más complejas, considera Great Expectations.
