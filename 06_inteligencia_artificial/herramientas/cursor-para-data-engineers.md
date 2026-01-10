# Cursor para Data Engineers

Cursor es un editor de código moderno basado en VS Code pero con **capacidades de AI integradas** que lo hacen especialmente útil para Data Engineers que quieren usar AI como copiloto.

> ⭐ **Opcional**: Cursor puede ayudarte durante el aprendizaje, pero **no es un requisito**. Puedes usar cualquier editor (VS Code, PyCharm, etc.) y configurar Cursor más adelante si lo deseas.

---

## 🧠 ¿Qué es Cursor?

Cursor es un editor de código que combina:
* **Todas las características de VS Code** (extensions, debugging, terminal integrado)
* **AI integrada** para ayudarte a escribir código, explicar código existente y refactorizar
* **Interfaz familiar** si ya conoces VS Code
* **Gratis** para uso personal

> Cursor es perfecto para Data Engineers que quieren usar AI como copiloto sin cambiar de editor. En este repositorio, puedes usar el chat de Cursor para hacer preguntas sobre cualquier contenido, pedir explicaciones adaptadas, o solicitar ayuda para ejecutar comandos.

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
├── 📁 06_inteligencia_artificial/
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
2. **Haz preguntas** sobre el repositorio:
   ```
   Explícame a grandes rasgos este repositorio
   ```
   ```   
   ¿Por dónde debería empezar si soy principiante?
   ```
   ```
   ¿Qué módulos tiene este repositorio y en qué orden debo seguirlos?
   ```
   
3. **Para preguntas sobre código específico**, puedes:
   
   **Opción A: Arrastrar archivos al chat**
   - Abre el archivo en Cursor (ej: `03_python/ejemplos/01-pipeline-etl-simple.py`)
   - Arrastra el archivo desde el explorador al panel de chat
   - O haz click derecho en el archivo → "Add to Chat"
   
   **Opción B: Mencionar el archivo en tu pregunta**
   - Escribe la ruta del archivo en tu pregunta
   - Cursor automáticamente lo incluirá en el contexto
   
   **Ejemplos de preguntas con archivos específicos:**
   ```
   Explica cómo funciona el pipeline en 03_python/ejemplos/01-pipeline-etl-simple.py
   ```
   ```
   ¿Qué hace la función transform() en 03_python/ejemplos/01-pipeline-etl-simple.py?
   ```
   ```
   Explica las queries SQL en 02_sql/ejercicios/01-ejercicios-basicos.md
   ```
   ```
   ¿Cómo se crean las tablas en 02_sql/init-scripts/01-create-example-tables.sql?
   ```
   ```
   Analiza el código de 03_python/ejemplos/03-conexion-db.py y explícame cómo se conecta a PostgreSQL
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
2. **Usa pyenv para el entorno virtual** (recomendado):
   ```bash
   # Si no tienes pyenv instalado, instálalo primero
   # Ver SETUP.md para instrucciones completas
   
   # Crear entorno virtual con pyenv-virtualenv
   pyenv virtualenv 3.11.0 ingenieria-de-datos
   
   # Activar entorno virtual
   pyenv activate ingenieria-de-datos
   
   # O configurar activación automática
   echo "ingenieria-de-datos" > .python-version
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
# Activar entorno virtual con pyenv
pyenv activate ingenieria-de-datos

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

## 💬 Cómo interactuar con el Chat de Cursor en este repositorio

El chat de Cursor puede ayudarte a navegar y aprender de este repositorio. Aquí tienes ejemplos de prompts que funcionan bien:

### 🎓 Preguntas sobre progreso y aprendizaje

**Ejemplos de prompts:**

```
"Ya terminé de aprender SQL, ¿qué sigue según el roadmap?"
```

```
"He completado los fundamentos, ¿cuál es el siguiente módulo recomendado?"
```

```
"¿En qué orden debo leer los archivos de 02_sql?"
```

