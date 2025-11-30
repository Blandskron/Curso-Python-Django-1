# 4) Listas: creación y operaciones básicas
numeros = [10, 20, 30]
vacia = []

numeros.append(40)
numeros.extend([50, 60])
numeros.insert(0, 5)   # inserta al inicio

print(numeros)         # [5, 10, 20, 30, 40, 50, 60]
print(numeros[0])      # acceso por índice
print(numeros[-1])     # acceso desde el final
print(numeros[2:5])    # slicing
