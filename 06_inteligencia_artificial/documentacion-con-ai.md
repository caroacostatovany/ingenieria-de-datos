# Documentación con AI

La AI puede ayudarte a generar y mantener documentación de calidad. Aprende a usarla efectivamente.

---

## 🧠 ¿Por qué documentar con AI?

**Ventajas:**
* **Ahorra tiempo**: Genera documentación rápidamente
* **Consistencia**: Mismo estilo en todo el proyecto
* **Completitud**: No olvida detalles importantes
* **Mantenimiento**: Fácil actualizar cuando cambia el código

> La documentación generada por AI es un punto de partida, no el producto final. Siempre revisa y ajusta.

---

## 📝 Tipos de documentación

### 1. Docstrings de funciones

**Prompt:**
```
"Genera docstring estilo Google para esta función:

def procesar_ventas(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna()
    df['total'] = df['cantidad'] * df['precio']
    return df
```

**Resultado:**
```python
def procesar_ventas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Procesa datos de ventas limpiando nulos y calculando totales.
    
    Args:
        df: DataFrame con columnas 'cantidad' y 'precio'
    
    Returns:
        DataFrame procesado con columna adicional 'total'
    
    Raises:
        KeyError: Si faltan columnas requeridas
    
    Example:
        >>> df = pd.DataFrame({'cantidad': [2, 3], 'precio': [10, 20]})
        >>> resultado = procesar_ventas(df)
        >>> resultado['total'].tolist()
        [20, 60]
    """
    df = df.dropna()
    df['total'] = df['cantidad'] * df['precio']
    return df
```

### 2. Documentación de módulos

**Prompt:**
```
"Genera documentación para este módulo de procesamiento de datos:

[pega código del módulo]

Incluye:
- Descripción del módulo
- Funciones principales
- Ejemplos de uso
- Dependencias"
```

### 3. README de proyecto

**Prompt:**
```
"Crea un README.md completo para este proyecto:

Proyecto: Pipeline ETL de ventas
- Lee de PostgreSQL
- Procesa y transforma
- Guarda en S3

Incluye:
- Descripción
- Instalación
- Configuración
- Uso
- Estructura
- Contribuir"
```

---

## 🔄 Flujo de trabajo

### 1. Genera documentación inicial

```python
# Código sin documentar
def extract_data(source):
    df = pd.read_csv(source)
    return df

# Prompt: "Agrega docstring estilo Google"
# Resultado: Documentación generada
```

### 2. Revisa y ajusta

```python
# ✅ Revisa que sea:
# - Correcta técnicamente
# - Clara y comprensible
# - Completa
# - Con ejemplos relevantes
```

### 3. Mantén actualizada

```python
# Cuando cambias código:
# 1. Actualiza documentación
# 2. O pide a AI: "Actualiza la documentación según estos cambios: [cambios]"
```

---

## 📊 Ejemplos prácticos

### Documentar pipeline ETL

**Prompt:**
```
"Genera documentación completa para este pipeline ETL:

[pega código del pipeline]

Incluye:
- Descripción del propósito
- Diagrama de flujo (en texto)
- Entrada y salida
- Dependencias
- Ejemplo de uso
- Troubleshooting"
```

### Documentar clase

**Prompt:**
```
"Genera documentación para esta clase:

[pega código de la clase]

Incluye:
- Descripción de la clase
- Atributos
- Métodos con docstrings
- Ejemplo de uso"
```

### Crear guía de uso

**Prompt:**
```
"Crea una guía de uso para este módulo de procesamiento de datos:

[pega código]

Incluye:
- Instalación
- Configuración inicial
- Ejemplos básicos
- Casos de uso avanzados
- FAQ"
```

---

## 💡 Mejores prácticas

### 1. Estilo consistente

```python
# ✅ Define estilo al inicio
"Genera docstrings estilo Google para todas las funciones"
"Usa formato Markdown para README"
```

### 2. Incluye ejemplos

```python
# ✅ Siempre pide ejemplos
"Incluye ejemplos de uso en la documentación"
```

### 3. Mantén actualizada

```python
# ✅ Actualiza cuando cambia código
"Actualiza esta documentación según estos cambios: [cambios]"
```

### 4. Revisa siempre

```python
# ✅ Nunca uses documentación sin revisar
# - Verifica que sea correcta
# - Ajusta según tu contexto
# - Agrega detalles específicos
```

---

## 🎯 Ejercicios

1. Genera docstrings para todas las funciones de un módulo
2. Crea un README completo para un proyecto
3. Documenta un pipeline ETL complejo
4. Genera guía de uso para una librería

---

## 🚀 Próximo paso

Continúa con **[Límites de la AI](limites-de-la-ai.md)** para entender qué NO puede hacer la AI.

---

> **Recuerda**: La documentación generada por AI es un buen punto de partida, pero siempre necesita revisión y ajuste según tu contexto específico.
