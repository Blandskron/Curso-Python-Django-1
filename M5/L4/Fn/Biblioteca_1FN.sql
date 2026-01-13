DROP TABLE IF EXISTS usuario_cupon;
DROP TABLE IF EXISTS libro;
DROP TABLE IF EXISTS carnet_biblioteca;
DROP TABLE IF EXISTS usuario;

CREATE TABLE usuario (
  usuario_id SERIAL PRIMARY KEY,
  nombre     VARCHAR(120) NOT NULL
);

-- 1 a 1 (simple)
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

-- muchos a muchos "directo" (sin tabla cupón)
-- OJO: si el mismo cupón se repite, repites porcentaje (no 3FN)
CREATE TABLE usuario_cupon (
  usuario_cupon_id SERIAL PRIMARY KEY,
  usuario_id       INT NOT NULL,
  codigo_cupon     VARCHAR(30) NOT NULL,
  porcentaje       INT NOT NULL,
  FOREIGN KEY (usuario_id) REFERENCES usuario(usuario_id),
  UNIQUE (usuario_id, codigo_cupon)
);
