# Ejercicios avanzados de SQL

Ejercicios complejos con patrones avanzados.

---

## 📝 Ejercicios

1. Crea un análisis de cohortes de usuarios
2. Encuentra gaps en secuencias de fechas
3. Calcula métricas acumuladas con frames personalizados
4. Crea un pivot de ventas por categoría y mes

---

## ✅ Soluciones

### Análisis de cohortes

```sql
WITH primera_compra AS (
    SELECT 
        usuario_id,
        MIN(fecha_venta) AS primera_fecha
    FROM ventas
    GROUP BY usuario_id
),
cohortes AS (
    SELECT 
        DATE_TRUNC('month', primera_fecha) AS cohorte,
        usuario_id
    FROM primera_compra
),
ventas_cohorte AS (
    SELECT 
        c.cohorte,
        DATE_TRUNC('month', v.fecha_venta) AS mes_venta,
        COUNT(DISTINCT v.usuario_id) AS usuarios_activos
    FROM cohortes c
    JOIN ventas v ON c.usuario_id = v.usuario_id
    GROUP BY c.cohorte, DATE_TRUNC('month', v.fecha_venta)
)
SELECT 
    cohorte,
    mes_venta,
    usuarios_activos,
    EXTRACT(MONTH FROM AGE(mes_venta, cohorte)) AS mes_cohorte
FROM ventas_cohorte
ORDER BY cohorte, mes_venta;
```

### Encontrar gaps en secuencias de fechas

```sql
-- Encuentra días sin ventas en un rango
WITH dias AS (
    SELECT generate_series(
        '2026-01-01'::date,
        '2026-01-31'::date,
        '1 day'::interval
    )::date AS dia
),
ventas_por_dia AS (
    SELECT DISTINCT DATE(fecha_venta) AS dia
    FROM ventas
)
SELECT d.dia
FROM dias d
LEFT JOIN ventas_por_dia v ON d.dia = v.dia
WHERE v.dia IS NULL
ORDER BY d.dia;
```

### Métricas acumuladas con frames personalizados

```sql
-- Suma móvil de 3 días
SELECT 
    fecha_venta,
    total,
    SUM(total) OVER (
        ORDER BY fecha_venta
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS suma_3_dias,
    AVG(total) OVER (
        ORDER BY fecha_venta
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS promedio_3_dias
FROM ventas
ORDER BY fecha_venta;
```

### Pivot de ventas por categoría y mes

```sql
-- Ventas por categoría y mes (pivot)
SELECT 
    p.categoria,
    SUM(CASE WHEN DATE_TRUNC('month', v.fecha_venta) = '2026-01-01'::date THEN v.total ELSE 0 END) AS enero,
    SUM(CASE WHEN DATE_TRUNC('month', v.fecha_venta) = '2026-02-01'::date THEN v.total ELSE 0 END) AS febrero,
    SUM(CASE WHEN DATE_TRUNC('month', v.fecha_venta) = '2026-03-01'::date THEN v.total ELSE 0 END) AS marzo
FROM ventas v
JOIN productos p ON v.producto_id = p.id
GROUP BY p.categoria
ORDER BY p.categoria;
```

---

## 🎯 Próximo nivel

Revisa **[Casos de uso reales](04-casos-uso-reales.md)**.
