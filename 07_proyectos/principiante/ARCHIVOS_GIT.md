# 📋 Guía: Archivos para Git en Proyectos Principiantes

Esta guía indica qué archivos **SÍ** incluir en Git y cuáles **NO**, manteniendo los proyectos educativos sin exponer soluciones completas.

---

## ✅ Archivos que SÍ deben estar en Git

### 📁 Estructura común a todos los proyectos

#### ✅ **README.md**
- Instrucciones del proyecto
- Objetivos y requisitos
- Pasos para completar
- Checklist de completado

#### ✅ **requirements.txt**
- Dependencias necesarias
- Versiones recomendadas

#### ✅ **.gitignore**
- Reglas para excluir archivos generados

---

## 📦 Proyecto 1: Pipeline ETL Simple

### ✅ Archivos a incluir:

```
proyecto_01_etl_simple/
├── README.md                    ✅ Instrucciones
├── requirements.txt             ✅ Dependencias
├── .gitignore                   ✅ Reglas de exclusión
├── pipeline.py                  ✅ Código base (estructura básica, NO solución completa)
└── data/
    └── ventas.csv               ✅ Dataset de ejemplo pequeño
```

### ❌ Archivos a EXCLUIR:

```
proyecto_01_etl_simple/
├── output/                      ❌ Carpeta completa (archivos generados)
│   ├── ventas_transformadas_*.csv
│   ├── ventas_transformadas_*.parquet
│   └── resumen_ventas_*.csv
└── __pycache__/                 ❌ Cache de Python
```

**Nota sobre `pipeline.py`**: 
- ✅ Incluir estructura básica con funciones vacías o comentarios
- ❌ NO incluir la solución completa implementada
- Ejemplo: Incluir `def extract(): pass` pero no la implementación completa

---

## 📊 Proyecto 2: Análisis de Datos con Pandas

### ✅ Archivos a incluir:

```
proyecto_02_analisis_pandas/
├── README.md                    ✅ Instrucciones
├── requirements.txt             ✅ Dependencias
├── data/
│   └── ecommerce_data.csv       ✅ Dataset de ejemplo pequeño
├── notebooks/
│   └── 01_analisis_exploratorio.ipynb  ✅ Notebook con estructura (sin outputs ejecutados)
├── src/
│   └── utils.py                 ✅ Utilidades básicas (opcional, solo estructura)
└── reports/
    └── insights.md              ✅ Template/ejemplo de insights (sin datos reales)
```

### ❌ Archivos a EXCLUIR:

```
proyecto_02_analisis_pandas/
├── reports/
│   ├── *.png                    ❌ Gráficos generados
│   └── insights.md              ❌ Si contiene resultados reales (solo template)
└── notebooks/
    └── 01_analisis_exploratorio.ipynb  ❌ Si tiene outputs ejecutados (limpiar antes)
```

**Nota sobre notebooks**:
- ✅ Incluir celdas de código sin ejecutar
- ✅ Incluir celdas markdown con instrucciones
- ❌ NO incluir outputs ejecutados (limpiar con "Clear All Outputs")
- ❌ NO incluir gráficos generados

---

## 🐳 Proyecto 3: Pipeline con Docker

### ✅ Archivos a incluir:

```
proyecto_03_docker_pipeline/
├── README.md                    ✅ Instrucciones
├── requirements.txt             ✅ Dependencias
├── Dockerfile                    ✅ Configuración Docker
├── docker-compose.yml            ✅ Orquestación
├── env.example                   ✅ Template de variables (sin valores reales)
├── data/
│   └── input/
│       └── datos.csv            ✅ Dataset de ejemplo pequeño
└── src/
    └── pipeline.py               ✅ Código base (estructura básica, NO solución completa)
```

### ❌ Archivos a EXCLUIR:

```
proyecto_03_docker_pipeline/
├── .env                         ❌ Variables de entorno reales (solo .env.example)
├── output/                      ❌ Carpeta completa (archivos generados)
│   └── datos_procesados.csv
└── src/
    └── __pycache__/             ❌ Cache de Python
```

**Nota sobre `pipeline.py`**:
- ✅ Incluir estructura básica con funciones vacías
- ✅ Incluir comentarios con instrucciones
- ❌ NO incluir la solución completa implementada

---

## 🎯 Resumen: Reglas Generales

### ✅ SIEMPRE incluir:
- ✅ README.md con instrucciones
- ✅ requirements.txt
- ✅ .gitignore
- ✅ Datos de ejemplo pequeños (CSV < 100KB)
- ✅ Estructura de carpetas (con .gitkeep si es necesario)
- ✅ Templates/ejemplos básicos (sin resultados)

### ❌ NUNCA incluir:
- ❌ Archivos en `output/` (resultados generados)
- ❌ Archivos con timestamps (resultados de ejecución)
- ❌ Gráficos/imágenes generadas (*.png, *.jpg)
- ❌ Archivos binarios grandes (*.parquet, *.xlsx)
- ❌ `__pycache__/` y archivos `.pyc`
- ❌ `.env` con credenciales reales (solo `.env.example`)
- ❌ Notebooks con outputs ejecutados
- ❌ Soluciones completas de código (solo estructura básica)

---

## 📝 Checklist antes de hacer commit

Antes de subir a Git, verifica:

- [ ] No hay archivos en `output/`
- [ ] No hay gráficos `.png` generados
- [ ] No hay archivos `.parquet` o `.xlsx`
- [ ] Los notebooks están sin outputs ejecutados
- [ ] No hay `__pycache__/` o `.pyc`
- [ ] No hay `.env` (solo `.env.example`)
- [ ] El código incluye solo estructura básica, no soluciones completas
- [ ] Los datos de ejemplo son pequeños (< 100KB)

---

## 💡 Tips

1. **Limpiar notebooks**: En Jupyter, `Cell → All Output → Clear`
2. **Verificar .gitignore**: Asegúrate de que está funcionando
3. **Revisar antes de commit**: `git status` para ver qué se va a subir
4. **Mantener educativos**: Los proyectos deben guiar, no resolver completamente

---

> **Recuerda**: El objetivo es que los estudiantes aprendan haciendo, no copiando soluciones completas.
