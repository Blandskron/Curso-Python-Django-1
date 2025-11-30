# 25) frozenset dentro de otro set
grupo1 = frozenset({1, 2, 3})
grupo2 = frozenset({2, 3, 4})

coleccion = {grupo1, grupo2}
print(coleccion)
