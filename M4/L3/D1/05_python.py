# Ejemplo 5: Asociación 1 a 1 (Persona -> Direccion)
class Direccion:
    def __init__(self, calle: str, ciudad: str):
        self.calle = calle
        self.ciudad = ciudad

class Cliente:
    def __init__(self, nombre: str, direccion: Direccion):
        self.nombre = nombre
        self.direccion = direccion    # mantiene referencia
