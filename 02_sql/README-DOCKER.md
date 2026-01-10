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

> 💡 **Nota**: Este módulo usa las variables `POSTGRES_*` para Docker Compose, pero también puedes usar `DB_*` si prefieres consistencia con el resto del proyecto. Lee más sobre archivos `.env` en [01_fundamentos/04_archivos-env-para-data-engineers.md](../01_fundamentos/04_archivos-env-para-data-engineers.md).

### 3. Iniciar servicios

```bash
docker-compose up -d
```

Esto iniciará:
* **PostgreSQL** en el puerto 5432 (por defecto)
* **pgAdmin** (interfaz web) en el puerto 5050 (por defecto)

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
docker exec -it sql-practice-db psql -U de_user -d data_engineering

# O desde tu máquina (si tienes psql instalado)
psql -h localhost -p 5432 -U de_user -d data_engineering
```

### Opción 2: DBeaver (Recomendado - Cliente Desktop)

DBeaver es nuestra recomendación principal. Es más intuitivo y potente que pgAdmin.

**Instalación:**
```bash
# macOS
brew install --cask dbeaver-community

# O descarga desde https://dbeaver.io/download/
```

**Configuración:**
1. Abre DBeaver
2. **File → New → Database Connection**
3. Selecciona **PostgreSQL**
4. Configura:
   - Host: `localhost`
   - Port: `5432`
   - Database: `data_engineering`
   - Username: `de_user`
   - Password: `de_password`
5. **Test Connection** y luego **Finish**

**Lee la guía completa:** [DBeaver para Data Engineers](herramientas/dbeaver-cliente-sql.md)

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

## 📝 Crear datos de ejemplo

### Opción 1: Scripts SQL en init-scripts/

Crea archivos `.sql` en la carpeta `init-scripts/` y se ejecutarán automáticamente al iniciar la base de datos por primera vez.

Ejemplo: `init-scripts/01-create-tables.sql`

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
docker exec -i sql-practice-db psql -U de_user -d data_engineering < mi-script.sql

# O desde psql interactivo
docker exec -it sql-practice-db psql -U de_user -d data_engineering
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

### Puerto ya en uso
Si el puerto 5432 ya está ocupado:
1. Edita el archivo `.env` en la **raíz del proyecto** y cambia `POSTGRES_PORT=5433` (o otro puerto)
2. Reinicia: `docker-compose down && docker-compose up -d`

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
