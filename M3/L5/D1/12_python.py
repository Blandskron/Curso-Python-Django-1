# 12) Listas: ordenar con sort() y sorted()
numeros = [5, 3, 8, 1, 2]

numeros.sort()              # in-place
print(numeros)

numeros_desc = sorted(numeros, reverse=True)
print(numeros_desc)
