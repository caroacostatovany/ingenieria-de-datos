# ❓ Preguntas Frecuentes (FAQ)

Preguntas comunes sobre el repositorio y cómo usarlo.

---

## 🎯 Sobre el Repositorio

### ¿Para quién es este repositorio?

Este repositorio es para:
* 👶 **Principiantes** que quieren entrar al mundo de datos
* 👩‍💻 **Perfiles intermedios** que ya usan SQL/Python pero quieren hacerlo mejor
* 🚀 **Perfiles avanzados** que buscan reforzar fundamentos y buenas prácticas

### ¿Necesito experiencia previa?

No necesitas experiencia previa para empezar. El roadmap está diseñado para empezar desde cero. Si ya tienes experiencia, puedes saltar a las secciones que te interesen.

### ¿Por qué está en español?

Para hacer el contenido más accesible a la comunidad de habla hispana. La mayoría del contenido técnico está en inglés, y queremos cambiar eso.

---

## 🚀 Cómo Empezar

### ¿Por dónde empiezo?

1. **PRIMERO**: Configura [Cursor](06_inteligencia_artificial/herramientas/cursor-para-data-engineers.md)
2. Sigue el [Roadmap](00_introduccion/roadmap-data-engineer.md) en orden
3. Empieza con [Introducción](00_introduccion/) y luego [Fundamentos](01_fundamentos/)

### ¿Debo seguir el orden del roadmap?

Recomendamos seguir el orden, especialmente si eres principiante. Si ya tienes experiencia, puedes saltar a las secciones relevantes, pero siempre revisa los fundamentos.

### ¿Necesito instalar todo de una vez?

No. Instala solo lo que necesites según el módulo que estés estudiando. Revisa [SETUP.md](SETUP.md) para más detalles.

---

## 🛠️ Configuración Técnica

### ¿Necesito Docker?

Docker es **opcional pero recomendado** para:
* Practicar SQL con PostgreSQL local
* Ejecutar pipelines en contenedores
* Crear entornos reproducibles

Puedes aprender sin Docker, pero te recomendamos instalarlo cuando llegues al módulo de SQL.

### ¿Qué versión de Python necesito?

Python 3.8 o superior. Verifica con:
```bash
python --version
# o
python3 --version
```

### ¿Necesito instalar todas las dependencias?

No. Instala solo lo que necesites según el módulo:
- **SQL**: `psycopg2-binary`, `python-dotenv`
- **Python/Pandas**: `pandas`, `numpy`, `matplotlib`
- **Jupyter**: `jupyter` o `jupyterlab`
- **Pipelines**: `prefect` o `apache-airflow`

Revisa [requirements.txt](requirements.txt) para ver todas las opciones.

### ¿Cómo configuro el archivo .env?

1. Copia `.env.example` a `.env`
2. Edita `.env` con tus valores reales
3. Lee [Archivos .env para Data Engineers](01_fundamentos/04_archivos-env-para-data-engineers.md) para más detalles

---

## 📚 Sobre el Contenido

### ¿El contenido está completo?

El repositorio está en constante evolución. Algunas secciones están completas (✅), otras están en desarrollo. Revisa el [README principal](README.md) para ver el estado de cada módulo.

### ¿Puedo contribuir con contenido?

¡Sí! Revisa [CONTRIBUTING.md](CONTRIBUTING.md) para ver cómo contribuir. Agradecemos cualquier mejora o nuevo contenido.

### ¿Hay ejercicios prácticos?

Sí. Hay ejercicios en:
* **[02_sql/ejercicios/](02_sql/ejercicios/)** - Ejercicios de SQL por nivel
* **[03_python/ejemplos/](03_python/ejemplos/)** - Ejemplos en Jupyter Notebooks
* **[07_proyectos/](07_proyectos/)** - Proyectos completos por nivel

### ¿Los ejemplos funcionan?

Sí, todos los ejemplos están probados y funcionan. Si encuentras algún problema, abre un Issue.

---

## 🤖 Sobre AI y Cursor

### ¿Debo usar Cursor?

**Sí, altamente recomendado**. Cursor te ayudará durante todo el aprendizaje. Configúralo ANTES de empezar con SQL o Python.

### ¿Puedo usar otro IDE?

