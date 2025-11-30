# Ejemplo 25: Composición Carro -> Motor
class Motor:
    def __init__(self, potencia_hp: int):
        self.potencia_hp = potencia_hp

class Carro:
    def __init__(self, modelo: str, potencia_hp: int):
        self.modelo = modelo
        self.motor = Motor(potencia_hp)  # creado adentro
