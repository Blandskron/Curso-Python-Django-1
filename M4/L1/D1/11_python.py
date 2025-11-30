# Ejemplo 11: Encapsulamiento con propiedades

class CuentaBancaria:
    def __init__(self, saldo_inicial: float):
        self.__saldo = float(saldo_inicial)  # privado

    @property
    def saldo(self):
        # sólo lectura pública
        return self.__saldo

    def depositar(self, cantidad: float):
        if cantidad <= 0:
            raise ValueError("Cantidad inválida")
        self.__saldo += cantidad

    def retirar(self, cantidad: float):
        if cantidad <= 0:
            raise ValueError("Cantidad inválida")
        if cantidad > self.__saldo:
            raise ValueError("Fondos insuficientes")
        self.__saldo -= cantidad

cuenta = CuentaBancaria(100)
cuenta.depositar(50)
cuenta.retirar(20)
print(cuenta.saldo)