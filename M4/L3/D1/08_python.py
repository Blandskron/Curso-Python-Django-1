# Ejemplo 8: Agregación (Aeropuerto agrega Avion externo)
class Avion:
    def __init__(self, matricula: str):
        self.matricula = matricula

class Aeropuerto:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.aviones: list[Avion] = []

    def recibir_avion(self, avion: Avion) -> None:
        self.aviones.append(avion)  # el avión se creó fuera
