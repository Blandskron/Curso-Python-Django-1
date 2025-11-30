# 59) Uso de zip para transponer matriz (listas de listas)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
]

transpuesta = [list(fila) for fila in zip(*matriz)]
print(transpuesta)
