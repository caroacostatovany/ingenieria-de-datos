# Manejo avanzado de fechas

El manejo de fechas es crucial en Data Engineering. Aprende a trabajar con fechas de forma eficiente.

> **Nota**: Este documento usa funciones de **PostgreSQL**. Funciones equivalentes existen en otros sistemas pero con sintaxis diferente.

---

## 📅 Funciones de fecha comunes

### Extraer componentes

```sql
-- Componentes de fecha
SELECT 
    fecha_venta,
    EXTRACT(YEAR FROM fecha_venta) AS año,
    EXTRACT(MONTH FROM fecha_venta) AS mes,
    EXTRACT(DAY FROM fecha_venta) AS dia,
    EXTRACT(DOW FROM fecha_venta) AS dia_semana,  -- 0=Domingo, 6=Sábado
    EXTRACT(QUARTER FROM fecha_venta) AS trimestre
FROM ventas;
```

### Formatear fechas

```sql
-- PostgreSQL
SELECT 
    fecha_venta,
    TO_CHAR(fecha_venta, 'YYYY-MM-DD') AS fecha_formato1,
    TO_CHAR(fecha_venta, 'DD/MM/YYYY') AS fecha_formato2,
    TO_CHAR(fecha_venta, 'Month YYYY') AS mes_texto
FROM ventas;

-- MySQL
SELECT 
    fecha_venta,
    DATE_FORMAT(fecha_venta, '%Y-%m-%d') AS fecha_formato1,
    DATE_FORMAT(fecha_venta, '%d/%m/%Y') AS fecha_formato2
FROM ventas;
```

---

## ⏰ Intervalos y cálculos

### Sumar/restar tiempo

```sql
-- PostgreSQL
SELECT 
    fecha_venta,
    fecha_venta + INTERVAL '7 days' AS fecha_semana_siguiente,
    fecha_venta - INTERVAL '1 month' AS fecha_mes_anterior,
    fecha_venta + INTERVAL '2 hours' AS fecha_con_hora
FROM ventas;

-- MySQL
SELECT 
    fecha_venta,
    DATE_ADD(fecha_venta, INTERVAL 7 DAY) AS fecha_semana_siguiente,
    DATE_SUB(fecha_venta, INTERVAL 1 MONTH) AS fecha_mes_anterior
FROM ventas;
```

### Diferencia entre fechas

```sql
-- PostgreSQL
SELECT 
    fecha_registro,
    fecha_venta,
    fecha_venta - fecha_registro AS dias_diferencia,
    AGE(fecha_venta, fecha_registro) AS edad_intervalo
FROM usuarios u
JOIN ventas v ON u.id = v.usuario_id;

-- MySQL
SELECT 
    fecha_registro,
    fecha_venta,
    DATEDIFF(fecha_venta, fecha_registro) AS dias_diferencia
FROM usuarios u
JOIN ventas v ON u.id = v.usuario_id;
```

---

## 📊 Agrupación por períodos

### Por mes

```sql
-- PostgreSQL
SELECT 
    DATE_TRUNC('month', fecha_venta) AS mes,
    COUNT(*) AS total_ventas,
    SUM(total) AS ingresos
FROM ventas
GROUP BY DATE_TRUNC('month', fecha_venta)
ORDER BY mes;

-- MySQL
SELECT 
    DATE_FORMAT(fecha_venta, '%Y-%m-01') AS mes,
    COUNT(*) AS total_ventas,
    SUM(total) AS ingresos
FROM ventas
GROUP BY DATE_FORMAT(fecha_venta, '%Y-%m-01')
ORDER BY mes;
```

### Por semana

```sql
-- PostgreSQL
SELECT 
    DATE_TRUNC('week', fecha_venta) AS semana,
    COUNT(*) AS total_ventas
FROM ventas
GROUP BY DATE_TRUNC('week', fecha_venta)
ORDER BY semana;
```

### Por trimestre

```sql
SELECT 
    EXTRACT(YEAR FROM fecha_venta) AS año,
    EXTRACT(QUARTER FROM fecha_venta) AS trimestre,
    COUNT(*) AS total_ventas,
    SUM(total) AS ingresos
FROM ventas
GROUP BY 
    EXTRACT(YEAR FROM fecha_venta),
    EXTRACT(QUARTER FROM fecha_venta)
ORDER BY año, trimestre;
```

