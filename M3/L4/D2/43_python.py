# 43) Uso de while para consumir elementos de una lista
cola = ["tarea1", "tarea2", "tarea3"]

while cola:
    tarea = cola.pop(0)
    print("Ejecutando:", tarea)
print("Cola vacía")
