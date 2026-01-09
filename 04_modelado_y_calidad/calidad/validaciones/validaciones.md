# Validaciones en Pipelines

Las validaciones aseguran que los datos cumplan con las expectativas antes de usarlos. Aprende a implementarlas efectivamente.

> 💡 **Ejemplo práctico**: Revisa el [notebook de Validaciones](../ejemplos/06-validaciones.ipynb) para ver cómo implementar validaciones de esquema, rangos y completitud en pipelines.

---

## 🧠 ¿Qué son las validaciones?

Las validaciones son **checks automáticos** que verifican:
* **Esquemas**: Estructura y tipos de datos
* **Reglas de negocio**: Lógica de negocio
* **Integridad**: Relaciones entre datos
* **Calidad**: Completitud, exactitud, etc.

> Las validaciones deben fallar rápido y claro. Mejor detener el pipeline que procesar datos incorrectos.

---

## 🔍 Tipos de validaciones

### 1. Validación de esquema

Verifica estructura y tipos.

```python
import pandas as pd

def validar_esquema(df, esquema_esperado):
    """Valida que el DataFrame tenga el esquema esperado."""
    errores = []
    
    # Verificar columnas
    columnas_esperadas = set(esquema_esperado.keys())
    columnas_actuales = set(df.columns)
    
    if columnas_esperadas != columnas_actuales:
        faltantes = columnas_esperadas - columnas_actuales
        extras = columnas_actuales - columnas_esperadas
        
        if faltantes:
            errores.append(f"Columnas faltantes: {faltantes}")
        if extras:
            errores.append(f"Columnas no esperadas: {extras}")
    
    # Verificar tipos
    for col, tipo_esperado in esquema_esperado.items():
        if col in df.columns:
            tipo_actual = df[col].dtype
            if tipo_actual != tipo_esperado:
                errores.append(
                    f"Columna {col}: esperado {tipo_esperado}, "
                    f"actual {tipo_actual}"
                )
    
    if errores:
        raise ValueError(f"Errores de esquema:\n" + "\n".join(errores))
    
    return True

# Uso
esquema = {
    'nombre': 'object',
    'edad': 'int64',
    'precio': 'float64'
}

validar_esquema(df, esquema)
```

### 2. Validación de rangos

Verifica que valores estén en rangos esperados.

```python
def validar_rangos(df):
    """Valida rangos de valores."""
    errores = []
    
    # Edad entre 0 y 120
    if 'edad' in df.columns:
        fuera_rango = df[(df['edad'] < 0) | (df['edad'] > 120)]
        if len(fuera_rango) > 0:
            errores.append(f"Edades fuera de rango: {len(fuera_rango)} filas")
    
    # Precio positivo
    if 'precio' in df.columns:
        negativos = df[df['precio'] < 0]
        if len(negativos) > 0:
            errores.append(f"Precios negativos: {len(negativos)} filas")
    
    if errores:
        raise ValueError("Errores de rango:\n" + "\n".join(errores))
    
    return True
```

### 3. Validación de completitud

Verifica valores nulos.

```python
def validar_completitud(df, columnas_criticas, umbral=0.95):
    """Valida completitud de columnas críticas."""
    errores = []
    
    for col in columnas_criticas:
        if col not in df.columns:
            errores.append(f"Columna crítica {col} no existe")
            continue
        
        completitud = (1 - df[col].isnull().sum() / len(df)) * 100
        
        if completitud < umbral * 100:
            errores.append(
                f"Columna {col}: completitud {completitud:.2f}% "
                f"(umbral: {umbral*100}%)"
            )
    
    if errores:
        raise ValueError("Errores de completitud:\n" + "\n".join(errores))
    
    return True

# Uso
validar_completitud(df, ['nombre', 'email', 'precio'], umbral=0.95)
```

### 4. Validación de unicidad

Verifica duplicados.

```python
def validar_unicidad(df, columnas_unicas):
    """Valida que columnas sean únicas."""
    errores = []
    
    for col in columnas_unicas:
        if col not in df.columns:
            continue
        
        duplicados = df[df[col].duplicated()]
        if len(duplicados) > 0:
            errores.append(
                f"Columna {col}: {len(duplicados)} duplicados encontrados"
            )
    
    if errores:
        raise ValueError("Errores de unicidad:\n" + "\n".join(errores))
    
    return True

# Uso
validar_unicidad(df, ['id', 'email'])
```

### 5. Validación de relaciones

Verifica integridad referencial.

```python
def validar_relaciones(df, df_referencia, col_local, col_referencia):
    """Valida que valores existan en tabla de referencia."""
    valores_validos = set(df_referencia[col_referencia].unique())
    valores_actuales = set(df[col_local].unique())
    
    valores_invalidos = valores_actuales - valores_validos
    
    if valores_invalidos:
        raise ValueError(
            f"Valores no encontrados en referencia: {valores_invalidos}"
        )
    
    return True

# Ejemplo: validar que todos los producto_id existan
validar_relaciones(df_ventas, df_productos, 'producto_id', 'id')
```