**Qué esperar:** El chat te guiará según el roadmap y la estructura del repositorio.

---

### 📖 Explicaciones adaptadas

**Ejemplos de prompts:**

```
"Explica el archivo 01_fundamentos/05_docker-para-data-engineers.md como para una persona de negocio"
```

```
"Explica qué es un pipeline de datos de forma simple, sin tecnicismos"
```

```
"Resume el contenido de 02_sql/sql-basico/01-select-y-where.md en términos simples"
```

**Qué esperar:** Explicaciones adaptadas al nivel que solicites (negocio, principiante, técnico).

---

### 📚 Más ejemplos y práctica

**Ejemplos de prompts:**

```
"Dame más ejemplos de queries SQL con GROUP BY"
```

```
"Genera más ejemplos de pipelines ETL en Python"
```

```
"Muéstrame más casos de uso de validaciones de datos"
```

**Qué esperar:** Ejemplos adicionales basados en el contenido del repositorio.

---

### 🐳 Ayuda con comandos y ejecución

**Ejemplos de prompts:**

```
"Ayúdame a ejecutar Docker para la base de datos SQL según las instrucciones del repositorio"
```

```
"¿Cómo ejecuto el docker-compose.yml de 02_sql?"
```

```
"Guíame paso a paso para configurar la base de datos PostgreSQL local"
```

**Qué esperar:** El chat te guiará usando las instrucciones específicas del repositorio (como `02_sql/README-DOCKER.md`).

---

### 🔍 Explorar contenido

**Ejemplos de prompts:**

```
"¿Qué archivos hablan sobre calidad de datos?"
```

```
"Muéstrame todos los ejemplos de pipelines en el repositorio"
```

```
"¿Dónde puedo encontrar información sobre Great Expectations?"
```

**Qué esperar:** Navegación inteligente por el repositorio.

---

### 🛠️ Ayuda con código

**Ejemplos de prompts:**

```
"Explica este código SQL del archivo 02_sql/ejercicios/01-ejercicios-basicos.md"
```

```
"¿Cómo puedo mejorar este pipeline Python?"
```

```
"Genera un ejemplo similar al que está en 03_python/ejemplos/01-pipeline-etl-simple.py"
```

**Qué esperar:** Análisis y mejora de código basado en los ejemplos del repositorio.

---

## 📋 Reglas para mejores resultados

### 🔄 Sincronización Automática README ↔ Landing Page

Este repositorio tiene configurado un archivo `.cursorrules` que contiene reglas para mantener sincronizados `README.md` y `docs/index.md`.

**Cuando modifiques README.md**, el asistente de Cursor automáticamente:
- Detectará los cambios
- Aplicará los mismos cambios a `docs/index.md`
- Mantendrá la consistencia entre ambos archivos

**Para activar esta funcionalidad:**
1. Asegúrate de que el archivo `.cursorrules` existe en la raíz del proyecto
2. El asistente de Cursor lo leerá automáticamente
3. Cuando pidas cambios en README.md, también actualizará docs/index.md

---

## 📋 Reglas para mejores resultados

### ✅ Haz esto:

1. **Sé específico sobre el archivo o módulo:**
   ```
   ✅ "Explica 02_sql/sql-intermedio/03-window-functions.md"
   ❌ "Explica window functions"
   ```

2. **Menciona el contexto del repositorio:**
   ```
   ✅ "Según el roadmap de este repositorio, ¿qué sigue después de SQL?"
   ❌ "¿Qué sigue después de SQL?"
   ```

3. **Pide ayuda con comandos específicos del repo:**
   ```
   ✅ "Ayúdame a ejecutar Docker según 02_sql/README-DOCKER.md"
   ❌ "Cómo ejecuto Docker"
   ```

4. **Solicita explicaciones adaptadas:**
   ```
   ✅ "Explica esto como para un principiante"
   ✅ "Explica esto como para una persona de negocio"
   ✅ "Explica esto de forma técnica"
   ```

