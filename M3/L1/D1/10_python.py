# Ejemplo 10: Bucle while con break y continue
contador = 0
while True:                   # Bucle infinito controlado por break
    contador += 1
    if contador == 3:
        continue              # Salta el resto de la iteración
    print("contador =", contador)
    if contador >= 5:
        break                 # Rompe el bucle
