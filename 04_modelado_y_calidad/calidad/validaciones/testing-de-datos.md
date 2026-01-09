# Testing de Datos

Los tests aseguran que tus transformaciones de datos funcionen correctamente. Aprende a escribir tests efectivos.

> 💡 **Ejemplo práctico**: Revisa el [notebook de Testing de Datos](../ejemplos/05-testing-datos.ipynb) para ver ejemplos ejecutables de diferentes tipos de tests para datos.

---

## 🧠 ¿Por qué testear datos?

Los tests de datos verifican que:
* **Transformaciones** producen resultados esperados
* **Validaciones** funcionan correctamente
* **Calidad** se mantiene después de cambios
* **Regresiones** no se introducen

> Testear datos es tan importante como testear código. Los datos incorrectos causan decisiones incorrectas.

---

## 🧪 Tipos de tests

### 1. Tests unitarios de transformaciones

Prueban funciones de transformación individuales.

```python
import pytest
import pandas as pd

def calcular_total(precio, cantidad):
    """Calcula el total de una venta."""
    return precio * cantidad

def test_calcular_total():
    """Test de función calcular_total."""
    assert calcular_total(10, 2) == 20
    assert calcular_total(5.5, 3) == 16.5
    assert calcular_total(0, 10) == 0

def limpiar_nombres(df):
    """Limpia nombres en un DataFrame."""
    df['nombre'] = df['nombre'].str.strip().str.title()
    return df

def test_limpiar_nombres():
    """Test de limpieza de nombres."""
    df = pd.DataFrame({
        'nombre': ['  juan  ', 'MARÍA', 'carlos']
    })
    
    resultado = limpiar_nombres(df)
    
    assert resultado['nombre'].tolist() == ['Juan', 'María', 'Carlos']
```

### 2. Tests de integridad

Verifican que los datos mantengan integridad después de transformaciones.

```python
def test_sin_perdida_de_filas(df_entrada, df_salida):
    """Verifica que no se pierdan filas críticas."""
    # Filas importantes no deben desaparecer
    ids_importantes = df_entrada[df_entrada['es_critico'] == True]['id'].tolist()
    ids_en_salida = df_salida['id'].tolist()
    
    for id_importante in ids_importantes:
        assert id_importante in ids_en_salida, f"ID crítico {id_importante} perdido"

def test_suma_conservada(df_entrada, df_salida):
    """Verifica que sumas se conserven."""
    total_entrada = df_entrada['precio'].sum()
    total_salida = df_salida['precio'].sum()
    
    assert abs(total_entrada - total_salida) < 0.01, "Suma no se conserva"
```

### 3. Tests de calidad

Verifican métricas de calidad.

```python
def test_completitud_minima(df, umbral=0.95):
    """Verifica completitud mínima."""
    for col in df.columns:
        completitud = (1 - df[col].isnull().sum() / len(df)) * 100
        assert completitud >= umbral * 100, \
            f"Completitud de {col} es {completitud}%, menor que {umbral*100}%"

def test_sin_duplicados(df, columnas_unicas):
    """Verifica que no haya duplicados."""
    for col in columnas_unicas:
        duplicados = df[col].duplicated().sum()
        assert duplicados == 0, f"Duplicados encontrados en {col}: {duplicados}"
```

### 4. Tests de reglas de negocio

Verifican que se cumplan reglas de negocio.

```python
def test_precios_positivos(df):
    """Verifica que todos los precios sean positivos."""
    precios_negativos = df[df['precio'] < 0]
    assert len(precios_negativos) == 0, \
        f"Encontrados {len(precios_negativos)} precios negativos"

def test_fechas_en_rango(df, fecha_inicio, fecha_fin):
    """Verifica que fechas estén en rango válido."""
    df['fecha'] = pd.to_datetime(df['fecha'])
    fuera_rango = df[
        (df['fecha'] < fecha_inicio) | (df['fecha'] > fecha_fin)
    ]
    assert len(fuera_rango) == 0, \
        f"Encontradas {len(fuera_rango)} fechas fuera de rango"
```

---

## 🔧 Framework: pytest

### Estructura de tests

```
proyecto/
├── src/
│   └── transform.py
├── tests/
│   ├── __init__.py
│   ├── test_transform.py
│   └── conftest.py
└── pytest.ini
```

### Ejemplo completo

