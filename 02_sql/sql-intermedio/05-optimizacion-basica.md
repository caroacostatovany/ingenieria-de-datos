# Optimización básica

Aprende técnicas básicas para hacer tus queries más rápidas y eficientes.

---

## 🚀 Índices

Los índices aceleran las búsquedas en columnas específicas.

### Crear índices

```sql
-- Índice simple
CREATE INDEX idx_ventas_fecha ON ventas(fecha_venta);

-- Índice compuesto
CREATE INDEX idx_ventas_usuario_fecha ON ventas(usuario_id, fecha_venta);

-- Índice único
CREATE UNIQUE INDEX idx_usuarios_email ON usuarios(email);
```

### Cuándo crear índices

✅ **Crea índices en:**
* Columnas usadas frecuentemente en WHERE
* Columnas usadas en JOINs
* Columnas usadas en ORDER BY

❌ **No crees índices en:**
* Tablas muy pequeñas
* Columnas que cambian frecuentemente
* Columnas con pocos valores únicos

---

## 🔍 EXPLAIN - Analizar queries

`EXPLAIN` te muestra cómo el motor ejecutará tu query.

```sql
-- Ver el plan de ejecución
EXPLAIN SELECT * FROM ventas WHERE fecha_venta >= '2024-01-01';

-- Con estadísticas
EXPLAIN ANALYZE SELECT * FROM ventas WHERE fecha_venta >= '2024-01-01';
```

**Qué buscar:**
* `Seq Scan` (secuencial) - puede ser lento
* `Index Scan` - usa índice, más rápido
* `Nested Loop` - puede ser lento en tablas grandes

---

## 💡 Optimizaciones comunes

### 1. Filtra temprano

```sql
-- ✅ Filtra antes de JOIN
SELECT u.nombre, v.total
FROM usuarios u
JOIN ventas v ON u.id = v.usuario_id
WHERE v.fecha_venta >= '2024-01-01';

-- ⚠️ JOIN primero, luego filtra
SELECT u.nombre, v.total
FROM usuarios u
JOIN ventas v ON u.id = v.usuario_id
WHERE v.fecha_venta >= '2024-01-01';
```

### 2. Limita resultados

```sql
-- ✅ Limita temprano
SELECT * FROM ventas
WHERE fecha_venta >= '2024-01-01'
ORDER BY fecha_venta DESC
LIMIT 100;

-- ⚠️ Procesa todo y luego limita
SELECT * FROM (
    SELECT * FROM ventas
    ORDER BY fecha_venta DESC
) LIMIT 100;
```

### 3. Usa EXISTS en lugar de IN cuando sea posible

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

### 4. Evita funciones en WHERE

```sql
-- ⚠️ No usa índice
SELECT * FROM ventas
WHERE EXTRACT(YEAR FROM fecha_venta) = 2024;

-- ✅ Usa índice
SELECT * FROM ventas
WHERE fecha_venta >= '2024-01-01' 
  AND fecha_venta < '2025-01-01';
```

### 5. Selecciona solo columnas necesarias

```sql
-- ✅ Solo lo necesario
SELECT nombre, email FROM usuarios;

-- ⚠️ Trae todo
SELECT * FROM usuarios;
```

---

## 📊 Estadísticas y mantenimiento

### Actualizar estadísticas

```sql
-- PostgreSQL
ANALYZE ventas;

-- Actualizar estadísticas de todas las tablas
ANALYZE;
```

### Vacuum (PostgreSQL)

```sql
-- Limpiar espacio y actualizar estadísticas
VACUUM ANALYZE ventas;
```

---

## 🎯 Ejercicios

1. Analiza el plan de ejecución de una query compleja
2. Crea índices apropiados para tus queries más comunes
3. Compara el rendimiento de EXISTS vs IN
4. Optimiza una query que usa funciones en WHERE
5. Mide el tiempo de ejecución antes y después de crear índices

---

## 🚀 Siguiente paso

¡Felicidades! Has completado SQL intermedio. Continúa con **[SQL Avanzado](../sql-avanzado/)**.
