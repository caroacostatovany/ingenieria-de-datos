# SELECT y filtrado básico

La base de SQL es la consulta `SELECT`. Con ella puedes leer datos de las tablas.

---

## 🔍 SELECT básico

### Seleccionar todas las columnas

```sql
SELECT * FROM usuarios;
```

**Nota**: `*` selecciona todas las columnas. Úsalo con cuidado en tablas grandes.

### Seleccionar columnas específicas

```sql
SELECT nombre, email, edad
FROM usuarios;
```

### Alias de columnas

```sql
SELECT 
    nombre AS nombre_completo,
    email AS correo_electronico,
    edad AS años
FROM usuarios;
```

O sin `AS`:

```sql
SELECT 
    nombre nombre_completo,
    email correo_electronico
FROM usuarios;
```

---

## 🔎 WHERE - Filtrar filas

`WHERE` te permite filtrar filas según condiciones.

### Comparaciones básicas

```sql
-- Igualdad
SELECT * FROM usuarios WHERE edad = 28;

-- Mayor que
SELECT * FROM productos WHERE precio > 100;

-- Menor o igual
SELECT * FROM ventas WHERE cantidad <= 5;

-- Diferente
SELECT * FROM usuarios WHERE ciudad != 'Madrid';
-- o
SELECT * FROM usuarios WHERE ciudad <> 'Madrid';
```

### Múltiples condiciones

```sql
-- AND (ambas condiciones deben cumplirse)
SELECT * FROM usuarios 
WHERE edad >= 25 AND ciudad = 'Madrid';

-- OR (al menos una condición debe cumplirse)
SELECT * FROM productos 
WHERE categoria = 'Electrónica' OR precio < 50;

-- Combinando AND y OR
SELECT * FROM ventas 
WHERE (cantidad > 10 OR precio_unitario > 100) 
  AND fecha_venta >= '2024-01-01';
```

### IN - Lista de valores

```sql
-- Usuarios de ciertas ciudades
SELECT * FROM usuarios 
WHERE ciudad IN ('Madrid', 'Barcelona', 'Valencia');

-- Equivale a:
SELECT * FROM usuarios 
WHERE ciudad = 'Madrid' 
   OR ciudad = 'Barcelona' 
   OR ciudad = 'Valencia';
```

### LIKE - Búsqueda de patrones

```sql
-- Nombres que empiezan con "Juan"
SELECT * FROM usuarios WHERE nombre LIKE 'Juan%';

-- Emails que contienen "example"
SELECT * FROM usuarios WHERE email LIKE '%example%';

-- Nombres que terminan con "ez"
SELECT * FROM usuarios WHERE nombre LIKE '%ez';
```

**Patrones:**
* `%` - Cualquier secuencia de caracteres (incluyendo ninguno)
* `_` - Un solo carácter

### BETWEEN - Rangos

```sql
-- Usuarios entre 25 y 35 años
SELECT * FROM usuarios 
WHERE edad BETWEEN 25 AND 35;

-- Equivale a:
SELECT * FROM usuarios 
WHERE edad >= 25 AND edad <= 35;
```

### NULL - Valores nulos

```sql
-- Usuarios sin ciudad
SELECT * FROM usuarios WHERE ciudad IS NULL;

-- Usuarios con ciudad definida
SELECT * FROM usuarios WHERE ciudad IS NOT NULL;
```

**⚠️ Importante**: No uses `= NULL` o `!= NULL`. Siempre usa `IS NULL` o `IS NOT NULL`.

---

## 📝 DISTINCT - Valores únicos

```sql
-- Ciudades únicas
SELECT DISTINCT ciudad FROM usuarios;

-- Combinaciones únicas
SELECT DISTINCT categoria, precio 
FROM productos;
```

---

## 💡 Buenas prácticas

### 1. Evita SELECT *

En producción, especifica las columnas que necesitas:

```sql
-- ❌ Evita
SELECT * FROM usuarios;

-- ✅ Mejor
SELECT id, nombre, email FROM usuarios;
```

### 2. Usa alias descriptivos

```sql
-- ✅ Claro
SELECT 
    nombre AS nombre_completo,
    fecha_registro AS fecha_de_alta
FROM usuarios;
```

### 3. Filtra temprano

Aplica filtros `WHERE` antes de procesar muchos datos:

```sql
-- ✅ Filtra primero
SELECT nombre, email 
FROM usuarios 
WHERE ciudad = 'Madrid' 
  AND edad > 25;
```

---

## 🎯 Ejercicios

Usa la base de datos de ejemplo para practicar:

1. Selecciona todos los usuarios de Madrid
2. Encuentra productos con precio mayor a 100
3. Lista usuarios con email que contenga "example"
4. Obtén ventas del último mes
5. Encuentra usuarios sin ciudad definida

---

## 🚀 Siguiente paso

Continúa con **[JOINs básicos](02-joins-basicos.md)** para combinar datos de múltiples tablas.
