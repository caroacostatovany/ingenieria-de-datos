# Otras Herramientas SQL

Comparación de herramientas alternativas para trabajar con SQL y bases de datos.

---

## 📊 Comparación rápida

| Herramienta | Gratis | Multi-DB | Visual | Editor SQL | Recomendado para |
|-------------|--------|----------|--------|------------|------------------|
| **DBeaver** | ✅ | ✅ | ✅ | ✅ | Data Engineers (recomendado) |
| **pgAdmin** | ✅ | ❌ (solo PostgreSQL) | ✅ | ✅ | PostgreSQL específico |
| **TablePlus** | ⚠️ (freemium) | ✅ | ✅ | ✅ | Diseño moderno |
| **DataGrip** | ❌ (pago) | ✅ | ✅ | ✅ | Profesionales |
| **VS Code** | ✅ | ✅ | ⚠️ | ✅ | Desarrolladores |

---

## 🐘 pgAdmin (PostgreSQL)

### Características

* **Específico para PostgreSQL**
* **Interfaz web** (se ejecuta en navegador)
* **Gratuito y open source**
* **Incluido en Docker** de este repositorio

### Cuándo usar

✅ **Usa pgAdmin cuando:**
* Trabajas solo con PostgreSQL
* Prefieres interfaz web
* Ya está configurado (como en nuestro Docker)

❌ **No uses pgAdmin cuando:**
* Necesitas trabajar con múltiples tipos de bases de datos
* Prefieres aplicación desktop

### Acceso en nuestro Docker

```
URL: http://localhost:5050
Email: admin@example.com
Password: admin
```

---

## 🎨 TablePlus

### Características

* **Diseño moderno y limpio**
* **Multi-base de datos**
* **Gratis con limitaciones** (freemium)
* **Solo macOS/Windows**

### Cuándo usar

✅ **Usa TablePlus cuando:**
* Prefieres diseño moderno
* Trabajas en macOS/Windows
* No te importa pagar por versión completa

❌ **No uses TablePlus cuando:**
* Necesitas Linux
* Prefieres completamente gratuito
* Necesitas muchas conexiones (versión free limitada)

---

## 💼 DataGrip (JetBrains)

### Características

* **IDE completo** para bases de datos
* **Multi-base de datos**
* **Muy potente** (refactoring, análisis, etc.)
* **De pago** (pero excelente)

### Cuándo usar

✅ **Usa DataGrip cuando:**
* Tienes presupuesto para herramienta profesional
* Necesitas features avanzadas
* Ya usas otras herramientas JetBrains

❌ **No uses DataGrip cuando:**
* Necesitas herramienta gratuita
* Solo necesitas funcionalidades básicas

---

## 💻 VS Code con extensiones

### Extensiones útiles

**1. SQLTools**
```bash
# Instalar extensión
# Busca "SQLTools" en VS Code Extensions
```

**Características:**
* Conectar a múltiples bases de datos
* Editor SQL con autocompletado
* Ver resultados en VS Code

**2. PostgreSQL**
```bash
# Extensión específica para PostgreSQL
```

### Cuándo usar

✅ **Usa VS Code cuando:**
* Ya usas VS Code para desarrollo
* Quieres todo en un solo editor
* Prefieres extensibilidad

❌ **No uses VS Code cuando:**
* Prefieres herramienta dedicada
* Necesitas visualización avanzada

---

## 🎯 Recomendación

### Para empezar: DBeaver

**Razones:**
* ✅ Completamente gratuito
* ✅ Funciona con múltiples bases de datos
* ✅ Interfaz intuitiva
* ✅ Query Builder visual
* ✅ Exportar datos fácilmente
* ✅ Multiplataforma

### Alternativas según necesidad

* **Solo PostgreSQL**: pgAdmin (ya incluido en Docker)
* **Diseño moderno**: TablePlus (si no te importa pagar)
* **Profesional**: DataGrip (si tienes presupuesto)
* **Todo en uno**: VS Code (si ya lo usas)

---

## 💡 Tips de elección

### Preguntas para decidir

1. **¿Trabajas con múltiples tipos de bases de datos?**
   * Sí → DBeaver o DataGrip
   * No → pgAdmin (si solo PostgreSQL)

2. **¿Presupuesto?**
   * Gratis → DBeaver o pgAdmin
   * Pago OK → DataGrip o TablePlus

3. **¿Prefieres aplicación o web?**
   * Aplicación → DBeaver, TablePlus, DataGrip
   * Web → pgAdmin

4. **¿Ya usas VS Code?**
   * Sí → Considera extensiones SQL
   * No → DBeaver es mejor opción

---

## 🚀 Próximo paso

Después de elegir tu herramienta:
* **[DBeaver](dbeaver-cliente-sql.md)** - Guía completa
* **[Ejercicios SQL](../ejercicios/)** - Practica con tu herramienta

---

> **Recuerda**: La mejor herramienta es la que usas efectivamente. Empieza con DBeaver (gratis y potente) y cambia si necesitas algo específico.
