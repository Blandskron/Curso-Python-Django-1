-- PostgreSQL (tablas ONLY) — base para “saldo + transferencias + log de estados”
-- Copiar/pegar en tu Query Tool.

-- Recomendado para UUID (opcional)
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- ==============
-- 1) CLIENTES
-- ==============
CREATE TABLE IF NOT EXISTS clientes (
  cli_id            BIGSERIAL PRIMARY KEY,
  cli_uuid          UUID NOT NULL DEFAULT gen_random_uuid(),

  nombre            TEXT NOT NULL,
  email             TEXT UNIQUE,
  estado            TEXT NOT NULL DEFAULT 'activo' CHECK (estado IN ('activo','bloqueado','eliminado')),

  created_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at        TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE UNIQUE INDEX IF NOT EXISTS ux_clientes_cli_uuid ON clientes(cli_uuid);


-- ==========================
-- 2) ACTIVOS / “MONEDA”
-- (para que tu sistema soporte 1 o N “tokens” internos)
-- ==========================
CREATE TABLE IF NOT EXISTS activos (
  act_id            SMALLSERIAL PRIMARY KEY,
  codigo            TEXT NOT NULL UNIQUE,     -- ej: "COIN", "GEM", "XP"
  nombre            TEXT NOT NULL,
  decimales         SMALLINT NOT NULL DEFAULT 2 CHECK (decimales BETWEEN 0 AND 18),
  activo            BOOLEAN NOT NULL DEFAULT TRUE,

  created_at        TIMESTAMPTZ NOT NULL DEFAULT now()
);


-- ==========================
-- 3) CUENTAS / BILLETERAS
-- (saldo por cliente y por activo)
-- ==========================
CREATE TABLE IF NOT EXISTS cuentas (
  cta_id            BIGSERIAL PRIMARY KEY,
  cta_uuid          UUID NOT NULL DEFAULT gen_random_uuid(),

  cli_id            BIGINT NOT NULL REFERENCES clientes(cli_id),
  act_id            SMALLINT NOT NULL REFERENCES activos(act_id),

  saldo             NUMERIC(20, 6) NOT NULL DEFAULT 0 CHECK (saldo >= 0),

  estado            TEXT NOT NULL DEFAULT 'activa' CHECK (estado IN ('activa','congelada','cerrada')),

  created_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at        TIMESTAMPTZ NOT NULL DEFAULT now(),

  CONSTRAINT ux_cuentas_cliente_activo UNIQUE (cli_id, act_id)
);

CREATE UNIQUE INDEX IF NOT EXISTS ux_cuentas_cta_uuid ON cuentas(cta_uuid);
CREATE INDEX IF NOT EXISTS ix_cuentas_cli_id ON cuentas(cli_id);


-- ==========================
-- 4) TRANSFERENCIAS
-- (registro “principal” de la operación)
-- ==========================
CREATE TABLE IF NOT EXISTS transferencias (
  tra_id            BIGSERIAL PRIMARY KEY,
  tra_uuid          UUID NOT NULL DEFAULT gen_random_uuid(),

  -- Origen/Destino (cliente)
  cli_origen_id     BIGINT NOT NULL REFERENCES clientes(cli_id),
  cli_destino_id    BIGINT NOT NULL REFERENCES clientes(cli_id),

  -- Activo / monto
  act_id            SMALLINT NOT NULL REFERENCES activos(act_id),
  monto             NUMERIC(20, 6) NOT NULL CHECK (monto > 0),

  -- Estado actual (se puede “derivar” del log, pero es útil como snapshot)
  estado_actual     TEXT NOT NULL DEFAULT 'creada'
                    CHECK (estado_actual IN ('creada','validando','aplicada','fallida','revertida','cancelada')),

  -- Idempotencia / referencia externa interna (evita duplicados si reintentas)
  referencia        TEXT UNIQUE, -- ej: "PAY_2026_000001" o un hash del request

  nota              TEXT,
  metadata          JSONB,

  created_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at        TIMESTAMPTZ NOT NULL DEFAULT now(),

  -- Evita auto-transferencias (si quieres permitirlas, elimina este CHECK)
  CONSTRAINT ck_transferencias_no_self CHECK (cli_origen_id <> cli_destino_id)
);

CREATE UNIQUE INDEX IF NOT EXISTS ux_transferencias_tra_uuid ON transferencias(tra_uuid);
CREATE INDEX IF NOT EXISTS ix_transferencias_origen ON transferencias(cli_origen_id, created_at DESC);
CREATE INDEX IF NOT EXISTS ix_transferencias_destino ON transferencias(cli_destino_id, created_at DESC);
CREATE INDEX IF NOT EXISTS ix_transferencias_estado ON transferencias(estado_actual);


-- =========================================
-- 5) CATÁLOGO DE ESTADOS (opcional pero ordena)
-- (útil si quieres codificar estados y severidades)
-- =========================================
CREATE TABLE IF NOT EXISTS transfer_estado_catalogo (
  est_code          TEXT PRIMARY KEY,     -- ej: "VALID_OK", "BALANCE_INSUF", "APPLIED"
  descripcion       TEXT NOT NULL,
  severidad         TEXT NOT NULL DEFAULT 'info' CHECK (severidad IN ('info','warning','error','critical')),
  aplica_saldos     BOOLEAN NOT NULL DEFAULT FALSE, -- TRUE cuando ese evento “aplica” débitos/créditos
  created_at        TIMESTAMPTZ NOT NULL DEFAULT now()
);


-- ======================================
-- 6) LOG / EVENTOS DE TRANSFERENCIA
-- (tu “tabla estados tipo log”)
-- ======================================
CREATE TABLE IF NOT EXISTS transferencias_log (
  log_id            BIGSERIAL PRIMARY KEY,

  tra_id            BIGINT NOT NULL REFERENCES transferencias(tra_id) ON DELETE CASCADE,

  -- Resultado del evento
  ok                BOOLEAN NOT NULL DEFAULT FALSE,   -- tu "estado true/false"
  est_code          TEXT REFERENCES transfer_estado_catalogo(est_code),

  -- Mensajería de error/diagnóstico
  error_code        TEXT,  -- ej: "INSUFFICIENT_FUNDS"
  error_msg         TEXT,

  -- Para auditoría/debug interno
  detalle           JSONB,

  created_at        TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS ix_transferencias_log_tra_id ON transferencias_log(tra_id, created_at DESC);
CREATE INDEX IF NOT EXISTS ix_transferencias_log_ok ON transferencias_log(ok, created_at DESC);