Sí, puedes usar VS Code, PyCharm, o cualquier otro IDE. Pero Cursor está optimizado para este repositorio y te dará mejor experiencia.

### ¿La AI reemplaza el aprendizaje?

**No**. La AI es una herramienta de apoyo. Debes entender los fundamentos. Lee [Límites de la AI](06_inteligencia_artificial/limites-de-la-ai.md) para más detalles.

---

## 🐛 Problemas Técnicos

### Error al conectar a PostgreSQL

1. Verifica que Docker esté corriendo: `docker ps`
2. Verifica los contenedores: `cd 02_sql && docker-compose ps`
3. Revisa el archivo `.env` en `02_sql/`
4. Lee [README-DOCKER.md](02_sql/README-DOCKER.md)

### Error: "ModuleNotFoundError"

1. Asegúrate de tener el entorno virtual activado
2. Instala las dependencias: `pip install -r requirements.txt`
3. Verifica que estás en el directorio correcto

### Jupyter no inicia

```bash
# Reinstalar Jupyter
pip install --upgrade jupyter jupyterlab

# O usar JupyterLab
jupyter lab
```

### Los notebooks no se ven bien

Asegúrate de tener Jupyter instalado y ábrelos con:
- Jupyter Notebook: `jupyter notebook`
- JupyterLab: `jupyter lab`
- VS Code: Abre directamente el archivo `.ipynb`

---

## 📖 Sobre el Aprendizaje

### ¿Cuánto tiempo toma completar el roadmap?

Depende de tu punto de partida y constancia:
* **3-6 meses** para bases sólidas
* **6-12 meses** para nivel intermedio
* **Aprendizaje continuo** para nivel senior

### ¿Debo hacer todos los proyectos?

No es necesario hacer todos. Elige proyectos según tu nivel y objetivos. Los proyectos son para practicar y construir tu portafolio.

### ¿Hay certificaciones o certificados?

No, este es un repositorio educativo. Puedes usar el contenido para prepararte para certificaciones oficiales (AWS, GCP, etc.), pero no emitimos certificados.

---

## 💼 Sobre Carrera Profesional

### ¿Esto me ayudará a conseguir trabajo?

Sí, si:
* Completas los proyectos y los agregas a tu portafolio
* Entiendes los fundamentos, no solo memorizas
* Practicas con casos reales
* Construyes proyectos propios

### ¿Qué nivel de Data Engineer alcanzaré?

Depende de cuánto practiques. Este repositorio te da las bases para:
* **Junior**: Después de completar fundamentos, SQL, Python y algunos proyectos
* **Mid-level**: Después de completar pipelines, calidad y proyectos avanzados
* **Senior**: Requiere experiencia práctica adicional en producción

---

## 🤝 Contribuciones

### ¿Cómo puedo contribuir?

Revisa [CONTRIBUTING.md](CONTRIBUTING.md) para detalles. Puedes:
* Reportar errores
* Mejorar contenido existente
* Agregar nuevo contenido
* Traducir o adaptar contenido

### ¿Puedo usar este contenido en mi curso/empresa?

Sí, bajo la licencia MIT. Revisa [LICENSE](LICENSE) para más detalles.

---

## 📞 Más Ayuda

### ¿Dónde puedo hacer preguntas?

* Abre un **Issue** en GitHub
* Usa el **chat de Cursor** para preguntas sobre el contenido
* Contacta al mantenedor por [LinkedIn](https://www.linkedin.com/in/carolina-acosta-tovany-1a6689275/)

### ¿Hay comunidad o foro?

Actualmente no hay comunidad oficial, pero puedes:
* Abrir Issues para discusiones
* Contribuir con contenido
* Compartir tus proyectos

---

## 🔄 Actualizaciones

### ¿Con qué frecuencia se actualiza?

El repositorio se actualiza regularmente. Revisa los commits o las Issues para ver las últimas actualizaciones.

### ¿Cómo me entero de nuevas actualizaciones?

* **Star** el repositorio en GitHub para recibir notificaciones
* Revisa los Issues y Pull Requests
* Sigue al mantenedor en [LinkedIn](https://www.linkedin.com/in/carolina-acosta-tovany-1a6689275/)

---

> **¿No encontraste tu pregunta?** Abre un Issue con la etiqueta `question` y la agregaremos al FAQ.
