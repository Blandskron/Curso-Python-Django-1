# 43) Función asignada dinámicamente
def comportamiento_a():
    return "A"

def comportamiento_b():
    return "B"

accion = comportamiento_a
print(accion())

accion = comportamiento_b
print(accion())
