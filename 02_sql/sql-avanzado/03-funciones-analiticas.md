# Funciones analíticas avanzadas

Funciones avanzadas para análisis complejos de datos.

---

## 📊 Funciones de ranking avanzadas

### PERCENT_RANK() - Percentil relativo

```sql
-- Percentil de cada producto por ventas
SELECT 
    p.nombre,
    SUM(v.cantidad) AS unidades_vendidas,
    PERCENT_RANK() OVER (ORDER BY SUM(v.cantidad)) AS percentil
FROM productos p
LEFT JOIN ventas v ON p.id = v.producto_id
GROUP BY p.id, p.nombre;
```

### CUME_DIST() - Distribución acumulada

```sql
-- Distribución acumulada
SELECT 
    precio,
    CUME_DIST() OVER (ORDER BY precio) AS distribucion_acumulada
FROM productos;
```

---

## 📈 Funciones de agregación en ventanas

### SUM() con frames personalizados

```sql
-- Suma móvil de 7 días
SELECT 
    fecha_venta,
    total,
    SUM(total) OVER (
        ORDER BY fecha_venta
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS suma_7_dias
FROM ventas;
```

### AVG() con frames

```sql
-- Promedio móvil centrado
SELECT 
    fecha_venta,
    total,
    AVG(total) OVER (
        ORDER BY fecha_venta
        ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
    ) AS promedio_centrado
FROM ventas;
```

---

## 🔄 FIRST_VALUE y LAST_VALUE

```sql
-- Primer y último valor en la ventana
SELECT 
    categoria,
    nombre,
    precio,
    FIRST_VALUE(precio) OVER (
        PARTITION BY categoria 
        ORDER BY precio
    ) AS precio_minimo,
    LAST_VALUE(precio) OVER (
        PARTITION BY categoria 
        ORDER BY precio
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS precio_maximo
FROM productos;
```

---

## 🎯 Ejercicios

1. Calcula percentiles de ventas por categoría
2. Crea una suma móvil de 30 días
3. Encuentra el primer y último producto vendido por usuario
4. Calcula la diferencia con el valor anterior usando LAG()

---

## 🚀 Siguiente paso

Continúa con **[Patrones complejos](04-patrones-complejos.md)**.
