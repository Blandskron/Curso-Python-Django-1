# 13) for con break: búsqueda lineal
valores = [3, 8, 10, 2, 7]
objetivo = 10

for v in valores:
    if v == objetivo:
        print("Encontrado:", v)
        break
else:
    print("No se encontró el valor")
