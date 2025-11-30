# Ejemplo 28: isinstance preservando polimorfismo

class Animal:
    def sonido(self) -> str:
        return "Sonido genérico"


class Perro(Animal):
    def sonido(self) -> str:
        return "Guau"


def procesar_animal_polimorfico(animal: Animal) -> str:
    if isinstance(animal, Animal):
        return animal.sonido()
    return "Desconocido"
