class Abuelo:
    def __init__(self, apellido):
        self.apellido = apellido

    def apellido_abuelo(self):
        return self.apellido

class Hijo(Abuelo):
    def __init__(self, nombre):
        self.nombre = nombre

    def name(self, apellido: Abuelo):
        print(f"Mi nombre es: {self.nombre}, mi apellido es {apellido.apellido_abuelo()}")
    
abuelo = Abuelo("reyes")
abuelo2 = Abuelo("perez")
hijo = Hijo("juan")
hijo2 = Hijo("pedro")
hijo.name(abuelo)
hijo2.name(abuelo2)