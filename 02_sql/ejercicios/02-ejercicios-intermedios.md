# Ejercicios intermedios de SQL

Ejercicios con subconsultas, CTEs y window functions.

---

## 📝 Ejercicios

### Ejercicio 1: Subconsultas y CTEs

1. Encuentra productos más caros que el promedio de su categoría
2. Lista usuarios cuyo total de compras es mayor que el promedio
3. Muestra el producto más vendido de cada categoría

### Ejercicio 2: Window Functions

1. Calcula el ranking de productos por ventas
2. Crea una columna con ventas acumuladas por mes
3. Compara cada venta con el promedio de ventas del usuario

---

## ✅ Soluciones

### Ejercicio 1 - Soluciones

```sql
-- 1. Productos más caros que el promedio de su categoría
SELECT 
    p1.nombre,
    p1.categoria,
    p1.precio,
    (SELECT AVG(precio) 
     FROM productos p2 
     WHERE p2.categoria = p1.categoria) AS precio_promedio
FROM productos p1
WHERE p1.precio > (
    SELECT AVG(precio) 
    FROM productos p2 
    WHERE p2.categoria = p1.categoria
);

-- 2. Usuarios con compras arriba del promedio
WITH ventas_por_usuario AS (
    SELECT 
        usuario_id,
        SUM(total) AS total_compras
    FROM ventas
    GROUP BY usuario_id
),
promedio_compras AS (
    SELECT AVG(total_compras) AS promedio
    FROM ventas_por_usuario
)
SELECT 
    u.nombre,
    vpu.total_compras,
    pc.promedio
FROM usuarios u
JOIN ventas_por_usuario vpu ON u.id = vpu.usuario_id
CROSS JOIN promedio_compras pc
WHERE vpu.total_compras > pc.promedio;

-- 3. Producto más vendido por categoría
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
SELECT categoria, nombre, unidades_vendidas
FROM ventas_por_producto
WHERE ranking = 1;
```

### Ejercicio 2 - Soluciones

```sql
-- 1. Ranking de productos
SELECT 
    p.nombre,
    SUM(v.cantidad) AS unidades_vendidas,
    RANK() OVER (ORDER BY SUM(v.cantidad) DESC) AS ranking
FROM productos p
JOIN ventas v ON p.id = v.producto_id
GROUP BY p.id, p.nombre;

-- 2. Ventas acumuladas
SELECT 
    DATE_TRUNC('month', fecha_venta) AS mes,
    SUM(total) AS ventas_mes,
    SUM(SUM(total)) OVER (
        ORDER BY DATE_TRUNC('month', fecha_venta)
    ) AS ventas_acumuladas
FROM ventas
GROUP BY DATE_TRUNC('month', fecha_venta)
ORDER BY mes;

-- 3. Comparación con promedio del usuario
SELECT 
    u.nombre,
    v.fecha_venta,
    v.total,
    AVG(v.total) OVER (PARTITION BY v.usuario_id) AS promedio_usuario,
    v.total - AVG(v.total) OVER (PARTITION BY v.usuario_id) AS diferencia
FROM ventas v
JOIN usuarios u ON v.usuario_id = u.id;
```

---

## 🎯 Próximo nivel

Continúa con **[Ejercicios avanzados](03-ejercicios-avanzados.md)**.
