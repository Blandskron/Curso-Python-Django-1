# 19) Uso de enumerate: índice + valor
nombres = ["Ana", "Luis", "Marta"]

# Anti-patrón clásico:
for i in range(len(nombres)):
    print("Mal estilo:", i, nombres[i])

# Estilo Pythonico:
for i, nombre in enumerate(nombres):
    print("Bien:", i, nombre)
