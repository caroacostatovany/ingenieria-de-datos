# Storytelling con Datos

Aprende a contar historias efectivas con datos y comunicar tus hallazgos a personas de negocios y stakeholders. Basado en principios de "Storytelling with Data" de Cole Nussbaumer Knaflic.

> 💡 **Ejemplo práctico**: Revisa el [notebook de storytelling](../ejemplos/02-storytelling-datos.ipynb) para ver visualizaciones buenas vs malas y ejemplos completos usando datos reales.

---

## 🧠 ¿Por qué storytelling?

Los datos por sí solos no comunican. Necesitas **contar una historia** que:

* **Enganche** a tu audiencia (especialmente personas de negocios)
* **Explique** el contexto y el "por qué"
* **Muestre** insights claramente sin jerga técnica
* **Lleve a la acción** con recomendaciones concretas

> 💡 **En Data Engineering**: No solo construyes pipelines, también necesitas **comunicar resultados** a ejecutivos, product managers, y otros stakeholders que no son técnicos. El storytelling es tu puente entre datos técnicos y decisiones de negocio.

> No es sobre los datos. Es sobre lo que los datos significan y qué hacer con esa información.

---

## 🎯 Principios fundamentales

### 1. Conoce tu audiencia

**Preguntas clave:**
* ¿Quién es tu audiencia? (Ejecutivos, analistas, técnicos, clientes)
* ¿Qué saben sobre el tema?
* ¿Qué necesitan saber para tomar decisiones?
* ¿Qué acción quieres que tomen?

**Ejemplo para personas de negocios:**
```python
# ❌ Mal: Muestra todos los datos sin contexto
df.plot()
# Demasiado técnico, sin contexto de negocio

# ✅ Bien: Enfócate en lo que importa a ejecutivos
# - Muestra tendencias y comparaciones
# - Destaca métricas de negocio (ventas, crecimiento, ROI)
# - Incluye recomendaciones accionables
# - Usa lenguaje de negocio, no técnico

# Ejemplo para ejecutivos:
print("""
📊 Resumen Ejecutivo - Ventas Q1 2024

Situación: Las ventas aumentaron 12% vs Q1 2023
Insight clave: La categoría Electrónica lidera con 45% del total
Recomendación: Aumentar inventario de productos top 3
""")
```

**Diferencia clave:**
* **Para ejecutivos**: Resumen alto nivel, métricas de negocio, recomendaciones claras
* **Para técnicos**: Detalles, metodología, código, validaciones
* **Para analistas**: Datos intermedios, exploración, hipótesis

### 2. Elige el gráfico correcto

**Guía rápida:**

| Propósito | Gráfico recomendado |
|-----------|---------------------|
| Comparar categorías | Bar chart |
| Mostrar tendencia en el tiempo | Line chart |
| Mostrar partes de un todo | Pie chart (solo si pocas categorías) |
| Mostrar relación | Scatter plot |
| Mostrar distribución | Histograma |

### 3. Elimina el ruido visual

**Principio:** Elimina todo lo que no aporta información.

```python
# ❌ Mal: Mucho ruido
plt.figure(figsize=(10, 6))
ax = df.plot(kind='bar', x='categoria', y='ventas')
ax.set_title('Ventas por Categoría', fontsize=16, fontweight='bold')
ax.set_xlabel('Categoría', fontsize=14)
ax.set_ylabel('Ventas', fontsize=14)
ax.grid(True, alpha=0.3)
ax.legend()
plt.xticks(rotation=45)
# ... más código innecesario

# ✅ Bien: Simple y claro
plt.figure(figsize=(8, 5))
df.plot(kind='bar', x='categoria', y='ventas', color='steelblue')
plt.title('Ventas por Categoría')
plt.xlabel('')
plt.ylabel('Ventas (€)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
```

### 4. Dirige la atención

**Usa:**
* **Color** estratégicamente (no todo en color)
* **Tamaño** para enfatizar
* **Posición** (lo más importante arriba/izquierda)

```python
# ✅ Enfatiza lo importante
colores = ['red' if x == max(df['ventas']) else 'steelblue' 
           for x in df['ventas']]
df.plot(kind='bar', x='categoria', y='ventas', color=colores)
```

---

