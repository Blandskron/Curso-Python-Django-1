# Ejemplo 26: Agregación Carro -> Conductor (Conductor independiente)
class Conductor:
    def __init__(self, nombre: str):
        self.nombre = nombre

class CarroAgregado:
    def __init__(self, modelo: str, conductor: Conductor | None = None):
        self.modelo = modelo
        self.conductor = conductor  # referencia externa opcional
