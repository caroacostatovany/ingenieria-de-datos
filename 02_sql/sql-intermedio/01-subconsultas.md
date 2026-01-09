# Subconsultas

Las subconsultas (subqueries) son consultas dentro de otras consultas. Te permiten resolver problemas complejos paso a paso.

---

## 🔍 Tipos de subconsultas

### Subconsultas escalares

Devuelven un solo valor. Se usan en SELECT, WHERE, o HAVING.

```sql
-- Precio promedio de todos los productos
SELECT 
    nombre,
    precio,
    (SELECT AVG(precio) FROM productos) AS precio_promedio,
    precio - (SELECT AVG(precio) FROM productos) AS diferencia
FROM productos;
```

### Subconsultas en WHERE

```sql
-- Productos más caros que el promedio
SELECT * FROM productos
WHERE precio > (SELECT AVG(precio) FROM productos);

-- Usuarios que han comprado más que el promedio
SELECT * FROM usuarios
WHERE id IN (
    SELECT usuario_id 
    FROM ventas 
    GROUP BY usuario_id 
    HAVING SUM(total) > (SELECT AVG(total) FROM ventas)
);
```

### Subconsultas en FROM

```sql
-- Ventas agrupadas por usuario
SELECT 
    u.nombre,
    ventas_usuario.total_ventas,
    ventas_usuario.ingresos
FROM usuarios u
JOIN (
    SELECT 
        usuario_id,
        COUNT(*) AS total_ventas,
        SUM(total) AS ingresos
    FROM ventas
    GROUP BY usuario_id
) AS ventas_usuario ON u.id = ventas_usuario.usuario_id;
```

---

## 🎯 Ejemplos prácticos

### Ejemplo 1: Top N por categoría

```sql
-- Top 3 productos más vendidos por categoría
SELECT 
    p.categoria,
    p.nombre,
    p.precio,
    ventas_producto.unidades_vendidas
FROM productos p
JOIN (
    SELECT 
        producto_id,
        SUM(cantidad) AS unidades_vendidas
    FROM ventas
    GROUP BY producto_id
) AS ventas_producto ON p.id = ventas_producto.producto_id
WHERE ventas_producto.unidades_vendidas IN (
    SELECT unidades_vendidas
    FROM (
        SELECT 
            p2.categoria,
            SUM(v2.cantidad) AS unidades_vendidas
        FROM productos p2
        JOIN ventas v2 ON p2.id = v2.producto_id
        WHERE p2.categoria = p.categoria
        GROUP BY p2.id, p2.categoria, p2.nombre
        ORDER BY unidades_vendidas DESC
        LIMIT 3
    ) AS top3
);
```

### Ejemplo 2: Comparación con promedios

```sql
-- Productos con precio superior al promedio de su categoría
SELECT 
    p1.nombre,
    p1.categoria,
    p1.precio,
    (SELECT AVG(precio) 
     FROM productos p2 
     WHERE p2.categoria = p1.categoria) AS precio_promedio_categoria
FROM productos p1
WHERE p1.precio > (
    SELECT AVG(precio) 
    FROM productos p2 
    WHERE p2.categoria = p1.categoria
);
```

### Ejemplo 3: EXISTS vs IN

```sql
-- Usuarios que han comprado (usando IN)
SELECT * FROM usuarios
WHERE id IN (SELECT DISTINCT usuario_id FROM ventas);

-- Usuarios que han comprado (usando EXISTS - más eficiente)
SELECT * FROM usuarios u
WHERE EXISTS (
    SELECT 1 FROM ventas v 
    WHERE v.usuario_id = u.id
);
```

**Diferencia:**
* `IN` devuelve todos los valores y luego compara
* `EXISTS` se detiene en la primera coincidencia (más eficiente)

---

## 💡 Buenas prácticas

### 1. Usa EXISTS cuando solo necesitas verificar existencia

```sql
-- ✅ Más eficiente
SELECT * FROM usuarios u
WHERE EXISTS (
    SELECT 1 FROM ventas v 
    WHERE v.usuario_id = u.id
);

-- ⚠️ Menos eficiente
SELECT * FROM usuarios
WHERE id IN (SELECT usuario_id FROM ventas);
```

### 2. Considera CTEs para subconsultas complejas

```sql
-- ⚠️ Difícil de leer
SELECT ... FROM (
    SELECT ... FROM (
        SELECT ... FROM ...
    ) AS sub1
) AS sub2;

-- ✅ Más legible con CTE
WITH sub1 AS (...),
     sub2 AS (...)
SELECT ... FROM sub2;
```

### 3. Evita subconsultas correlacionadas cuando sea posible

```sql
-- ⚠️ Subconsulta correlacionada (lenta)
SELECT 
    nombre,
    (SELECT COUNT(*) FROM ventas v WHERE v.usuario_id = u.id) AS total_ventas
FROM usuarios u;

-- ✅ JOIN es más eficiente
SELECT 
    u.nombre,
    COUNT(v.id) AS total_ventas
FROM usuarios u
LEFT JOIN ventas v ON u.id = v.usuario_id
GROUP BY u.id, u.nombre;
```

---

## 🎯 Ejercicios

1. Encuentra productos que nunca se han vendido usando subconsultas
2. Lista usuarios cuyo total de compras es mayor que el promedio
3. Muestra categorías donde el precio promedio es mayor que 100
4. Encuentra el producto más vendido de cada categoría
5. Lista usuarios que han comprado todos los productos de una categoría

---

## 🚀 Siguiente paso

Continúa con **[CTEs](02-ctes.md)** para hacer subconsultas más legibles.
