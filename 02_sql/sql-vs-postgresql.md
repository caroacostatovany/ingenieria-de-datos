# SQL vs PostgreSQL: ¿Cuál es la diferencia?

Como Data Engineer, es importante entender la diferencia entre **SQL** (el lenguaje) y **PostgreSQL** (el sistema de gestión de bases de datos).

---

## 🧠 SQL: El lenguaje

**SQL (Structured Query Language)** es un **lenguaje estándar** para trabajar con bases de datos relacionales.

### Características:

* **Estándar**: Definido por ANSI/ISO
* **Universal**: Funciona en múltiples sistemas (PostgreSQL, MySQL, SQL Server, etc.)
* **Declarativo**: Describes QUÉ quieres, no CÓMO hacerlo

### Ejemplo de SQL estándar:

```sql
SELECT nombre, email 
FROM usuarios 
WHERE ciudad = 'Madrid';
```

Esta query funciona en **cualquier** base de datos SQL estándar.

---

## 🐘 PostgreSQL: El sistema

**PostgreSQL** (también llamado "Postgres") es un **sistema de gestión de bases de datos relacionales (RDBMS)** que implementa SQL.

### Características:

* **Open source**: Gratis y de código abierto
* **Robusto**: Muy confiable y estable
* **Estándar SQL**: Sigue muy de cerca los estándares SQL
* **Extensible**: Permite funciones personalizadas
* **Avanzado**: Soporta características avanzadas (JSON, arrays, etc.)

### psql: El cliente

**psql** es el cliente de línea de comandos para interactuar con PostgreSQL.

```bash
# Conectarse a PostgreSQL
psql -h localhost -U usuario -d base_de_datos
```

---

## 🤔 ¿Por qué PostgreSQL para Data Engineering?

### 1. Estándar SQL robusto

PostgreSQL implementa SQL estándar muy bien, lo que significa:

* ✅ Lo que aprendes aquí funciona en otros sistemas
* ✅ Fácil migrar queries a otros sistemas
* ✅ Buenas prácticas aplicables universalmente

### 2. Características avanzadas

PostgreSQL tiene características útiles para Data Engineering:

* **Window Functions**: Excelente soporte
* **CTEs**: Muy bien implementadas
* **JSON**: Soporte nativo para datos semi-estructurados
* **Arrays**: Manejo de arrays nativo
* **Particionamiento**: Particionamiento de tablas avanzado

### 3. Popular en la industria

PostgreSQL es ampliamente usado en:

* Startups y empresas tecnológicas
* Data Warehouses (como base para sistemas más grandes)
* Aplicaciones web modernas
* Sistemas de analytics

### 4. Open source y gratuito

* No necesitas licencias costosas
* Comunidad activa y soporte
* Documentación excelente

### 5. Excelente para aprender

* Sintaxis clara y estándar
* Mensajes de error útiles
* Herramientas de desarrollo buenas

---

## 🔄 SQL estándar vs extensiones PostgreSQL

### SQL estándar (funciona en todos lados)

```sql
-- Esto funciona en PostgreSQL, MySQL, SQL Server, etc.
SELECT nombre, email 
FROM usuarios 
WHERE ciudad = 'Madrid';
```

### Extensiones PostgreSQL (solo en PostgreSQL)

```sql
-- DATE_TRUNC es específico de PostgreSQL
SELECT DATE_TRUNC('month', fecha_venta) AS mes
FROM ventas;

-- En MySQL sería:
SELECT DATE_FORMAT(fecha_venta, '%Y-%m-01') AS mes
FROM ventas;

-- En SQL Server sería:
SELECT DATETRUNC(month, fecha_venta) AS mes
FROM ventas;
```

---

## 📊 Comparación rápida

| Característica | SQL (estándar) | PostgreSQL |
|----------------|----------------|------------|
| **Tipo** | Lenguaje | Sistema de base de datos |
| **Portabilidad** | Universal | Específico de PostgreSQL |
| **Sintaxis básica** | Igual en todos | Igual en todos |
| **Funciones avanzadas** | Limitadas | Muy extensas |
| **Window Functions** | Estándar | Excelente soporte |
| **JSON** | Limitado | Soporte nativo |
| **Particionamiento** | Básico | Avanzado |

---

## 🎯 En este repositorio

### ¿Qué usamos?

**PostgreSQL** como sistema de base de datos, pero enseñamos **SQL estándar** siempre que sea posible.

### ¿Por qué?

1. **Aprendes SQL real**: Lo que aprendes funciona en otros sistemas
2. **PostgreSQL es excelente**: Características avanzadas cuando las necesites
3. **Práctica real**: PostgreSQL es usado en la industria

### Notas sobre portabilidad

Cuando usamos funciones específicas de PostgreSQL (como `DATE_TRUNC`), lo indicamos y proporcionamos alternativas para otros sistemas cuando es relevante.

---

## 🐳 Docker y PostgreSQL

En este repositorio, el Docker Compose levanta **PostgreSQL 15**:

```yaml
postgres:
  image: postgres:15-alpine
  # ...
```

**¿Por qué PostgreSQL en Docker?**

* ✅ Entorno consistente para todos
* ✅ Fácil de levantar y destruir
* ✅ No interfiere con instalaciones locales
* ✅ Misma versión para todos los estudiantes

---

## 💡 ¿Debo aprender solo PostgreSQL?

**No necesariamente**, pero es un excelente punto de partida:

### Ventajas de empezar con PostgreSQL:

* ✅ SQL estándar bien implementado
* ✅ Características avanzadas disponibles
* ✅ Popular en la industria
* ✅ Gratis y open source

### Después puedes aprender:

* **MySQL/MariaDB**: Muy popular en web
* **SQL Server**: Común en empresas Microsoft
* **BigQuery/Snowflake**: Data Warehouses en la nube
* **SQLite**: Para desarrollo local simple

**La buena noticia**: El SQL básico es muy similar entre todos. Las diferencias están en funciones avanzadas y características específicas.

---

## 🚀 Próximos pasos

1. **Aprende SQL estándar** con PostgreSQL
2. **Practica** con la base de datos Docker
3. **Aprende modelado relacional** en **[modelado-relacional.md](modelado-relacional.md)** - Diseño de esquemas y normalización
4. **Cuando necesites otro sistema**, adapta las funciones específicas
5. **El 90% del SQL** que aprendas funcionará en otros sistemas

---

## 📝 Resumen

* **SQL** = Lenguaje estándar (funciona en muchos sistemas)
* **PostgreSQL** = Sistema de base de datos que implementa SQL
* **psql** = Cliente para interactuar con PostgreSQL
* **Usamos PostgreSQL** porque es excelente para aprender y muy usado en la industria
* **Aprendes SQL estándar** que funciona en otros sistemas también

---

> **Recuerda**: SQL es el lenguaje universal. PostgreSQL es una excelente implementación para aprenderlo. Una vez que dominas SQL, adaptarte a otros sistemas es relativamente fácil.
