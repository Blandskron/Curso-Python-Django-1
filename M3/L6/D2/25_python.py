# 25) Lambda con sorted
datos = [(1, 'b'), (2, 'a'), (3, 'c')]
ordenado = sorted(datos, key=lambda x: x[1])
print(ordenado)
