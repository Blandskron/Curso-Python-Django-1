DROP TABLE IF EXISTS usuario_cupon;
DROP TABLE IF EXISTS libro;
DROP TABLE IF EXISTS cupon_descuento;
DROP TABLE IF EXISTS carnet_biblioteca;
DROP TABLE IF EXISTS usuario;

CREATE TABLE usuario (
  usuario_id SERIAL PRIMARY KEY,
  nombre     VARCHAR(120) NOT NULL
);

-- 1 a 1 con PK compartida (carnet_id = usuario_id)
CREATE TABLE carnet_biblioteca (
  usuario_id INT PRIMARY KEY,
  numero     VARCHAR(30) UNIQUE NOT NULL,
  FOREIGN KEY (usuario_id) REFERENCES usuario(usuario_id) ON DELETE CASCADE
);

-- 1 a muchos
CREATE TABLE libro (
  libro_id   SERIAL PRIMARY KEY,
  usuario_id INT NOT NULL,
  titulo     VARCHAR(200) NOT NULL,
  FOREIGN KEY (usuario_id) REFERENCES usuario(usuario_id) ON DELETE CASCADE
);

CREATE TABLE cupon_descuento (
  cupon_id   SERIAL PRIMARY KEY,
  codigo     VARCHAR(30) UNIQUE NOT NULL,
  porcentaje INT NOT NULL
);

-- muchos a muchos con ID propio + UNIQUE (usuario_id, cupon_id)
CREATE TABLE usuario_cupon (
  usuario_cupon_id SERIAL PRIMARY KEY,
  usuario_id       INT NOT NULL,
  cupon_id         INT NOT NULL,
  fecha_asignacion DATE NOT NULL DEFAULT CURRENT_DATE,
  FOREIGN KEY (usuario_id) REFERENCES usuario(usuario_id) ON DELETE CASCADE,
  FOREIGN KEY (cupon_id) REFERENCES cupon_descuento(cupon_id) ON DELETE CASCADE,
  UNIQUE (usuario_id, cupon_id)
);
