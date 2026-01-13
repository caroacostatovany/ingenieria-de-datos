# CTEs (Common Table Expressions)

Las CTEs (WITH clauses) hacen que las consultas complejas sean más legibles y mantenibles.

---

## 📝 ¿Qué son las CTEs?

Una CTE es una tabla temporal que existe solo durante la ejecución de la consulta. Es como una "variable" para subconsultas.

### Sintaxis básica

```sql
WITH nombre_cte AS (
    SELECT ...
)
SELECT * FROM nombre_cte;
```

---

## 🎯 Ejemplos básicos

### Ejemplo 1: CTE simple

```sql
-- Ventas del último mes
WITH ventas_recientes AS (
    SELECT *
    FROM ventas
    WHERE fecha_venta >= CURRENT_DATE - INTERVAL '30 days'
)
SELECT 
    COUNT(*) AS total_ventas,
    SUM(total) AS ingresos
FROM ventas_recientes;
```

### Ejemplo 2: Múltiples CTEs

```sql
WITH 
    ventas_por_usuario AS (
        SELECT 
            usuario_id,
            COUNT(*) AS total_ventas,
            SUM(total) AS ingresos
        FROM ventas
        GROUP BY usuario_id
    ),
    estadisticas AS (
        SELECT 
            AVG(total_ventas) AS promedio_ventas,
            AVG(ingresos) AS promedio_ingresos
        FROM ventas_por_usuario
    )
SELECT 
    u.nombre,
    vpu.total_ventas,
    vpu.ingresos,
    CASE 
        WHEN vpu.total_ventas > est.promedio_ventas THEN 'Arriba del promedio'
        ELSE 'Abajo del promedio'
    END AS categoria
FROM usuarios u
JOIN ventas_por_usuario vpu ON u.id = vpu.usuario_id
CROSS JOIN estadisticas est;
```

---

## 🔄 CTEs recursivas

Las CTEs recursivas te permiten trabajar con datos jerárquicos.

> 💡 **Nota**: El siguiente ejemplo es teórico y usa una tabla `empleados` que no existe en nuestra base de datos de ejemplo. Se muestra para ilustrar el concepto de CTEs recursivas.

```sql
-- Ejemplo teórico: Organigrama (estructura jerárquica)
-- Requiere una tabla con estructura jerárquica (ej: empleados con jefe_id)
WITH RECURSIVE organigrama AS (
    -- Caso base: empleados sin jefe
    SELECT id, nombre, jefe_id, 1 AS nivel
    FROM empleados
    WHERE jefe_id IS NULL
    
    UNION ALL
    
    -- Caso recursivo: empleados con jefe
    SELECT e.id, e.nombre, e.jefe_id, o.nivel + 1
    FROM empleados e
    JOIN organigrama o ON e.jefe_id = o.id
)
SELECT * FROM organigrama;
```

**Casos de uso comunes:**
* Organigramas (empleados → jefes)
* Categorías jerárquicas (categoría → subcategoría)
* Rutas en árboles (nodos → padres)

---

## 🎯 Ejemplos prácticos

### Ejemplo 1: Análisis de ventas por período

```sql
WITH 
    ventas_mensuales AS (
        SELECT 
            DATE_TRUNC('month', fecha_venta) AS mes,
            COUNT(*) AS total_ventas,
            SUM(total) AS ingresos
        FROM ventas
        GROUP BY DATE_TRUNC('month', fecha_venta)
    ),
    ventas_previas AS (
        SELECT 
            mes,
            total_ventas,
            ingresos,
            LAG(ingresos) OVER (ORDER BY mes) AS ingresos_mes_anterior
        FROM ventas_mensuales
    )
SELECT 
    mes,
    total_ventas,
    ingresos,
    ingresos_mes_anterior,
    ingresos - ingresos_mes_anterior AS diferencia,
    ROUND(
        ((ingresos - ingresos_mes_anterior) / ingresos_mes_anterior) * 100, 
        2
    ) AS crecimiento_porcentual
FROM ventas_previas
ORDER BY mes DESC;
```

