# Proyecto 1: Pipeline End-to-End Completo

Construye un pipeline completo que integra múltiples fuentes de datos, transformaciones complejas y modelado analítico.

---

## 🎯 Objetivo

Aprender a:
* Diseñar arquitectura completa de pipeline
* Integrar múltiples fuentes de datos
* Implementar transformaciones complejas
* Crear modelo analítico (star schema)
* Implementar calidad de datos end-to-end

---

## 📋 Requisitos previos

* Conocimientos sólidos de SQL, Python, Docker
* Entendimiento de modelado analítico
* Experiencia con pipelines

---

## 🚀 Pasos del proyecto

### 1. Arquitectura del pipeline

```
Fuentes de Datos:
├── API REST (ventas)
├── CSV (productos)
├── PostgreSQL (clientes)
└── JSON (eventos)

Pipeline:
├── Extract (múltiples fuentes)
├── Transform (limpieza, enriquecimiento)
├── Validate (calidad de datos)
└── Load (star schema)

Destino:
└── Data Warehouse (PostgreSQL)
    ├── Fact Table: ventas_fact
    └── Dimension Tables: dim_producto, dim_cliente, dim_tiempo
```

### 2. Estructura del proyecto

```
proyecto_01_pipeline_completo/
├── README.md
├── docker-compose.yml
├── src/
│   ├── extract/
│   │   ├── api_extractor.py
│   │   ├── csv_extractor.py
│   │   └── db_extractor.py
│   ├── transform/
│   │   ├── cleaner.py
│   │   ├── enricher.py
│   │   └── aggregator.py
│   ├── validate/
│   │   └── quality_checker.py
│   ├── load/
│   │   └── warehouse_loader.py
│   └── pipeline.py
├── sql/
│   ├── ddl/
│   │   ├── dim_tables.sql
│   │   └── fact_tables.sql
│   └── transformations/
│       └── transformations.sql
└── tests/
    └── test_pipeline.py
```

### 3. Implementación

Implementa cada componente:
1. **Extract**: Múltiples extractores
2. **Transform**: Limpieza y enriquecimiento
3. **Validate**: Validaciones robustas
4. **Load**: Carga a star schema

---

## ✅ Checklist

- [ ] Arquitectura diseñada
- [ ] Múltiples fuentes integradas
- [ ] Transformaciones complejas implementadas
- [ ] Star schema creado
- [ ] Validaciones end-to-end
- [ ] Pipeline completo funcionando
- [ ] Documentación completa

---

## 🚀 Próximo paso

Avanza a **[Proyecto 2: Pipeline en Producción Local](../proyecto_02_produccion_local/)**.
