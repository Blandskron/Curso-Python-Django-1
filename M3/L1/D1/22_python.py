# Ejemplo 22: Clase simple y método de instancia (POO)
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")

p = Persona("Ana", 30)
p.saludar()
