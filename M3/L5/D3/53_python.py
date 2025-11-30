# 53) Matriz como lista de listas + función vecinos válidos (grid)
matriz = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 0, 1],
]

filas = len(matriz)
cols = len(matriz[0])

def vecinos(i, j):
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di == 0 and dj == 0:
                continue
            ni, nj = i + di, j + dj
            if 0 <= ni < filas and 0 <= nj < cols:
                yield ni, nj

for i in range(filas):
    for j in range(cols):
        print((i, j), "vecinos:", list(vecinos(i, j)))
