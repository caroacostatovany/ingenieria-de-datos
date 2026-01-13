-- Script de ejemplo: Crear tablas para practicar SQL
-- Este script se ejecuta automáticamente al crear la base de datos por primera vez

-- Tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    edad INTEGER CHECK (edad >= 0),
    ciudad VARCHAR(50),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    activo BOOLEAN DEFAULT TRUE
);

-- Tabla de productos
CREATE TABLE IF NOT EXISTS productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    categoria VARCHAR(50),
    precio DECIMAL(10, 2) NOT NULL CHECK (precio >= 0),
    stock INTEGER DEFAULT 0 CHECK (stock >= 0),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de ventas
CREATE TABLE IF NOT EXISTS ventas (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER REFERENCES usuarios(id),
    producto_id INTEGER REFERENCES productos(id),
    cantidad INTEGER NOT NULL CHECK (cantidad > 0),
    precio_unitario DECIMAL(10, 2) NOT NULL,
    fecha_venta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10, 2) GENERATED ALWAYS AS (cantidad * precio_unitario) STORED
);

-- Insertar datos de ejemplo: Usuarios
INSERT INTO usuarios (nombre, email, edad, ciudad) VALUES
    ('Juan Pérez', 'juan.perez@example.com', 28, 'Madrid'),
    ('María García', 'maria.garcia@example.com', 35, 'Barcelona'),
    ('Carlos López', 'carlos.lopez@example.com', 42, 'Valencia'),
    ('Carmen Ruiz', 'carmen.ruiz@example.com', 29, 'Madrid'),
    ('Luis Sánchez', 'luis.sanchez@example.com', 31, 'Sevilla'),
    ('Laura Fernández', 'laura.fernandez@example.com', 26, 'Barcelona'),
    ('Pedro Rodríguez', 'pedro.rodriguez@example.com', 38, 'Madrid'),
    ('Sofía Torres', 'sofia.torres@example.com', 33, 'Valencia')
ON CONFLICT (email) DO NOTHING;

-- Insertar datos de ejemplo: Productos
INSERT INTO productos (nombre, categoria, precio, stock) VALUES
    ('Laptop Dell', 'Electrónica', 899.99, 15),
    ('Mouse Logitech', 'Electrónica', 29.99, 50),
    ('Teclado Mecánico', 'Electrónica', 79.99, 30),
    ('Monitor 27"', 'Electrónica', 249.99, 20),
    ('Silla Ergonómica', 'Muebles', 199.99, 10),
    ('Escritorio Moderno', 'Muebles', 149.99, 8),
    ('Lámpara LED', 'Iluminación', 39.99, 25),
    ('Auriculares Bluetooth', 'Electrónica', 59.99, 40)
ON CONFLICT DO NOTHING;

-- Insertar datos de ejemplo: Ventas
INSERT INTO ventas (usuario_id, producto_id, cantidad, precio_unitario) VALUES
    (1, 1, 1, 899.99),
    (2, 2, 2, 29.99),
    (3, 3, 1, 79.99),
    (1, 4, 1, 249.99),
    (4, 5, 1, 199.99),
    (5, 6, 1, 149.99),
    (2, 7, 3, 39.99),
    (6, 8, 2, 59.99),
    (7, 1, 1, 899.99),
    (8, 2, 1, 29.99),
    (1, 3, 1, 79.99),
    (3, 4, 2, 249.99)
ON CONFLICT DO NOTHING;

-- Crear índices para mejorar performance
CREATE INDEX IF NOT EXISTS idx_ventas_usuario ON ventas(usuario_id);
CREATE INDEX IF NOT EXISTS idx_ventas_producto ON ventas(producto_id);
CREATE INDEX IF NOT EXISTS idx_ventas_fecha ON ventas(fecha_venta);
CREATE INDEX IF NOT EXISTS idx_usuarios_ciudad ON usuarios(ciudad);
CREATE INDEX IF NOT EXISTS idx_productos_categoria ON productos(categoria);

-- Mensaje de confirmación
DO $$
BEGIN
    RAISE NOTICE 'Tablas de ejemplo creadas exitosamente!';
    RAISE NOTICE 'Usuarios: %', (SELECT COUNT(*) FROM usuarios);
    RAISE NOTICE 'Productos: %', (SELECT COUNT(*) FROM productos);
    RAISE NOTICE 'Ventas: %', (SELECT COUNT(*) FROM ventas);
END $$;