### 6. Validación de formato

Verifica formatos específicos.

```python
import re

def validar_formato_email(df, columna='email'):
    """Valida formato de email."""
    if columna not in df.columns:
        return True
    
    patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    emails_invalidos = df[
        ~df[columna].astype(str).str.match(patron_email, na=False)
    ]
    
    if len(emails_invalidos) > 0:
        raise ValueError(f"Emails con formato inválido: {len(emails_invalidos)}")
    
    return True

def validar_formato_fecha(df, columna='fecha', formato='%Y-%m-%d'):
    """Valida formato de fecha."""
    if columna not in df.columns:
        return True
    
    try:
        pd.to_datetime(df[columna], format=formato)
    except ValueError as e:
        raise ValueError(f"Fechas con formato inválido: {e}")
    
    return True
```

---

## 🔄 Integración en pipelines

### Patrón: Validar antes de procesar

```python
def pipeline_con_validacion(ruta_entrada, ruta_salida):
    """Pipeline con validaciones en cada etapa."""
    
    # 1. Extraer
    df = pd.read_csv(ruta_entrada)
    
    # 2. Validar entrada
    validar_esquema(df, esquema_esperado)
    validar_completitud(df, columnas_criticas)
    
    # 3. Transformar
    df = transformar_datos(df)
    
    # 4. Validar salida
    validar_rangos(df)
    validar_unicidad(df, ['id'])
    
    # 5. Cargar
    df.to_parquet(ruta_salida, index=False)
    
    print("✅ Pipeline completado exitosamente")
```

### Patrón: Fail fast

```python
def validar_y_fallar_rapido(df):
    """Acumula errores y falla al final."""
    errores = []
    
    # Ejecutar todas las validaciones
    try:
        validar_esquema(df, esquema)
    except ValueError as e:
        errores.append(f"Esquema: {e}")
    
    try:
        validar_rangos(df)
    except ValueError as e:
        errores.append(f"Rangos: {e}")
    
    # Si hay errores, fallar con todos
    if errores:
        raise ValueError("Errores de validación:\n" + "\n".join(errores))
```

---

## 📊 Reportes de validación

```python
def generar_reporte_validacion(df):
    """Genera reporte de validaciones."""
    reporte = {
        'fecha': pd.Timestamp.now(),
        'total_filas': len(df),
        'total_columnas': len(df.columns),
        'validaciones': {}
    }
    
    # Ejecutar validaciones y capturar resultados
    try:
        validar_esquema(df, esquema)
        reporte['validaciones']['esquema'] = '✅ OK'
    except Exception as e:
        reporte['validaciones']['esquema'] = f'❌ {str(e)}'
    
    # ... más validaciones
    
    return reporte
```

---

## 🚨 Alertas y notificaciones

```python
def enviar_alerta_validacion(errores):
    """Envía alerta cuando hay errores."""
    mensaje = f"⚠️ Errores de validación detectados:\n{errores}"
    
    # Opciones:
    # - Logging
    # - Email
    # - Slack
    # - PagerDuty
    
    print(mensaje)
    # logging.error(mensaje)
    # send_email(to='team@example.com', subject='Error de validación', body=mensaje)
```

---

## 💡 Buenas prácticas

### 1. Valida temprano

```python
# ✅ Valida al inicio
df = pd.read_csv('datos.csv')
validar_esquema(df, esquema)  # Antes de procesar

# ⚠️ No valides al final
df = procesar(df)
validar_esquema(df, esquema)  # Demasiado tarde
```

### 2. Mensajes de error claros

```python
# ✅ Claro
raise ValueError("Columna 'email' tiene 150 valores nulos (15% del total)")

# ⚠️ Confuso
raise ValueError("Error en validación")
```

### 3. Valida en múltiples etapas

```python
# Validar entrada
validar_esquema(df_raw, esquema_raw)

# Validar después de transformación
validar_esquema(df_procesado, esquema_procesado)

# Validar salida final
validar_rangos(df_final)
```

---

## 🎯 Ejercicios

1. Implementa validaciones de esquema para un dataset
2. Crea validaciones de reglas de negocio
3. Integra validaciones en un pipeline ETL
4. Genera reportes de validación

---

## 🚀 Próximo paso

Continúa con **[Testing de datos](testing-de-datos.md)** y **[Great Expectations](../herramientas/great-expectations-para-calidad.md)**.

---

> **Recuerda**: Las validaciones son tu red de seguridad. Sin ellas, los errores se propagan y causan problemas mayores.
