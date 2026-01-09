# Modelado Relacional

El modelado relacional es la base para diseñar bases de datos eficientes y mantenibles.

---

## 🧠 Conceptos fundamentales

### Tablas y relaciones

Una base de datos relacional organiza datos en **tablas** relacionadas entre sí.

**Componentes:**
* **Tabla**: Colección de filas y columnas
* **Fila (registro)**: Una instancia de datos
* **Columna (campo)**: Un atributo del dato
* **Clave primaria (PK)**: Identificador único
* **Clave foránea (FK)**: Referencia a otra tabla

---

## 🔑 Claves

### Clave primaria (Primary Key)

Identifica de forma única cada fila.

```sql
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,  -- Clave primaria
    nombre VARCHAR(100),
    email VARCHAR(100) UNIQUE
);
```

### Clave foránea (Foreign Key)

Establece relación con otra tabla.

```sql
CREATE TABLE ventas (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER REFERENCES usuarios(id),  -- Clave foránea
    producto_id INTEGER REFERENCES productos(id),
    fecha_venta DATE,
    total DECIMAL(10,2)
);
```

---

## 📊 Normalización

La normalización reduce redundancia y mejora la integridad de datos.

### Primera forma normal (1NF)

* Cada columna contiene un solo valor
* No hay grupos repetitivos
* Cada fila es única

```sql
-- ❌ No normalizado
CREATE TABLE ventas (
    id INT,
    productos VARCHAR(200)  -- "Laptop, Mouse, Teclado"
);

-- ✅ Normalizado
CREATE TABLE ventas (
    id INT PRIMARY KEY,
    fecha_venta DATE
);

CREATE TABLE ventas_items (
    venta_id INT REFERENCES ventas(id),
    producto_id INT REFERENCES productos(id),
    cantidad INT
);
```

### Segunda forma normal (2NF)

* Cumple 1NF
* Todos los atributos no clave dependen completamente de la clave primaria

### Tercera forma normal (3NF)

* Cumple 2NF
* No hay dependencias transitivas (atributos que dependen de otros atributos no clave)

---

## 🏗️ Diseño de esquemas

### Relaciones uno a muchos (1:N)

```sql
-- Un usuario tiene muchas ventas
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100)
);

CREATE TABLE ventas (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER REFERENCES usuarios(id)  -- Muchas ventas, un usuario
);
```

### Relaciones muchos a muchos (N:M)

```sql
-- Muchos productos en muchas ventas
CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100)
);

CREATE TABLE ventas (
    id SERIAL PRIMARY KEY,
    fecha_venta DATE
);

-- Tabla intermedia
CREATE TABLE ventas_productos (
    venta_id INTEGER REFERENCES ventas(id),
    producto_id INTEGER REFERENCES productos(id),
    cantidad INTEGER,
    PRIMARY KEY (venta_id, producto_id)
);
```

---

## 📈 Data Warehouses

### Modelo Star Schema

**Estructura:**
* **Tabla de hechos (Fact)**: Eventos/transacciones
* **Tablas de dimensiones (Dimensions)**: Contexto descriptivo

```sql
-- Tabla de hechos
CREATE TABLE fact_ventas (
    id SERIAL PRIMARY KEY,
    fecha_id INTEGER,
    usuario_id INTEGER,
    producto_id INTEGER,
    cantidad INTEGER,
    total DECIMAL(10,2)
);

-- Dimensión de tiempo
CREATE TABLE dim_fecha (
    fecha_id SERIAL PRIMARY KEY,
    fecha DATE,
    año INTEGER,
    mes INTEGER,
    dia INTEGER,
    dia_semana VARCHAR(20)
);

-- Dimensión de producto
CREATE TABLE dim_producto (
    producto_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    categoria VARCHAR(50),
    precio DECIMAL(10,2)
);
```

### Ventajas del Star Schema

* Consultas más rápidas (menos JOINs)
* Fácil de entender
* Optimizado para analytics

---

## 💡 Buenas prácticas

### 1. Usa nombres descriptivos

```sql
-- ✅ Claro
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre_completo VARCHAR(100),
    correo_electronico VARCHAR(100)
);

-- ⚠️ Confuso
CREATE TABLE usr (
    id SERIAL PRIMARY KEY,
    nm VARCHAR(100),
    eml VARCHAR(100)
);
```

### 2. Define tipos de datos apropiados

```sql
-- ✅ Específico
CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    precio DECIMAL(10,2),  -- Para dinero
    stock INTEGER,
    activo BOOLEAN
);
```

### 3. Agrega constraints

```sql
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    edad INTEGER CHECK (edad >= 0),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🎯 Ejercicios

1. Diseña un esquema para un sistema de e-commerce
2. Normaliza una tabla con datos redundantes
3. Crea un star schema para análisis de ventas
4. Diseña relaciones entre usuarios, productos y pedidos

---

## 🚀 Próximo paso

Practica con los **[Ejercicios](../ejercicios/)** del repositorio.
