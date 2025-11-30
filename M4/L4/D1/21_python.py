# Ejemplo 21: Composición en lugar de herencia

class Motor:
    def encender(self) -> str:
        return "Motor encendido"


class CocheConMotor:
    def __init__(self):
        self.motor = Motor()

    def arrancar(self) -> str:
        return self.motor.encender()
