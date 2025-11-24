# Evaluación de cortocircuito para evitar división por cero

total = 100
divisor = int(input("Ingrese divisor: "))

if divisor != 0 and (total / divisor) > 5:
    print("La división es mayor que 5")
else:
    print("No se cumple la condición o divisor es 0")