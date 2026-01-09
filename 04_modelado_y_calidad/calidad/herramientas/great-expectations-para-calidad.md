# Great Expectations para Calidad de Datos

Great Expectations es una herramienta open-source para validar, documentar y perfilar tus datos. Aprende a usarla efectivamente.

> 💡 **Ejemplo práctico**: Revisa el [notebook de Great Expectations](../ejemplos/03-great-expectations.ipynb) para ver cómo crear expectativas y validar datos paso a paso.

---

## 🧠 ¿Qué es Great Expectations?

Great Expectations (GX) es un framework que te permite:
* **Definir expectativas** sobre tus datos
* **Validar automáticamente** que se cumplan
* **Documentar** el comportamiento de tus datos
* **Detectar cambios** en esquemas y distribuciones
* **Generar reportes** de calidad

> Great Expectations es como unit testing, pero para datos.

---

## 🚀 Instalación

```bash
# Instalación básica
pip install great-expectations

# Con dependencias adicionales
pip install great-expectations[sql]
```

---

## 📊 Conceptos clave

### 1. Expectations (Expectativas)

Definiciones de cómo deberían verse tus datos.

```python
import great_expectations as gx

# Crear contexto
context = gx.get_context()

# Crear datasource
datasource = context.sources.add_pandas("my_datasource")

# Crear asset (dataset)
asset = datasource.add_dataframe_asset(name="my_dataframe")

# Definir expectativas
validator = context.get_validator(
    datasource_name="my_datasource",
    data_asset_name="my_dataframe",
    dataframe=df
)

# Expectativa: columna no debe tener nulos
validator.expect_column_values_to_not_be_null("nombre")

# Expectativa: valores en rango
validator.expect_column_values_to_be_between("edad", min_value=0, max_value=120)

# Expectativa: sin duplicados
validator.expect_column_values_to_be_unique("id")
```

### 2. Validators

Objetos que ejecutan expectativas sobre datos.

```python
# Crear validator
validator = context.get_validator(
    datasource_name="my_datasource",
    data_asset_name="my_dataframe",
    dataframe=df
)

# Ejecutar expectativas
results = validator.validate()
print(results)
```

### 3. Checkpoints

Puntos de validación en tus pipelines.

```python
# Crear checkpoint
checkpoint = context.add_or_update_checkpoint(
    name="my_checkpoint",
    validator=validator
)

# Ejecutar checkpoint
results = checkpoint.run()
```

---

## 🔧 Uso básico

### Ejemplo 1: Validar DataFrame

```python
import great_expectations as gx
import pandas as pd

# Datos
df = pd.DataFrame({
    'id': [1, 2, 3],
    'nombre': ['Juan', 'María', 'Carlos'],
    'edad': [28, 35, 42],
    'email': ['juan@example.com', 'maria@example.com', 'carlos@example.com']
})

# Inicializar contexto
context = gx.get_context()

# Crear datasource
datasource = context.sources.add_pandas("pandas_datasource")

# Crear asset
asset = datasource.add_dataframe_asset(name="usuarios")

# Crear validator
validator = context.get_validator(
    datasource_name="pandas_datasource",
    data_asset_name="usuarios",
    dataframe=df
)

# Definir expectativas
validator.expect_column_values_to_not_be_null("id")
validator.expect_column_values_to_not_be_null("nombre")
validator.expect_column_values_to_be_between("edad", min_value=0, max_value=120)
validator.expect_column_values_to_match_regex("email", r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
validator.expect_column_values_to_be_unique("id")

# Validar
results = validator.validate()
print(results)
```

### Ejemplo 2: Validar desde archivo

```python
import great_expectations as gx

# Inicializar contexto
context = gx.get_context()

# Crear datasource para archivos
datasource = context.sources.add_pandas_filesystem(
    name="filesystem_datasource",
    base_directory="./data"
)

# Crear asset
asset = datasource.add_csv_asset(
    name="ventas",
    batching_regex=r"ventas_\d{4}-\d{2}-\d{2}\.csv"
)

# Crear validator
validator = context.get_validator(
    datasource_name="filesystem_datasource",
    data_asset_name="ventas",
    batch_request=asset.build_batch_request()
)

# Expectativas
validator.expect_table_row_count_to_be_between(min_value=100, max_value=10000)
validator.expect_column_values_to_not_be_null("fecha")
validator.expect_column_values_to_be_between("precio", min_value=0)

# Validar
results = validator.validate()
```

---

## 📋 Expectativas comunes

### Esquema y estructura

```python
# Número de filas
validator.expect_table_row_count_to_be_between(min_value=100, max_value=1000)

# Columnas esperadas
validator.expect_table_columns_to_match_ordered_list([
    'id', 'nombre', 'edad', 'email'
])

# Tipo de datos
validator.expect_column_values_to_be_of_type("edad", "int64")
```

### Valores

```python
# No nulos
validator.expect_column_values_to_not_be_null("nombre")

# En rango
validator.expect_column_values_to_be_between("edad", min_value=0, max_value=120)

# Valores únicos
validator.expect_column_values_to_be_unique("id")

# Valores en conjunto
validator.expect_column_values_to_be_in_set(
    "categoria",
    ["Electrónica", "Muebles", "Ropa"]
)

# Formato regex
validator.expect_column_values_to_match_regex(
    "email",
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)
```

