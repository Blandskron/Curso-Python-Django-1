# 11) Actualizar elementos de una matriz
filas, columnas = 3, 3
matriz = [[0] * columnas for _ in range(filas)]
"""
matriz = []
for n in range(filas):
    matriz.append([0] * columnas)
"""
for i in range(filas):
    for j in range(columnas):
        matriz[i][j] = i + j

#[[0, 1, 2], [1, 2, 3], [2, 3, 4]]
#[[0, 1, 2], [1, 2, 3], [2, 3, 4]]
print(matriz)