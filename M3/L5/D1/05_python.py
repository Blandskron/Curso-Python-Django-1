# 5) Listas: eliminar elementos
datos = ["a", "b", "c", "d", "e"]

x = datos.pop()        # quita último
y = datos.pop(1)       # quita en índice 1
datos.remove("c")      # quita por valor
del datos[0]           # elimina por índice
datos.clear()          # deja la lista vacía
