# =====================================
# Ejemplo 6: Atributos público, protegido y privado (__mangling)
# =====================================

class Cuenta:
    def __init__(self, numero, saldo):
        self.numero = numero        # público
        self._saldo = saldo         # "protegido"
        self.__pin = "1234"         # privado (name mangling)

    def mostrar_pin_seguro(self):
        print("*" * len(self.__pin))

cuenta = Cuenta("001", 100)
cuenta._saldo += 50        # posible pero no recomendado
cuenta.mostrar_pin_seguro()
# acceso "forzado" al privado: cuenta._Cuenta__pin
