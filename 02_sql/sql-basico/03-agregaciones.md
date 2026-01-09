# Agregaciones

Las agregaciones te permiten resumir datos: contar, sumar, promediar, etc.

---

## 📊 Funciones de agregación básicas

### COUNT - Contar filas

```sql
-- Total de usuarios
SELECT COUNT(*) FROM usuarios;

-- Usuarios con ciudad definida
SELECT COUNT(ciudad) FROM usuarios;

-- Usuarios únicos por ciudad
SELECT COUNT(DISTINCT ciudad) FROM usuarios;
```

**Diferencia:**
* `COUNT(*)` cuenta todas las filas
* `COUNT(columna)` cuenta filas donde la columna no es NULL
* `COUNT(DISTINCT columna)` cuenta valores únicos

### SUM - Sumar valores

```sql
-- Total de ventas
SELECT SUM(total) FROM ventas;

-- Total de productos en stock
SELECT SUM(stock) FROM productos;
```

### AVG - Promedio

```sql
-- Edad promedio de usuarios
SELECT AVG(edad) FROM usuarios;

-- Precio promedio de productos
SELECT AVG(precio) FROM productos;
```

### MIN y MAX - Valores mínimo y máximo

```sql
-- Usuario más joven y más viejo
SELECT 
    MIN(edad) AS edad_minima,
    MAX(edad) AS edad_maxima
FROM usuarios;

-- Rango de precios
SELECT 
    MIN(precio) AS precio_minimo,
    MAX(precio) AS precio_maximo
FROM productos;
```

---

## 📦 GROUP BY - Agrupar datos

`GROUP BY` agrupa filas que tienen el mismo valor en una o más columnas.

### Ejemplo básico

```sql
-- Ventas por categoría de producto
SELECT 
    categoria,
    COUNT(*) AS total_ventas,
    SUM(total) AS ingresos_totales
FROM ventas v
JOIN productos p ON v.producto_id = p.id
GROUP BY categoria;
```

### Múltiples columnas

```sql
-- Ventas por ciudad y categoría
SELECT 
    u.ciudad,
    p.categoria,
    COUNT(*) AS total_ventas,
    SUM(v.total) AS ingresos
FROM ventas v
JOIN usuarios u ON v.usuario_id = u.id
JOIN productos p ON v.producto_id = p.id
GROUP BY u.ciudad, p.categoria;
```

### Regla importante

Todas las columnas en `SELECT` que no sean agregaciones deben estar en `GROUP BY`:

```sql
-- ✅ Correcto
SELECT ciudad, COUNT(*) 
FROM usuarios 
GROUP BY ciudad;

-- ❌ Error (en la mayoría de sistemas)
SELECT ciudad, nombre, COUNT(*) 
FROM usuarios 
GROUP BY ciudad;
```

---

## 🔍 HAVING - Filtrar grupos

`HAVING` filtra grupos después de la agregación (similar a `WHERE` pero para grupos).

```sql
-- Categorías con más de 5 ventas
SELECT 
    categoria,
    COUNT(*) AS total_ventas
FROM ventas v
JOIN productos p ON v.producto_id = p.id
GROUP BY categoria
HAVING COUNT(*) > 5;
```

**Diferencia WHERE vs HAVING:**
* `WHERE` filtra filas **antes** de la agregación
* `HAVING` filtra grupos **después** de la agregación

```sql
-- Ejemplo combinando ambos
SELECT 
    u.ciudad,
    COUNT(*) AS total_ventas,
    SUM(v.total) AS ingresos
FROM ventas v
JOIN usuarios u ON v.usuario_id = u.id
WHERE v.fecha_venta >= '2024-01-01'  -- Filtra filas
GROUP BY u.ciudad
HAVING SUM(v.total) > 1000;  -- Filtra grupos
```

---

## 🎯 Ejemplos prácticos

### Ejemplo 1: Top 5 productos más vendidos

```sql
SELECT 
    p.nombre,
    SUM(v.cantidad) AS unidades_vendidas,
    SUM(v.total) AS ingresos
FROM ventas v
JOIN productos p ON v.producto_id = p.id
GROUP BY p.id, p.nombre
ORDER BY unidades_vendidas DESC
LIMIT 5;
```

### Ejemplo 2: Estadísticas por ciudad

```sql
SELECT 
    u.ciudad,
    COUNT(DISTINCT u.id) AS total_clientes,
    COUNT(v.id) AS total_ventas,
    SUM(v.total) AS ingresos_totales,
    AVG(v.total) AS ticket_promedio
FROM usuarios u
LEFT JOIN ventas v ON u.id = v.usuario_id
GROUP BY u.ciudad
ORDER BY ingresos_totales DESC;
```

### Ejemplo 3: Ventas mensuales

```sql
SELECT 
    DATE_TRUNC('month', fecha_venta) AS mes,
    COUNT(*) AS total_ventas,
    SUM(total) AS ingresos,
    AVG(total) AS ticket_promedio
FROM ventas
GROUP BY DATE_TRUNC('month', fecha_venta)
ORDER BY mes DESC;
```

**Nota**: `DATE_TRUNC` es específico de PostgreSQL. En otros sistemas usa funciones equivalentes.

---

## 💡 Buenas prácticas

### 1. Usa alias descriptivos

```sql
-- ✅ Claro
SELECT 
    categoria,
    COUNT(*) AS total_productos,
    AVG(precio) AS precio_promedio
FROM productos
GROUP BY categoria;
```

### 2. Filtra antes de agrupar cuando sea posible

```sql
-- ✅ Más eficiente
SELECT categoria, COUNT(*)
FROM productos
WHERE precio > 50
GROUP BY categoria;

-- ⚠️ Menos eficiente (agrupa todo y luego filtra)
SELECT categoria, COUNT(*)
FROM productos
GROUP BY categoria
HAVING AVG(precio) > 50;
```

### 3. Ordena los resultados

```sql
-- ✅ Resultados ordenados
SELECT ciudad, COUNT(*)
FROM usuarios
GROUP BY ciudad
ORDER BY COUNT(*) DESC;
```

---

## 🎯 Ejercicios

1. Calcula el total de ingresos por categoría de producto
2. Encuentra las 3 ciudades con más ventas
3. Calcula el ticket promedio por mes
4. Lista categorías con más de 3 productos
5. Encuentra usuarios que han comprado más de 5 veces

---

## 🚀 Siguiente paso

Continúa con **[Ordenamiento y límites](04-ordenamiento-y-limites.md)**.
