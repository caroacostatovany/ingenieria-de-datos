# Particionamiento

El particionamiento divide tablas grandes en partes más pequeñas para mejorar el rendimiento.

> **Nota**: Los ejemplos usan sintaxis de **PostgreSQL**. Otros sistemas tienen sintaxis diferente para particionamiento.

---

## 🧠 ¿Por qué particionar?

**Ventajas:**
* Consultas más rápidas (menos datos a escanear)
* Mantenimiento más fácil (puedes eliminar particiones viejas)
* Mejor paralelización

**Cuándo usar:**
* Tablas con millones de filas
* Datos con patrón temporal claro (fechas)
* Necesitas eliminar datos antiguos frecuentemente

---

## 📅 Particionamiento por rango (Range Partitioning)

### Crear tabla particionada

```sql
-- PostgreSQL: Tabla de ventas particionada por mes
CREATE TABLE ventas (
    id SERIAL,
    usuario_id INTEGER,
    producto_id INTEGER,
    fecha_venta DATE,
    total DECIMAL(10,2)
) PARTITION BY RANGE (fecha_venta);

-- Crear particiones
CREATE TABLE ventas_2024_01 PARTITION OF ventas
    FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');

CREATE TABLE ventas_2024_02 PARTITION OF ventas
    FOR VALUES FROM ('2024-02-01') TO ('2024-03-01');
```

### Consultar tabla particionada

```sql
-- El motor selecciona automáticamente la partición correcta
SELECT * FROM ventas
WHERE fecha_venta >= '2024-01-15' 
  AND fecha_venta < '2024-01-20';
```

---

## 🔢 Particionamiento por lista (List Partitioning)

```sql
-- Particionar por categoría
CREATE TABLE productos (
    id SERIAL,
    nombre VARCHAR(100),
    categoria VARCHAR(50),
    precio DECIMAL(10,2)
) PARTITION BY LIST (categoria);

CREATE TABLE productos_electronica PARTITION OF productos
    FOR VALUES IN ('Electrónica');

CREATE TABLE productos_muebles PARTITION OF productos
    FOR VALUES IN ('Muebles', 'Iluminación');
```

---

## 💡 Buenas prácticas

### 1. Particiona por columnas usadas frecuentemente en WHERE

```sql
-- ✅ Si siempre filtras por fecha
PARTITION BY RANGE (fecha_venta);

-- ⚠️ Si raramente filtras por fecha
PARTITION BY RANGE (fecha_venta);  -- No útil
```

### 2. Crea particiones futuras automáticamente

```sql
-- Script para crear particiones mensuales
DO $$
DECLARE
    fecha_inicio DATE;
    fecha_fin DATE;
BEGIN
    FOR i IN 0..11 LOOP
        fecha_inicio := DATE_TRUNC('month', CURRENT_DATE) + (i || ' months')::INTERVAL;
        fecha_fin := fecha_inicio + '1 month'::INTERVAL;
        
        EXECUTE format(
            'CREATE TABLE IF NOT EXISTS ventas_%s PARTITION OF ventas
             FOR VALUES FROM (%L) TO (%L)',
            TO_CHAR(fecha_inicio, 'YYYY_MM'),
            fecha_inicio,
            fecha_fin
        );
    END LOOP;
END $$;
```

### 3. Elimina particiones antiguas

```sql
-- Eliminar particiones de más de 1 año
DROP TABLE IF EXISTS ventas_2023_01;
```

---

## 🎯 Ejercicios

1. Crea una tabla particionada por mes para ventas
2. Consulta datos de una partición específica
3. Elimina particiones antiguas automáticamente
4. Mide el rendimiento de queries en tabla particionada vs no particionada

---

## 🚀 Siguiente paso

Continúa con **[Índices avanzados](02-indices-avanzados.md)**.
