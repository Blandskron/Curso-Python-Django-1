# Ejemplo 9: Ciclo de vida del objeto

class RecursoTemporal:
    def __init__(self):
        print("Recurso creado")

    def usar(self):
        print("Usando recurso")

    def __del__(self):
        # en CPython suele llamarse al recolectar
        print("Recurso destruido")

def crear_y_usar():
    r = RecursoTemporal()
    r.usar()

crear_y_usar()