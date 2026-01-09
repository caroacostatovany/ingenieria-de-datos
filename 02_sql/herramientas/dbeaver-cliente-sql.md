# DBeaver: Cliente Universal de Bases de Datos

DBeaver es un cliente SQL universal, gratuito y open-source que funciona con múltiples bases de datos. Es especialmente útil para Data Engineers.

---

## 🧠 ¿Qué es DBeaver?

DBeaver es:
* **Universal**: Funciona con PostgreSQL, MySQL, SQL Server, Oracle, etc.
* **Gratuito**: Versión Community completamente gratuita
* **Visual**: Interfaz gráfica intuitiva
* **Potente**: Editor SQL avanzado con autocompletado
* **Open Source**: Código abierto y activamente mantenido

> DBeaver es como un "Swiss Army Knife" para bases de datos. Una herramienta que hace todo.

---

## 🚀 Instalación

### macOS

```bash
# Opción 1: Homebrew
brew install --cask dbeaver-community

# Opción 2: Descargar desde
# https://dbeaver.io/download/
```

### Windows

1. Descarga desde https://dbeaver.io/download/
2. Ejecuta el instalador
3. Sigue las instrucciones

### Linux

```bash
# Opción 1: Snap
sudo snap install dbeaver-ce

# Opción 2: Descargar desde
# https://dbeaver.io/download/
```

---

## 🔌 Conectar a PostgreSQL

### Paso 1: Crear nueva conexión

1. **File → New → Database Connection**
2. **Selecciona PostgreSQL**
3. **Click Next**

### Paso 2: Configurar conexión

```
Host: localhost
Port: 5432
Database: data_engineering
Username: de_user
Password: de_password
```

**Opciones útiles:**
* ✅ **Save password**: Para no escribirla cada vez
* ✅ **Show all databases**: Ver todas las bases de datos
* ✅ **Test Connection**: Verificar que funciona

### Paso 3: Conectar

Click **Finish** y DBeaver se conectará a tu base de datos.

---

## 📊 Visualizar datos

### Ver estructura de tablas

1. **Navega** en el panel izquierdo:
   ```
   Databases → data_engineering → Schemas → public → Tables
   ```
2. **Expande** una tabla para ver:
   * Columnas y tipos
   * Índices
   * Constraints
   * Datos (con click derecho → View Data)

### Ver datos de una tabla

**Opción 1: Click derecho**
1. Click derecho en la tabla
2. **View Data**
3. Se abre una pestaña con los datos

**Opción 2: SQL Editor**
```sql
SELECT * FROM usuarios LIMIT 100;
```
Ejecuta la query (F5 o botón Execute)

### Navegar datos

* **Scroll**: Navega por filas
* **Filtros**: Click en header de columna para filtrar
* **Ordenar**: Click en header para ordenar
* **Búsqueda**: Ctrl+F para buscar en datos

---

## ✏️ Editor SQL

### Características

**1. Autocompletado**
```sql
-- Escribe "SEL" y presiona Ctrl+Space
-- DBeaver sugiere: SELECT
```

**2. Syntax highlighting**
* Colores para keywords, strings, números
* Fácil de leer código

**3. Formateo automático**
* Ctrl+Shift+F: Formatea el código
* Organiza automáticamente

**4. Ejecutar queries**

**Opciones:**
* **F5**: Ejecuta query completa
* **Ctrl+Enter**: Ejecuta query seleccionada
* **Alt+X**: Ejecuta query actual

### Ejemplo de uso

```sql
-- 1. Escribe tu query
SELECT 
    u.nombre,
    COUNT(v.id) AS total_ventas,
    SUM(v.total) AS ingresos_totales
FROM usuarios u
LEFT JOIN ventas v ON u.id = v.usuario_id
GROUP BY u.id, u.nombre
ORDER BY ingresos_totales DESC
LIMIT 10;

-- 2. Ejecuta (F5)
-- 3. Ve resultados en pestaña "Data"
```

---

## 🎨 Generar queries visualmente

### Query Builder

DBeaver incluye un Query Builder visual:

1. **Click derecho en tabla → Generate SQL → SELECT**
2. **Se abre Query Builder**
3. **Selecciona tablas** a incluir
4. **Selecciona columnas** a mostrar
5. **Define JOINs** visualmente
6. **Agrega filtros** (WHERE)
7. **Agrega agrupaciones** (GROUP BY)
8. **Click "Generate SQL"** o "Execute"

**Ventajas:**
* ✅ No necesitas escribir SQL manualmente
* ✅ Visualiza relaciones entre tablas
* ✅ Genera SQL correcto
* ✅ Aprende SQL viendo queries generadas

### Ejemplo: Query Builder

**Pasos:**
1. Selecciona tabla `ventas`
2. Agrega JOIN con `usuarios`
3. Selecciona columnas: `nombre`, `total`
4. Agrega filtro: `fecha >= '2024-01-01'`
5. Agrega GROUP BY: `nombre`
6. Genera SQL:

