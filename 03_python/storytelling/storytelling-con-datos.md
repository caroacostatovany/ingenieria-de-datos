# Storytelling con Datos

Aprende a contar historias efectivas con datos. Basado en principios de "Storytelling with Data" de Cole Nussbaumer Knaflic.

> 💡 **Ejemplo práctico**: Revisa el [notebook de storytelling](../ejemplos/02-storytelling-datos.ipynb) para ver visualizaciones buenas vs malas y ejemplos completos.

---

## 🧠 ¿Por qué storytelling?

Los datos por sí solos no comunican. Necesitas **contar una historia** que:

* **Enganche** a tu audiencia
* **Explique** el contexto
* **Muestre** insights claramente
* **Lleve a la acción**

> No es sobre los datos. Es sobre lo que los datos significan y qué hacer con esa información.

---

## 🎯 Principios fundamentales

### 1. Conoce tu audiencia

**Preguntas clave:**
* ¿Quién es tu audiencia?
* ¿Qué saben sobre el tema?
* ¿Qué necesitan saber?
* ¿Qué acción quieres que tomen?

**Ejemplo:**
```python
# ❌ Mal: Muestra todos los datos sin contexto
df.plot()

# ✅ Bien: Enfócate en lo que importa a tu audiencia
# Si es para ejecutivos: muestra tendencias y acciones recomendadas
# Si es para técnicos: muestra detalles y metodología
```

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

### 1. Contexto (Beginning)

**Establece:**
* ¿Qué problema estamos resolviendo?
* ¿Por qué es importante?
* ¿Qué datos tenemos?

```python
# Ejemplo de contexto
"""
Análisis de ventas Q1 2024

Problema: Las ventas han disminuido 15% comparado con Q1 2023
Objetivo: Identificar causas y proponer acciones
Datos: Ventas diarias, productos, categorías, regiones
"""
```

### 2. Conflicto/Insight (Middle)

**Muestra:**
* ¿Qué encontraste?
* ¿Qué patrones identificaste?
* ¿Qué es sorprendente o importante?

```python
# Visualización que muestra el insight
plt.figure(figsize=(10, 6))
df_2023.plot(label='2023', linewidth=2)
df_2024.plot(label='2024', linewidth=2, style='--')
plt.axvline(x='2024-02-15', color='red', linestyle=':', 
            label='Cambio de estrategia')
plt.title('Ventas Q1: 2023 vs 2024')
plt.ylabel('Ventas (€)')
plt.legend()
plt.show()

# Insight claro
print("""
Insight principal:
- Las ventas cayeron 15% después del 15 de febrero
- Coincide con cambio de estrategia de marketing
- Categoría 'Electrónica' más afectada (-25%)
""")
```

### 3. Resolución/Acción (End)

**Proporciona:**
* ¿Qué significa esto?
* ¿Qué acciones recomiendas?
* ¿Qué sigue?

```python
# Recomendaciones basadas en datos
recomendaciones = """
Acciones recomendadas:
1. Revisar estrategia de marketing implementada el 15/02
2. Investigar por qué 'Electrónica' fue más afectada
3. Considerar campaña específica para recuperar ventas
4. Monitorear métricas semanalmente
"""
```

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

## 🚀 Próximo paso

Aplica estos principios en tus análisis. Practica creando visualizaciones que cuenten historias claras.

---

## 📚 Referencias

Basado en principios de:
* **"Storytelling with Data"** - Cole Nussbaumer Knaflic
* **"The Visual Display of Quantitative Information"** - Edward Tufte

---

> **Recuerda**: Los datos son el medio, no el mensaje. Tu trabajo es extraer el mensaje y comunicarlo claramente.
