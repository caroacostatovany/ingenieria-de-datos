# Cómo usar AI como Data Engineer

La AI puede ser un copiloto poderoso para Data Engineers. Aprende cuándo y cómo usarla efectivamente.

---

## 🧠 ¿Cuándo usar AI?

### ✅ Usa AI para:

**1. Generar código boilerplate**
```python
# Prompt: "Crea una función Python que lea un CSV y retorne un DataFrame con validación de esquema"
# La AI genera el código base, tú lo revisas y ajustas
```

**2. Explicar código existente**
```python
# Selecciona código complejo y pregunta: "¿Qué hace este código?"
# La AI explica la lógica, tú validas que sea correcto
```

**3. Refactorizar código**
```python
# Prompt: "Refactoriza esta función para que sea más legible y eficiente"
# La AI sugiere mejoras, tú decides qué aplicar
```

**4. Generar documentación**
```python
# Prompt: "Genera docstrings para estas funciones siguiendo el estilo Google"
# La AI crea documentación, tú la revisas y ajustas
```

**5. Crear tests**
```python
# Prompt: "Crea tests unitarios para esta función usando pytest"
# La AI genera tests, tú los ejecutas y ajustas
```

**6. Debugging asistido**
```python
# Pega el error y pregunta: "¿Por qué falla este código?"
# La AI sugiere causas, tú investigas y solucionas
```

**7. Generar queries SQL**
```sql
-- Prompt: "Crea una query SQL que calcule ventas por mes con crecimiento mes a mes"
-- La AI genera la query, tú la validas y optimizas
```

---

## ❌ NO uses AI para:

**1. Reemplazar tu entendimiento**
* ❌ No uses código que no entiendas
* ❌ No copies sin revisar
* ❌ No confíes ciegamente

**2. Decisiones de arquitectura críticas**
* ❌ No dejes que AI diseñe sistemas complejos
* ❌ No uses sugerencias sin validar impacto

**3. Datos sensibles o secretos**
* ❌ No compartas datos reales con AI
* ❌ No uses credenciales en prompts

**4. Lógica de negocio compleja**
* ❌ No uses AI para reglas de negocio sin validar
* ❌ No confíes en cálculos críticos sin verificar

---

## 🔄 Flujo de trabajo recomendado

### 1. Define el problema claramente

**❌ Mal prompt:**
```
"haz un pipeline"
```

**✅ Buen prompt:**
```
"Crea una función Python que:
1. Lea un archivo CSV de ventas
2. Valide que tenga las columnas: fecha, producto_id, cantidad, precio
3. Calcule el total (cantidad * precio)
4. Retorne un DataFrame con los datos procesados
5. Maneje errores si el archivo no existe"
```

### 2. Genera código con AI

Usa el prompt claro para generar código inicial.

### 3. Revisa y entiende

**Siempre:**
* Lee el código generado
* Entiende qué hace cada parte
* Verifica la lógica

### 4. Valida y prueba

**Siempre:**
* Ejecuta el código
* Prueba casos edge
* Verifica resultados

### 5. Ajusta y mejora

**Siempre:**
* Refina según tus necesidades
* Optimiza si es necesario
* Documenta cambios importantes

---

## 🛠️ Herramientas recomendadas

### Para código

* **Cursor**: Editor con AI integrada (recomendado)
* **GitHub Copilot**: Extensión para VS Code
* **ChatGPT/Claude**: Para consultas y explicaciones

### Para documentación

* **Cursor Chat**: Para generar documentación
* **ChatGPT**: Para explicar conceptos complejos

### Para SQL

* **Cursor**: Para generar queries SQL
* **ChatGPT**: Para optimizar queries existentes

---

## 💡 Casos de uso prácticos

### Caso 1: Crear pipeline ETL básico

**Prompt:**
```
"Crea un pipeline ETL en Python que:
1. Extraiga datos de un CSV
2. Transforme: limpie nulos, calcule totales
3. Cargue a Parquet
4. Incluya logging y manejo de errores"
```

**Resultado:** Código base que revisas y ajustas.

### Caso 2: Explicar código complejo

**Acción:**
1. Selecciona código que no entiendes
2. Pregunta: "Explica qué hace este código paso a paso"
3. La AI explica, tú validas

### Caso 3: Optimizar query SQL

**Prompt:**
```
"Optimiza esta query SQL para que sea más rápida:
[pega tu query]

La tabla tiene índices en: fecha_venta, producto_id
Tiene 10 millones de filas"
```

**Resultado:** Sugerencias de optimización que validas.

### Caso 4: Generar tests

**Prompt:**
```
"Crea tests unitarios para esta función usando pytest:
[pega tu función]

Incluye:
- Test de caso normal
- Test de caso edge (valores nulos)
- Test de error esperado"
```

---

## 🎯 Mejores prácticas

### 1. Prompts específicos

```python
# ❌ Vago
"haz una función"

# ✅ Específico
"Crea una función Python llamada 'procesar_ventas' que:
- Recibe un DataFrame con columnas: fecha, producto_id, cantidad, precio
- Valida que todas las columnas existan
- Calcula total = cantidad * precio
- Retorna el DataFrame con una columna adicional 'total'
- Maneja errores con try/except y logging"
```

### 2. Contexto suficiente

```python
# ✅ Proporciona contexto
"""
Estoy trabajando con un pipeline ETL que procesa ventas.
Necesito una función que:
- Lea de PostgreSQL (usando sqlalchemy)
- Transforme los datos
- Escriba a S3 en formato Parquet
- Use variables de entorno para credenciales
"""
```

### 3. Iteración y refinamiento

```python
# Primera iteración: Genera código básico
# Segunda iteración: "Agrega validación de esquema"
# Tercera iteración: "Optimiza para grandes volúmenes"
```

### 4. Validación siempre

```python
# ✅ Siempre valida
def funcion_generada_por_ai():
    # Código generado
    pass

# Ejecuta y verifica
resultado = funcion_generada_por_ai()
assert resultado is not None
assert len(resultado) > 0
```

---

## 🚨 Errores comunes

### 1. Confiar sin validar

```python
# ❌ Mal
codigo_ai = generar_codigo()
ejecutar(codigo_ai)  # Sin revisar

# ✅ Bien
codigo_ai = generar_codigo()
revisar(codigo_ai)  # Entender qué hace
testear(codigo_ai)  # Probar
ejecutar(codigo_ai)  # Solo entonces
```

### 2. Prompts vagos

```python
# ❌ Mal
"haz algo con datos"

# ✅ Bien
"Crea una función que procese ventas diarias y calcule totales por categoría"
```

### 3. No entender el código

```python
# ❌ Mal
# Usar código sin entenderlo

# ✅ Bien
# Leer, entender, validar, luego usar
```

---

## 🎯 Ejercicios

1. Genera un pipeline ETL básico con AI y revísalo
2. Usa AI para explicar código complejo que no entiendas
3. Genera tests para una función existente
4. Optimiza una query SQL con ayuda de AI

---

## 🚀 Próximo paso

Continúa con **[Ejemplos de Prompts](ejemplos-prompts.md)** para ver prompts efectivos específicos.

---

> **Recuerda**: La AI es un copiloto, no un piloto. Tú siempre estás al control y eres responsable del código que produces.
