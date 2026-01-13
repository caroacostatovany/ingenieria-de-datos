# 🐳 Base de Datos Local con Docker

Este directorio incluye una configuración de Docker para levantar una base de datos PostgreSQL local y practicar SQL.

---

## 🚀 Inicio rápido

### 1. Asegúrate de tener el archivo .env en la raíz del proyecto

El `docker-compose.yml` de este módulo **usa automáticamente el `.env` de la raíz del proyecto** (no necesitas crear uno en `02_sql/`).

```bash
# Si aún no tienes el .env en la raíz, cópialo desde la raíz del proyecto
# (desde la raíz, no desde 02_sql/)
cd ..  # Ir a la raíz del proyecto
cp .env.example .env
```

> 💡 **Importante**: El `.env` siempre debe estar en la **raíz del proyecto**, no en `02_sql/`. El `docker-compose.yml` está configurado para leerlo automáticamente desde la raíz.

### 2. (Opcional) Ajustar configuración

Si necesitas cambiar valores, edita el archivo `.env` en la **raíz del proyecto** (no en `02_sql/`):

* Nombre de la base de datos (`POSTGRES_DB` o `DB_NAME`)
* Usuario y contraseña (`POSTGRES_USER`, `POSTGRES_PASSWORD` o `DB_USER`, `DB_PASSWORD`)
* Puertos (`POSTGRES_PORT` o `DB_PORT`)
* **Connection String** (`DATABASE_URL`) - Para SQLTools y otras herramientas

> 💡 **Nota**: Este módulo usa las variables `POSTGRES_*` para Docker Compose, pero también puedes usar `DB_*` si prefieres consistencia con el resto del proyecto. El `DATABASE_URL` es útil para herramientas como SQLTools que pueden leer connection strings directamente. Lee más sobre archivos `.env` en [01_fundamentos/04_archivos-env-para-data-engineers.md](../01_fundamentos/04_archivos-env-para-data-engineers.md).

**Ejemplo de `DATABASE_URL` en tu `.env`:**
```bash
DATABASE_URL=postgresql://de_user:de_password@localhost:5432/data_engineering
```

### 3. Iniciar servicios

```bash
docker-compose up -d
```

Esto iniciará:
* **PostgreSQL** en el puerto configurado en `POSTGRES_PORT` (por defecto: 5432)
* **pgAdmin** (interfaz web) en el puerto configurado en `PGADMIN_PORT` (por defecto: 5050)

