# 27) Clasificación de lecturas de temperatura (for + if/elif/else)
lecturas = [22, 25, 30, 18, 40, -5]
alertas = []
normales = []

for temp in lecturas:
    if temp > 35:
        alertas.append(f"ALTA: {temp}")
    elif temp < 0:
        alertas.append(f"BAJA: {temp}")
    else:
        normales.append(temp)

print("Alertas:", alertas)
print("Normales:", normales)
