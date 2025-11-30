# Ejemplo 16: Herencia UML (Person <- Estudiante)
class Person:
    def __init__(self, nombre: str):
        self.nombre = nombre

class Student(Person):
    def __init__(self, nombre: str, matricula: str):
        super().__init__(nombre)
        self.matricula = matricula
