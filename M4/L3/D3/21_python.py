# Ejemplo 21: Multiplicidad 1..* (Equipo -> 11 Jugadores)
class Jugador:
    def __init__(self, nombre: str, dorsal: int):
        self.nombre = nombre
        self.dorsal = dorsal

class Equipo:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.jugadores: list[Jugador] = []

    def agregar_jugador(self, jugador: Jugador) -> None:
        self.jugadores.append(jugador)
