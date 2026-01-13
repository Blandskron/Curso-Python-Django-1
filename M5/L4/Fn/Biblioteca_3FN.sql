DROP TABLE IF EXISTS usuario_cupon;
DROP TABLE IF EXISTS libro;
DROP TABLE IF EXISTS cupon_descuento;
DROP TABLE IF EXISTS carnet_biblioteca;
DROP TABLE IF EXISTS usuario;

CREATE TABLE usuario (
  usuario_id SERIAL PRIMARY KEY,
  nombre     VARCHAR(120) NOT NULL
);

-- 1 a 1 (con id propio + UNIQUE)
CREATE TABLE carnet_biblioteca (
  carnet_id  SERIAL PRIMARY KEY,
  usuario_id INT UNIQUE NOT NULL,
  numero     VARCHAR(30) UNIQUE NOT NULL,
  FOREIGN KEY (usuario_id) REFERENCES usuario(usuario_id)
);

-- 1 a muchos
CREATE TABLE libro (
  libro_id   SERIAL PRIMARY KEY,
  usuario_id INT NOT NULL,
  titulo     VARCHAR(200) NOT NULL,
  FOREIGN KEY (usuario_id) REFERENCES usuario(usuario_id)
);

-- cupon
CREATE TABLE cupon_descuento (
  cupon_id   SERIAL PRIMARY KEY,
  codigo     VARCHAR(30) UNIQUE NOT NULL,
  porcentaje INT NOT NULL
);

-- muchos a muchos (tabla puente con PK compuesta)
CREATE TABLE usuario_cupon (
  usuario_id INT NOT NULL,
  cupon_id   INT NOT NULL,
  PRIMARY KEY (usuario_id, cupon_id),
  FOREIGN KEY (usuario_id) REFERENCES usuario(usuario_id),
  FOREIGN KEY (cupon_id) REFERENCES cupon_descuento(cupon_id)
);
