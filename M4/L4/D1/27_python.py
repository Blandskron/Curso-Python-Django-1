# Ejemplo 27: type() rompiendo polimorfismo

class Animal:
    def sonido(self) -> str:
        return "Sonido genérico"


class Perro(Animal):
    def sonido(self) -> str:
        return "Guau"


def procesar_animal(animal: Animal) -> str:
    if type(animal) is Animal:  # evita subclases
        return "Animal genérico"
    return "Otro tipo de animal"
