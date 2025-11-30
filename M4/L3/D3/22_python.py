# Ejemplo 22: Asociación usando diccionario (Empresa -> Empleado)
class Empleado:
    def __init__(self, rut: str, nombre: str):
        self.rut = rut
        self.nombre = nombre

class Empresa:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.empleados: dict[str, Empleado] = {}

    def contratar(self, empleado: Empleado) -> None:
        self.empleados[empleado.rut] = empleado
