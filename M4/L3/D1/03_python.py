# Ejemplo 3: Atributo de clase vs atributo de instancia
class Sesion:
    sesiones_activas = 0  # estático (subrayado en UML)

    def __init__(self, usuario: str):
        self.usuario = usuario
        Sesion.sesiones_activas += 1
