# 48) Recorrer lista de listas (matriz) con for anidado y enumerate
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

for i, fila in enumerate(matriz):
    for j, valor in enumerate(fila):
        print(f"matriz[{i}][{j}] = {valor}")
