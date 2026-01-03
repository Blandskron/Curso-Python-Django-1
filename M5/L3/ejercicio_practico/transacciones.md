## 1) ¿Qué es una transacción y por qué es importante?

Una **transacción** es un conjunto de operaciones SQL (INSERT/UPDATE/DELETE) que se ejecutan como una sola unidad lógica de trabajo.

La idea es:
- **o se aplican todas**, o
- **no se aplica ninguna** (si ocurre un error o si decidimos deshacer).

**Importancia:** mantiene los datos consistentes en escenarios críticos (pagos, facturación, stock), evitando estados “a medias” (por ejemplo, descontar dinero sin registrar el abono).

---

## 2) ACID (definiciones breves)

### Atomicidad
“Todo o nada”. Si una parte falla, se deshace todo lo hecho dentro de la transacción.

### Consistencia
La transacción no debe dejar la base en un estado inválido: se deben respetar reglas (PK, FK, CHECK, etc.).

### Aislamiento
Una transacción en curso no debería “mezclarse” con otras de forma que genere resultados incorrectos. El motor controla concurrencia.

### Durabilidad
Una vez que se hace **COMMIT**, los cambios quedan persistidos aunque se caiga el sistema.

---

## 3) Ejercicio práctico: COMMIT vs ROLLBACK

> Nota: los IDs exactos dependen de tus datos. Para hacerlo sin adivinar IDs, se usan subconsultas por nombre.

### 3.1 Caso A — Probar ROLLBACK (deshacer)

```sql
BEGIN;

-- 1) Insertar un cliente "temporal"
INSERT INTO clientes (nombre, ciudad)
VALUES ('Cliente Temporal', 'TemporalCity');

-- 2) Insertar un pedido asociado a ese cliente
INSERT INTO pedidos (cliente_id, total, fecha)
VALUES (
  (SELECT id FROM clientes WHERE nombre = 'Cliente Temporal'),
  99999,
  DEFAULT
);

-- Verificar dentro de la transacción (debería aparecer)
SELECT * FROM clientes WHERE nombre = 'Cliente Temporal';
SELECT * FROM pedidos WHERE cliente_id = (SELECT id FROM clientes WHERE nombre = 'Cliente Temporal');

-- Deshacer todo
ROLLBACK;

-- Verificar después del rollback (NO debería existir)
SELECT * FROM clientes WHERE nombre = 'Cliente Temporal';
