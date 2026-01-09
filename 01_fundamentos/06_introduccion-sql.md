# Introducción a SQL para Data Engineers

SQL (Structured Query Language) es el **lenguaje fundamental** para trabajar con datos estructurados. Como Data Engineer, SQL será una de tus herramientas más importantes.

---

## 🧠 ¿Por qué SQL es esencial en Data Engineering?

En Data Engineering, SQL se usa para:

* **Extraer datos** de bases de datos y data warehouses
* **Transformar datos** antes de cargarlos
* **Validar datos** y verificar calidad
* **Consultar datos** para análisis y reportes
* **Crear vistas** y modelos analíticos

> SQL es el lenguaje universal de los datos.

---

## 🔁 SQL Transaccional vs SQL Analítico

Como Data Engineer, trabajarás principalmente con **SQL Analítico**, que es diferente del SQL transaccional:

### SQL Transaccional (OLTP)
* Usado en aplicaciones (INSERT, UPDATE, DELETE frecuentes)
* Optimizado para transacciones rápidas
* Datos normalizados
* Ejemplo: Sistema de ventas en tiempo real

### SQL Analítico (OLAP)
* Usado en data warehouses y analytics
* Optimizado para consultas complejas sobre grandes volúmenes
* Datos desnormalizados (star schema, etc.)
* Ejemplo: Reportes y dashboards

**Como Data Engineer, trabajarás principalmente con SQL Analítico.**

---

## 📊 Conceptos fundamentales de SQL

### 1️⃣ SELECT - Consultar datos

La base de todo: leer datos de una tabla.

```sql
SELECT columna1, columna2
FROM tabla
WHERE condicion;
```

### 2️⃣ JOIN - Combinar tablas

Conectar datos de múltiples tablas relacionadas.

```sql
SELECT *
FROM tabla1
JOIN tabla2 ON tabla1.id = tabla2.id;
```

### 3️⃣ Agregaciones - Resumir datos

Calcular totales, promedios, conteos.

```sql
SELECT categoria, SUM(ventas) as total_ventas
FROM ventas
GROUP BY categoria;
```

### 4️⃣ Transformaciones - Modificar datos

Cambiar formato, calcular campos nuevos, limpiar.

```sql
SELECT 
    UPPER(nombre) as nombre_mayusculas,
    precio * 1.16 as precio_con_iva
FROM productos;
```

---

## 🎯 SQL en el flujo de datos

SQL aparece en diferentes etapas del pipeline:

### Extracción (Extract)
```sql
-- Leer datos de una fuente
SELECT * FROM fuente_datos
WHERE fecha >= '2024-01-01';
```

### Transformación (Transform)
```sql
-- Limpiar y transformar
SELECT 
    id,
    UPPER(TRIM(nombre)) as nombre_limpio,
    CASE 
        WHEN edad < 18 THEN 'Menor'
        ELSE 'Adulto'
    END as categoria_edad
FROM usuarios
WHERE nombre IS NOT NULL;
```

### Carga (Load)
```sql
-- Insertar datos transformados
INSERT INTO tabla_destino
SELECT * FROM datos_transformados;
```

---

## 🔧 Herramientas SQL comunes en Data Engineering

* **PostgreSQL**: Base de datos relacional open source (la que usamos en este repositorio)
* **MySQL**: Popular para aplicaciones web
* **BigQuery**: Data warehouse de Google Cloud
* **Snowflake**: Data warehouse en la nube
* **Redshift**: Data warehouse de AWS
* **SQL Server**: Microsoft SQL Server

**No importa cuál uses, el SQL básico es muy similar entre todas.**

> 💡 **Nota**: En este repositorio usamos **PostgreSQL** porque es excelente para aprender SQL estándar y muy usado en la industria. Lee más sobre [SQL vs PostgreSQL](../02_sql/sql-vs-postgresql.md) para entender las diferencias.

---

## 💡 SQL vs Python vs otras herramientas

### ¿Cuándo usar SQL?

✅ **Usa SQL cuando:**
* Los datos ya están en una base de datos
* Necesitas hacer transformaciones que SQL maneja bien
* El volumen de datos es grande (SQL está optimizado)
* Necesitas que otros puedan leer/entender fácilmente

### ¿Cuándo usar Python?

✅ **Usa Python cuando:**
* Necesitas lógica compleja o condicional
* Trabajas con APIs o archivos
* Necesitas librerías especializadas
* La transformación es muy compleja para SQL

**En la práctica, combinarás SQL y Python según el caso.**

---

## 🚀 Próximos pasos

Una vez que entiendas estos conceptos básicos:

1. **Aprende SQL básico** en **[02_sql/sql-basico/](../02_sql/sql-basico/)**
2. **Practica con ejercicios** en **[02_sql/ejercicios/](../02_sql/ejercicios/)**
3. **Avanza a SQL intermedio** en **[02_sql/sql-intermedio/](../02_sql/sql-intermedio/)**

---

## 📝 Notas importantes

* **SQL no es case-sensitive** para palabras clave (SELECT = select = Select)
* **SQL es declarativo**: describes QUÉ quieres, no CÓMO hacerlo
* **La práctica es clave**: escribe queries, no solo las leas
* **Cada base de datos tiene variaciones**: aprende los conceptos, luego las diferencias específicas

---

## 🎓 Recursos adicionales

* Practica con datos reales cuando sea posible
* Lee queries de otros Data Engineers
* Experimenta con diferentes bases de datos
* No tengas miedo de hacer queries "malas" primero, luego las optimizas

---

> **Recuerda**: SQL es una herramienta, no un fin. El objetivo es obtener datos útiles y confiables, no escribir queries perfectas desde el inicio.