> ⚠️ **Si tienes otro PostgreSQL local**: Si el puerto 5432 ya está en uso, cambia `POSTGRES_PORT` en tu `.env` a otro puerto (ej: 5433). Ver [Troubleshooting](#-troubleshooting) para más detalles.

### 4. Verificar que está corriendo

```bash
docker-compose ps
```

Deberías ver ambos servicios como "Up" y "healthy".

---

## 🔌 Conectarse a la base de datos

### Opción 1: Desde la línea de comandos (psql)

```bash
# Conectarse usando docker exec
docker exec -it ing-datos-db psql -U de_user -d data_engineering

# O desde tu máquina (si tienes psql instalado)
psql -h localhost -p 5432 -U de_user -d data_engineering
```

### Opción 2: DBeaver (Recomendado - Cliente Desktop)

DBeaver es nuestra recomendación principal. Es más intuitivo y potente que pgAdmin.

#### Instalación de DBeaver

**macOS:**
```bash
brew install --cask dbeaver-community
```

**Windows/Linux:**
Descarga desde: https://dbeaver.io/download/

#### Configuración paso a paso

**Paso 1: Abrir DBeaver y crear nueva conexión**
1. Abre DBeaver
2. Ve a **File → New → Database Connection** (o presiona `Cmd+N` / `Ctrl+N`)
3. En la lista de bases de datos, busca y selecciona **PostgreSQL**
4. Click en **Next**

**Paso 2: Configurar los datos de conexión**

En la ventana de configuración, completa los siguientes campos:

```
Main (pestaña principal):
├── Host: localhost
├── Port: 5432
├── Database: data_engineering    ⚠️ IMPORTANTE: No uses "de_user" aquí
├── Username: de_user             ⚠️ Este es el USUARIO, no la base de datos
└── Password: de_password
```

> ⚠️ **Error común**: No confundas el **Username** (`de_user`) con el **Database** (`data_engineering`). Son diferentes:
> - **Database**: `data_engineering` (nombre de la base de datos)
> - **Username**: `de_user` (usuario para conectarse)
> - **Password**: `de_password` (contraseña del usuario)

**Opciones importantes:**
- ✅ **Save password**: Marca esta casilla para guardar la contraseña (no tendrás que escribirla cada vez)
- ✅ **Show all databases**: Opcional, si quieres ver todas las bases de datos disponibles

**Paso 3: Probar la conexión**

1. Click en el botón **Test Connection** (abajo a la izquierda)
2. Si es la primera vez, DBeaver te pedirá descargar el driver de PostgreSQL - click **Download**
3. Deberías ver un mensaje verde: **"Connected"** o **"Connection test successful"**

**Paso 4: Finalizar**

1. Si la prueba fue exitosa, click en **Finish**
2. La conexión aparecerá en el panel izquierdo bajo "Database Navigator"
3. Expande la conexión para ver la base de datos `data_engineering`

#### Verificar que funciona

1. **Expande la conexión** en el panel izquierdo:
   ```
   PostgreSQL - localhost
   └── Databases
       └── data_engineering
           └── Schemas
               └── public
                   └── Tables
   ```

2. **Ver datos de ejemplo:**
   - Expande **Tables** para ver las tablas disponibles
   - Click derecho en una tabla → **View Data**
   - Deberías ver los datos de ejemplo cargados desde `init-scripts/`

#### Guía completa

Para más detalles sobre cómo usar DBeaver (query builder, visualización, exportar datos, etc.), lee la **[guía completa de DBeaver](herramientas/dbeaver-cliente-sql.md)**.

### Opción 3: pgAdmin (interfaz web)

1. Abre tu navegador en: `http://localhost:5050`
2. Login con:
   - Email: `admin@example.com` (o el que configuraste en .env)
   - Password: `admin` (o el que configuraste en .env)
3. Agrega un nuevo servidor:
   - Host: `postgres` (nombre del servicio en docker-compose)
   - Port: `5432`
   - Database: `data_engineering` (o el que configuraste)
   - Username: `de_user` (o el que configuraste)
   - Password: `de_password` (o el que configuraste)

### Opción 4: Desde Python

```python
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="data_engineering",
    user="de_user",
    password="de_password"
)

cursor = conn.cursor()
cursor.execute("SELECT version();")
print(cursor.fetchone())
conn.close()
```

---

## 👤 Usuario y Base de Datos

### ✅ Creación automática

**PostgreSQL crea automáticamente** el usuario y la base de datos cuando levantas Docker por primera vez:

**Usuario creado automáticamente:**
- **Usuario**: `de_user` (configurado en `POSTGRES_USER` o por defecto)
- **Contraseña**: `de_password` (configurado en `POSTGRES_PASSWORD` o por defecto)
- **Privilegios**: Superusuario (puede crear bases de datos, roles, etc.)

**Base de datos creada automáticamente:**
- **Nombre**: `data_engineering` (configurado en `POSTGRES_DB` o por defecto)
- **Propietario**: `de_user`

> 💡 **Cómo funciona**: La imagen oficial de PostgreSQL (`postgres:15-alpine`) lee las variables de entorno `POSTGRES_USER`, `POSTGRES_PASSWORD` y `POSTGRES_DB` al inicializar el contenedor por primera vez. Si el volumen de datos está vacío, crea automáticamente el usuario, la base de datos y asigna los permisos.

**Para verificar:**
```bash
# Ver el usuario creado
docker exec ing-datos-db psql -U de_user -d data_engineering -c "\du"

# Verificar conexión
docker exec ing-datos-db psql -U de_user -d data_engineering -c "SELECT current_user, current_database();"
```

---

## 📝 Datos de ejemplo

### ✅ Datos ya cargados automáticamente

**¡Buenas noticias!** Los datos de ejemplo **ya están cargados** automáticamente cuando levantas Docker por primera vez.

El archivo `init-scripts/01-create-example-tables.sql` se ejecuta automáticamente al crear la base de datos y contiene:

**Tablas creadas:**
* `usuarios` - 8 usuarios de ejemplo
* `productos` - Productos de ejemplo con categorías y precios
* `ventas` - Ventas relacionadas con usuarios y productos

**Para verificar los datos:**
```bash
# Ver todas las tablas
docker exec ing-datos-db psql -U de_user -d data_engineering -c "\dt"

# Ver usuarios
docker exec ing-datos-db psql -U de_user -d data_engineering -c "SELECT * FROM usuarios;"
```

> ⚠️ **Importante**: Los scripts en `init-scripts/` solo se ejecutan **la primera vez** que se crea la base de datos. Si el volumen de datos ya existe, no se vuelven a ejecutar (para evitar duplicar datos).

### Agregar más datos de ejemplo

Si quieres agregar más datos o crear tus propias tablas:

**Opción 1: Scripts SQL en init-scripts/**

Crea archivos `.sql` en la carpeta `init-scripts/` y se ejecutarán automáticamente **solo la primera vez** que se crea la base de datos.

Ejemplo: `init-scripts/02-mis-datos.sql`

```sql
-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertar datos de ejemplo
INSERT INTO usuarios (nombre, email) VALUES
    ('Juan Pérez', 'juan@example.com'),
    ('María García', 'maria@example.com'),
    ('Carlos López', 'carlos@example.com');
```

### Opción 2: Ejecutar SQL manualmente

```bash
# Conectarse y ejecutar
docker exec -i ing-datos-db psql -U de_user -d data_engineering < mi-script.sql

# O desde psql interactivo
docker exec -it ing-datos-db psql -U de_user -d data_engineering
```

---

## 🛠️ Comandos útiles

### Ver logs
```bash
docker-compose logs -f postgres
```

### Detener servicios
```bash
docker-compose down
```

### Detener y eliminar datos (⚠️ borra todo)
```bash
docker-compose down -v
```

### Reiniciar servicios
```bash
docker-compose restart
```

### Ver estado
```bash
docker-compose ps
```

---

## 📊 Estructura de archivos

```
02_sql/
├── docker-compose.yml      # Configuración de Docker (lee .env de la raíz)
└── init-scripts/           # Scripts SQL que se ejecutan al iniciar
    └── 01-create-tables.sql

# El .env está en la raíz del proyecto (no en 02_sql/)
../.env                     # Variables de entorno (no commiteado)
../.env.example             # Plantilla de variables de entorno
```

---

## 🔒 Seguridad

⚠️ **Importante para desarrollo local:**
* Las credenciales en `.env.example` son solo para desarrollo
* **NUNCA** commitees el archivo `.env` (ya está en .gitignore)
* En producción, usa secretos seguros y variables de entorno

---

## 🐛 Troubleshooting

### Puerto 5432 ya en uso

**Problema**: Si tienes otra instancia de PostgreSQL corriendo localmente en el puerto 5432, Docker no podrá usar ese puerto.

**Solución: Cambiar el puerto en el `.env`**

1. **Edita tu `.env`** en la raíz del proyecto:
   ```bash
   # Cambia el puerto a uno disponible (ej: 5433)
   POSTGRES_PORT=5433
   DB_PORT=5433
   ```

2. **Actualiza también `DATABASE_URL`** si lo estás usando:
   ```bash
   DATABASE_URL=postgresql://de_user:de_password@localhost:5433/data_engineering
   ```

3. **Reinicia Docker** (importante: exporta la variable antes de ejecutar):
   ```bash
   cd 02_sql
   docker-compose down
   # Exporta la variable para que docker-compose la use
   export POSTGRES_PORT=5433  # o el puerto que elegiste
   docker-compose up -d
   ```
   
   > ⚠️ **Nota**: `docker-compose` necesita que `POSTGRES_PORT` esté en el entorno del shell para usarlo en la configuración de `ports:`. El `.env` se usa para variables dentro del contenedor, pero para la configuración de docker-compose necesitas exportarla.

4. **Verifica que funciona**:
   ```bash
   docker-compose ps
   # Deberías ver el puerto 5433 en lugar de 5432
   ```

5. **Actualiza tus conexiones**:
   - **DBeaver**: Cambia el puerto a `5433` en la configuración de conexión
   - **SQLTools**: Actualiza la connection string con el nuevo puerto
   - **Python**: Si usas variables de entorno, ya se actualizará automáticamente

> 💡 **Puertos comunes alternativos**: 5433, 5434, 5435, 15432

### No puedo conectarme
1. Verifica que los servicios estén corriendo: `docker-compose ps`
2. Revisa los logs: `docker-compose logs postgres`
3. Verifica que el puerto no esté bloqueado por firewall

### Los datos desaparecen
Los datos persisten en un volumen de Docker. Si ejecutas `docker-compose down -v`, se eliminan. Para mantenerlos, usa solo `docker-compose down`.

---

## 📚 Próximos pasos

Una vez que tengas la base de datos corriendo:

1. **Practica SQL básico** en `sql-basico/`
2. **Ejecuta los ejercicios** en `ejercicios/`
3. **Experimenta** con diferentes queries
4. **Crea tus propias tablas** y datos de prueba

---

## 🛠️ Herramientas recomendadas

### DBeaver (Recomendado)

**Ventajas:**
* ✅ Interfaz más intuitiva que pgAdmin
* ✅ Query Builder visual
* ✅ Mejor para visualizar datos
* ✅ Exportar datos fácilmente
* ✅ Gratis y multiplataforma

**Instalación:**
```bash
# macOS
brew install --cask dbeaver-community

# O descarga desde https://dbeaver.io/download/
```

**Configuración:**
* Host: `localhost`
* Port: `5432`
* Database: `data_engineering`
* Username: `de_user`
* Password: `de_password`

Lee la **[guía completa de DBeaver](herramientas/dbeaver-cliente-sql.md)** para más detalles.

### pgAdmin (Incluido en Docker)

Ya está disponible en `http://localhost:5050` si usas Docker Compose.

---

## 🛠️ Herramientas recomendadas

### DBeaver (Recomendado)

**Instalación:**
```bash
# macOS
brew install --cask dbeaver-community

# Windows/Linux: Descarga desde https://dbeaver.io/download/
```

**Configuración:**
* Host: `localhost`
* Port: `5432`
* Database: `data_engineering`
* Username: `de_user`
* Password: `de_password`

**Lee la guía completa:** [DBeaver para Data Engineers](herramientas/dbeaver-cliente-sql.md)

### pgAdmin (Incluido en Docker)

Ya está disponible en `http://localhost:5050` si usas Docker Compose.

**Comparación de herramientas:** [Otras Herramientas SQL](herramientas/otras-herramientas-sql.md)

---

## 💡 Tips

* Usa `\dt` en psql para listar todas las tablas
* Usa `\d nombre_tabla` para ver la estructura de una tabla
* Usa `\q` para salir de psql
* Los datos persisten entre reinicios del contenedor
* Puedes tener múltiples bases de datos en el mismo PostgreSQL
* **Recomendación**: Usa DBeaver para mejor experiencia visual

---

¡Listo para practicar SQL! 🚀
