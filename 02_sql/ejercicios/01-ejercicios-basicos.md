# Ejercicios básicos de SQL

Ejercicios para practicar SELECT, WHERE, JOINs y agregaciones.

---

## 📝 Ejercicios

### Ejercicio 1: Consultas básicas

1. Lista todos los usuarios de Madrid
2. Encuentra productos con precio mayor a 100
3. Muestra usuarios con email que contenga "example"
4. Lista ventas del último mes

### Ejercicio 2: JOINs

1. Muestra todas las ventas con nombre del cliente y producto
2. Encuentra usuarios que nunca han comprado
3. Lista productos que nunca se han vendido
4. Calcula el total de ventas por ciudad del cliente

### Ejercicio 3: Agregaciones

1. Calcula el total de ingresos por categoría
2. Encuentra las 3 ciudades con más ventas
3. Calcula el ticket promedio por mes
4. Lista categorías con más de 3 productos

---

## ✅ Soluciones

### Ejercicio 1 - Soluciones

```sql
-- 1. Usuarios de Madrid
SELECT * FROM usuarios WHERE ciudad = 'Madrid';

-- 2. Productos caros
SELECT * FROM productos WHERE precio > 100;

-- 3. Emails con "example"
SELECT * FROM usuarios WHERE email LIKE '%example%';

-- 4. Ventas del último mes
SELECT * FROM ventas 
WHERE fecha_venta >= CURRENT_DATE - INTERVAL '30 days';
```

### Ejercicio 2 - Soluciones

```sql
-- 1. Ventas con información completa
SELECT 
    v.id,
    u.nombre AS cliente,
    p.nombre AS producto,
    v.cantidad,
    v.total
FROM ventas v
JOIN usuarios u ON v.usuario_id = u.id
JOIN productos p ON v.producto_id = p.id;

-- 2. Usuarios sin compras
SELECT u.*
FROM usuarios u
LEFT JOIN ventas v ON u.id = v.usuario_id
WHERE v.id IS NULL;

-- 3. Productos sin ventas
SELECT p.*
FROM productos p
LEFT JOIN ventas v ON p.id = v.producto_id
WHERE v.id IS NULL;

-- 4. Ventas por ciudad
SELECT 
    u.ciudad,
    SUM(v.total) AS total_ventas
FROM ventas v
JOIN usuarios u ON v.usuario_id = u.id
GROUP BY u.ciudad;
```

### Ejercicio 3 - Soluciones

```sql
-- 1. Ingresos por categoría
SELECT 
    p.categoria,
    SUM(v.total) AS ingresos
FROM ventas v
JOIN productos p ON v.producto_id = p.id
GROUP BY p.categoria;

-- 2. Top 3 ciudades
SELECT 
    u.ciudad,
    COUNT(*) AS total_ventas
FROM ventas v
JOIN usuarios u ON v.usuario_id = u.id
GROUP BY u.ciudad
ORDER BY total_ventas DESC
LIMIT 3;

-- 3. Ticket promedio mensual
SELECT 
    DATE_TRUNC('month', fecha_venta) AS mes,
    AVG(total) AS ticket_promedio
FROM ventas
GROUP BY DATE_TRUNC('month', fecha_venta);

-- 4. Categorías con más productos
SELECT 
    categoria,
    COUNT(*) AS total_productos
FROM productos
GROUP BY categoria
HAVING COUNT(*) > 3;
```

---

## 🎯 Próximo nivel

Continúa con **[Ejercicios intermedios](02-ejercicios-intermedios.md)**.
