# Ejemplo 14: Biblioteca registrando socios (agregación)
class Socio:
    def __init__(self, nombre: str, numero: int):
        self.nombre = nombre
        self.numero = numero

class BibliotecaSocios:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self._socios: list[Socio] = []

    def registrar_socio(self, socio: Socio) -> None:
        if socio not in self._socios:
            self._socios.append(socio)
