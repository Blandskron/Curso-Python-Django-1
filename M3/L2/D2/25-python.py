# 25_python.py
# listas: creación, modificación y slicing

numeros = [1, 2, 3]
numeros.append(4)
numeros.extend([5, 6])
numeros[0] = 100

print("Lista completa:", numeros)
print("Primeros 3:", numeros[:3])
print("Últimos 2:", numeros[-2:])

if 4 in numeros:
    numeros.remove(4)

print("Sin el 4:", numeros)
