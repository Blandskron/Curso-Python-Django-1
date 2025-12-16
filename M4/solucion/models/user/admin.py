from usuario import Usuario

class Admin(Usuario):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)
