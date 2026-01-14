#!/usr/bin/env python3
"""
Fintech Gamificada (DB) — Cliente + Transferencias desde consola
- Python puro (sin frameworks)
- PostgreSQL con psycopg (v3)
- Crea clientes (saldo inicial lo hace el trigger)
- Crea transferencias (saldo se aplica SOLO con INSERT gracias a tus triggers)

Instalación:
  pip install "psycopg[binary]"

Uso:
  python app.py init
  python app.py create-client --name "Cliente X" --email "x@fintech.local"
  python app.py balance --client-id 1
  python app.py transfer --from 1 --to 2 --amount 500 --ref TRX_PY_0001 --note "Pago python"
  python app.py tx --ref TRX_PY_0001
"""

from __future__ import annotations

import argparse
import os
import sys
from decimal import Decimal, InvalidOperation
from dotenv import load_dotenv


import psycopg2
import psycopg2.extras


load_dotenv()

# =========================
# Config DB (ENV)
# =========================
def get_dsn() -> str:
    """
    Preferencia:
    - DATABASE_URL (dsn completo)
    o variables separadas:
      PGHOST, PGPORT, PGDATABASE, PGUSER, PGPASSWORD
    """
    dsn = os.getenv("DATABASE_URL")
    if dsn:
        return dsn

    host = os.getenv("PGHOST", "localhost")
    port = os.getenv("PGPORT", "5432")
    db = os.getenv("PGDATABASE", "postgres")
    user = os.getenv("PGUSER", "postgres")
    pw = os.getenv("PGPASSWORD", "")

    # DSN estilo libpq
    return f"host={host} port={port} dbname={db} user={user} password={pw}"


def connect():
    return psycopg2.connect(get_dsn())


# =========================
# Helpers
# =========================
def require_positive_decimal(value: str) -> Decimal:
    try:
        d = Decimal(value)
    except InvalidOperation:
        raise SystemExit(f"Monto inválido: {value!r}")
    if d <= 0:
        raise SystemExit("El monto debe ser > 0")
    return d


def ensure_activo_coin(conn) -> int:
    """
    Asegura que exista 'COIN' en activos y retorna act_id.
    """
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute(
            """
            INSERT INTO activos (codigo, nombre, decimales, activo)
            VALUES ('COIN','Moneda interna',2,TRUE)
            ON CONFLICT (codigo) DO NOTHING
            """
        )
        cur.execute("SELECT act_id FROM activos WHERE codigo='COIN'")
        row = cur.fetchone()
        if not row:
            raise RuntimeError("No se pudo obtener act_id para COIN")
        return int(row["act_id"])


# =========================
# Commands
# =========================
def cmd_init(_args):
    dsn = get_dsn()
    with connect() as conn:
        act_id = ensure_activo_coin(conn)
        conn.commit()
    print(f"OK: activo COIN listo (act_id={act_id})")
    print("Tip: define env vars PGHOST/PGPORT/PGDATABASE/PGUSER/PGPASSWORD o DATABASE_URL")


def cmd_create_client(args):
    with connect() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(
                """
                INSERT INTO clientes (nombre, email, estado)
                VALUES (%s, %s, 'activo')
                RETURNING cli_id, cli_uuid, nombre, email
                """,
                (args.name, args.email),
            )
            client = cur.fetchone()

            # El trigger AFTER INSERT ON clientes crea cuenta con 10000 automáticamente
            cur.execute(
                """
                SELECT c.cli_id, a.codigo AS activo, c.saldo
                FROM cuentas c
                JOIN activos a ON a.act_id = c.act_id
                WHERE c.cli_id = %s
                ORDER BY c.act_id
                """,
                (client["cli_id"],),
            )
            cuentas = cur.fetchall()
            conn.commit()

    print("CLIENTE CREADO:")
    print(f"  cli_id   : {client['cli_id']}")
    print(f"  cli_uuid : {client['cli_uuid']}")
    print(f"  nombre   : {client['nombre']}")
    print(f"  email    : {client['email']}")
    print("CUENTAS:")
    for c in cuentas:
        print(f"  - {c['activo']}: {c['saldo']}")


def cmd_balance(args):
    with connect() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:

            cur.execute(
                """
                SELECT cl.cli_id, cl.nombre, a.codigo AS activo, c.saldo, c.updated_at
                FROM cuentas c
                JOIN clientes cl ON cl.cli_id = c.cli_id
                JOIN activos a ON a.act_id = c.act_id
                WHERE c.cli_id = %s
                ORDER BY a.codigo
                """,
                (args.client_id,),
            )
            rows = cur.fetchall()

    if not rows:
        print("No se encontró cliente/cuentas para ese cli_id.")
        return

    print(f"BALANCE cliente {rows[0]['cli_id']} — {rows[0]['nombre']}")
    for r in rows:
        print(f"  {r['activo']}: {r['saldo']} (updated_at={r['updated_at']})")


