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

---

## 🎯 Próximo nivel

Revisa **[Casos de uso reales](04-casos-uso-reales.md)**.
