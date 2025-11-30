# 26) Salir de múltiples bucles anidados usando función + return
def buscar_en_matriz(matriz, objetivo):
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor == objetivo:
                return i, j  # termina todos los bucles
    return None  # no encontrado

m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(buscar_en_matriz(m, 5))   # (1, 1)
print(buscar_en_matriz(m, 10))  # None