```sql
SELECT 
    u.nombre,
    SUM(v.total) AS total_ventas
FROM ventas v
INNER JOIN usuarios u ON v.usuario_id = u.id
WHERE v.fecha >= '2024-01-01'
GROUP BY u.nombre
ORDER BY total_ventas DESC;
```

---

## 📈 Visualizar resultados

### Gráficos

DBeaver puede generar gráficos de resultados:

1. **Ejecuta una query** que retorne datos numéricos
2. **Click en pestaña "Chart"** (junto a "Data")
3. **Selecciona tipo de gráfico**:
   * Bar chart
   * Line chart
   * Pie chart
   * Scatter plot

**Ejemplo:**
```sql
SELECT 
    categoria,
    SUM(total) AS ingresos
FROM ventas v
JOIN productos p ON v.producto_id = p.id
GROUP BY categoria;
```

**Resultado:** Gráfico de barras con ingresos por categoría

---

## 💾 Exportar datos

### Exportar resultados

1. **Ejecuta query** y ve resultados
2. **Click derecho en resultados → Export Data**
3. **Selecciona formato**:
   * CSV
   * Excel
   * JSON
   * SQL (INSERT statements)
   * Parquet

4. **Configura opciones**:
   * Delimitador (para CSV)
   * Encoding
   * Headers

5. **Export**

### Exportar estructura

1. **Click derecho en tabla → Export Data**
2. **Selecciona "Structure"** (no datos)
3. **Exporta** a SQL script

---

## 🔍 Explorar base de datos

### Ver esquema completo

**Database Navigator:**
```
Databases
  └── data_engineering
      └── Schemas
          └── public
              ├── Tables
              │   ├── usuarios
              │   ├── productos
              │   └── ventas
              ├── Views
              ├── Functions
              └── Indexes
```

### Ver propiedades de tabla

1. **Click derecho en tabla → Properties**
2. **Ve información:**
   * Columnas y tipos
   * Índices
   * Constraints
   * Estadísticas
   * DDL (Data Definition Language)

### Ver datos relacionados

1. **Click derecho en tabla → View References**
2. **Ve tablas relacionadas** (foreign keys)

---

## 🛠️ Funciones avanzadas

### 1. ER Diagram (Diagrama Entidad-Relación)

1. **Click derecho en schema → View Diagram**
2. **Ve relaciones** entre tablas visualmente
3. **Útil para entender** estructura de base de datos

### 2. SQL Scripts

1. **File → New → SQL Script**
2. **Escribe múltiples queries**
3. **Ejecuta todas** o selecciona y ejecuta

### 3. Bookmarks

1. **Marca queries importantes** como bookmarks
2. **Acceso rápido** desde panel de bookmarks

### 4. History

1. **Ve historial** de queries ejecutadas
2. **Reutiliza queries** anteriores

---

## 💡 Tips y trucos

### 1. Atajos de teclado útiles

* **F5**: Ejecutar query
* **Ctrl+Enter**: Ejecutar query seleccionada
* **Ctrl+Shift+F**: Formatear código
* **Ctrl+Space**: Autocompletado
* **Ctrl+/**: Comentar/descomentar línea

### 2. Múltiples conexiones

Puedes tener múltiples conexiones abiertas:
* Una a base de datos de desarrollo
* Otra a producción (solo lectura)
* Otra a data warehouse

### 3. Comparar datos

1. **Ejecuta query en dos conexiones diferentes**
2. **Compara resultados** lado a lado

### 4. Buscar en esquema

1. **Ctrl+Shift+S**: Buscar en esquema
2. **Encuentra tablas/columnas** rápidamente

---

## 🎯 Casos de uso para Data Engineers

### 1. Explorar datos nuevos

```sql
-- Ver estructura
SELECT * FROM nueva_tabla LIMIT 10;

-- Ver estadísticas
SELECT 
    COUNT(*) AS total_filas,
    COUNT(DISTINCT columna) AS valores_unicos
FROM nueva_tabla;
```

### 2. Validar transformaciones

```sql
-- Antes de transformar
SELECT * FROM datos_raw WHERE fecha >= '2024-01-01';

-- Después de transformar
SELECT * FROM datos_procesados WHERE fecha >= '2024-01-01';

-- Compara resultados
```

### 3. Generar queries complejas

Usa Query Builder para:
* Generar JOINs complejos
* Crear agregaciones
* Construir queries paso a paso

### 4. Exportar para análisis

```sql
-- Query para análisis
SELECT 
    categoria,
    mes,
    SUM(total) AS ingresos
FROM ventas
GROUP BY categoria, mes;

-- Exporta a Excel para análisis en Python/R
```

---

## 🚀 Próximo paso

Revisa **[Otras Herramientas SQL](otras-herramientas-sql.md)** para comparar opciones.

---

> **Recuerda**: DBeaver es excelente para empezar. Es gratuito, potente y funciona con múltiples bases de datos. Úsalo para visualizar datos, generar queries y administrar bases de datos.
