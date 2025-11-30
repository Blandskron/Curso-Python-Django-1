# 30) continue en for: filtrar transacciones inválidas
def procesar_pago(tx):
    print("Procesando pago:", tx)

transacciones = [100, -50, 0, 200, None, 50]
for tx in transacciones:
    if tx is None or tx <= 0:
        continue
    procesar_pago(tx)
