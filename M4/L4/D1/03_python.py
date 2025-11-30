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