## 📖 Estructura de una historia con datos

### 1. Contexto (Beginning) - El "Por qué"

**Establece para tu audiencia de negocio:**
* ¿Qué problema de negocio estamos resolviendo?
* ¿Por qué es importante para la empresa?
* ¿Qué impacto tiene en métricas clave (ventas, costos, satisfacción)?
* ¿Qué datos tenemos disponibles?

```python
# Ejemplo de contexto para ejecutivos
"""
📊 Análisis de Ventas Q1 2024

Situación de negocio:
- Las ventas han disminuido 15% comparado con Q1 2023
- Impacto estimado: €500K en ingresos perdidos
- Pregunta clave: ¿Qué está causando esta disminución?

Objetivo:
- Identificar causas raíz
- Proponer acciones correctivas
- Recuperar crecimiento

Datos disponibles:
- Ventas diarias (30 días)
- Productos y categorías
- Regiones y ciudades
- Comparación año anterior
"""
```

> 💡 **Para personas de negocios**: Siempre empieza con el impacto en el negocio, no con los datos técnicos. Conecta los datos con objetivos empresariales.

### 2. Conflicto/Insight (Middle) - El "Qué"

**Muestra para personas de negocios:**
* ¿Qué encontraste? (en lenguaje de negocio)
* ¿Qué patrones identificaste? (conectados a acciones)
* ¿Qué es sorprendente o importante? (impacto en métricas)

```python
# Visualización que muestra el insight
plt.figure(figsize=(10, 6))
df_2023.plot(label='2023', linewidth=2, color='steelblue')
df_2024.plot(label='2024', linewidth=2, style='--', color='darkred')
plt.axvline(x='2024-02-15', color='orange', linestyle=':', 
            linewidth=2, label='Cambio de estrategia')
plt.title('Ventas Q1: Comparación 2023 vs 2024', fontsize=14, fontweight='bold')
plt.ylabel('Ventas Diarias (€)')
plt.xlabel('Fecha')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Insight claro para ejecutivos
print("""
🔍 Hallazgos Principales:

1. Caída del 15% en ventas totales
   - Impacto: €500K en ingresos perdidos
   - Período crítico: Después del 15 de febrero

2. Categoría 'Electrónica' más afectada
   - Disminución del 25% vs 2023
   - Representa 40% de nuestras ventas totales

3. Coincidencia temporal
   - La caída coincide con cambio de estrategia de marketing
   - Necesitamos investigar la relación causal
""")
```

> 💡 **Para personas de negocios**: Traduce insights técnicos a lenguaje de negocio. En lugar de "correlación del 0.85", di "fuerte relación entre X e Y que explica el 85% de la variación".

### 3. Resolución/Acción (End) - El "Cómo"

**Proporciona para personas de negocios:**
* ¿Qué significa esto para el negocio? (impacto)
* ¿Qué acciones recomiendas? (concretas y accionables)
* ¿Qué sigue? (próximos pasos con responsables)

```python
# Recomendaciones basadas en datos (formato ejecutivo)
recomendaciones = """
✅ Acciones Recomendadas (Priorizadas):

1. 🔴 URGENTE: Revisar estrategia de marketing
   - Acción: Analizar campaña implementada el 15/02
   - Responsable: Marketing Manager
   - Timeline: Esta semana
   - Impacto esperado: Identificar causa raíz

2. 🟡 ALTA PRIORIDAD: Campaña de recuperación para Electrónica
   - Acción: Lanzar promoción específica para productos top
   - Responsable: Product Manager + Marketing
   - Timeline: Próximas 2 semanas
   - Impacto esperado: Recuperar 10-15% de ventas perdidas

3. 🟢 MEDIANO PLAZO: Monitoreo y alertas
   - Acción: Dashboard de métricas semanales
   - Responsable: Data Engineering
   - Timeline: 1 mes
   - Impacto esperado: Detección temprana de problemas

4. 📊 SEGUIMIENTO: Revisión mensual
   - Acción: Reunión de seguimiento con métricas actualizadas
   - Responsable: Data Analyst
   - Timeline: Mensual
   - Impacto esperado: Ajuste continuo de estrategia
"""

print(recomendaciones)
```

