# Índices avanzados

Aprende a crear y mantener índices complejos para optimizar queries.

---

## 🔍 Tipos de índices

### Índice B-tree (por defecto)

```sql
-- Índice simple
CREATE INDEX idx_ventas_fecha ON ventas(fecha_venta);

-- Índice compuesto
CREATE INDEX idx_ventas_usuario_fecha ON ventas(usuario_id, fecha_venta);
```

### Índice parcial

```sql
-- Solo indexa filas que cumplen condición
CREATE INDEX idx_ventas_recientes 
ON ventas(fecha_venta) 
WHERE fecha_venta >= '2024-01-01';
```

### Índice de expresión

```sql
-- Indexa resultado de función
CREATE INDEX idx_usuarios_nombre_upper 
ON usuarios(UPPER(nombre));
```

### Índice único

```sql
-- Garantiza unicidad
CREATE UNIQUE INDEX idx_usuarios_email 
ON usuarios(email);
```

---

## 📊 Índices compuestos

### Orden de columnas importa

```sql
-- ✅ Bueno para: WHERE usuario_id = X AND fecha_venta >= Y
CREATE INDEX idx_ventas_usuario_fecha 
ON ventas(usuario_id, fecha_venta);

-- ⚠️ No útil para: WHERE fecha_venta >= Y (sin usuario_id)
-- Necesitarías otro índice solo en fecha_venta
```

### Regla general

Pon primero la columna más selectiva (con más valores únicos).

---

## 💡 Mantenimiento

### Ver índices existentes

```sql
-- PostgreSQL
SELECT 
    tablename,
    indexname,
    indexdef
FROM pg_indexes
WHERE tablename = 'ventas';
```

### Eliminar índices no usados

```sql
-- Ver índices no usados
SELECT 
    schemaname,
    tablename,
    indexname,
    idx_scan  -- Número de veces usado
FROM pg_stat_user_indexes
WHERE idx_scan = 0;

-- Eliminar
DROP INDEX nombre_indice;
```

---

## 🎯 Ejercicios

1. Crea índices compuestos para tus queries más comunes
2. Analiza qué índices se están usando
3. Elimina índices no utilizados
4. Crea índices parciales para datos recientes

---

## 🚀 Siguiente paso

Continúa con **[Funciones analíticas avanzadas](03-funciones-analiticas.md)**.
