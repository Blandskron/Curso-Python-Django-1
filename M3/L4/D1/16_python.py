# 16) for + acumuladores: máximo en una lista
numeros = [3, 41, 12, 9, 74, 15]
mayor = None

for valor in numeros:
    if mayor is None or valor > mayor:
        mayor = valor

print("Mayor encontrado:", mayor)