> 💡 **Para personas de negocios**: Las recomendaciones deben ser:
> - **Concretas**: No "mejorar marketing", sino "lanzar campaña X para producto Y"
> - **Accionables**: Con responsables y timelines claros
> - **Con impacto**: Muestra el valor esperado de cada acción
> - **Priorizadas**: Usa un sistema claro (urgente, alta, media prioridad)

---

## 🎨 Visualizaciones efectivas

### 1. Gráfico de barras (comparar categorías)

```python
import matplotlib.pyplot as plt
import pandas as pd

# ✅ Buen gráfico de barras
plt.figure(figsize=(10, 6))
df_sorted = df.sort_values('ventas', ascending=True)
plt.barh(df_sorted['categoria'], df_sorted['ventas'], color='steelblue')
plt.xlabel('Ventas (€)')
plt.title('Ventas por Categoría - Q1 2024')
plt.tight_layout()
plt.show()
```

**Por qué funciona:**
* Ordenado (fácil de comparar)
* Horizontal (mejor para etiquetas largas)
* Color simple
* Título claro

### 2. Gráfico de líneas (tendencias)

```python
# ✅ Buen gráfico de líneas
plt.figure(figsize=(12, 6))
plt.plot(df['fecha'], df['ventas'], marker='o', linewidth=2, markersize=4)
plt.axhline(y=df['ventas'].mean(), color='red', linestyle='--', 
            label=f'Promedio: {df["ventas"].mean():.0f}€')
plt.title('Tendencia de Ventas Diarias')
plt.xlabel('Fecha')
plt.ylabel('Ventas (€)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

### 3. Scatter plot (relaciones)

```python
# ✅ Buen scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['edad'], df['gasto'], alpha=0.6, s=50)
plt.xlabel('Edad')
plt.ylabel('Gasto Mensual (€)')
plt.title('Relación entre Edad y Gasto')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

---

## ❌ Trampas comunes a evitar

### 1. Gráficos 3D innecesarios

```python
# ❌ Mal: 3D innecesario
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.bar3d(...)  # Difícil de leer

# ✅ Bien: 2D claro
plt.bar(df['categoria'], df['ventas'])
```

### 2. Demasiados colores

```python
# ❌ Mal: Arcoíris innecesario
df.plot(color=['red', 'blue', 'green', 'yellow', 'purple', 'orange'])

# ✅ Bien: Colores estratégicos
df.plot(color=['steelblue', 'darkred'])  # Solo 2 líneas, 2 colores
```

### 3. Ejes que no empiezan en cero (cuando es apropiado)

```python
# ⚠️ Para comparaciones, empieza en 0
plt.bar(df['categoria'], df['ventas'])
plt.ylim(0, max(df['ventas']) * 1.1)  # Empieza en 0

# ✅ Para tendencias, puedes ajustar el rango
plt.plot(df['fecha'], df['ventas'])
plt.ylim(df['ventas'].min() * 0.9, df['ventas'].max() * 1.1)
```

### 4. Información innecesaria

```python
# ❌ Mal: Grid, leyenda innecesaria, etc.
df.plot(grid=True, legend=True, title='Ventas', 
        xlabel='Fecha', ylabel='€', style='-o')

# ✅ Bien: Solo lo esencial
df.plot(title='Ventas')
plt.ylabel('Ventas (€)')
```

---

## 📊 Caso práctico: Historia completa

### Paso 1: Contexto

```python
"""
Situación: Las ventas del Q1 2024 han disminuido 15% vs Q1 2023
Pregunta: ¿Qué está causando esta disminución?
Datos: Ventas diarias, productos, categorías, regiones
"""
```

### Paso 2: Exploración

```python
# Cargar y explorar
df_2023 = pd.read_csv('ventas_2023_q1.csv')
df_2024 = pd.read_csv('ventas_2024_q1.csv')

# Comparar totales
print(f"2023 Q1: {df_2023['total'].sum():,.0f}€")
print(f"2024 Q1: {df_2024['total'].sum():,.0f}€")
print(f"Diferencia: {(df_2024['total'].sum() / df_2023['total'].sum() - 1) * 100:.1f}%")
```

### Paso 3: Visualización del insight

