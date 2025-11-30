# 36) Diccionario como matriz dispersa (sparse matrix)
matriz_dispersa = {}
matriz_dispersa[(0, 1)] = 10
matriz_dispersa[(100, 200)] = 5

print(matriz_dispersa.get((0, 1), 0))
print(matriz_dispersa.get((1, 1), 0))  # 0 si no existe
