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

> 💡 **Nota**: Los siguientes ejemplos requieren crear nuevas tablas particionadas. La tabla `ventas` existente en nuestra base de datos de ejemplo no está particionada. Estos ejemplos son para aprender el concepto.

### Crear tabla particionada

```sql
-- PostgreSQL: Tabla de ventas particionada por mes
-- ⚠️ Esto crea una NUEVA tabla, no modifica la existente
CREATE TABLE ventas_particionadas (
    id SERIAL,
    usuario_id INTEGER,
    producto_id INTEGER,
    fecha_venta DATE,
    total DECIMAL(10,2)
) PARTITION BY RANGE (fecha_venta);

-- Crear particiones
CREATE TABLE ventas_particionadas_2024_01 PARTITION OF ventas_particionadas
    FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');

CREATE TABLE ventas_particionadas_2024_02 PARTITION OF ventas_particionadas
    FOR VALUES FROM ('2024-02-01') TO ('2024-03-01');
```

### Consultar tabla particionada

```sql
-- El motor selecciona automáticamente la partición correcta
-- PostgreSQL optimiza automáticamente para usar solo las particiones relevantes
SELECT * FROM ventas_particionadas
WHERE fecha_venta >= '2024-01-15' 
  AND fecha_venta < '2024-01-20';
```

---

## 🔢 Particionamiento por lista (List Partitioning)

> 💡 **Nota**: Este ejemplo crea una nueva tabla particionada. La tabla `productos` existente no está particionada.

```sql
-- Particionar por categoría
-- ⚠️ Esto crea una NUEVA tabla, no modifica la existente
CREATE TABLE productos_particionados (
    id SERIAL,
    nombre VARCHAR(100),
    categoria VARCHAR(50),
    precio DECIMAL(10,2)
) PARTITION BY LIST (categoria);

CREATE TABLE productos_particionados_electronica PARTITION OF productos_particionados
    FOR VALUES IN ('Electrónica');

CREATE TABLE productos_particionados_muebles PARTITION OF productos_particionados
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
-- ⚠️ Asegúrate de que la tabla 'ventas_particionadas' exista antes de ejecutar
DO $$
DECLARE
    fecha_inicio DATE;
    fecha_fin DATE;
BEGIN
    FOR i IN 0..11 LOOP
        fecha_inicio := DATE_TRUNC('month', CURRENT_DATE) + (i || ' months')::INTERVAL;
        fecha_fin := fecha_inicio + '1 month'::INTERVAL;
        
        EXECUTE format(
            'CREATE TABLE IF NOT EXISTS ventas_particionadas_%s PARTITION OF ventas_particionadas
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
