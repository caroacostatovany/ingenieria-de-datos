# Ordenamiento y límites

Aprende a ordenar resultados y limitar la cantidad de filas devueltas.

---

## 📊 ORDER BY - Ordenar resultados

`ORDER BY` ordena los resultados según una o más columnas.

### Ordenamiento básico

```sql
-- Ordenar por nombre (ascendente por defecto)
SELECT * FROM usuarios ORDER BY nombre;

-- Explícitamente ascendente
SELECT * FROM usuarios ORDER BY nombre ASC;

-- Descendente
SELECT * FROM productos ORDER BY precio DESC;
```

### Múltiples columnas

```sql
-- Ordenar por ciudad, luego por nombre
SELECT * FROM usuarios 
ORDER BY ciudad ASC, nombre ASC;

-- Ciudad ascendente, edad descendente
SELECT * FROM usuarios 
ORDER BY ciudad ASC, edad DESC;
```

### Ordenar por posición

```sql
-- Ordenar por la segunda columna (edad)
SELECT nombre, edad, ciudad 
FROM usuarios 
ORDER BY 2 DESC;
```

**⚠️ No recomendado**: Es mejor usar nombres de columnas para claridad.

### Ordenar por expresiones

```sql
-- Ordenar por longitud del nombre
SELECT nombre 
FROM usuarios 
ORDER BY LENGTH(nombre) DESC;

-- Ordenar por cálculo
SELECT nombre, precio, stock 
FROM productos 
ORDER BY precio * stock DESC;
```

---

## 🔢 LIMIT - Limitar resultados

`LIMIT` restringe el número de filas devueltas.

### Uso básico

```sql
-- Primeros 10 usuarios
SELECT * FROM usuarios LIMIT 10;

-- Top 5 productos más caros
SELECT nombre, precio 
FROM productos 
ORDER BY precio DESC 
LIMIT 5;
```

### OFFSET - Saltar filas

`OFFSET` salta un número de filas antes de empezar a devolver resultados.

```sql
-- Filas 11 a 20 (paginación)
SELECT * FROM usuarios 
ORDER BY nombre 
LIMIT 10 OFFSET 10;
```

**Uso común**: Paginación de resultados

```sql
-- Página 1 (primeros 10)
SELECT * FROM usuarios LIMIT 10 OFFSET 0;

-- Página 2 (siguientes 10)
SELECT * FROM usuarios LIMIT 10 OFFSET 10;

-- Página 3 (siguientes 10)
SELECT * FROM usuarios LIMIT 10 OFFSET 20;
```

---

## 🎯 Ejemplos prácticos

### Top N resultados

```sql
-- Top 5 productos más vendidos
SELECT 
    p.nombre,
    SUM(v.cantidad) AS unidades_vendidas
FROM productos p
JOIN ventas v ON p.id = v.producto_id
GROUP BY p.id, p.nombre
ORDER BY unidades_vendidas DESC
LIMIT 5;
```

### Últimos registros

```sql
-- Últimas 10 ventas
SELECT 
    v.fecha_venta,
    u.nombre AS cliente,
    p.nombre AS producto,
    v.total
FROM ventas v
JOIN usuarios u ON v.usuario_id = u.id
JOIN productos p ON v.producto_id = p.id
ORDER BY v.fecha_venta DESC
LIMIT 10;
```

### Paginación

```sql
-- Página de resultados (ejemplo: página 2, 20 por página)
SELECT 
    u.nombre,
    u.email,
    COUNT(v.id) AS total_ventas
FROM usuarios u
LEFT JOIN ventas v ON u.id = v.usuario_id
GROUP BY u.id, u.nombre, u.email
ORDER BY total_ventas DESC
LIMIT 20 OFFSET 20;
```

---

## 💡 Buenas prácticas

### 1. Siempre usa ORDER BY con LIMIT

```sql
-- ✅ Resultados predecibles
SELECT * FROM productos 
ORDER BY precio DESC 
LIMIT 5;

-- ⚠️ Resultados no garantizados
SELECT * FROM productos LIMIT 5;
```

### 2. Ordena por índices cuando sea posible

```sql
-- ✅ Si hay índice en fecha_venta
SELECT * FROM ventas 
ORDER BY fecha_venta DESC;

-- ⚠️ Más lento si no hay índice
SELECT * FROM ventas 
ORDER BY DATE_TRUNC('month', fecha_venta);
```

### 3. Usa alias en ORDER BY

```sql
-- ✅ Claro
SELECT 
    categoria,
    COUNT(*) AS total
FROM productos
GROUP BY categoria
ORDER BY total DESC;
```

---

## 🎯 Ejercicios

1. Lista los 10 usuarios más jóvenes
2. Encuentra los 3 productos más caros por categoría
3. Muestra las últimas 5 ventas de cada ciudad
4. Implementa paginación: página 2 con 15 resultados por página
5. Top 5 ciudades por número de clientes

---

## 🚀 Siguiente paso

Continúa con **[Funciones comunes](05-funciones-comunes.md)**.
