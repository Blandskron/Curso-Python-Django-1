# Condiciones compuestas largas descompuestas en variables intermedias

saldo = 1200
tiene_tarjeta_credito = True
historial_bueno = False
es_cliente_vip = True

# Versión compacta difícil de leer
if (saldo > 1000 and tiene_tarjeta_credito and historial_bueno) or es_cliente_vip:
    print("Aprobado para crédito (versión compacta)")

# Versión descompuesta y más legible
tiene_saldo_suficiente = saldo > 1000
cumple_condiciones_normales = tiene_saldo_suficiente and tiene_tarjeta_credito and historial_bueno
cumple_condicion_vip = es_cliente_vip

if cumple_condiciones_normales or cumple_condicion_vip:
    print("Aprobado para crédito (versión descompuesta)")