```python
# Comparar tendencias
plt.figure(figsize=(12, 6))
plt.plot(df_2023['fecha'], df_2023['total'], 
         label='2023', linewidth=2, color='steelblue')
plt.plot(df_2024['fecha'], df_2024['total'], 
         label='2024', linewidth=2, color='darkred', linestyle='--')

# Marcar punto de cambio
plt.axvline(x='2024-02-15', color='orange', linestyle=':', 
            linewidth=2, label='Cambio de estrategia')

plt.title('Ventas Q1: Comparación 2023 vs 2024', fontsize=14, fontweight='bold')
plt.xlabel('Fecha')
plt.ylabel('Ventas Diarias (€)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### Paso 4: Análisis por categoría

```python
# Agrupar por categoría
ventas_cat_2023 = df_2023.groupby('categoria')['total'].sum()
ventas_cat_2024 = df_2024.groupby('categoria')['total'].sum()
cambio = ((ventas_cat_2024 / ventas_cat_2023 - 1) * 100).sort_values()

# Visualizar
plt.figure(figsize=(10, 6))
colores = ['darkred' if x < -10 else 'steelblue' for x in cambio]
plt.barh(cambio.index, cambio.values, color=colores)
plt.xlabel('Cambio % vs 2023')
plt.title('Cambio de Ventas por Categoría: Q1 2024 vs 2023')
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.5)
plt.tight_layout()
plt.show()
```

### Paso 5: Recomendaciones

```python
"""
Hallazgos:
1. Caída del 15% en ventas totales
2. Caída más pronunciada después del 15 de febrero
3. Categoría 'Electrónica' más afectada (-25%)

Recomendaciones:
1. Revisar estrategia de marketing implementada el 15/02
2. Investigar por qué 'Electrónica' fue más afectada
3. Considerar campaña específica para recuperar ventas
4. Monitorear métricas semanalmente
"""
```

---

## 💡 Principios clave

### 1. Menos es más

```python
# ✅ Simple y claro
plt.bar(df['categoria'], df['ventas'])
plt.title('Ventas por Categoría')
plt.show()
```

### 2. Enfócate en lo importante

```python
# ✅ Destaca lo importante
colores = ['red' if x == max(df['ventas']) else 'gray' 
           for x in df['ventas']]
plt.bar(df['categoria'], df['ventas'], color=colores)
plt.title('Ventas por Categoría - Electrónica lidera')
plt.show()
```

### 3. Cuenta una historia

```python
# ✅ Secuencia que cuenta una historia
# Gráfico 1: Situación actual
# Gráfico 2: Comparación con período anterior
# Gráfico 3: Desglose por categoría
# Gráfico 4: Recomendaciones
```

### 4. Sé honesto con los datos

```python
# ✅ No distorsiones
# - Empieza ejes en 0 cuando compares magnitudes
# - Muestra incertidumbre cuando exista
# - No ocultes datos que no apoyan tu narrativa
```

---

## 🎯 Estructura de presentación

### 1. Título claro

```python
# ❌ Mal
plt.title('Datos')

# ✅ Bien
plt.title('Ventas Q1 2024: Disminución del 15% vs 2023')
```

### 2. Etiquetas descriptivas

```python
# ❌ Mal
plt.xlabel('x')
plt.ylabel('y')

# ✅ Bien
plt.xlabel('Categoría')
plt.ylabel('Ventas (miles de €)')
```

### 3. Anotaciones cuando sea necesario

```python
# ✅ Agrega contexto
plt.annotate('Cambio de estrategia', 
             xy=('2024-02-15', 5000),
             xytext=(10, 10),
             textcoords='offset points',
             arrowprops=dict(arrowstyle='->'))
```

---

## 💼 Comunicando con personas de negocios

### Lenguaje de negocio vs técnico

```python
# ❌ Técnico (evitar con ejecutivos)
"""
Encontramos una correlación de 0.85 entre la variable X y Y.
El p-value es 0.001, indicando significancia estadística.
El modelo tiene un R² de 0.72.
"""