```python
# tests/conftest.py
import pytest
import pandas as pd

@pytest.fixture
def df_ejemplo():
    """Fixture con datos de ejemplo."""
    return pd.DataFrame({
        'id': [1, 2, 3],
        'nombre': ['Juan', 'María', 'Carlos'],
        'precio': [10.5, 20.0, 15.5],
        'cantidad': [2, 1, 3]
    })

# tests/test_transform.py
import pytest
import pandas as pd
from src.transform import calcular_total, limpiar_nombres

def test_calcular_total(df_ejemplo):
    """Test de cálculo de total."""
    df = df_ejemplo.copy()
    df['total'] = df.apply(
        lambda row: calcular_total(row['precio'], row['cantidad']),
        axis=1
    )
    
    assert df['total'].tolist() == [21.0, 20.0, 46.5]

def test_limpiar_nombres(df_ejemplo):
    """Test de limpieza."""
    df = df_ejemplo.copy()
    df['nombre'] = ['  juan  ', 'MARÍA', 'carlos']
    
    resultado = limpiar_nombres(df)
    
    assert resultado['nombre'].tolist() == ['Juan', 'María', 'Carlos']
```

### Ejecutar tests

```bash
# Todos los tests
pytest

# Test específico
pytest tests/test_transform.py::test_calcular_total

# Con cobertura
pytest --cov=src tests/
```

---

## 📊 Tests con datos de ejemplo

### Fixtures con datos realistas

```python
@pytest.fixture
def df_ventas():
    """Fixture con datos de ventas."""
    return pd.DataFrame({
        'venta_id': [1, 2, 3, 4, 5],
        'producto_id': [101, 102, 101, 103, 102],
        'cantidad': [2, 1, 3, 1, 2],
        'precio': [10.0, 20.0, 10.0, 30.0, 20.0],
        'fecha': pd.date_range('2024-01-01', periods=5, freq='D')
    })

def test_agregacion_ventas(df_ventas):
    """Test de agregación."""
    resultado = df_ventas.groupby('producto_id')['cantidad'].sum()
    
    assert resultado[101] == 5
    assert resultado[102] == 3
    assert resultado[103] == 1
```

---

## 🎯 Tests de pipelines completos

```python
def test_pipeline_completo():
    """Test de pipeline end-to-end."""
    # Datos de entrada
    df_entrada = pd.DataFrame({
        'nombre': ['  juan  ', 'MARÍA'],
        'precio': [10.0, 20.0],
        'cantidad': [2, 1]
    })
    
    # Ejecutar pipeline
    df_limpio = limpiar_nombres(df_entrada)
    df_limpio['total'] = df_limpio['precio'] * df_limpio['cantidad']
    
    # Verificaciones
    assert len(df_limpio) == 2
    assert df_limpio['nombre'].tolist() == ['Juan', 'María']
    assert df_limpio['total'].tolist() == [20.0, 20.0]
```

---

## 💡 Buenas prácticas

### 1. Tests independientes

```python
# ✅ Cada test es independiente
def test_uno():
    df = crear_df()
    # ...

def test_dos():
    df = crear_df()  # No depende de test_uno
    # ...
```

### 2. Tests rápidos

```python
# ✅ Usa datos pequeños para tests
df_test = df.head(100)  # No todo el dataset

# ⚠️ Evita procesar datasets grandes en tests
```

### 3. Tests determinísticos

```python
# ✅ Resultado predecible
def test_suma():
    assert sum([1, 2, 3]) == 6

# ⚠️ Evita aleatoriedad
def test_aleatorio():
    resultado = random.randint(1, 10)  # No determinístico
    assert resultado > 0
```

### 4. Nombres descriptivos

```python
# ✅ Claro
def test_calcular_total_con_precio_cero():
    assert calcular_total(0, 10) == 0

# ⚠️ Confuso
def test_1():
    assert calcular_total(0, 10) == 0
```

---

## 🎯 Ejercicios

1. Escribe tests para funciones de transformación
2. Crea tests de integridad de datos
3. Implementa tests de calidad
4. Configura pytest para tu proyecto

---

## 🚀 Próximo paso

Aprende a usar **[Great Expectations](../herramientas/great-expectations-para-calidad.md)** para validaciones avanzadas.

---

> **Recuerda**: Los tests te dan confianza para cambiar código. Sin tests, cada cambio es un riesgo.
