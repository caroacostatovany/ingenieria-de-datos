# Calidad de Datos

La calidad de datos es fundamental para confiar en tus análisis y decisiones. Aprende a medir y mejorar la calidad.

---

## 🧠 ¿Qué es calidad de datos?

Datos de calidad son:
* **Completos**: Sin valores faltantes críticos
* **Exactos**: Reflejan la realidad
* **Consistentes**: Coherentes entre sistemas
* **Oportunos**: Disponibles cuando se necesitan
* **Válidos**: Cumplen reglas de negocio
* **Únicos**: Sin duplicados no deseados

> La calidad de datos no es perfecta, es "suficientemente buena" para el propósito.

---

## 📊 Dimensiones de calidad

### 1. Completitud (Completeness)

¿Qué porcentaje de datos está presente?

```python
# Calcular completitud
completitud = (datos_no_nulos / total_datos) * 100

# Ejemplo
total_filas = len(df)
filas_completas = len(df.dropna())
completitud = (filas_completas / total_filas) * 100
print(f"Completitud: {completitud:.2f}%")
```

**Umbrales típicos:**
* ✅ > 95%: Excelente
* ⚠️ 80-95%: Aceptable (investigar)
* ❌ < 80%: Problema crítico

### 2. Exactitud (Accuracy)

¿Los datos son correctos?

```python
# Validar rangos esperados
df['edad'].between(0, 120).sum() / len(df) * 100

# Validar formatos
df['email'].str.contains('@').sum() / len(df) * 100

# Comparar con fuente de verdad
df_validado = df[df['edad'].between(0, 120)]
exactitud = len(df_validado) / len(df) * 100
```

### 3. Consistencia (Consistency)

¿Los datos son coherentes entre sistemas?

```python
# Validar relaciones
# Ejemplo: suma de items debe igualar total
df['suma_items'] = df.groupby('orden_id')['precio'].transform('sum')
inconsistencias = df[df['suma_items'] != df['total']]
tasa_consistencia = (1 - len(inconsistencias) / len(df)) * 100
```

### 4. Validez (Validity)

¿Los datos cumplen reglas de negocio?

```python
# Validar reglas
reglas_cumplidas = (
    df['precio'] > 0 &
    df['cantidad'] > 0 &
    df['fecha'] >= '2020-01-01'
).sum()
validez = reglas_cumplidas / len(df) * 100
```

### 5. Unicidad (Uniqueness)

¿Hay duplicados no deseados?

```python
# Detectar duplicados
duplicados = df.duplicated().sum()
unicidad = (1 - duplicados / len(df)) * 100
```

### 6. Oportunidad (Timeliness)

¿Los datos están disponibles a tiempo?

```python
# Verificar retraso en datos
from datetime import datetime

fecha_ultima_actualizacion = df['fecha_actualizacion'].max()
fecha_esperada = datetime.now()
retraso = (fecha_esperada - fecha_ultima_actualizacion).days

if retraso > 1:
    print(f"⚠️ Datos con {retraso} días de retraso")
```

---

## 📈 Métricas y KPIs

### Scorecard de calidad

```python
def calcular_scorecard_calidad(df):
    """Calcula métricas de calidad."""
    metrics = {
        'completitud': calcular_completitud(df),
        'exactitud': calcular_exactitud(df),
        'consistencia': calcular_consistencia(df),
        'validez': calcular_validez(df),
        'unicidad': calcular_unicidad(df)
    }
    
    # Score general (promedio ponderado)
    score_general = (
        metrics['completitud'] * 0.3 +
        metrics['exactitud'] * 0.3 +
        metrics['consistencia'] * 0.2 +
        metrics['validez'] * 0.1 +
        metrics['unicidad'] * 0.1
    )
    
    metrics['score_general'] = score_general
    return metrics
```

### Dashboard de calidad

```python
import pandas as pd
import matplotlib.pyplot as plt

def crear_dashboard_calidad(df):
    """Crea visualización de calidad."""
    metrics = calcular_scorecard_calidad(df)
    
    # Gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(metrics.keys(), metrics.values())
    plt.title('Scorecard de Calidad de Datos')
    plt.ylabel('Porcentaje')
    plt.ylim(0, 100)
    plt.show()
```

---

## 🔍 Detección de problemas

### Análisis exploratorio de calidad

```python
def analizar_calidad(df):
    """Análisis completo de calidad."""
    reporte = {
        'filas': len(df),
        'columnas': len(df.columns),
        'nulos_por_columna': df.isnull().sum().to_dict(),
        'porcentaje_nulos': (df.isnull().sum() / len(df) * 100).to_dict(),
        'duplicados': df.duplicated().sum(),
        'tipos_datos': df.dtypes.to_dict(),
        'valores_unicos_por_columna': df.nunique().to_dict()
    }
    return reporte
```

### Detectar anomalías

```python
def detectar_anomalias(df, columna):
    """Detecta valores anómalos usando IQR."""
    Q1 = df[columna].quantile(0.25)
    Q3 = df[columna].quantile(0.75)
    IQR = Q3 - Q1
    
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    
    anomalias = df[
        (df[columna] < limite_inferior) | 
        (df[columna] > limite_superior)
    ]
    
    return anomalias
```

---

## 🛠️ Estrategias de mejora

### 1. Prevención

**En la fuente:**
* Validaciones en el sistema origen
* Formularios con validación
* Constraints en base de datos

### 2. Detección temprana

**En el pipeline:**
* Validaciones en cada etapa
* Alertas automáticas
* Checks de calidad

### 3. Corrección

**Opciones:**
* **Eliminar**: Si no son críticos
* **Rellenar**: Con valores por defecto o estimados
* **Corregir**: Basado en reglas o fuentes externas
* **Marcar**: Para revisión manual

```python
def corregir_datos(df):
    """Aplica correcciones automáticas."""
    # Rellenar nulos con mediana
    df['precio'].fillna(df['precio'].median(), inplace=True)
    
    # Corregir valores fuera de rango
    df.loc[df['edad'] < 0, 'edad'] = None
    df.loc[df['edad'] > 120, 'edad'] = None
    
    # Normalizar texto
    df['email'] = df['email'].str.lower().str.strip()
    
    return df
```

---

## 📋 Checklist de calidad

Antes de usar datos en producción:

- [ ] Completitud > 95% en columnas críticas
- [ ] Sin duplicados no deseados
- [ ] Valores dentro de rangos esperados
- [ ] Formatos correctos (emails, fechas, etc.)
- [ ] Relaciones consistentes (foreign keys válidos)
- [ ] Datos actualizados (timeliness)
- [ ] Documentación de calidad disponible

---

## 🎯 Ejercicios

1. Calcula métricas de calidad para un dataset
2. Crea un dashboard de calidad
3. Detecta y corrige problemas comunes
4. Implementa validaciones en un pipeline

---

## 🚀 Próximo paso

Continúa con **[Validaciones](validaciones.md)** para implementar checks automáticos.

---

> **Recuerda**: La calidad de datos es un proceso continuo, no un evento único. Monitorea y mejora constantemente.
