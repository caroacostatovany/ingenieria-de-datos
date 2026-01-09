# 🗄️ SQL para Data Engineers

Esta carpeta contiene todo lo que necesitas saber sobre SQL aplicado a la Ingeniería de Datos.

---

## 📖 Contenido

### 📘 Estructura

* **[SQL básico](sql-basico/)** *(próximo)*
  * SELECT, FROM, WHERE
  * JOINs básicos
  * Agregaciones (GROUP BY, HAVING)
  * Funciones comunes

* **[SQL intermedio](sql-intermedio/)** *(próximo)*
  * Subconsultas y CTEs
  * Window functions
  * Manejo de fechas y strings
  * Optimización básica

* **[SQL avanzado](sql-avanzado/)** *(próximo)*
  * Particionamiento
  * Índices y performance
  * Funciones analíticas avanzadas
  * Patrones complejos

* **[Modelado Relacional](modelado-relacional.md)** *(próximo)*
  * Normalización
  * Diseño de esquemas
  * Relaciones y claves
  * Data Warehouses

* **[Ejercicios](ejercicios/)** *(próximo)*
  * Ejercicios prácticos por nivel
  * Casos de uso reales
  * Soluciones comentadas

---

## 🎯 Objetivo de esta sección

Al finalizar esta sección, deberías poder:

* Escribir consultas SQL eficientes y mantenibles
* Diseñar esquemas de bases de datos apropiados
* Optimizar queries para grandes volúmenes de datos
* Aplicar SQL en pipelines de datos

---

## 🔗 Relación con otras secciones

* SQL se usa extensivamente en **[05_pipelines](../05_pipelines/)** para transformaciones
* El modelado relacional es base para **[04_modelado_y_calidad](../04_modelado_y_calidad/)**
* Puedes combinar SQL con Python en **[03_python](../03_python/)**

---

## 🚀 Siguiente paso

Después de dominar SQL, continúa con:

* **[03_python](../03_python/)** para automatización y pipelines más complejos
* **[04_modelado_y_calidad](../04_modelado_y_calidad/)** para diseño de modelos analíticos

---

## 🐳 Base de Datos Local con Docker

Para practicar SQL, puedes usar una base de datos PostgreSQL local con Docker:

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
* PostgreSQL listo para usar
* Datos de ejemplo (usuarios, productos, ventas)
* pgAdmin (interfaz web opcional)

---

## 💡 Tip

SQL es fundamental para Data Engineering. Dedica tiempo a practicar y entender los conceptos, no solo memorizar sintaxis.
