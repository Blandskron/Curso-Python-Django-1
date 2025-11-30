# Ejemplo 2: Clase (plantilla) vs Objeto (instancia)

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

# Clase: definición única
# Objetos: múltiples instancias con identidades distintas
u1 = Usuario("Ana")
u2 = Usuario("Ana")

u1.saludar()
u2.saludar()
print(id(u1), id(u2))  # identidades distintas

