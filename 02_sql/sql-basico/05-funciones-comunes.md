# Funciones comunes

SQL tiene muchas funciones útiles para trabajar con datos. Aquí las más comunes para Data Engineering.

---

## 📝 Funciones de texto (Strings)

### UPPER y LOWER

```sql
-- Convertir a mayúsculas
SELECT UPPER(nombre) FROM usuarios;
-- Resultado: "JUAN PÉREZ"

-- Convertir a minúsculas
SELECT LOWER(email) FROM usuarios;
-- Resultado: "juan@example.com"
```

### TRIM - Eliminar espacios

```sql
-- Eliminar espacios al inicio y final
SELECT TRIM('  Juan Pérez  ') AS nombre;
-- Resultado: "Juan Pérez"

-- Eliminar espacios solo al inicio
SELECT LTRIM('  Juan Pérez') AS nombre;

-- Eliminar espacios solo al final
SELECT RTRIM('Juan Pérez  ') AS nombre;
```

### CONCAT - Concatenar strings

```sql
-- Concatenar nombre y apellido
SELECT CONCAT(nombre, ' ', apellido) AS nombre_completo
FROM usuarios;

-- O usando ||
SELECT nombre || ' ' || apellido AS nombre_completo
FROM usuarios;
```

### SUBSTRING - Extraer parte del string

```sql
-- Primeros 3 caracteres
SELECT SUBSTRING(nombre, 1, 3) FROM usuarios;

-- Desde la posición 5, 10 caracteres
SELECT SUBSTRING(email, 5, 10) FROM usuarios;
```

### LENGTH - Longitud del string

```sql
-- Longitud del nombre
SELECT nombre, LENGTH(nombre) AS longitud
FROM usuarios;
```

---

## 📅 Funciones de fecha

### CURRENT_DATE y CURRENT_TIMESTAMP

```sql
-- Fecha actual
SELECT CURRENT_DATE;

-- Fecha y hora actual
SELECT CURRENT_TIMESTAMP;
```

### EXTRACT - Extraer parte de fecha

```sql
-- Año de la fecha
SELECT EXTRACT(YEAR FROM fecha_venta) AS año
FROM ventas;

-- Mes
SELECT EXTRACT(MONTH FROM fecha_venta) AS mes
FROM ventas;

-- Día
SELECT EXTRACT(DAY FROM fecha_venta) AS dia
FROM ventas;
```

### DATE_TRUNC - Truncar fecha

```sql
-- Agrupar por mes
SELECT 
    DATE_TRUNC('month', fecha_venta) AS mes,
    COUNT(*) AS ventas
FROM ventas
GROUP BY DATE_TRUNC('month', fecha_venta);

-- Agrupar por día
SELECT 
    DATE_TRUNC('day', fecha_venta) AS dia,
    SUM(total) AS ingresos
FROM ventas
GROUP BY DATE_TRUNC('day', fecha_venta);
```

**Nota**: `DATE_TRUNC` es específico de PostgreSQL. En otros sistemas:
- MySQL: `DATE_FORMAT(fecha, '%Y-%m-01')`
- SQL Server: `DATETRUNC(month, fecha)`

### Intervalos

```sql
-- Fechas de hace 30 días
SELECT * FROM ventas
WHERE fecha_venta >= CURRENT_DATE - INTERVAL '30 days';

-- Fechas del último mes
SELECT * FROM ventas
WHERE fecha_venta >= DATE_TRUNC('month', CURRENT_DATE);
```

---

## 🔢 Funciones numéricas

### ROUND - Redondear

```sql
-- Redondear a 2 decimales
SELECT ROUND(precio, 2) FROM productos;

-- Redondear al entero más cercano
SELECT ROUND(precio) FROM productos;
```

### CEIL y FLOOR

```sql
-- Redondear hacia arriba
SELECT CEIL(4.3);  -- Resultado: 5

-- Redondear hacia abajo
SELECT FLOOR(4.7);  -- Resultado: 4
```

### ABS - Valor absoluto

```sql
SELECT ABS(-10);  -- Resultado: 10
```

---

## 🔄 CASE - Condicionales

`CASE` te permite crear lógica condicional en SQL.

### CASE simple

```sql
SELECT 
    nombre,
    edad,
    CASE 
        WHEN edad < 18 THEN 'Menor'
        WHEN edad < 65 THEN 'Adulto'
        ELSE 'Senior'
    END AS categoria_edad
FROM usuarios;
```

### CASE con expresión

```sql
SELECT 
    nombre,
    precio,
    CASE categoria
        WHEN 'Electrónica' THEN precio * 1.16
        WHEN 'Muebles' THEN precio * 1.10
        ELSE precio
    END AS precio_con_impuesto
FROM productos;
```

---

## 🎯 Ejemplos prácticos

### Ejemplo 1: Limpiar y normalizar datos

```sql
SELECT 
    UPPER(TRIM(nombre)) AS nombre_limpio,
    LOWER(email) AS email_normalizado,
    CASE 
        WHEN ciudad IS NULL THEN 'Sin ciudad'
        ELSE UPPER(ciudad)
    END AS ciudad_normalizada
FROM usuarios;
```

### Ejemplo 2: Análisis temporal

```sql
SELECT 
    DATE_TRUNC('month', fecha_venta) AS mes,
    EXTRACT(DOW FROM fecha_venta) AS dia_semana,
    COUNT(*) AS total_ventas,
    SUM(total) AS ingresos
FROM ventas
GROUP BY 
    DATE_TRUNC('month', fecha_venta),
    EXTRACT(DOW FROM fecha_venta)
ORDER BY mes DESC;
```

### Ejemplo 3: Categorización

```sql
SELECT 
    nombre,
    precio,
    CASE 
        WHEN precio < 50 THEN 'Económico'
        WHEN precio < 200 THEN 'Medio'
        WHEN precio < 500 THEN 'Alto'
        ELSE 'Premium'
    END AS categoria_precio,
    CASE 
        WHEN stock = 0 THEN 'Agotado'
        WHEN stock < 10 THEN 'Bajo stock'
        ELSE 'Disponible'
    END AS estado_stock
FROM productos;
```

---

## 💡 Buenas prácticas

### 1. Usa funciones para normalizar datos

```sql
-- ✅ Normaliza al consultar
SELECT UPPER(TRIM(nombre)) AS nombre
FROM usuarios;
```

### 2. Documenta lógica compleja

```sql
-- ✅ Con comentarios
SELECT 
    nombre,
    CASE 
        WHEN edad < 18 THEN 'Menor'      -- Menores de 18
        WHEN edad < 65 THEN 'Adulto'     -- 18-64 años
        ELSE 'Senior'                     -- 65+ años
    END AS categoria
FROM usuarios;
```

### 3. Considera el rendimiento

```sql
-- ⚠️ Funciones en WHERE pueden ser lentas
SELECT * FROM usuarios 
WHERE UPPER(nombre) = 'JUAN';

-- ✅ Mejor si es posible
SELECT * FROM usuarios 
WHERE nombre = 'Juan';
```

---

## 🎯 Ejercicios

1. Normaliza todos los nombres a mayúsculas y elimina espacios
2. Categoriza productos por precio (Económico, Medio, Alto, Premium)
3. Calcula la edad promedio por categoría de edad
4. Extrae el año y mes de todas las ventas
5. Crea una columna que muestre "Alto" si el stock es > 20, "Medio" si es 10-20, "Bajo" si es < 10

---

## 🚀 Siguiente paso

¡Felicidades! Has completado SQL básico. Continúa con **[SQL Intermedio](../sql-intermedio/)** para aprender conceptos más avanzados.