def cmd_transfer(args):
    monto = require_positive_decimal(args.amount)

    with connect() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:

            act_id = ensure_activo_coin(conn)

            # Inserta transferencia en estado 'creada'
            # Con tu trigger AFTER INSERT ON transferencias:
            #   => inserta CONFIRMED en transferencias_log
            # Con tu trigger AFTER INSERT ON transferencias_log:
            #   => aplica saldos y cambia estado_actual a 'aplicada' o 'fallida'
            cur.execute(
                """
                INSERT INTO transferencias
                (cli_origen_id, cli_destino_id, act_id, monto, estado_actual, referencia, nota)
                VALUES
                (%s, %s, %s, %s, 'creada', %s, %s)
                RETURNING tra_id, tra_uuid, estado_actual
                """,
                (args.from_id, args.to_id, act_id, monto, args.ref, args.note),
            )
            tx = cur.fetchone()

            # Refrescamos estado (porque triggers lo pueden cambiar dentro de la misma transacción)
            cur.execute(
                """
                SELECT tra_id, cli_origen_id, cli_destino_id, monto, estado_actual, updated_at
                FROM transferencias
                WHERE tra_id = %s
                """,
                (tx["tra_id"],),
            )
            tx2 = cur.fetchone()

            # Últimos logs
            cur.execute(
                """
                SELECT log_id, ok, est_code, error_code, error_msg, created_at
                FROM transferencias_log
                WHERE tra_id = %s
                ORDER BY log_id DESC
                LIMIT 5
                """,
                (tx["tra_id"],),
            )
            logs = cur.fetchall()

            # Saldos origen/destino
            cur.execute(
                """
                SELECT c.cli_id, cl.nombre, c.saldo
                FROM cuentas c
                JOIN clientes cl ON cl.cli_id = c.cli_id
                WHERE c.act_id = %s AND c.cli_id IN (%s, %s)
                ORDER BY c.cli_id
                """,
                (act_id, args.from_id, args.to_id),
            )
            balances = cur.fetchall()

            conn.commit()

    print("TRANSFERENCIA CREADA:")
    print(f"  tra_id    : {tx2['tra_id']}")
    print(f"  origen    : {tx2['cli_origen_id']}")
    print(f"  destino   : {tx2['cli_destino_id']}")
    print(f"  monto     : {tx2['monto']}")
    print(f"  estado    : {tx2['estado_actual']}")
    print(f"  updated_at: {tx2['updated_at']}")
    print("LOGS (últimos 5):")
    for l in logs:
        print(f"  - log_id={l['log_id']} ok={l['ok']} est={l['est_code']} err={l['error_code']} msg={l['error_msg']}")
    print("SALDOS:")
    for b in balances:
        print(f"  - {b['cli_id']} {b['nombre']}: {b['saldo']}")


def cmd_tx(args):
    with connect() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(
                """
                SELECT tra_id, tra_uuid, cli_origen_id, cli_destino_id, monto, estado_actual, referencia, created_at, updated_at
                FROM transferencias
                WHERE referencia = %s
                """,
                (args.ref,),
            )
            tx = cur.fetchone()

            if not tx:
                print("No existe transferencia con esa referencia.")
                return

            cur.execute(
                """
                SELECT log_id, ok, est_code, error_code, error_msg, created_at
                FROM transferencias_log
                WHERE tra_id = %s
                ORDER BY log_id
                """,
                (tx["tra_id"],),
            )
            logs = cur.fetchall()

    print("TRANSFERENCIA:")
    for k in ["tra_id","tra_uuid","cli_origen_id","cli_destino_id","monto","estado_actual","referencia","created_at","updated_at"]:
        print(f"  {k}: {tx[k]}")
    print("LOG:")
    for l in logs:
        print(f"  - log_id={l['log_id']} ok={l['ok']} est={l['est_code']} err={l['error_code']} msg={l['error_msg']} at={l['created_at']}")


# =========================
# CLI
# =========================
def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="fintech-db-cli", description="CLI Python puro para tu DB gamificada")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("init", help="Asegura activo COIN (si no existe)")
    s.set_defaults(func=cmd_init)

    s = sub.add_parser("create-client", help="Crea un cliente (saldo inicial lo crea el trigger)")
    s.add_argument("--name", required=True)
    s.add_argument("--email", required=True)
    s.set_defaults(func=cmd_create_client)

    s = sub.add_parser("balance", help="Ver saldo de un cliente")
    s.add_argument("--client-id", type=int, required=True)
    s.set_defaults(func=cmd_balance)

    s = sub.add_parser("transfer", help="Crear transferencia (triggers aplican saldo automáticamente)")
    s.add_argument("--from", dest="from_id", type=int, required=True)
    s.add_argument("--to", dest="to_id", type=int, required=True)
    s.add_argument("--amount", required=True, help="monto > 0 (ej: 500 o 10.5)")
    s.add_argument("--ref", required=True, help="referencia única (ej: TRX_PY_0001)")
    s.add_argument("--note", default="")
    s.set_defaults(func=cmd_transfer)

    s = sub.add_parser("tx", help="Ver detalle de una transferencia por referencia")
    s.add_argument("--ref", required=True)
    s.set_defaults(func=cmd_tx)

    return p


def main(argv: list[str]) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
