from ..carrito import Carrito

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = str(nombre)
        self.email = str(email)

class Cliente(Usuario):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)
        self.carrito = Carrito()

class Admin(Usuario):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)