---

## 🎯 Ejemplos prácticos

### Ejemplo 1: Ventas del último mes

```sql
-- PostgreSQL
SELECT * FROM ventas
WHERE fecha_venta >= DATE_TRUNC('month', CURRENT_DATE)
  AND fecha_venta < DATE_TRUNC('month', CURRENT_DATE) + INTERVAL '1 month';

-- O más simple
SELECT * FROM ventas
WHERE fecha_venta >= DATE_TRUNC('month', CURRENT_DATE)
  AND fecha_venta < CURRENT_DATE + INTERVAL '1 month';
```

### Ejemplo 2: Comparar períodos

```sql
WITH 
    ventas_actual AS (
        SELECT 
            DATE_TRUNC('month', fecha_venta) AS mes,
            SUM(total) AS ingresos
        FROM ventas
        WHERE fecha_venta >= DATE_TRUNC('month', CURRENT_DATE)
        GROUP BY DATE_TRUNC('month', fecha_venta)
    ),
    ventas_anterior AS (
        SELECT 
            DATE_TRUNC('month', fecha_venta) AS mes,
            SUM(total) AS ingresos
        FROM ventas
        WHERE fecha_venta >= DATE_TRUNC('month', CURRENT_DATE) - INTERVAL '1 month'
          AND fecha_venta < DATE_TRUNC('month', CURRENT_DATE)
        GROUP BY DATE_TRUNC('month', fecha_venta)
    )
SELECT 
    va.ingresos AS ingresos_actual,
    vp.ingresos AS ingresos_anterior,
    va.ingresos - vp.ingresos AS diferencia,
    ROUND(((va.ingresos - vp.ingresos) / vp.ingresos) * 100, 2) AS crecimiento_porcentual
FROM ventas_actual va
CROSS JOIN ventas_anterior vp;
```

### Ejemplo 3: Análisis por día de la semana

```sql
SELECT 
    CASE EXTRACT(DOW FROM fecha_venta)
        WHEN 0 THEN 'Domingo'
        WHEN 1 THEN 'Lunes'
        WHEN 2 THEN 'Martes'
        WHEN 3 THEN 'Miércoles'
        WHEN 4 THEN 'Jueves'
        WHEN 5 THEN 'Viernes'
        WHEN 6 THEN 'Sábado'
    END AS dia_semana,
    COUNT(*) AS total_ventas,
    SUM(total) AS ingresos,
    AVG(total) AS ticket_promedio
FROM ventas
GROUP BY EXTRACT(DOW FROM fecha_venta)
ORDER BY EXTRACT(DOW FROM fecha_venta);
```

---

## 💡 Buenas prácticas

### 1. Usa índices en columnas de fecha

```sql
-- ✅ Si hay índice en fecha_venta
SELECT * FROM ventas
WHERE fecha_venta >= '2024-01-01';
```

### 2. Evita funciones en WHERE cuando sea posible

```sql
-- ⚠️ Puede ser lento (no usa índice)
SELECT * FROM ventas
WHERE EXTRACT(YEAR FROM fecha_venta) = 2024;

-- ✅ Mejor (usa índice)
SELECT * FROM ventas
WHERE fecha_venta >= '2024-01-01' 
  AND fecha_venta < '2025-01-01';
```

### 3. Considera zonas horarias

```sql
-- Especifica zona horaria si es necesario
SELECT 
    fecha_venta AT TIME ZONE 'UTC' AS fecha_utc,
    fecha_venta AT TIME ZONE 'Europe/Madrid' AS fecha_madrid
FROM ventas;
```

---

## 🎯 Ejercicios

1. Calcula las ventas del último trimestre
2. Compara ventas de este mes con el mismo mes del año pasado
3. Encuentra el día de la semana con más ventas
4. Calcula la diferencia en días entre la primera y última venta de cada usuario
5. Agrupa ventas por semana y calcula crecimiento semanal

---

## 🚀 Siguiente paso

Continúa con **[Optimización básica](05-optimizacion-basica.md)**.
