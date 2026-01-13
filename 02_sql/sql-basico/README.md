# SQL Básico

Esta sección cubre los fundamentos de SQL que todo Data Engineer debe dominar.

> **Nota**: Los ejemplos usan **PostgreSQL**, pero el SQL básico es estándar y funciona en otros sistemas. Lee [SQL vs PostgreSQL](../sql-vs-postgresql.md) para más detalles.

---

## 🚀 Empezar a practicar

Antes de comenzar, necesitas un editor SQL para ejecutar las queries. Aquí tienes dos opciones:

### Opción 1: DBeaver (Recomendado)

**DBeaver** es un cliente SQL visual y gratuito. Es la opción más recomendada para practicar.

#### Paso 1: Abrir SQL Editor

1. **Abre DBeaver** y conéctate a tu base de datos (si aún no lo has hecho, sigue las instrucciones en [README-DOCKER.md](../README-DOCKER.md))
2. **Click derecho** en la conexión `data_engineering` → **SQL Editor → New SQL Script**
   - O usa el atajo: **Alt+Shift+N** (Windows/Linux) / **Cmd+Shift+N** (macOS)
   - O desde el menú: **File → New → SQL Script**

#### Paso 2: Escribir y ejecutar queries

```sql
-- Escribe tu query aquí
SELECT * FROM usuarios LIMIT 5;
```

**Para ejecutar:**
- **F5**: Ejecuta toda la query
- **Ctrl+Enter** (Windows/Linux) / **Cmd+Enter** (macOS): Ejecuta la query seleccionada
- **Alt+X**: Ejecuta la query actual

**Resultados:**
- Los resultados aparecen en la pestaña **"Data"** debajo del editor
- Puedes ver múltiples resultados si ejecutas varias queries

#### Características útiles

* ✅ **Autocompletado**: Escribe `SEL` y presiona **Ctrl+Space** para sugerencias
* ✅ **Syntax highlighting**: Colores para keywords, strings, números
* ✅ **Formateo**: **Ctrl+Shift+F** para formatear automáticamente
* ✅ **Múltiples pestañas**: Puedes tener varios scripts abiertos

> 💡 **Guía completa**: Lee [DBeaver: Cliente Universal de Bases de Datos](../herramientas/dbeaver-cliente-sql.md) para más detalles.

---

### Opción 2: Cursor (Editor de código)

Si usas **Cursor**, puedes ejecutar SQL directamente desde el editor.

#### Paso 1: Instalar extensión SQL

1. **Abre Cursor**
2. **Ve a Extensions** (Cmd+Shift+X / Ctrl+Shift+X)
3. **Busca "SQLTools"** o **"PostgreSQL"**
4. **Instala** la extensión

**Extensiones recomendadas:**
* **SQLTools** - Soporte multi-base de datos
* **SQLTools PostgreSQL** - Driver específico para PostgreSQL

#### Paso 2: Conectar a la base de datos usando Connection String

**Opción A: Usar Connection String directo (Recomendado - Más simple)**

1. **Abre Command Palette** (Cmd+Shift+P / Ctrl+Shift+P)
2. **Escribe "SQLTools: Add New Connection"**
3. **En la configuración:**
   - **Connection name**: `PostgreSQL Local`
   - **Connect using**: Selecciona **"Connection String"**
   - **Connection String**: Escribe directamente:
     ```
     postgresql://de_user:de_password@localhost:15432/data_engineering
     ```
     > ⚠️ **Importante**: 
     > - Reemplaza `de_password` con tu contraseña real si es diferente
     > - Si cambiaste el puerto en tu `.env` (ej: 5433, 5434), usa ese puerto en lugar de 15432

4. **Click en "Test Connection"** para verificar que funciona
5. **Click en "Save Connection"** para guardar la conexión

**Opción A2: Usar Connection String desde .env (Requiere extensión dotenv)**

Si prefieres usar la variable del `.env`, necesitas instalar la extensión **"dotenv"** para VS Code/Cursor:

1. **Instala la extensión "dotenv"**:
   - Abre Extensions (Cmd+Shift+X / Ctrl+Shift+X)
   - Busca "dotenv" e instala la extensión

2. **Asegúrate de tener `DATABASE_URL` en tu `.env`** (en la raíz del proyecto):
   ```bash
   DATABASE_URL=postgresql://de_user:de_password@localhost:15432/data_engineering
   ```
   > ⚠️ **Nota**: Si cambiaste el puerto en tu `.env`, usa ese puerto en la URL

3. **En SQLTools, usa**: `${env:DATABASE_URL}` en el campo Connection String

> 💡 **Nota**: La extensión dotenv carga automáticamente las variables del `.env` al iniciar VS Code/Cursor. Si no funciona, reinicia el editor.

