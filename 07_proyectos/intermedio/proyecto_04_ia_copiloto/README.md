# Proyecto 4: Pipeline con IA como Copiloto

Aprende a usar inteligencia artificial (IA) para acelerar el desarrollo de pipelines de datos.

---

## 🎯 Objetivo

Aprender a:
* Usar IA para generar código de pipelines
* Documentar código con IA
* Optimizar queries SQL con IA
* Usar IA para debugging y testing

---

## 📋 Requisitos previos

* Acceso a ChatGPT, Claude, o Cursor IDE
* Conocimientos básicos de Python y SQL
* Entendimiento de conceptos de pipelines

---

## 🚀 Pasos del proyecto

### 1. Estructura del proyecto

```
proyecto_04_ia_copiloto/
├── README.md
├── prompts/
│   ├── generar_pipeline.md
│   ├── documentar_codigo.md
│   ├── optimizar_sql.md
│   └── generar_tests.md
├── src/
│   ├── pipeline_ia_generado.py
│   └── pipeline_manual.py
└── docs/
    └── documentacion_ia.md
```

### 2. Generar pipeline con IA

**Prompt para ChatGPT/Claude:**

```
Necesito un pipeline ETL en Python que:
1. Extraiga datos de un CSV con columnas: fecha, producto, cantidad, precio
2. Transforme los datos:
   - Calcule total = cantidad * precio
   - Valide que cantidad y precio sean positivos
   - Elimine duplicados
3. Cargue los datos a PostgreSQL

Usa:
- pandas para transformaciones
- psycopg2 para PostgreSQL
- python-dotenv para variables de entorno
- logging para registro de operaciones

Incluye:
- Manejo de errores robusto
- Logging detallado
- Validaciones de datos
- Documentación en código
```

**Guarda el código generado en `src/pipeline_ia_generado.py`**

### 3. Documentar código con IA

**Prompt:**

```
Documenta este código Python de pipeline ETL:
[Pega el código]

Agrega:
- Docstrings para todas las funciones
- Comentarios explicativos
- Type hints
- Ejemplos de uso
```

### 4. Optimizar SQL con IA

**Prompt:**

```
Tengo esta query SQL que es lenta:

SELECT 
    u.nombre,
    COUNT(v.id) as total_ventas,
    SUM(v.total) as ingresos
FROM usuarios u
LEFT JOIN ventas v ON u.id = v.usuario_id
WHERE v.fecha >= '2024-01-01'
GROUP BY u.id, u.nombre
ORDER BY ingresos DESC
LIMIT 100;

¿Cómo puedo optimizarla? Sugiere:
- Índices necesarios
- Mejoras en la query
- Explicación de por qué es lenta
```

### 5. Generar tests con IA

**Prompt:**

```
Genera tests unitarios para este pipeline ETL:
[Pega el código del pipeline]

Usa pytest. Incluye tests para:
- Función de extracción
- Función de transformación
- Función de carga
- Manejo de errores
```

### 6. Comparar: Manual vs IA

Crea `comparacion.md`:

```markdown
# Comparación: Pipeline Manual vs IA

## Pipeline Manual
- Tiempo de desarrollo: X horas
- Líneas de código: X
- Bugs encontrados: X

## Pipeline con IA
- Tiempo de desarrollo: X horas
- Líneas de código: X
- Bugs encontrados: X

## Lecciones aprendidas
1. [Lección 1]
2. [Lección 2]
3. [Lección 3]
```

### 7. Mejores prácticas con IA

Crea `mejores_practicas_ia.md`:

```markdown
# Mejores Prácticas: Usar IA en Data Engineering

## 1. Prompts efectivos
- Sé específico sobre lo que necesitas
- Proporciona contexto (tecnologías, versiones)
- Pide ejemplos y explicaciones

## 2. Revisión crítica
- Siempre revisa el código generado
- Prueba antes de usar en producción
- Entiende lo que hace el código

## 3. Iteración
- Mejora prompts basado en resultados
- Combina múltiples respuestas
- Refina código generado

## 4. Documentación
- Documenta qué prompts usaste
- Guarda versiones del código generado
- Compara resultados
```

---

## ✅ Checklist de completado

- [ ] Pipeline generado con IA
- [ ] Código documentado con IA
- [ ] SQL optimizado con IA
- [ ] Tests generados con IA
- [ ] Comparación manual vs IA realizada
- [ ] Mejores prácticas documentadas
- [ ] Pipeline funcionando correctamente

---

## 🎓 Conceptos aprendidos

* ✅ Usar IA como herramienta de desarrollo
* ✅ Escribir prompts efectivos
* ✅ Revisar y validar código generado
* ✅ Integrar IA en flujo de trabajo
* ✅ Mejores prácticas con IA

---

## 🚀 Próximo paso

Después de completar este proyecto:
* Explora más usos de IA (generar documentación, crear dashboards)
* Avanza a **[Proyectos Avanzados](../../avanzado/)**

---

## 💡 Recursos

* **Cursor IDE**: Editor con IA integrada
* **ChatGPT**: Para generación de código
* **Claude**: Alternativa a ChatGPT
* **GitHub Copilot**: Extensión para VS Code

---

> **Recuerda**: IA es una herramienta poderosa, pero siempre revisa y entiende el código generado. No confíes ciegamente.