### Ejemplo 2: Top N por categoría

```sql
WITH ventas_por_producto AS (
    SELECT 
        p.id,
        p.nombre,
        p.categoria,
        SUM(v.cantidad) AS unidades_vendidas,
        SUM(v.total) AS ingresos
    FROM productos p
    JOIN ventas v ON p.id = v.producto_id
    GROUP BY p.id, p.nombre, p.categoria
),
ranked_productos AS (
    SELECT 
        *,
        ROW_NUMBER() OVER (
            PARTITION BY categoria 
            ORDER BY unidades_vendidas DESC
        ) AS ranking
    FROM ventas_por_producto
)
SELECT 
    categoria,
    nombre,
    unidades_vendidas,
    ingresos
FROM ranked_productos
WHERE ranking <= 3
ORDER BY categoria, ranking;
```

### Ejemplo 3: Comparación de períodos

```sql
WITH 
    ventas_actual AS (
        SELECT 
            categoria,
            SUM(total) AS ingresos
        FROM ventas v
        JOIN productos p ON v.producto_id = p.id
        WHERE fecha_venta >= DATE_TRUNC('month', CURRENT_DATE)
        GROUP BY categoria
    ),
    ventas_anterior AS (
        SELECT 
            categoria,
            SUM(total) AS ingresos
        FROM ventas v
        JOIN productos p ON v.producto_id = p.id
        WHERE fecha_venta >= DATE_TRUNC('month', CURRENT_DATE) - INTERVAL '1 month'
          AND fecha_venta < DATE_TRUNC('month', CURRENT_DATE)
        GROUP BY categoria
    )
SELECT 
    COALESCE(va.categoria, vp.categoria) AS categoria,
    COALESCE(va.ingresos, 0) AS ingresos_actual,
    COALESCE(vp.ingresos, 0) AS ingresos_anterior,
    COALESCE(va.ingresos, 0) - COALESCE(vp.ingresos, 0) AS diferencia
FROM ventas_actual va
FULL OUTER JOIN ventas_anterior vp ON va.categoria = vp.categoria;
```

---

## 💡 Buenas prácticas

### 1. Usa CTEs para mejorar legibilidad

```sql
-- ✅ Legible con CTEs
WITH ventas_agrupadas AS (...),
     estadisticas AS (...)
SELECT ... FROM estadisticas;

-- ⚠️ Difícil de leer con subconsultas anidadas
SELECT ... FROM (
    SELECT ... FROM (
        SELECT ... FROM ...
    ) AS sub1
) AS sub2;
```

### 2. Nombra CTEs descriptivamente

```sql
-- ✅ Nombres claros
WITH ventas_por_categoria AS (...),
     top_productos AS (...)
SELECT ...;

-- ⚠️ Nombres genéricos
WITH temp1 AS (...),
     temp2 AS (...)
SELECT ...;
```

### 3. Usa CTEs para reutilizar lógica

```sql
-- ✅ Reutiliza la CTE
WITH productos_vendidos AS (
    SELECT DISTINCT producto_id FROM ventas
)
SELECT 
    (SELECT COUNT(*) FROM productos) AS total_productos,
    (SELECT COUNT(*) FROM productos_vendidos) AS productos_con_ventas;
```

---

## 🎯 Ejercicios

1. Crea una CTE que calcule ventas mensuales y compáralas con el mes anterior
2. Usa CTEs para encontrar el producto más vendido de cada categoría
3. Crea un análisis de cohortes usando CTEs recursivas
4. Compara ventas por ciudad usando múltiples CTEs
5. Calcula métricas acumuladas usando CTEs

---

## 🚀 Siguiente paso

Continúa con **[Window Functions](03-window-functions.md)** para análisis avanzado.