**Opción B: Usar campos individuales (alternativa)**

Si prefieres no usar connection string, puedes usar campos individuales:
```
Connection name: PostgreSQL Local
Connect using: Server and Port
Server: localhost
Port: 15432    ⚠️ Si cambiaste el puerto en .env, usa ese puerto
Database: data_engineering    ⚠️ IMPORTANTE: No uses "de_user" aquí
Username: de_user             ⚠️ Este es el USUARIO, no la base de datos
Password: de_password
```

#### Paso 3: Conectar a la base de datos

Después de guardar la conexión, necesitas conectarte:

1. **Abre el panel de SQLTools**:
   - Abre Command Palette: `Cmd+Shift+P` / `Ctrl+Shift+P`
   - Escribe: `View: Show SQLTools`
   - O busca el ícono de SQLTools en la barra lateral izquierda

2. **Conecta a tu base de datos**:
   - En el panel de SQLTools, verás tu conexión "PostgreSQL Local"
   - **Click derecho** en "PostgreSQL Local" → **"Connect"**
   - O click en el ícono de conexión (⚡) junto al nombre
   - Cuando esté conectado, verás un check verde ✅

3. **Explora las tablas**:
   - Expande "PostgreSQL Local" → "data_engineering" → "public" → "Tables"
   - Verás las tablas: `usuarios`, `productos`, `ventas`
   - Puedes expandir cada tabla para ver sus columnas

#### Paso 4: Ver datos de las tablas

**Opción 1: Desde el panel de SQLTools**

1. **Expande una tabla** (ej: `usuarios`)
2. **Click derecho** en la tabla → **"Show Table Records"** o **"Select Top 1000 Rows"**
3. Los datos aparecerán en una nueva pestaña

**Opción 2: Crear y ejecutar queries SQL**

1. **Crea un archivo** `.sql` (ej: `practica.sql` o `test.sql`)
2. **Escribe tu query:**
   ```sql
   -- Ver usuarios
   SELECT * FROM usuarios LIMIT 5;
   
   -- Ver productos
   SELECT * FROM productos;
   
   -- Ver ventas
   SELECT * FROM ventas LIMIT 10;
   ```
3. **Ejecuta la query**:
   - **Selecciona la query** (o deja el cursor en ella)
   - **Click derecho** → **"Run Query"** o **"SQLTools: Run Selected Query"**
   - O desde Command Palette: `Cmd+Shift+P` → escribe "SQLTools: Run Selected Query"

**Resultados:**
- Los resultados aparecen en un panel debajo del editor o en una nueva pestaña
- Puedes ver múltiples resultados si ejecutas varias queries en el mismo archivo
- Puedes exportar los resultados a CSV, JSON, etc. desde el panel de resultados

#### Paso 5: Prueba estas queries básicas

Una vez conectado, prueba estas queries para familiarizarte:

```sql
-- 1. Ver todas las tablas disponibles
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public';

-- 2. Ver estructura de una tabla
SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'usuarios';

-- 3. Ver datos de usuarios
SELECT * FROM usuarios;

-- 4. Contar registros
SELECT COUNT(*) AS total_usuarios FROM usuarios;
SELECT COUNT(*) AS total_productos FROM productos;
SELECT COUNT(*) AS total_ventas FROM ventas;
```

#### Ventajas de usar Cursor

* ✅ **Todo en un editor**: Código Python y SQL en el mismo lugar
* ✅ **AI integrado**: Puedes pedir ayuda a Cursor sobre SQL
* ✅ **Versionado**: Tus queries SQL están en Git junto con tu código
* ✅ **Autocompletado con AI**: Cursor puede sugerir queries basadas en contexto

> 💡 **Tip con Cursor**: Puedes pedir ayuda a la AI como: `@02_sql/sql-basico/01-select-y-where.md explica esta query y ayúdame a mejorarla` para obtener ayuda contextual.

---

## 📖 Contenido

* **[SELECT y filtrado básico](01-select-y-where.md)**
* **[JOINs básicos](02-joins-basicos.md)**
* **[Agregaciones](03-agregaciones.md)**
* **[Ordenamiento y límites](04-ordenamiento-y-limites.md)**
* **[Funciones comunes](05-funciones-comunes.md)**

---

## 🎯 Objetivo

Al finalizar esta sección, deberías poder:

* Consultar datos de una o más tablas
* Filtrar y ordenar resultados
* Agrupar y agregar datos
* Usar funciones básicas de SQL

---

## 🚀 Próximo paso

Una vez dominado SQL básico, continúa con **[SQL Intermedio](../sql-intermedio/)**.
