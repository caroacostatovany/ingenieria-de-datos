# Cursor para Data Engineers

Cursor es un editor de código moderno basado en VS Code pero con **capacidades de AI integradas** que lo hacen especialmente útil para Data Engineers que quieren usar AI como copiloto.

---

## 🧠 ¿Qué es Cursor?

Cursor es un editor de código que combina:
* **Todas las características de VS Code** (extensions, debugging, terminal integrado)
* **AI integrada** para ayudarte a escribir código, explicar código existente y refactorizar
* **Interfaz familiar** si ya conoces VS Code
* **Gratis** para uso personal

> Cursor es perfecto para Data Engineers que quieren usar AI como copiloto sin cambiar de editor.

---

## 🚀 Clonar el repositorio con Cursor

### Opción 1: Desde la interfaz de Cursor

1. **Abre Cursor**
2. **File → Clone Repository** (o `Cmd+Shift+P` / `Ctrl+Shift+P`)
3. **Pega la URL del repositorio:**
   ```
   https://github.com/USERNAME/REPO.git
   ```
4. **Selecciona la carpeta** donde quieres clonarlo
5. **Abre la carpeta** cuando termine de clonar

### Opción 2: Desde la terminal

```bash
# Clonar el repositorio
git clone https://github.com/USERNAME/REPO.git

# Entrar a la carpeta
cd REPO

# Abrir en Cursor
cursor .
```

O simplemente:
```bash
cursor .  # Si ya estás en la carpeta del proyecto
```

---

## 📁 Estructura del proyecto en Cursor

Una vez abierto el proyecto, verás:

```
📁 ingenieria-de-datos/
├── 📁 00_introduccion/
├── 📁 01_fundamentos/
├── 📁 02_sql/
├── 📁 03_python/
├── 📁 04_modelado_y_calidad/
├── 📁 05_pipelines/
├── 📁 06_ai_como_copiloto/
├── 📁 07_proyectos/
├── 📄 README.md
├── 📄 LICENSE
├── 📄 CONTRIBUTING.md
└── 📄 .gitignore
```

### Explorador de archivos

* **Sidebar izquierda**: Navega por todos los archivos
* **Click en archivos**: Abre en el editor
* **Búsqueda rápida**: `Cmd+P` / `Ctrl+P` para buscar archivos

---

## 🤖 Usar AI en Cursor

### Chat con AI

1. **Abre el panel de AI**: `Cmd+L` / `Ctrl+L`
2. **Haz preguntas** sobre el código:
   ```
   ¿Cómo funciona este pipeline?
   Explica esta función SQL
   ¿Qué hace este código?
   ```

### Composer (Editar múltiples archivos)

1. **Abre Composer**: `Cmd+I` / `Ctrl+I`
2. **Describe lo que quieres hacer**:
   ```
   Crea un nuevo pipeline que lea de PostgreSQL y escriba a Parquet
   Agrega validaciones a esta función
   Refactoriza este código para mejorarlo
   ```

### Inline Edit (Editar código inline)

1. **Selecciona código**
2. **Presiona `Cmd+K`** / `Ctrl+K`
3. **Escribe tu instrucción**:
   ```
   Optimiza esta query SQL
   Agrega manejo de errores
   Documenta esta función
   ```

---

## 🔧 Configuración inicial

### 1. Extensiones recomendadas

Instala estas extensiones para Data Engineering:

**Python:**
* Python (Microsoft)
* Pylance
* Python Docstring Generator

**SQL:**
* SQLTools
* SQLTools PostgreSQL/Cockroach Driver

**Markdown:**
* Markdown All in One
* Markdown Preview Enhanced

**Git:**
* GitLens

**Docker:**
* Docker
* Remote - Containers

### 2. Configurar Python

Si trabajas con Python:

1. **Selecciona el intérprete**: `Cmd+Shift+P` → "Python: Select Interpreter"
2. **Crea un entorno virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   # o
   venv\Scripts\activate  # Windows
   ```
3. **Instala dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Configurar Git

Cursor tiene Git integrado:

* **Ver cambios**: Panel de Source Control (icono de ramificación)
* **Commit**: Escribe mensaje y presiona `Cmd+Enter`
* **Push/Pull**: Botones en la barra inferior

---

## 💡 Flujo de trabajo recomendado

### 1. Leer y entender código

```markdown
1. Abre un archivo .md o .py
2. Selecciona código que no entiendas
3. Presiona Cmd+L y pregunta: "Explica este código"
4. La AI te explicará qué hace
```

### 2. Escribir nuevo código

```markdown
1. Crea un nuevo archivo
2. Presiona Cmd+I (Composer)
3. Describe lo que necesitas:
   "Crea una función que lea un CSV, limpie los datos nulos y guarde en Parquet"
4. Revisa y ajusta el código generado
```

### 3. Refactorizar código existente

```markdown
1. Selecciona el código a refactorizar
2. Presiona Cmd+K (Inline Edit)
3. Escribe: "Refactoriza esto para mejorarlo"
4. Revisa los cambios sugeridos
```

### 4. Documentar código

```markdown
1. Selecciona una función
2. Presiona Cmd+K
3. Escribe: "Agrega documentación completa a esta función"
4. La AI generará docstrings
```

---

## 🎯 Casos de uso específicos para Data Engineering

### Generar código SQL

```
Prompt: "Crea una query SQL que calcule el total de ventas por mes 
         agrupando por categoría de producto"