# ✅ Lenguaje de negocio (usar con ejecutivos)
"""
Los datos muestran una relación fuerte entre la campaña de marketing
y las ventas. Esta relación explica el 72% de las variaciones en ventas,
lo que significa que podemos predecir con confianza el impacto de futuras
campañas. La probabilidad de que esto sea casualidad es menor al 0.1%.
"""
```

### Métricas que importan a ejecutivos

```python
# Enfócate en métricas de negocio:
metricas_negocio = {
    'Ingresos': '€500K',
    'Crecimiento': '+12% vs año anterior',
    'ROI': '3.5x retorno de inversión',
    'Tiempo de recuperación': '2 meses',
    'Impacto en clientes': '+15% satisfacción'
}

# No solo métricas técnicas:
# - R², p-values, correlaciones (a menos que sea necesario)
# - Detalles de implementación técnica
# - Complejidad del modelo
```

### Estructura de presentación para ejecutivos

```python
"""
1. RESUMEN EJECUTIVO (1 slide)
   - Situación en 1-2 frases
   - Hallazgo principal
   - Recomendación clave

2. CONTEXTO (1-2 slides)
   - Problema de negocio
   - Por qué es importante
   - Métricas actuales

3. HALLAZGOS (2-3 slides)
   - Insights principales con visualizaciones
   - Comparaciones relevantes
   - Patrones identificados

4. RECOMENDACIONES (1-2 slides)
   - Acciones priorizadas
   - Responsables y timelines
   - Impacto esperado

5. PRÓXIMOS PASOS (1 slide)
   - Seguimiento
   - Métricas a monitorear
"""
```

---

## 🚀 Próximo paso

Aplica estos principios en tus análisis. Practica creando visualizaciones que cuenten historias claras y comuniquen efectivamente con personas de negocios.

**Práctica recomendada:**
1. Toma un análisis que hayas hecho
2. Reescríbelo para una audiencia ejecutiva
3. Elimina jerga técnica
4. Enfócate en impacto de negocio y acciones
5. Crea visualizaciones simples y claras

---

## 📚 Siguiente etapa: Modelado y Calidad de Datos

Después de dominar Python, manejo de archivos y comunicación de datos, el siguiente paso en tu ruta de aprendizaje es:

### **[Modelado y Calidad de Datos](../../04_modelado_y_calidad/)**

En este módulo aprenderás:

* **Modelado Analítico**: Diseñar modelos de datos para analytics (Star Schema, Snowflake, tablas de hechos y dimensiones)
* **Calidad de Datos**: Asegurar que tus datos sean confiables, completos y consistentes
* **Validaciones**: Implementar tests y validaciones en tus pipelines
* **Herramientas**: Great Expectations y otras herramientas para garantizar calidad

> 💡 **Flujo de aprendizaje**: Fundamentos Python → Pandas → Storytelling → **Modelado y Calidad** → Pipelines → Proyectos

Continúa con: **[04_modelado_y_calidad/](../../04_modelado_y_calidad/README.md)**

---

## 💼 Checklist para presentar a ejecutivos

Antes de presentar a personas de negocios, verifica:

### ✅ Contenido
- [ ] ¿El mensaje principal está claro en 30 segundos?
- [ ] ¿Usas lenguaje de negocio, no técnico?
- [ ] ¿Las métricas están conectadas a objetivos empresariales?
- [ ] ¿Las recomendaciones son concretas y accionables?
- [ ] ¿Hay un "call to action" claro?

### ✅ Visualizaciones
- [ ] ¿Los gráficos son simples y fáciles de entender?
- [ ] ¿Eliminaste ruido visual innecesario?
- [ ] ¿Los colores tienen propósito (no decorativo)?
- [ ] ¿Las etiquetas son claras y descriptivas?
- [ ] ¿El título cuenta la historia?

### ✅ Estructura
- [ ] ¿Empiezas con el impacto en el negocio?
- [ ] ¿El flujo lógico es claro (problema → hallazgo → solución)?
- [ ] ¿Cada slide tiene un propósito claro?
- [ ] ¿Terminas con acciones concretas?

---

## 📚 Referencias

Basado en principios de:
* **"Storytelling with Data"** - Cole Nussbaumer Knaflic
* **"The Visual Display of Quantitative Information"** - Edward Tufte

---

> **Recuerda**: Los datos son el medio, no el mensaje. Tu trabajo es extraer el mensaje y comunicarlo claramente a personas de negocios que tomarán decisiones basadas en tu análisis.
