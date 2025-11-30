# 17) Tupla hashable como clave en dict
costos = {
    (0, 0): 10,
    (0, 1): 20,
    (1, 0): 15,
}

print(costos[(0, 1)])
