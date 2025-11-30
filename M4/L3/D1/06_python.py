# Ejemplo 6: Asociación 1 a muchos (Curso -> Estudiante)
class Estudiante:
    def __init__(self, nombre: str):
        self.nombre = nombre

class Curso:
    def __init__(self, titulo: str):
        self.titulo = titulo
        self.estudiantes: list[Estudiante] = []  # multiplicidad *

    def inscribir(self, estudiante: Estudiante) -> None:
        self.estudiantes.append(estudiante)
