# Ejemplo 3: Atributos (posibilidad) vs Estado (valores actuales)

class Semaforo:
    def __init__(self):
        self.color = "rojo"  # atributo con estado inicial

    def cambiar_a_verde(self):
        self.color = "verde"  # mutación de estado

    def cambiar_a_amarillo(self):
        self.color = "amarillo"

s = Semaforo()
print(s.color)
s.cambiar_a_verde()
print(s.color)