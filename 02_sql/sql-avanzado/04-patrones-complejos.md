# Patrones complejos

Patrones SQL avanzados para resolver problemas complejos en Data Engineering.

---

## 🔄 Pivoting (Pivot)

Convertir filas en columnas.

```sql
-- Ventas por mes como columnas
SELECT 
    categoria,
    SUM(CASE WHEN mes = '2024-01' THEN ingresos ELSE 0 END) AS enero,
    SUM(CASE WHEN mes = '2024-02' THEN ingresos ELSE 0 END) AS febrero,
    SUM(CASE WHEN mes = '2024-03' THEN ingresos ELSE 0 END) AS marzo
FROM (
    SELECT 
        p.categoria,
        DATE_TRUNC('month', v.fecha_venta) AS mes,
        SUM(v.total) AS ingresos
    FROM ventas v
    JOIN productos p ON v.producto_id = p.id
    GROUP BY p.categoria, DATE_TRUNC('month', v.fecha_venta)
) AS ventas_mensuales
GROUP BY categoria;
```

---

## 📊 Unpivoting

Convertir columnas en filas.

> 💡 **Nota**: PostgreSQL no tiene `UNPIVOT` como SQL Server. Se usa `UNION ALL` o `LATERAL` para lograr lo mismo.

```sql
-- Convertir columnas de meses en filas (usando UNION ALL)
-- Primero creamos una vista o CTE con datos pivotados
WITH ventas_pivot AS (
    SELECT 
        p.categoria,
        SUM(CASE WHEN DATE_TRUNC('month', v.fecha_venta) = '2026-01-01'::date THEN v.total ELSE 0 END) AS enero,
        SUM(CASE WHEN DATE_TRUNC('month', v.fecha_venta) = '2026-02-01'::date THEN v.total ELSE 0 END) AS febrero,
        SUM(CASE WHEN DATE_TRUNC('month', v.fecha_venta) = '2026-03-01'::date THEN v.total ELSE 0 END) AS marzo
    FROM ventas v
    JOIN productos p ON v.producto_id = p.id
    GROUP BY p.categoria
)
-- Unpivot usando UNION ALL
SELECT categoria, 'enero' AS mes, enero AS ingresos FROM ventas_pivot
UNION ALL
SELECT categoria, 'febrero' AS mes, febrero AS ingresos FROM ventas_pivot
UNION ALL
SELECT categoria, 'marzo' AS mes, marzo AS ingresos FROM ventas_pivot
ORDER BY categoria, mes;
```

**Alternativa con LATERAL (más elegante):**
```sql
WITH ventas_pivot AS (
    SELECT 
        p.categoria,
        SUM(CASE WHEN DATE_TRUNC('month', v.fecha_venta) = '2026-01-01'::date THEN v.total ELSE 0 END) AS enero,
        SUM(CASE WHEN DATE_TRUNC('month', v.fecha_venta) = '2026-02-01'::date THEN v.total ELSE 0 END) AS febrero,
        SUM(CASE WHEN DATE_TRUNC('month', v.fecha_venta) = '2026-03-01'::date THEN v.total ELSE 0 END) AS marzo
    FROM ventas v
    JOIN productos p ON v.producto_id = p.id
    GROUP BY p.categoria
)
SELECT 
    p.categoria,
    unpvt.mes,
    unpvt.ingresos
FROM ventas_pivot p
CROSS JOIN LATERAL (
    VALUES 
        ('enero', p.enero),
        ('febrero', p.febrero),
        ('marzo', p.marzo)
) AS unpvt(mes, ingresos)
WHERE unpvt.ingresos > 0
ORDER BY p.categoria, unpvt.mes;
```

---

## 🔍 Búsqueda de gaps

Encontrar valores faltantes en secuencias.

```sql
-- Encontrar días sin ventas
WITH dias AS (
    SELECT generate_series(
        '2024-01-01'::date,
        '2024-01-31'::date,
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
WHERE v.dia IS NULL;
```

---

## 📈 Análisis de cohortes

```sql
-- Cohortes de usuarios por mes de registro
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

---

## 🎯 Ejercicios

1. Crea un pivot de ventas por categoría y mes
2. Encuentra gaps en secuencias de fechas
3. Analiza retención de usuarios por cohorte
4. Calcula métricas acumuladas con frames personalizados

---

## 🚀 Próximo paso

Revisa **[Modelado Relacional](../modelado-relacional.md)** y **[Ejercicios](../ejercicios/)**.
