# 🗄️ SQL para Data Engineers

Esta carpeta contiene todo lo que necesitas saber sobre SQL aplicado a la Ingeniería de Datos.

> **💡 Nota importante**: Este módulo usa **PostgreSQL** como sistema de base de datos, pero enseña **SQL estándar** que funciona en otros sistemas. Lee [SQL vs PostgreSQL](sql-vs-postgresql.md) para entender las diferencias y por qué elegimos PostgreSQL.

## 🛠️ Herramientas recomendadas

Antes de empezar, necesitas una herramienta para ejecutar SQL. Te recomendamos:

* **[DBeaver](herramientas/dbeaver-cliente-sql.md)** - Cliente SQL universal, gratuito y potente (recomendado)
* **[Otras opciones](herramientas/otras-herramientas-sql.md)** - pgAdmin, TablePlus, DataGrip, VS Code extensions

> 💡 **¿No sabes cuál elegir?** Lee la [comparación de herramientas](herramientas/otras-herramientas-sql.md) o ve directo con DBeaver, es la opción más completa y gratuita.

---

## 📖 Contenido

### 📘 Estructura

* ✅ **[SQL vs PostgreSQL](sql-vs-postgresql.md)**
  * ¿Cuál es la diferencia?
  * ¿Por qué usamos PostgreSQL?
  * SQL estándar vs extensiones PostgreSQL

* ✅ **[Herramientas SQL](herramientas/)**
  * **[DBeaver: Cliente Universal](herramientas/dbeaver-cliente-sql.md)** - Recomendado para empezar
    * Instalación y configuración paso a paso
    * Conectar a PostgreSQL
    * Editor SQL con autocompletado
    * Query Builder visual
    * Exportar datos
  * **[Otras Herramientas](herramientas/otras-herramientas-sql.md)**
    * pgAdmin (incluido en Docker)
    * TablePlus, DataGrip, VS Code extensions
    * Comparación y cuándo usar cada una

* ✅ **[SQL básico](sql-basico/)**
  * SELECT, FROM, WHERE
  * JOINs básicos
  * Agregaciones (GROUP BY, HAVING)
  * Ordenamiento y límites
  * Funciones comunes

* ✅ **[SQL intermedio](sql-intermedio/)**
  * Subconsultas y CTEs
  * Window functions
  * Manejo avanzado de fechas
  * Optimización básica

* ✅ **[SQL avanzado](sql-avanzado/)**
  * Particionamiento
  * Índices avanzados
  * Funciones analíticas avanzadas
  * Patrones complejos

* ✅ **[Modelado Relacional](modelado-relacional.md)**
  * Normalización
  * Diseño de esquemas
  * Relaciones y claves
  * Data Warehouses

* ✅ **[Ejercicios](ejercicios/)**
  * Ejercicios prácticos por nivel
  * Casos de uso reales
  * Soluciones comentadas

---

## 🎯 Objetivo de esta sección

Al finalizar esta sección, deberías poder:

* Usar herramientas SQL (DBeaver, pgAdmin, etc.) para visualizar datos
* Escribir consultas SQL eficientes y mantenibles
* Generar queries con ayuda visual (Query Builder)
* Diseñar esquemas de bases de datos apropiados
* Optimizar queries para grandes volúmenes de datos
* Aplicar SQL en pipelines de datos

---


## 📚 Flujo de aprendizaje recomendado

1. **Configura tu entorno**
   * **Base de datos local**: Sigue [README-DOCKER.md](README-DOCKER.md) para levantar PostgreSQL con Docker
   * **Herramienta SQL**: Instala y configura **[DBeaver](herramientas/dbeaver-cliente-sql.md)** (recomendado) o elige otra de [Otras Herramientas](herramientas/otras-herramientas-sql.md)
   * **Conecta DBeaver** a tu base de datos local siguiendo las instrucciones en [README-DOCKER.md](README-DOCKER.md#opción-2-dbeaver-recomendado---cliente-desktop)

2. **Aprende [SQL básico](sql-basico/)** - Fundamentos con ayuda visual
   * Usa el editor SQL de DBeaver para practicar
   * Visualiza resultados directamente en DBeaver

3. **Profundiza en [SQL intermedio](sql-intermedio/)** - Conceptos avanzados
   * Aprovecha el autocompletado y formateo de DBeaver

4. **Explora [SQL avanzado](sql-avanzado/)** - Optimización y patrones complejos
   * Usa EXPLAIN en DBeaver para analizar rendimiento

5. **Practica con [Ejercicios](ejercicios/)** - Usa DBeaver para visualizar resultados

---

## 🚀 ¿Qué sigue?

Según el roadmap, después de dominar SQL:

**👉 Siguiente etapa: [03_python](../03_python/)** (Etapa 2 del roadmap)
* Automatización y estructurar procesos
* Python para Data Engineering
* Manejo de archivos y Pandas

**Después**: **[04_modelado_y_calidad](../04_modelado_y_calidad/)** (Etapa 3) para diseño de modelos analíticos y calidad de datos.

> 💡 **Tip**: Revisa el [Roadmap completo](../00_introduccion/roadmap-data-engineer.md) para ver la ruta completa.

---

## 🐳 Base de Datos Local con Docker

Para practicar SQL, puedes usar una base de datos **PostgreSQL 15** local con Docker:

1. **Asegúrate de tener el archivo `.env` en la raíz del proyecto:**
   ```bash
   # Desde la raíz del proyecto (no desde 02_sql/)
   cp .env.example .env
   ```
   > 💡 **Nota**: El `docker-compose.yml` usa automáticamente el `.env` de la raíz del proyecto, no necesitas crear uno en `02_sql/`.

2. **Inicia la base de datos:**
   ```bash
   cd 02_sql
   docker-compose up -d
   ```

3. **Conecta tu herramienta SQL:**
   * **DBeaver (recomendado)**: Sigue las instrucciones en [README-DOCKER.md - Opción 2: DBeaver](README-DOCKER.md#opción-2-dbeaver-recomendado---cliente-desktop)
   * **pgAdmin (web)**: Accede a http://localhost:5050 (ver [README-DOCKER.md](README-DOCKER.md#opción-1-pgadmin-interfaz-web))
   * **Otras herramientas**: Consulta [Otras Herramientas SQL](herramientas/otras-herramientas-sql.md) para más opciones

Esto te dará:
* **PostgreSQL 15** listo para usar
* Datos de ejemplo (usuarios, productos, ventas)
* **Herramientas para trabajar**: DBeaver, pgAdmin, o la que prefieras

> 💡 **¿Por qué PostgreSQL?** Lee [SQL vs PostgreSQL](sql-vs-postgresql.md) para entender por qué usamos PostgreSQL en este repositorio y cómo se relaciona con SQL estándar.

---

## 💡 Tip

SQL es fundamental para Data Engineering. Dedica tiempo a practicar y entender los conceptos, no solo memorizar sintaxis.
