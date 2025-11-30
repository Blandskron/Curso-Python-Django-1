# Ejemplo 7: Composición (objetos dentro de objetos)

class Motor:
    def __init__(self, potencia_hp: int):
        self.potencia_hp = potencia_hp

    def encender(self):
        print("Motor encendido")

class Coche:
    def __init__(self, marca, motor: Motor):
        self.marca = marca
        self.motor = motor  # composición

    def arrancar(self):
        self.motor.encender()
        print(f"{self.marca} en marcha")

motor_pequeno = Motor(90)
auto = Coche("Toyota", motor_pequeno)
auto.arrancar()