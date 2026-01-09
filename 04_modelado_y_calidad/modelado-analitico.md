# Modelado Analítico

El modelado analítico organiza datos para facilitar análisis y reportes. Aprende a diseñar modelos efectivos.

---

## 🧠 ¿Qué es el modelado analítico?

El modelado analítico organiza datos de forma que sean:
* **Fáciles de consultar** para análisis
* **Rápidos** para reportes
* **Intuitivos** para usuarios de negocio
* **Optimizados** para analytics

> El modelado analítico es diferente del modelado transaccional (OLTP). Está optimizado para lectura, no escritura.

---

## 📊 Modelos dimensionales

### Star Schema (Esquema estrella)

El modelo más común para data warehouses.

**Estructura:**
* **Tabla de hechos (Fact)**: Eventos/transacciones (centro)
* **Tablas de dimensiones (Dimensions)**: Contexto descriptivo (alrededor)

```
        Dimension: Tiempo
              |
              |
    Dimension: Producto --- Fact: Ventas --- Dimension: Cliente
              |
              |
        Dimension: Tienda
```

**Ejemplo:**

```sql
-- Tabla de hechos
CREATE TABLE fact_ventas (
    venta_id SERIAL PRIMARY KEY,
    fecha_id INTEGER,
    producto_id INTEGER,
    cliente_id INTEGER,
    tienda_id INTEGER,
    cantidad INTEGER,
    precio_unitario DECIMAL(10,2),
    total DECIMAL(10,2)
);

-- Dimensión: Tiempo
CREATE TABLE dim_tiempo (
    fecha_id SERIAL PRIMARY KEY,
    fecha DATE,
    año INTEGER,
    trimestre INTEGER,
    mes INTEGER,
    dia INTEGER,
    dia_semana VARCHAR(20),
    es_fin_de_semana BOOLEAN
);

-- Dimensión: Producto
CREATE TABLE dim_producto (
    producto_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    categoria VARCHAR(50),
    subcategoria VARCHAR(50),
    precio_base DECIMAL(10,2)
);

-- Dimensión: Cliente
CREATE TABLE dim_cliente (
    cliente_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    ciudad VARCHAR(50),
    pais VARCHAR(50),
    segmento VARCHAR(50)
);
```

**Ventajas:**
* ✅ Simple de entender
* ✅ Consultas rápidas (menos JOINs)
* ✅ Fácil para usuarios de negocio

### Snowflake Schema (Esquema copo de nieve)

Similar a Star Schema, pero las dimensiones están normalizadas.

```
        Dimension: Tiempo
              |
              |
    Dimension: Producto --- Fact: Ventas --- Dimension: Cliente
         |                                        |
         |                                        |
    Subcategoria                            Ciudad
         |                                        |
    Categoria                              Pais
```

**Ventajas:**
* ✅ Menos redundancia
* ✅ Ahorra espacio

**Desventajas:**
* ⚠️ Más JOINs (más lento)
* ⚠️ Más complejo

**Cuándo usar:**
* Dimensiones muy grandes
* Necesitas ahorrar espacio
* Dimensiones cambian frecuentemente

---

## 📈 Tablas de hechos

### Tipos de tablas de hechos

#### 1. Transaccional

Una fila por transacción.

```sql
CREATE TABLE fact_ventas (
    venta_id INTEGER,
    fecha_id INTEGER,
    producto_id INTEGER,
    cantidad INTEGER,
    total DECIMAL(10,2)
);
```

#### 2. Snapshot (Instantánea)

Estado en un momento específico.

```sql
CREATE TABLE fact_inventario_diario (
    fecha_id INTEGER,
    producto_id INTEGER,
    cantidad_en_stock INTEGER,
    valor_inventario DECIMAL(10,2)
);
```

#### 3. Accumulating Snapshot

Sigue el progreso de un proceso.

