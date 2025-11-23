# Ejemplo 23: Herencia y polimorfismo
class Animal:
    def hablar(self):
        print("Sonido genérico")  # Método base

class Perro(Animal):
    def hablar(self):
        print("Guau")             # Sobrescribe el método

class Gato(Animal):
    def hablar(self):
        print("Miau")             # Otra implementación

animales = [Perro(), Gato()]
for a in animales:
    a.hablar()                    # Llama a la versión adecuada (polimorfismo)
