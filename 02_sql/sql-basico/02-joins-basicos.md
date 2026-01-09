# JOINs básicos

Los JOINs te permiten combinar datos de múltiples tablas relacionadas.

---

## 🔗 ¿Por qué necesitamos JOINs?

En bases de datos relacionales, los datos están normalizados en múltiples tablas. Los JOINs te permiten unirlos.

**Ejemplo:**
- Tabla `ventas` tiene `usuario_id` y `producto_id`
- Tabla `usuarios` tiene información del usuario
- Tabla `productos` tiene información del producto

Para ver el nombre del usuario y del producto en una venta, necesitas JOINs.

---

## 📊 Tipos de JOIN

### INNER JOIN

Devuelve solo las filas que tienen coincidencias en ambas tablas.

```sql
SELECT 
    v.id,
    u.nombre AS usuario,
    p.nombre AS producto,
    v.cantidad,
    v.total
FROM ventas v
INNER JOIN usuarios u ON v.usuario_id = u.id
INNER JOIN productos p ON v.producto_id = p.id;
```

**Resultado**: Solo ventas que tienen usuario y producto válidos.

### LEFT JOIN (LEFT OUTER JOIN)

Devuelve todas las filas de la tabla izquierda, y las coincidencias de la derecha (o NULL si no hay).

```sql
SELECT 
    u.nombre,
    v.id AS venta_id,
    v.total
FROM usuarios u
LEFT JOIN ventas v ON u.id = v.usuario_id;
```

**Resultado**: Todos los usuarios, incluso si no tienen ventas.

### RIGHT JOIN (RIGHT OUTER JOIN)

Devuelve todas las filas de la tabla derecha, y las coincidencias de la izquierda (o NULL si no hay).

```sql
SELECT 
    p.nombre AS producto,
    v.id AS venta_id,
    v.cantidad
FROM ventas v
RIGHT JOIN productos p ON v.producto_id = p.id;
```

**Resultado**: Todos los productos, incluso si no se han vendido.

### FULL OUTER JOIN

Devuelve todas las filas de ambas tablas, con NULL donde no hay coincidencias.

```sql
SELECT 
    u.nombre AS usuario,
    p.nombre AS producto
FROM usuarios u
FULL OUTER JOIN productos p ON 1=1;  -- Ejemplo teórico
```

**Nota**: No todos los sistemas soportan FULL OUTER JOIN (PostgreSQL sí, MySQL no).

---

## 🎯 Ejemplos prácticos

### Ejemplo 1: Ventas con información completa

```sql
SELECT 
    v.fecha_venta,
    u.nombre AS cliente,
    u.ciudad,
    p.nombre AS producto,
    p.categoria,
    v.cantidad,
    v.precio_unitario,
    v.total
FROM ventas v
INNER JOIN usuarios u ON v.usuario_id = u.id
INNER JOIN productos p ON v.producto_id = p.id
ORDER BY v.fecha_venta DESC;
```

### Ejemplo 2: Usuarios sin ventas

```sql
SELECT 
    u.id,
    u.nombre,
    u.email
FROM usuarios u
LEFT JOIN ventas v ON u.id = v.usuario_id
WHERE v.id IS NULL;
```

### Ejemplo 3: Productos más vendidos

```sql
SELECT 
    p.nombre,
    p.categoria,
    SUM(v.cantidad) AS total_vendido,
    SUM(v.total) AS ingresos_totales
FROM productos p
INNER JOIN ventas v ON p.id = v.producto_id
GROUP BY p.id, p.nombre, p.categoria
ORDER BY total_vendido DESC;
```

---

## 🔄 Múltiples JOINs

Puedes unir varias tablas en una sola consulta:

```sql
SELECT 
    v.id AS venta_id,
    v.fecha_venta,
    u.nombre AS cliente,
    u.ciudad AS ciudad_cliente,
    p.nombre AS producto,
    p.categoria,
    v.cantidad,
    v.total
FROM ventas v
INNER JOIN usuarios u ON v.usuario_id = u.id
INNER JOIN productos p ON v.producto_id = p.id
WHERE u.ciudad = 'Madrid'
  AND p.categoria = 'Electrónica'
ORDER BY v.fecha_venta DESC;
```

---

## 💡 Buenas prácticas

### 1. Usa alias de tabla

```sql
-- ✅ Claro y legible
SELECT u.nombre, v.total
FROM usuarios u
JOIN ventas v ON u.id = v.usuario_id;

-- ❌ Confuso
SELECT usuarios.nombre, ventas.total
FROM usuarios
JOIN ventas ON usuarios.id = ventas.usuario_id;
```

### 2. Especifica el tipo de JOIN

```sql
-- ✅ Explícito
SELECT * FROM usuarios u
INNER JOIN ventas v ON u.id = v.usuario_id;

-- ⚠️ Funciona pero menos claro
SELECT * FROM usuarios u
JOIN ventas v ON u.id = v.usuario_id;
```

### 3. Filtra en WHERE, no en ON

```sql
-- ✅ Correcto
SELECT u.nombre, v.total
FROM usuarios u
LEFT JOIN ventas v ON u.id = v.usuario_id
WHERE v.fecha_venta >= '2024-01-01';

-- ⚠️ Puede cambiar el resultado
SELECT u.nombre, v.total
FROM usuarios u
LEFT JOIN ventas v ON u.id = v.usuario_id 
  AND v.fecha_venta >= '2024-01-01';
```

---

## 🎯 Ejercicios

1. Lista todas las ventas con el nombre del cliente y producto
2. Encuentra usuarios que nunca han comprado nada
3. Muestra productos que nunca se han vendido
4. Calcula el total de ventas por ciudad del cliente
5. Lista las 5 categorías de productos más vendidas

---

## 🚀 Siguiente paso

Continúa con **[Agregaciones](03-agregaciones.md)** para resumir y agrupar datos.
