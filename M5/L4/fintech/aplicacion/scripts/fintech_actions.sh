#!/usr/bin/env bash
# fintech_actions.sh
# Ejecuta ~100 acciones aleatorias usando tu app.py (init, create-client, balance, transfer, tx)
# Requisitos:
# - python en PATH
# - app.py en el mismo directorio (o ajusta APP)
# - .env configurado para la DB
#
# Uso:
#   bash fintech_actions.sh
#   ACTIONS=200 bash fintech_actions.sh
#   SEED=123 bash fintech_actions.sh

set -euo pipefail

APP="${APP:-python app.py}"
ACTIONS="${ACTIONS:-100}"
SEED="${SEED:-$RANDOM}"
LOG_DIR="${LOG_DIR:-./logs}"
mkdir -p "$LOG_DIR"

RUN_ID="$(date +%Y%m%d_%H%M%S)_$SEED"
LOG_FILE="$LOG_DIR/run_$RUN_ID.log"

# Para usar $RANDOM de forma reproducible (bash no siempre es determinista),
# hacemos un PRNG simple:
prng() {
  # LCG: X_{n+1} = (aX + c) mod m
  # m = 2^31
  SEED=$(( (1103515245 * SEED + 12345) & 0x7fffffff ))
  echo "$SEED"
}

rand_int() {
  # rand_int MIN MAX  (inclusive)
  local min="$1" max="$2"
  local r
  r="$(prng)"
  echo $(( min + (r % (max - min + 1)) ))
}

rand_email() {
  local n="$1"
  echo "cliente${n}@fintech.local"
}

rand_name() {
  local n="$1"
  echo "Cliente ${n}"
}

echo "=== RUN $RUN_ID ===" | tee "$LOG_FILE"
echo "ACTIONS=$ACTIONS SEED=$SEED" | tee -a "$LOG_FILE"

echo ">> init" | tee -a "$LOG_FILE"
$APP init | tee -a "$LOG_FILE"

# Mantendremos un rango conocido de clientes (1..MAX_CLIENT_ID_EST)
# Tú ya insertaste 20 en SQL, pero igual lo hacemos dinámico:
MAX_CLIENT_ID_EST="${MAX_CLIENT_ID_EST:-20}"
NEXT_CLIENT_ID_GUESS=$((MAX_CLIENT_ID_EST + 1))

# Guardamos referencias creadas para luego hacer tx --ref
declare -a REFS=()

# Probabilidades (0-100)
P_CREATE=25   # 25% crear cliente
P_BALANCE=25  # 25% consultar saldo
P_TRANSFER=45 # 45% transferencias
P_TX=5        # 5% consultar tx por ref (si hay)

# Helper: corre comando y loguea
run_cmd() {
  local label="$1"; shift
  echo ">> $label: $*" | tee -a "$LOG_FILE"
  # no rompemos todo si una transferencia falla por saldo, etc.
  set +e
  "$@" | tee -a "$LOG_FILE"
  local rc=${PIPESTATUS[0]}
  set -e
  if [[ $rc -ne 0 ]]; then
    echo "!! Command failed (rc=$rc): $*" | tee -a "$LOG_FILE"
  fi
  echo "" | tee -a "$LOG_FILE"
  return 0
}

for ((i=1; i<=ACTIONS; i++)); do
  roll="$(rand_int 1 100)"

  if [[ $roll -le $P_CREATE ]]; then
    # CREATE CLIENT
    cid="$NEXT_CLIENT_ID_GUESS"
    name="$(rand_name "$cid")"
    email="$(rand_email "$cid")"
    run_cmd "action#$i create-client" bash -lc "$APP create-client --name \"$name\" --email \"$email\""
    MAX_CLIENT_ID_EST=$((MAX_CLIENT_ID_EST + 1))
    NEXT_CLIENT_ID_GUESS=$((NEXT_CLIENT_ID_GUESS + 1))

  elif [[ $roll -le $((P_CREATE + P_BALANCE)) ]]; then
    # BALANCE
    cid="$(rand_int 1 "$MAX_CLIENT_ID_EST")"
    run_cmd "action#$i balance" bash -lc "$APP balance --client-id $cid"

  elif [[ $roll -le $((P_CREATE + P_BALANCE + P_TRANSFER)) ]]; then
    # TRANSFER
    from="$(rand_int 1 "$MAX_CLIENT_ID_EST")"
    to="$(rand_int 1 "$MAX_CLIENT_ID_EST")"
    # evita self-transfer (tu DB tiene CHECK)
    if [[ "$to" -eq "$from" ]]; then
      to=$(( (to % MAX_CLIENT_ID_EST) + 1 ))
      if [[ "$to" -eq "$from" ]]; then
        to=1
      fi
    fi

    amount="$(rand_int 1 2500)"  # montos chicos para no quebrar saldos demasiado rápido
    ref="TRX_PY_${RUN_ID}_$(printf '%04d' "$i")"
    note="Auto action $i"

    REFS+=("$ref")
    run_cmd "action#$i transfer" bash -lc "$APP transfer --from $from --to $to --amount $amount --ref \"$ref\" --note \"$note\""

  else
    # TX (si hay refs)
    if [[ ${#REFS[@]} -gt 0 ]]; then
      idx="$(rand_int 0 $((${#REFS[@]} - 1)) )"
      ref="${REFS[$idx]}"
      run_cmd "action#$i tx" bash -lc "$APP tx --ref \"$ref\""
    else
      cid="$(rand_int 1 "$MAX_CLIENT_ID_EST")"
      run_cmd "action#$i balance (fallback)" bash -lc "$APP balance --client-id $cid"
    fi
  fi
done

echo "=== DONE RUN $RUN_ID ===" | tee -a "$LOG_FILE"
echo "Log: $LOG_FILE"
