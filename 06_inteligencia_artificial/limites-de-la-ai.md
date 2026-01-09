# Límites de la AI

Entender qué NO puede hacer la AI es tan importante como saber qué puede hacer. Conoce los límites para usarla efectivamente.

---

## 🚨 Qué NO puede hacer la AI

### 1. Entender tu contexto de negocio

**❌ No puede:**
* Conocer reglas de negocio específicas
* Entender requisitos no documentados
* Saber qué datos son críticos para tu empresa

**✅ Tú debes:**
* Validar que el código cumpla reglas de negocio
* Verificar que los cálculos sean correctos
* Asegurar que los datos sean apropiados

### 2. Reemplazar tu conocimiento técnico

**❌ No puede:**
* Entender arquitectura de sistemas complejos
* Decidir qué tecnología usar
* Diseñar soluciones escalables

**✅ Tú debes:**
* Entender los fundamentos
* Tomar decisiones arquitectónicas
* Validar que las soluciones sean apropiadas

### 3. Garantizar código correcto

**❌ No puede:**
* Generar código 100% correcto siempre
* Conocer todos los edge cases
* Predecir todos los errores

**✅ Tú debes:**
* Revisar todo el código generado
* Probar exhaustivamente
* Validar resultados

### 4. Acceder a información privada

**❌ No puede:**
* Ver tus datos reales (a menos que los compartas)
* Acceder a sistemas internos
* Conocer secretos o credenciales

**✅ Tú debes:**
* Nunca compartir datos sensibles
* No incluir credenciales en prompts
* Usar datos de ejemplo para testing

### 5. Mantener código actualizado

**❌ No puede:**
* Saber cuándo cambió tu código
* Actualizar automáticamente
* Mantener sincronización

**✅ Tú debes:**
* Actualizar documentación cuando cambias código
* Revisar que todo esté sincronizado
* Mantener consistencia manualmente

---

## ⚠️ Errores comunes al confiar en AI

### 1. Confiar sin validar

```python
# ❌ Mal
codigo = ai.generar()
ejecutar(codigo)  # Sin revisar

# ✅ Bien
codigo = ai.generar()
revisar(codigo)
testear(codigo)
validar_resultados(codigo)
ejecutar(codigo)
```

### 2. Usar código sin entender

```python
# ❌ Mal
# Copiar código sin entender qué hace

# ✅ Bien
# Leer, entender, validar, luego usar
```

### 3. No probar edge cases

```python
# ❌ Mal
# Probar solo caso normal

# ✅ Bien
# Probar:
# - Caso normal
# - Valores nulos
# - Valores extremos
# - Errores esperados
```

### 4. Ignorar errores de la AI

```python
# ❌ Mal
# La AI dijo que funciona, debe funcionar

# ✅ Bien
# Probar y validar siempre
```

---

## 🔍 Cuándo validar especialmente

### 1. Cálculos financieros o críticos

```python
# ⚠️ Siempre valida manualmente
total = calcular_ingresos(datos)
# Verifica que el cálculo sea correcto
```

### 2. Transformaciones de datos complejas

```python
# ⚠️ Valida resultados
df_transformado = transformar(df)
# Compara con resultado esperado
```

### 3. Queries SQL sobre datos reales

```sql
-- ⚠️ Valida antes de ejecutar en producción
SELECT * FROM ventas WHERE fecha >= '2024-01-01';
-- Verifica que retorne lo esperado
```

### 4. Código que afecta producción

```python
# ⚠️ Extra validación
codigo_produccion = ai.generar()
# Revisa línea por línea
# Prueba en ambiente de desarrollo
# Valida con datos de prueba
```

---

## ✅ Cuándo confiar más (pero siempre validar)

### 1. Código boilerplate simple

```python
# ✅ Más seguro (pero revisa)
def leer_csv(ruta: str) -> pd.DataFrame:
    return pd.read_csv(ruta)
```

### 2. Documentación

```python
# ✅ Más seguro (pero revisa)
"""
Función que lee un CSV.
...
"""
```

### 3. Refactorización de estilo

```python
# ✅ Más seguro (pero revisa)
# Cambios de formato, nombres, etc.
```

---

## 🛡️ Checklist de validación

Antes de usar código generado por AI:

- [ ] **Entiendo qué hace** el código
- [ ] **He probado** el código
- [ ] **He validado** los resultados
- [ ] **He revisado** edge cases
- [ ] **He verificado** que cumple requisitos
- [ ] **He probado** con datos reales (si aplica)
- [ ] **He revisado** seguridad (si aplica)
- [ ] **He documentado** cambios importantes

---

## 🎯 Ejercicios

1. Genera código con AI y valídalo completamente
2. Identifica qué partes del código necesitan más validación
3. Crea un proceso de revisión para código generado por AI
4. Prueba edge cases en código generado

---

## 🚀 Próximo paso

Revisa **[Buenas Prácticas de AI](buenas-practicas-ai.md)** para un enfoque completo y seguro.

---

> **Recuerda**: La AI es una herramienta poderosa, pero tú eres el responsable final. Siempre valida, prueba y entiende el código que usas.
