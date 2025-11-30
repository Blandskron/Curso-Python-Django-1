# 11) Actualizar elementos de una matriz
filas, columnas = 3, 3
matriz = [[0] * columnas for _ in range(filas)]

for i in range(filas):
    for j in range(columnas):
        matriz[i][j] = i + j

print(matriz)
