# 19_python.py
# while con entrada de usuario (sentinela)

total = 0
cantidad = 0

while True:
    entrada = input("Ingresa un número o 'fin' para terminar: ")
    if entrada == "fin":
        break
    numero = float(entrada)
    total += numero
    cantidad += 1

if cantidad > 0:
    promedio = total / cantidad
    print("Total:", total)
    print("Promedio:", promedio)
else:
    print("No se ingresaron números")
