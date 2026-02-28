#  Sistema de Transferencias Gamificadas (DB)

Base de datos PostgreSQL para un sistema interno tipo fintech gamificado.  
No maneja dinero real ni integra sistemas bancarios externos.

El sistema permite:
- Crear clientes con saldo inicial automático
- Registrar transferencias entre clientes
- Aplicar transferencias de forma **100% automática con triggers**
- Mantener auditoría completa mediante logs
- Garantizar atomicidad, consistencia e idempotencia

---

##  Características Clave

- **Saldo inicial automático:** todos los clientes comienzan con `10000`
- **Una sola operación manual:** `INSERT INTO transferencias`
- **Todo lo demás es automático**
- **Diseño orientado a eventos**
- **Seguro contra doble aplicación**
- **Escalable a múltiples monedas**

---

##  Modelo de Datos

### 1 clientes
Representa a los usuarios del sistema.

```sql
clientes (
  cli_id PK,
  cli_uuid UUID,
  nombre,
  email,
  estado,
  created_at,
  updated_at
)
````

 Al crear un cliente:

* Se genera automáticamente su cuenta
* Se le asigna saldo inicial = **10000**

---

### 2 activos

Define las monedas internas del sistema.

```sql
activos (
  act_id PK,
  codigo UNIQUE,
  nombre,
  decimales,
  activo
)
```

 Ejemplo:

* `COIN` → moneda interna del sistema

---

### 3 cuentas

Billetera por cliente y por activo.

```sql
cuentas (
  cta_id PK,
  cli_id FK,
  act_id FK,
  saldo,
  estado,
  created_at,
  updated_at
)
```

 Reglas:

* Una cuenta por cliente + activo
* El saldo **nunca puede ser negativo**

---

### 4 transferencias

Registro principal de una operación de envío.

```sql
transferencias (
  tra_id PK,
  tra_uuid UUID,
  cli_origen_id,
  cli_destino_id,
  act_id,
  monto,
  estado_actual,
  referencia UNIQUE,
  nota,
  metadata,
  created_at,
  updated_at
)
```

 Importante:

* **Insertar aquí NO mueve saldo**
* Solo representa la intención de transferencia

---

### 5 transfer_estado_catalogo

Catálogo de estados posibles del sistema.

```sql
transfer_estado_catalogo (
  est_code PK,
  descripcion,
  severidad,
  aplica_saldos BOOLEAN
)
```

 Estados clave:

* `CONFIRMED` → `aplica_saldos = true`
* `BAL_INSUF` → saldo insuficiente
* `ALREADY_APPL` → idempotencia

---

### 6 transferencias_log

Sistema de eventos / auditoría.

```sql
transferencias_log (
  log_id PK,
  tra_id FK,
  ok BOOLEAN,
  est_code,
  error_code,
  error_msg,
  detalle JSONB,
  created_at
)
```

 Esta tabla:

* Dispara la aplicación real de saldos
* Registra errores
* Permite auditoría completa

---

##  Flujo Automático de una Transferencia

### Paso 1 (manual)

```sql
INSERT INTO transferencias (...)
VALUES (...);
```

### Paso 2 (automático)

Trigger `AFTER INSERT ON transferencias`:

* Inserta `CONFIRMED` en `transferencias_log`

### Paso 3 (automático)

Trigger `AFTER INSERT ON transferencias_log`:

* Valida saldo
* Bloquea cuentas (`FOR UPDATE`)
* Descuenta saldo al origen
* Suma saldo al destino
* Marca la transferencia como `aplicada`

 **No se requieren UPDATEs ni inserts manuales adicionales**

---

##  Triggers Principales

###  Crear cuenta inicial al crear cliente

```text
clientes → AFTER INSERT → crea cuenta con saldo = 10000
```

---

###  Auto-confirmar transferencia al insertarla

```text
transferencias → AFTER INSERT → inserta CONFIRMED en log
```

---

###  Aplicar transferencia al confirmar

```text
transferencias_log → AFTER INSERT (ok=true + aplica_saldos=true)
```

Incluye:

* Validación de saldo
* Prevención de doble ejecución
* Manejo de errores
* Atomicidad total

---

##  Seguridad y Consistencia

 Transacciones atómicas
 Locks ordenados para evitar deadlocks
 Prevención de doble aplicación
 Auditoría completa
 Compatible con alta concurrencia

---

##  Testing Incluido

* Inserción masiva de clientes
* Múltiples series de transferencias
* Confirmación automática
* Casos exitosos y fallidos
* Validación de saldos y logs

---

##  Escalabilidad Futura

Este diseño permite fácilmente:

* Reversiones (refunds)
* Ledger contable de doble entrada
* Multi-moneda
* Límites diarios
* Congelamiento de cuentas
* Integración con API / microservicios
* Sistema antifraude

---

##  Nota Importante

> Este sistema **NO maneja dinero real**
> Es un sistema **interno y gamificado**
> No está conectado a bancos ni sistemas externos

---

##  Recomendación de uso

Usar esta DB como:

* Motor financiero interno
* Backend de simulación fintech
* Gamificación económica
* Base para MVP / startup experimental

---

**Autor:**
Proyecto personal – arquitectura y lógica diseñada paso a paso
