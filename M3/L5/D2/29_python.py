# 29) Dict: eliminar elementos
inventario = {"p1": 10, "p2": 5, "p3": 0}

cantidad_p2 = inventario.pop("p2")   # devuelve 5
clave, valor = inventario.popitem()  # último par insertado
del inventario["p3"]
inventario.clear()
