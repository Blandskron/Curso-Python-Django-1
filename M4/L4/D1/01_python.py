# Ejemplo 1: Herencia simple y sobrescritura

class Persona:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def presentarse(self) -> str:
        return f"Soy {self.nombre}"


class Estudiante(Persona):
    def __init__(self, nombre: str, carrera: str):
        super().__init__(nombre)
        self.carrera = carrera

    def presentarse(self) -> str:
        return f"Soy {self.nombre} y estudio {self.carrera}"
