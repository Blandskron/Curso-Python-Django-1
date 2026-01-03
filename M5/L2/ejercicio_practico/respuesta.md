## 1) ¿Qué es un modelo de datos y para qué sirve en bases relacionales?

Un **modelo de datos** es una representación organizada de cómo se estructura la información de un dominio (por ejemplo: ventas, inventario, alumnos), definiendo:

- **Entidades** (tablas): clientes, pedidos, productos, etc.
- **Atributos** (columnas): nombre, ciudad, total, fecha, etc.
- **Relaciones** entre entidades: un cliente puede tener muchos pedidos, un pedido pertenece a un cliente.

### ¿Para qué sirve en bases relacionales?
Sirve para:
- **Diseñar correctamente** la base de datos antes de construirla.
- **Evitar duplicidad** y desorden: cada dato vive donde corresponde.
- **Permitir integridad y consistencia**: relaciones claras (PK/FK).
- **Facilitar consultas SQL**: JOINs coherentes, reportes y análisis confiables.
- **Escalar el sistema**: es más fácil mantener y extender el esquema.

---

## 2) ¿Qué es una clave foránea y qué garantiza?

Una **clave foránea (Foreign Key, FK)** es una columna (o conjunto de columnas) en una tabla que **referencia** la clave primaria (o una clave única) de otra tabla.

### ¿Qué garantiza?
Garantiza la **integridad referencial**, es decir:
- No puedes registrar un pedido con `cliente_id` que **no exista** en `clientes.id`.
- Evita registros “huérfanos” y datos inconsistentes.
- Permite reglas en cascada (según configuración):
  - **ON DELETE RESTRICT**: impide borrar un cliente si tiene pedidos.
  - **ON DELETE CASCADE**: borra los pedidos si se borra el cliente (no siempre recomendable).
  - **ON UPDATE CASCADE**: si cambia el id (poco común), se actualiza en pedidos.

Ejemplo conceptual:
- `clientes(id)` es PK
- `pedidos(cliente_id)` es FK → referencia `clientes(id)`