5. **Pregunta sobre progreso:**
   ```
   ✅ "Ya terminé de aprender SQL, ¿qué sigue según el roadmap?"
   ✅ "He completado los fundamentos, ¿cuál es el siguiente módulo?"
   ```

6. **Pide más ejemplos:**
   ```
   ✅ "Dame más ejemplos de queries SQL con GROUP BY"
   ✅ "Muéstrame más casos de uso de validaciones de datos"
   ```

### ❌ Evita esto:

1. **Preguntas muy genéricas sin contexto:**
   ```
   ❌ "¿Qué es SQL?"
   ✅ "Explica la introducción a SQL en 01_fundamentos/06_introduccion-sql.md"
   ```

2. **Pedir código sin revisar ejemplos existentes:**
   ```
   ❌ "Crea un pipeline ETL"
   ✅ "Crea un pipeline ETL similar al ejemplo en 03_python/ejemplos/01-pipeline-etl-simple.py"
   ```

3. **Preguntas sin mencionar el repositorio:**
   ```
   ❌ "¿Qué sigue después de SQL?"
   ✅ "Según el roadmap de este repositorio, ¿qué sigue después de SQL?"
   ```

---

## 🎯 Ejemplos de flujos completos

### Flujo 1: Aprender un módulo nuevo

```
1. "¿Qué debo leer primero en 02_sql?"
2. "Explica 02_sql/sql-basico/01-select-y-where.md de forma simple"
3. "Dame más ejemplos de SELECT con WHERE"
4. "Ya terminé SQL básico, ¿qué sigue?"
```

### Flujo 2: Configurar entorno

```
1. "Ayúdame a configurar Docker para SQL según las instrucciones del repo"
2. "¿Cómo ejecuto el docker-compose.yml de 02_sql?"
3. "¿Qué debo hacer después de que Docker esté corriendo?"
```

**Instrucciones para el chat:** Cuando el usuario pida ayuda con Docker, sigue estos pasos del repositorio:

1. **Referenciar** `02_sql/README-DOCKER.md` para instrucciones completas
2. **Guía paso a paso:**
   ```bash
   # Paso 1: Ir a la carpeta SQL
   cd 02_sql
   
   # Paso 2: Copiar archivo de configuración
   cp .env.example .env
   
   # Paso 3: (Opcional) Editar .env si se necesita
   
   # Paso 4: Iniciar servicios
   docker-compose up -d
   
   # Paso 5: Verificar que está corriendo
   docker-compose ps
   ```
3. **Explicar conexión:**
   - **DBeaver (recomendado):** Host: localhost, Port: 5432, Database: data_engineering, User: de_user, Password: de_password
   - **pgAdmin:** http://localhost:5050 (admin@example.com / admin)
4. **Mencionar** que los datos de ejemplo se cargan automáticamente desde `init-scripts/`

### Flujo 3: Entender un concepto

```
1. "Explica qué es un pipeline de datos como para un principiante"
2. "Muéstrame ejemplos de pipelines en este repositorio"
3. "¿Cómo se relaciona esto con lo que aprendí en fundamentos?"
```

---

## 🎓 Próximos pasos

1. **Clona el repositorio** siguiendo los pasos arriba
2. **Configura Cursor** con las extensiones recomendadas
3. **Abre el chat** (`Cmd+L` / `Ctrl+L`) y prueba los prompts de arriba
4. **Explora los archivos** usando la navegación de Cursor
5. **Usa AI** para entender código que no conozcas
6. **Practica** escribiendo código con ayuda de AI
7. **Contribuye** al repositorio usando Git integrado

---

> **Tip**: Cursor es una herramienta poderosa, pero recuerda siempre **revisar y entender** el código que la AI genera. La AI es un copiloto, no un reemplazo de tu conocimiento. Usa estos prompts como punto de partida y adapta según tus necesidades.