```

### Crear pipelines Python

```
Prompt: "Crea un pipeline ETL que:
         1. Lea datos de un CSV
         2. Limpie valores nulos
         3. Transforme fechas
         4. Guarde en Parquet"
```

### Explicar código complejo

```
Prompt: "Explica cómo funciona este pipeline de Airflow"
```

### Generar tests

```
Prompt: "Crea tests unitarios para esta función de validación de datos"
```

### Documentar funciones

```
Prompt: "Agrega docstrings completos a todas las funciones de este archivo"
```

---

## 🔍 Búsqueda y navegación

### Buscar en archivos

* **Búsqueda rápida**: `Cmd+F` (en archivo actual)
* **Búsqueda global**: `Cmd+Shift+F` (en todo el proyecto)
* **Buscar por símbolo**: `Cmd+Shift+O` (funciones, clases, etc.)

### Navegación rápida

* **Ir a definición**: `Cmd+Click` en una función/clase
* **Ver referencias**: Click derecho → "Go to References"
* **Navegar entre archivos**: `Cmd+P` y escribe el nombre

---

## 📝 Trabajar con Markdown

Cursor es excelente para trabajar con Markdown:

### Vista previa

* **Abre un archivo .md**
* **Presiona `Cmd+Shift+V`** para vista previa
* **O `Cmd+K V`** para vista previa al lado

### Edición asistida

```
Prompt: "Mejora la estructura de este documento markdown"
Prompt: "Agrega una sección sobre mejores prácticas"
Prompt: "Corrige la gramática y ortografía"
```

---

## 🐳 Trabajar con Docker

### Ver docker-compose.yml

1. **Abre `02_sql/docker-compose.yml`**
2. **Pregunta a la AI**: "Explica esta configuración de Docker"
3. **Para ejecutar**: Abre terminal integrada (`Ctrl+` `) y ejecuta:
   ```bash
   cd 02_sql
   docker-compose up -d
   ```

### Debugging en contenedores

Cursor puede conectarse a contenedores Docker para debugging (con la extensión Remote - Containers).

---

## 🔗 Integración con Git

### Ver cambios

* **Panel Source Control**: Ve todos los archivos modificados
* **Diff view**: Click en archivo para ver cambios
* **Stage/Unstage**: Click en el `+` al lado del archivo

### Commits

1. **Escribe mensaje de commit** descriptivo
2. **Presiona `Cmd+Enter`** para commit
3. **Push**: Click en el icono de sincronización

### Ramas

* **Crear rama**: `Cmd+Shift+P` → "Git: Create Branch"
* **Cambiar rama**: Click en el nombre de la rama (barra inferior)

---

## 💻 Terminal integrada

Cursor incluye terminal integrada:

* **Abrir terminal**: `` Ctrl+` `` o `Cmd+` ``
* **Múltiples terminales**: Click en el `+` en el panel de terminal
* **Dividir terminal**: Click derecho → "Split Terminal"

### Comandos útiles

```bash
# Activar entorno virtual
source venv/bin/activate

# Ejecutar scripts Python
python pipeline.py

# Ejecutar Docker
docker-compose up -d

# Ejecutar tests
pytest tests/
```

---

## 🎨 Personalización

### Tema

* **Settings**: `Cmd+,` / `Ctrl+,`
* **Color Theme**: Busca "Color Theme" y elige uno
* **Icon Theme**: Para cambiar iconos de archivos

### Atajos de teclado

* **Ver todos**: `Cmd+K Cmd+S` / `Ctrl+K Ctrl+S`
* **Personalizar**: `Cmd+K Cmd+S` → busca comando → click en el lápiz

---

## 🚨 Troubleshooting

### AI no responde

* Verifica tu conexión a internet
* Revisa si hay límites de uso
* Intenta recargar la ventana: `Cmd+Shift+P` → "Reload Window"

### Extensiones no funcionan

* Recarga la ventana
* Reinstala la extensión
* Verifica compatibilidad con tu versión de Cursor

### Git no funciona

* Verifica que Git esté instalado: `git --version`
* Configura tu identidad:
  ```bash
  git config --global user.name "Tu Nombre"
  git config --global user.email "tu@email.com"
  ```

---

## 📚 Recursos adicionales

* **Documentación oficial**: [cursor.sh/docs](https://cursor.sh/docs)
* **Atajos de teclado**: `Cmd+K Cmd+S` en Cursor
* **Comunidad**: Discord de Cursor

---

## 🎓 Próximos pasos

1. **Clona el repositorio** siguiendo los pasos arriba
2. **Explora los archivos** usando la navegación de Cursor
3. **Usa AI** para entender código que no conozcas
4. **Practica** escribiendo código con ayuda de AI
5. **Contribuye** al repositorio usando Git integrado

---

> **Tip**: Cursor es una herramienta poderosa, pero recuerda siempre **revisar y entender** el código que la AI genera. La AI es un copiloto, no un reemplazo de tu conocimiento.
