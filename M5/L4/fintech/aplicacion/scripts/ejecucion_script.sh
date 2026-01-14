# 1) Guardar como fintech_actions.sh
# 2) Dar permisos (Linux/Mac/WSL)
chmod +x ./scripts/fintech_actions.sh

# 3) Ejecutar 100 acciones
./scripts/fintech_actions.sh

# Ejecutar 300 acciones
ACTIONS=300 ./scripts/fintech_actions.sh

# Reproducible (mismo SEED)
SEED=123 ACTIONS=100 ./scripts/fintech_actions.sh
