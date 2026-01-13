# Casos de uso reales

Ejercicios basados en problemas reales de Data Engineering.

---

## 📊 Caso 1: Análisis de ventas

**Problema:** Necesitas un reporte mensual de ventas con comparación mes a mes.

**Solución:**

```sql
WITH ventas_mensuales AS (
    SELECT 
        DATE_TRUNC('month', fecha_venta) AS mes,
        COUNT(*) AS total_ventas,
        SUM(total) AS ingresos,
        AVG(total) AS ticket_promedio
    FROM ventas
    GROUP BY DATE_TRUNC('month', fecha_venta)
)
SELECT 
    mes,
    total_ventas,
    ingresos,
    ticket_promedio,
    LAG(ingresos) OVER (ORDER BY mes) AS ingresos_mes_anterior,
    ingresos - LAG(ingresos) OVER (ORDER BY mes) AS crecimiento,
    ROUND(
        ((ingresos - LAG(ingresos) OVER (ORDER BY mes)) / 
         LAG(ingresos) OVER (ORDER BY mes)) * 100, 
        2
    ) AS crecimiento_porcentual
FROM ventas_mensuales
ORDER BY mes DESC;
```

---

## 📈 Caso 2: Top productos por categoría

**Problema:** Encuentra los 3 productos más vendidos de cada categoría.

**Solución:**

```sql
WITH ventas_por_producto AS (
    SELECT 
        p.categoria,
        p.nombre,
        SUM(v.cantidad) AS unidades_vendidas,
        ROW_NUMBER() OVER (
            PARTITION BY p.categoria 
            ORDER BY SUM(v.cantidad) DESC
        ) AS ranking
    FROM productos p
    JOIN ventas v ON p.id = v.producto_id
    GROUP BY p.id, p.categoria, p.nombre
)
SELECT 
    categoria,
    nombre,
    unidades_vendidas
FROM ventas_por_producto
WHERE ranking <= 3
ORDER BY categoria, ranking;
```

---

## 🔍 Caso 3: Detección de anomalías

**Problema:** Encuentra ventas que están muy por encima del promedio.

**Solución:**

```sql
WITH estadisticas AS (
    SELECT 
        AVG(total) AS promedio,
        STDDEV(total) AS desviacion_estandar
    FROM ventas
)
SELECT 
    v.id,
    v.fecha_venta,
    v.total,
    est.promedio,
    v.total - est.promedio AS diferencia,
    (v.total - est.promedio) / est.desviacion_estandar AS z_score
FROM ventas v
CROSS JOIN estadisticas est
WHERE ABS((v.total - est.promedio) / est.desviacion_estandar) > 2  -- Más de 2 desviaciones
ORDER BY ABS((v.total - est.promedio) / est.desviacion_estandar) DESC;
```

> 💡 **Nota**: Si esta query no devuelve resultados, significa que no hay ventas con más de 2 desviaciones estándar del promedio. Esto es normal y puede indicar que los datos están bien distribuidos. Puedes ajustar el umbral (cambiar `> 2` a `> 1.5` o `> 1`) para encontrar más anomalías.

---

## 💡 Tips para casos reales

1. **Empieza simple**: Resuelve el problema básico primero
2. **Itera**: Agrega complejidad gradualmente
3. **Optimiza después**: Primero que funcione, luego optimiza
4. **Documenta**: Explica la lógica en comentarios

---

¡Sigue practicando y experimentando! 🚀
