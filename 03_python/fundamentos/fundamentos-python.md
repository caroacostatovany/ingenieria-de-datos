# Fundamentos Python para Data Engineers

Python es el lenguaje más usado en Data Engineering. No necesitas ser experto, pero sí competente en lo esencial.

> 💡 **Trabajaremos con Jupyter Notebooks**: Todos los ejemplos de este documento están diseñados para ejecutarse en Jupyter Notebooks. Si aún no has instalado Jupyter, revisa el [README de Fundamentos](README.md) para las instrucciones de instalación.

---

## 🧠 ¿Por qué Python para Data Engineering?

**Ventajas:**
* **Librerías potentes**: pandas, numpy, requests, sqlalchemy
* **Fácil de leer**: Sintaxis clara y expresiva
* **Versátil**: Scripts, APIs, pipelines, análisis
* **Comunidad grande**: Muchos recursos y ejemplos
* **Integración**: Funciona bien con SQL, APIs, cloud

> Python es el "pegamento" que conecta todas las piezas en Data Engineering.

---

## 📝 Sintaxis esencial

### Variables y tipos

```python
# Variables básicas
nombre = "Juan"
edad = 28
activo = True
precio = 99.99

# Tipos dinámicos (Python infiere el tipo)
tipo_nombre = type(nombre)  # <class 'str'>
tipo_edad = type(edad)      # <class 'int'>
```

### Estructuras de datos

```python
# Lista (ordenada, mutable)
productos = ["Laptop", "Mouse", "Teclado"]
productos.append("Monitor")

# Diccionario (clave-valor)
usuario = {
    "nombre": "Juan",
    "edad": 28,
    "ciudad": "Madrid"
}
print(usuario["nombre"])  # "Juan"

# Tupla (ordenada, inmutable)
coordenadas = (40.4168, -3.7038)

# Set (únicos, no ordenados)
ciudades = {"Madrid", "Barcelona", "Valencia"}
```

---

## 🔄 Control de flujo

### Condicionales

```python
# if/elif/else
edad = 25

if edad < 18:
    categoria = "Menor"
elif edad < 65:
    categoria = "Adulto"
else:
    categoria = "Senior"
```

### Bucles

```python
# For loop
productos = ["Laptop", "Mouse", "Teclado"]
for producto in productos:
    print(producto)

# Con índice
for i, producto in enumerate(productos):
    print(f"{i}: {producto}")

# While loop
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

### List comprehensions

```python
# Crear lista de cuadrados
cuadrados = [x**2 for x in range(10)]

# Con condición
pares = [x for x in range(10) if x % 2 == 0]

# Diccionario comprehension
edades = {"Juan": 28, "María": 35, "Carlos": 42}
mayores_30 = {nombre: edad for nombre, edad in edades.items() if edad > 30}
```

---

## 🔧 Funciones

### Funciones básicas

```python
def calcular_total(precio, cantidad):
    """Calcula el total de una compra."""
    return precio * cantidad

# Uso
total = calcular_total(99.99, 2)
```

### Funciones con valores por defecto

```python
def saludar(nombre, saludo="Hola"):
    """Saluda a una persona."""
    return f"{saludo}, {nombre}!"

saludar("Juan")  # "Hola, Juan!"
saludar("María", "Buenos días")  # "Buenos días, María!"
```

### Funciones con múltiples valores de retorno

```python
def dividir(a, b):
    """Divide dos números y retorna cociente y resto."""
    cociente = a // b
    resto = a % b
    return cociente, resto

coc, res = dividir(10, 3)
```

---

## 📚 Librerías esenciales para Data Engineering

### pandas - Manipulación de datos

```python
import pandas as pd

# Crear DataFrame
df = pd.DataFrame({
    'nombre': ['Juan', 'María', 'Carlos'],
    'edad': [28, 35, 42],
    'ciudad': ['Madrid', 'Barcelona', 'Valencia']
})

# Leer CSV
df = pd.read_csv('datos.csv')

# Operaciones básicas
df.head()           # Primeras 5 filas
df.info()           # Información del DataFrame
df.describe()       # Estadísticas descriptivas
```

### requests - APIs HTTP

```python
import requests

# GET request
response = requests.get('https://api.ejemplo.com/datos')
datos = response.json()

# POST request
response = requests.post(
    'https://api.ejemplo.com/datos',
    json={'nombre': 'Juan', 'edad': 28}
)
```

### sqlalchemy - Bases de datos

```python
from sqlalchemy import create_engine
import pandas as pd

# Conectar a PostgreSQL
engine = create_engine('postgresql://user:pass@localhost/db')

# Leer datos
df = pd.read_sql('SELECT * FROM usuarios', engine)

# Escribir datos
df.to_sql('usuarios_nuevos', engine, if_exists='append')
```

---

## 🛠️ Manejo de errores

### Try/Except

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Esto siempre se ejecuta")
```

### Buenas prácticas

```python
def leer_archivo(ruta):
    """Lee un archivo con manejo de errores."""
    try:
        with open(ruta, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Archivo {ruta} no encontrado")
        return None
    except Exception as e:
        print(f"Error leyendo archivo: {e}")
        return None
```

---

## 📦 Módulos y imports

### Importar módulos

```python
# Import completo
import pandas as pd

# Import específico
from datetime import datetime

# Import con alias
import numpy as np

# Import múltiple
from sqlalchemy import create_engine, text
```

### Crear tu propio módulo

```python
# archivo: utils.py
def limpiar_texto(texto):
    """Limpia un texto."""
    return texto.strip().upper()

# archivo: main.py
from utils import limpiar_texto

resultado = limpiar_texto("  hola mundo  ")
```

---

## 💡 Buenas prácticas

### 1. Nombres descriptivos

```python
# ✅ Claro
def calcular_total_ventas(ventas):
    return sum(venta['total'] for venta in ventas)

# ⚠️ Confuso
def calc(v):
    return sum(x['t'] for x in v)
```

### 2. Documentación

```python
def procesar_datos(archivo, formato='csv'):
    """
    Procesa un archivo de datos y retorna un DataFrame.
    
    Args:
        archivo (str): Ruta al archivo
        formato (str): Formato del archivo ('csv', 'json', 'parquet')
    
    Returns:
        pd.DataFrame: Datos procesados
    """
    # Código aquí
    pass
```

### 3. Type hints (opcional pero recomendado)

```python
from typing import List, Dict

def procesar_usuarios(usuarios: List[Dict[str, any]]) -> pd.DataFrame:
    """Procesa una lista de usuarios."""
    return pd.DataFrame(usuarios)
```

---

## 🎯 Ejercicios

1. Crea una función que calcule el promedio de una lista de números
2. Escribe una función que filtre usuarios mayores de 25 años
3. Crea un diccionario con estadísticas de una lista de números
4. Escribe código que maneje errores al leer un archivo

---

## 🚀 Próximo paso

Continúa con **[Manejo de archivos](manejo-de-archivos.md)** para aprender a leer y escribir diferentes formatos de datos.

---

> **Recuerda**: No necesitas saber todo Python. Enfócate en lo que usas en Data Engineering: estructuras de datos, funciones, manejo de archivos, y librerías como pandas.
