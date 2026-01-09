# Ejemplos de Prompts Efectivos

Aprende a escribir prompts efectivos para obtener mejores resultados de la AI en Data Engineering.

---

## 🎯 Principios de buenos prompts

### 1. Específico y claro

**❌ Mal:**
```
"haz un pipeline"
```

**✅ Bien:**
```
"Crea un pipeline ETL en Python que:
1. Lea datos de un archivo CSV llamado 'ventas.csv'
2. Valide que tenga las columnas: fecha, producto_id, cantidad, precio
3. Limpie datos: elimine nulos y duplicados
4. Calcule total = cantidad * precio
5. Guarde el resultado en Parquet
6. Incluya logging y manejo de errores"
```

### 2. Proporciona contexto

**✅ Ejemplo:**
```
"Estoy trabajando en un proyecto de Data Engineering.
Necesito una función que procese datos de ventas desde PostgreSQL.

Contexto:
- Uso pandas y sqlalchemy
- Los datos tienen millones de filas
- Necesito procesar por chunks
- El resultado va a S3 en formato Parquet

Crea una función que:
[detalles específicos]"
```

### 3. Define el formato esperado

**✅ Ejemplo:**
```
"Genera código Python que:
- Use type hints
- Incluya docstrings estilo Google
- Maneje errores con try/except
- Use logging para mensajes importantes
- Siga PEP 8"
```

---

## 📊 Prompts para SQL

### Generar query básica

**Prompt:**
```
"Crea una query SQL en PostgreSQL que:
- Seleccione ventas del último mes
- Agrupe por categoría de producto
- Calcule total de ventas y número de transacciones
- Ordene por total descendente
- Limite a top 10"
```

### Optimizar query

**Prompt:**
```
"Optimiza esta query SQL para mejor rendimiento:

SELECT * FROM ventas v
JOIN productos p ON v.producto_id = p.id
WHERE v.fecha >= '2024-01-01'
GROUP BY p.categoria
HAVING COUNT(*) > 100;

Contexto:
- La tabla ventas tiene 10 millones de filas
- Hay índices en: fecha, producto_id
- PostgreSQL 15"
```

### Query compleja con CTEs

**Prompt:**
```
"Crea una query SQL que calcule crecimiento mes a mes usando CTEs:

1. CTE 1: Ventas por mes
2. CTE 2: Ventas del mes anterior usando LAG
3. SELECT final: Calcular crecimiento porcentual

Usa PostgreSQL con funciones de ventana."
```

---

## 🐍 Prompts para Python

### Crear función de transformación

**Prompt:**
```
"Crea una función Python llamada 'limpiar_datos_ventas' que:

Parámetros:
- df: pandas DataFrame con columnas: fecha, producto_id, cantidad, precio

Proceso:
1. Validar que todas las columnas existan
2. Eliminar filas con nulos en columnas críticas (producto_id, cantidad, precio)
3. Convertir fecha a datetime
4. Filtrar cantidades y precios negativos
5. Eliminar duplicados

Retorna:
- DataFrame limpio

Incluye:
- Type hints
- Docstring estilo Google
- Logging de operaciones
- Manejo de errores"
```

### Crear pipeline ETL

**Prompt:**
```
"Crea un pipeline ETL completo en Python con esta estructura:

1. Función extract(): Lee CSV de 'data/raw/ventas.csv'
2. Función transform(): Limpia y calcula totales
3. Función load(): Guarda en Parquet a 'data/processed/ventas.parquet'
4. Función run_pipeline(): Orquesta las tres funciones

Requisitos:
- Usar pandas
- Incluir logging
- Manejo de errores robusto
- Validaciones en cada etapa
- Type hints y docstrings"
```

### Generar tests

**Prompt:**
```
"Crea tests unitarios con pytest para esta función:

[pega tu función]

Incluye:
- Test de caso normal
- Test con datos inválidos
- Test con valores nulos
- Test de errores esperados
- Usa fixtures cuando sea apropiado"
```

---

## 📝 Prompts para documentación

