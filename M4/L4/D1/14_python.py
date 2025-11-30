# Ejemplo 14: isinstance con jerarquía

class Animal:
    def sonido(self) -> str:
        return "Sonido genérico"


class Perro(Animal):
    def sonido(self) -> str:
        return "Guau"


def contar_perros(animales: list[Animal]) -> int:
    return sum(isinstance(a, Perro) for a in animales)
