# 🗄️ SQL para Data Engineers

Esta carpeta contiene todo lo que necesitas saber sobre SQL aplicado a la Ingeniería de Datos.

> **💡 Nota importante**: Este módulo usa **PostgreSQL** como sistema de base de datos, pero enseña **SQL estándar** que funciona en otros sistemas. Lee [SQL vs PostgreSQL](sql-vs-postgresql.md) para entender las diferencias y por qué elegimos PostgreSQL.

---

## 📖 Contenido

### 📘 Estructura

* ✅ **[SQL vs PostgreSQL](sql-vs-postgresql.md)**
  * ¿Cuál es la diferencia?
  * ¿Por qué usamos PostgreSQL?
  * SQL estándar vs extensiones PostgreSQL

* ✅ **[Herramientas SQL](herramientas/)**
  * DBeaver (recomendado)
  * Visualización de datos
  * Generación de queries
  * Otras herramientas (pgAdmin, TablePlus, etc.)

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

## 🔗 Relación con otras secciones

* SQL se usa extensivamente en **[05_pipelines](../05_pipelines/)** para transformaciones
* El modelado relacional es base para **[04_modelado_y_calidad](../04_modelado_y_calidad/)**
* Puedes combinar SQL con Python en **[03_python](../03_python/)**

---

## 📚 Flujo de aprendizaje recomendado

1. **Empieza con [Herramientas SQL](herramientas/)** - Configura DBeaver y aprende a visualizar datos
2. **Aprende [SQL básico](sql-basico/)** - Fundamentos con ayuda visual
3. **Profundiza en [SQL intermedio](sql-intermedio/)** - Conceptos avanzados
4. **Explora [SQL avanzado](sql-avanzado/)** - Optimización y patrones complejos
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

1. **Copia el archivo de configuración:**
   ```bash
   cp .env.example .env
   ```

2. **Inicia la base de datos:**
   ```bash
   docker-compose up -d
   ```

3. **Lee las instrucciones completas** en [README-DOCKER.md](README-DOCKER.md)

Esto te dará:
* **PostgreSQL 15** listo para usar
* Datos de ejemplo (usuarios, productos, ventas)
* pgAdmin (interfaz web opcional)

> 💡 **¿Por qué PostgreSQL?** Lee [SQL vs PostgreSQL](sql-vs-postgresql.md) para entender por qué usamos PostgreSQL en este repositorio y cómo se relaciona con SQL estándar.

---

## 💡 Tip

SQL es fundamental para Data Engineering. Dedica tiempo a practicar y entender los conceptos, no solo memorizar sintaxis.