```sql
CREATE TABLE fact_ordenes (
    orden_id INTEGER,
    fecha_creacion_id INTEGER,
    fecha_envio_id INTEGER,
    fecha_entrega_id INTEGER,
    estado VARCHAR(50)
);
```

### Granularidad

La granularidad define qué representa cada fila.

**Ejemplos:**
* Una venta por fila
* Un día por producto por fila
* Una hora por sensor por fila

**Regla:** Define la granularidad más baja que necesitas.

---

## 🎯 Dimensiones

### Tipos de dimensiones

#### 1. Dimensiones lentamente cambiantes (SCD)

**Tipo 1: Sobrescribir**
```sql
-- Actualiza el valor directamente
UPDATE dim_cliente 
SET ciudad = 'Nueva Ciudad' 
WHERE cliente_id = 123;
```

**Tipo 2: Histórico**
```sql
-- Mantiene historial con fechas
CREATE TABLE dim_cliente (
    cliente_id INTEGER,
    nombre VARCHAR(100),
    ciudad VARCHAR(50),
    fecha_inicio DATE,
    fecha_fin DATE,
    es_actual BOOLEAN
);
```

**Tipo 3: Columna adicional**
```sql
-- Guarda valor anterior en columna separada
CREATE TABLE dim_cliente (
    cliente_id INTEGER,
    nombre VARCHAR(100),
    ciudad_actual VARCHAR(50),
    ciudad_anterior VARCHAR(50)
);
```

#### 2. Dimensiones degeneradas

Dimensiones que están en la tabla de hechos.

```sql
-- Número de orden podría ser dimensión degenerada
CREATE TABLE fact_ventas (
    venta_id INTEGER,
    numero_orden VARCHAR(50),  -- Dimensión degenerada
    fecha_id INTEGER,
    producto_id INTEGER
);
```

#### 3. Dimensiones conformadas

Dimensiones compartidas entre múltiples data marts.

```sql
-- dim_tiempo es conformada si se usa en múltiples marts
```

---

## 💡 Buenas prácticas

### 1. Diseña para consultas, no para normalización

```sql
-- ✅ Bueno para analytics (desnormalizado)
CREATE TABLE dim_producto (
    producto_id INTEGER,
    nombre VARCHAR(100),
    categoria VARCHAR(50),      -- Desnormalizado
    categoria_padre VARCHAR(50) -- Desnormalizado
);

-- ⚠️ Normalizado (más JOINs, más lento)
CREATE TABLE dim_producto (
    producto_id INTEGER,
    nombre VARCHAR(100),
    categoria_id INTEGER  -- Requiere JOIN
);
```

### 2. Usa claves sustitutas (surrogate keys)

```sql
-- ✅ Clave sustituta (independiente del sistema fuente)
CREATE TABLE dim_cliente (
    cliente_id SERIAL PRIMARY KEY,  -- Clave sustituta
    cliente_sk VARCHAR(50),          -- Clave del sistema fuente
    nombre VARCHAR(100)
);
```

### 3. Pre-agrega cuando sea apropiado

```sql
-- Tabla agregada para consultas comunes
CREATE TABLE fact_ventas_diarias (
    fecha_id INTEGER,
    producto_id INTEGER,
    total_ventas INTEGER,
    ingresos_totales DECIMAL(10,2)
);
```

### 4. Particiona tablas de hechos grandes

```sql
-- Particionar por fecha
CREATE TABLE fact_ventas (
    ...
) PARTITION BY RANGE (fecha_id);
```

---

## 🎯 Ejercicios

1. Diseña un Star Schema para un sistema de e-commerce
2. Crea dimensiones con SCD Tipo 2
3. Identifica la granularidad apropiada para diferentes casos
4. Diseña un modelo para análisis de ventas por región y tiempo

---

## 🚀 Próximo paso

Continúa con **[Calidad de datos](calidad-de-datos.md)**.

---

> **Recuerda**: El modelado analítico es un arte. Empieza simple (Star Schema) y evoluciona según necesidades.