### Documentar función

**Prompt:**
```
"Genera docstring estilo Google para esta función:

[pega tu función]

Incluye:
- Descripción clara
- Args con tipos y descripciones
- Returns con tipo y descripción
- Raises si aplica
- Ejemplo de uso"
```

### Documentar pipeline

**Prompt:**
```
"Genera documentación para este pipeline ETL:

[pega código del pipeline]

Incluye:
- Descripción del propósito
- Flujo de datos (entrada → proceso → salida)
- Requisitos y dependencias
- Ejemplo de uso
- Troubleshooting común"
```

### Crear README

**Prompt:**
```
"Crea un README.md para este proyecto de Data Engineering:

Proyecto: Pipeline de procesamiento de ventas
- Lee datos de PostgreSQL
- Procesa y transforma
- Guarda en S3

Incluye:
- Descripción del proyecto
- Instalación
- Configuración
- Uso
- Estructura del proyecto
- Contribuir"
```

---

## 🔍 Prompts para debugging

### Explicar error

**Prompt:**
```
"Explica por qué falla este código y cómo solucionarlo:

[pega código y error]

Error:
[pega mensaje de error completo]"
```

### Optimizar código lento

**Prompt:**
```
"Este código es lento al procesar 1 millón de filas.
Analiza y sugiere optimizaciones:

[pega código]

Contexto:
- Usa pandas
- Procesa DataFrame grande
- Necesita ser más eficiente"
```

---

## 🎨 Prompts para refactorización

### Mejorar legibilidad

**Prompt:**
```
"Refactoriza este código para mejorar legibilidad y mantenibilidad:

[pega código]

Mantén la funcionalidad pero:
- Separa responsabilidades
- Usa nombres descriptivos
- Agrega type hints
- Incluye docstrings"
```

### Convertir a funciones modulares

**Prompt:**
```
"Refactoriza este script monolítico en funciones modulares:

[pega código]

Crea:
- Función para cada responsabilidad
- Función main() que orqueste
- Estructura clara y reutilizable"
```

---

## 🧪 Prompts para testing

### Generar tests completos

**Prompt:**
```
"Crea suite de tests con pytest para este módulo:

[pega código del módulo]

Incluye:
- Tests unitarios para cada función
- Tests de integración
- Tests de casos edge
- Fixtures para datos de prueba
- Mocks para dependencias externas"
```

### Test de pipeline

**Prompt:**
```
"Crea tests para este pipeline ETL:

[pega código del pipeline]

Incluye:
- Test de cada etapa (extract, transform, load)
- Test end-to-end
- Test de manejo de errores
- Test con datos de ejemplo"
```

---

## 💡 Tips para prompts efectivos

### 1. Sé específico sobre el contexto

```
✅ "En un proyecto de Data Engineering usando pandas y PostgreSQL..."
❌ "haz algo con datos"
```

### 2. Define restricciones

```
✅ "No uses librerías externas, solo pandas y estándar de Python"
✅ "Debe funcionar con Python 3.9+"
```

### 3. Pide ejemplos

```
✅ "Incluye un ejemplo de uso con datos de muestra"
```

### 4. Especifica estilo

```
✅ "Sigue PEP 8 y usa type hints"
✅ "Docstrings estilo Google"
```

### 5. Itera y refina

```
Primera: "Crea función básica"
Segunda: "Agrega validación de esquema"
Tercera: "Optimiza para grandes volúmenes"
```

---

## 🎯 Ejercicios

1. Escribe un prompt para generar un pipeline ETL completo
2. Crea un prompt para optimizar una query SQL lenta
3. Genera un prompt para documentar código complejo
4. Escribe un prompt para crear tests comprehensivos

---

## 🚀 Próximo paso

Continúa con **[Documentación con AI](documentacion-con-ai.md)** para aprender a generar documentación efectiva.

---

> **Recuerda**: Un buen prompt es específico, contextual y claro. Invierte tiempo en escribir buenos prompts y ahorrarás tiempo después.
