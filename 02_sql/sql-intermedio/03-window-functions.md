# Window Functions

Las Window Functions (funciones de ventana) te permiten realizar cálculos sobre un conjunto de filas relacionadas sin agrupar los resultados.

---

## 🔍 ¿Qué son Window Functions?

A diferencia de las agregaciones con `GROUP BY`, las window functions mantienen todas las filas y agregan una columna con el resultado.

### Sintaxis básica

```sql
SELECT 
    columna,
    FUNCION() OVER (PARTITION BY ... ORDER BY ...) AS resultado
FROM tabla;
```

---

## 📊 Funciones de ventana comunes

### ROW_NUMBER() - Numerar filas

```sql
-- Numerar ventas por usuario
SELECT 
    usuario_id,
    fecha_venta,
    total,
    ROW_NUMBER() OVER (
        PARTITION BY usuario_id 
        ORDER BY fecha_venta DESC
    ) AS numero_venta
FROM ventas;
```

### RANK() y DENSE_RANK()

```sql
-- Ranking de productos por ventas
SELECT 
    producto_id,
    SUM(cantidad) AS unidades_vendidas,
    RANK() OVER (ORDER BY SUM(cantidad) DESC) AS ranking,
    DENSE_RANK() OVER (ORDER BY SUM(cantidad) DESC) AS ranking_denso
FROM ventas
GROUP BY producto_id;
```

**Diferencia:**
* `RANK()` deja gaps (1, 2, 2, 4, 5...)
* `DENSE_RANK()` no deja gaps (1, 2, 2, 3, 4...)

### SUM() OVER - Suma acumulada

```sql
-- Ventas acumuladas por mes
SELECT 
    DATE_TRUNC('month', fecha_venta) AS mes,
    SUM(total) AS ventas_mes,
    SUM(SUM(total)) OVER (
        ORDER BY DATE_TRUNC('month', fecha_venta)
    ) AS ventas_acumuladas
FROM ventas
GROUP BY DATE_TRUNC('month', fecha_venta)
ORDER BY mes;
```

### AVG() OVER - Promedio móvil

```sql
-- Promedio móvil de 3 meses
SELECT 
    mes,
    ventas,
    AVG(ventas) OVER (
        ORDER BY mes
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS promedio_movil_3_meses
FROM ventas_mensuales;
```

### LAG() y LEAD() - Valores anteriores/siguientes

```sql
-- Comparar con el mes anterior
SELECT 
    mes,
    ingresos,
    LAG(ingresos) OVER (ORDER BY mes) AS ingresos_mes_anterior,
    ingresos - LAG(ingresos) OVER (ORDER BY mes) AS diferencia
FROM ventas_mensuales;
```

```sql
-- Comparar con el mes siguiente
SELECT 
    mes,
    ingresos,
    LEAD(ingresos) OVER (ORDER BY mes) AS ingresos_mes_siguiente
FROM ventas_mensuales;
```

---

## 🎯 Ejemplos prácticos

### Ejemplo 1: Top N por categoría

```sql
-- Top 3 productos por categoría
SELECT 
    categoria,
    nombre,
    precio,
    unidades_vendidas
FROM (
    SELECT 
        p.categoria,
        p.nombre,
        p.precio,
        SUM(v.cantidad) AS unidades_vendidas,
        ROW_NUMBER() OVER (
            PARTITION BY p.categoria 
            ORDER BY SUM(v.cantidad) DESC
        ) AS ranking
    FROM productos p
    JOIN ventas v ON p.id = v.producto_id
    GROUP BY p.id, p.categoria, p.nombre, p.precio
) AS ranked
WHERE ranking <= 3;
```

### Ejemplo 2: Crecimiento mes a mes

```sql
WITH ventas_mensuales AS (
    SELECT 
        DATE_TRUNC('month', fecha_venta) AS mes,
        SUM(total) AS ingresos
    FROM ventas
    GROUP BY DATE_TRUNC('month', fecha_venta)
)
SELECT 
    mes,
    ingresos,
    LAG(ingresos) OVER (ORDER BY mes) AS ingresos_anterior,
    ingresos - LAG(ingresos) OVER (ORDER BY mes) AS crecimiento_absoluto,
    ROUND(
        ((ingresos - LAG(ingresos) OVER (ORDER BY mes)) / 
         LAG(ingresos) OVER (ORDER BY mes)) * 100, 
        2
    ) AS crecimiento_porcentual
FROM ventas_mensuales
ORDER BY mes;
```

### Ejemplo 3: Percentiles

```sql
-- Percentil 50 (mediana) y percentil 90 por categoría
-- Nota: PERCENTILE_CONT no puede usarse directamente como window function
-- Se usa con GROUP BY o como subconsulta
SELECT 
    p.categoria,
    p.nombre,
    p.precio,
    percentiles.mediana,
    percentiles.percentil_90
FROM productos p
JOIN (
    SELECT 
        categoria,
        PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY precio) AS mediana,
        PERCENTILE_CONT(0.9) WITHIN GROUP (ORDER BY precio) AS percentil_90
    FROM productos
    GROUP BY categoria
) AS percentiles ON p.categoria = percentiles.categoria;
```

---

## 💡 Buenas prácticas

### 1. Usa PARTITION BY para grupos lógicos

```sql
-- ✅ Agrupa por categoría
SELECT 
    categoria,
    nombre,
    precio,
    AVG(precio) OVER (PARTITION BY categoria) AS precio_promedio_categoria
FROM productos;
```

### 2. Especifica ORDER BY cuando sea necesario

```sql
-- ✅ Orden claro
SELECT 
    fecha_venta,
    total,
    SUM(total) OVER (ORDER BY fecha_venta) AS acumulado
FROM ventas;
```

### 3. Considera el rendimiento

```sql
-- ⚠️ Puede ser lento en tablas grandes
SELECT 
    *,
    ROW_NUMBER() OVER (ORDER BY fecha_venta)
FROM ventas;

-- ✅ Más eficiente con índice
SELECT 
    *,
    ROW_NUMBER() OVER (ORDER BY fecha_venta)
FROM ventas
WHERE fecha_venta >= '2024-01-01';
```

---

## 🎯 Ejercicios

1. Calcula el ranking de productos por ingresos usando RANK()
2. Crea una columna con las ventas acumuladas por mes
3. Compara cada venta con el promedio de ventas del usuario
4. Encuentra el producto más vendido de cada mes
5. Calcula el crecimiento porcentual mes a mes

---

## 🚀 Siguiente paso

Continúa con **[Manejo avanzado de fechas](04-fechas-avanzadas.md)**.
