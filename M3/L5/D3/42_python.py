# 42) Pila de deshacer/rehacer usando listas
acciones = []
acciones.append("escribir A")
acciones.append("escribir B")

ultima = acciones.pop()      # deshacer
acciones.append("escribir C")
print(acciones)
