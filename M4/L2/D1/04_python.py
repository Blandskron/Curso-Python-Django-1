# =====================================
# Ejemplo 4: Composición ("contiene un" fuerte)
# =====================================

class Habitacion:
    def __init__(self, nombre):
        self.nombre = nombre

class Casa:
    def __init__(self, cantidad_habitaciones: int):
        # la casa crea sus propias habitaciones
        self.habitaciones = [Habitacion(f"Habitación {i+1}") for i in range(cantidad_habitaciones)]

    def listar(self):
        for h in self.habitaciones:
            print(h.nombre)

casa = Casa(3)
casa.listar()