### Estadísticas

```python
# Media en rango
validator.expect_column_mean_to_be_between("precio", min_value=10, max_value=100)

# Mediana
validator.expect_column_median_to_be_between("edad", min_value=25, max_value=50)

# Desviación estándar
validator.expect_column_stdev_to_be_between("precio", min_value=5, max_value=20)
```

### Relaciones

```python
# Suma de columnas
validator.expect_column_sum_to_be_between("total", min_value=1000, max_value=10000)

# Relación entre columnas
validator.expect_column_pair_values_A_to_be_greater_than_B(
    "precio_total",
    "precio_unitario"
)
```

---

## 🔄 Integración en pipelines

### Patrón: Validar antes de procesar

```python
import great_expectations as gx
import pandas as pd

def pipeline_con_gx(ruta_entrada, ruta_salida):
    """Pipeline con validación usando Great Expectations."""
    
    # 1. Cargar datos
    df = pd.read_csv(ruta_entrada)
    
    # 2. Validar entrada
    context = gx.get_context()
    datasource = context.sources.add_pandas("pandas_ds")
    asset = datasource.add_dataframe_asset(name="input_data")
    
    validator = context.get_validator(
        datasource_name="pandas_ds",
        data_asset_name="input_data",
        dataframe=df
    )
    
    # Expectativas de entrada
    validator.expect_table_row_count_to_be_between(min_value=1, max_value=1000000)
    validator.expect_column_values_to_not_be_null("id")
    
    # Validar
    results = validator.validate()
    
    if not results.success:
        raise ValueError(f"Validación falló: {results}")
    
    # 3. Procesar
    df_procesado = procesar_datos(df)
    
    # 4. Validar salida
    validator_salida = context.get_validator(
        datasource_name="pandas_ds",
        data_asset_name="output_data",
        dataframe=df_procesado
    )
    
    validator_salida.expect_column_values_to_not_be_null("total")
    validator_salida.expect_column_values_to_be_between("total", min_value=0)
    
    results_salida = validator_salida.validate()
    
    if not results_salida.success:
        raise ValueError(f"Validación de salida falló: {results_salida}")
    
    # 5. Guardar
    df_procesado.to_parquet(ruta_salida, index=False)
    
    print("✅ Pipeline completado con validaciones exitosas")
```

---

## 📊 Data Docs (Documentación)

Great Expectations genera documentación automática.

```python
# Generar data docs
context.build_data_docs()

# Ver en navegador
context.open_data_docs()
```

La documentación incluye:
* Expectativas definidas
* Resultados de validaciones
* Perfiles de datos
* Historial de cambios

---

## 🔍 Profiling automático

Great Expectations puede generar expectativas automáticamente.

```python
# Profiling básico
validator = context.get_validator(
    datasource_name="pandas_ds",
    data_asset_name="my_data",
    dataframe=df
)

# Generar expectativas automáticamente
profiler = UserConfigurableProfiler(
    validator,
    ignored_columns=["id"]  # Columnas a ignorar
)

suite = profiler.build_suite()

# Agregar al validator
validator.expectation_suite = suite
```

---

## 💡 Buenas prácticas

### 1. Empieza simple

```python
# ✅ Empieza con expectativas básicas
validator.expect_column_values_to_not_be_null("id")
validator.expect_column_values_to_be_unique("id")

# Luego agrega más complejidad
```

### 2. Usa checkpoints en CI/CD

```python
# Integrar en pipeline de CI/CD
checkpoint = context.get_checkpoint("my_checkpoint")
results = checkpoint.run()

if not results.success:
    # Falla el build
    exit(1)
```

### 3. Documenta expectativas

```python
# Agregar descripción a expectativas
validator.expect_column_values_to_be_between(
    "edad",
    min_value=0,
    max_value=120,
    meta={"description": "Edad debe estar entre 0 y 120 años"}
)
```

### 4. Monitorea cambios

```python
# Comparar con validación anterior
results = validator.validate()
previous_results = load_previous_results()

if results.statistics["successful_expectations"] < previous_results:
    print("⚠️ Calidad de datos ha disminuido")
```

---

## 🎯 Ejercicios

1. Instala Great Expectations y crea tu primer validator
2. Define expectativas para un dataset real
3. Integra validaciones en un pipeline ETL
4. Genera data docs y explora la documentación

---

## 🚀 Recursos adicionales

* [Documentación oficial](https://docs.greatexpectations.io/)
* [Expectativas disponibles](https://greatexpectations.io/expectations/)
* [Ejemplos](https://github.com/great-expectations/great_expectations/tree/develop/examples)

---

## 💡 Comparación con validaciones manuales

| Aspecto | Validaciones manuales | Great Expectations |
|---------|----------------------|-------------------|
| **Esfuerzo** | Alto (código custom) | Bajo (framework) |
| **Documentación** | Manual | Automática |
| **Historial** | Difícil de mantener | Automático |
| **Profiling** | Manual | Automático |
| **Reportes** | Custom | Incluidos |

---

> **Recuerda**: Great Expectations no reemplaza el entendimiento de tus datos, pero facilita validarlos y documentarlos sistemáticamente.
