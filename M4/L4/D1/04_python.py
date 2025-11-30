# Ejemplo 3: Herencia jerárquica

class Animal:
    def sonido(self) -> str:
        return "Sonido genérico"


class Perro(Animal):
    def sonido(self) -> str:
        return "Guau"


class Gato(Animal):
    def sonido(self) -> str:
        return "Miau"

# Ejemplo 4: Polimorfismo con una función genérica

def hacer_sonar(animal: Animal) -> None:
    print(animal.sonido())


animales: list[Animal] = [Perro(), Gato(), Animal()]
for a in animales:
    hacer_sonar(a)
