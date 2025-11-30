# Ejemplo 2: Herencia multinivel

class Vehiculo:
    def mover(self) -> str:
        return "El vehículo se mueve"


class VehiculoTerrestre(Vehiculo):
    def mover(self) -> str:
        return "El vehículo se mueve por tierra"


class Coche(VehiculoTerrestre):
    def mover(self) -> str:
        return "El coche avanza por la carretera"


class CocheDeportivo(Coche):
    def mover(self) -> str:
        return "El coche deportivo acelera a gran velocidad"
