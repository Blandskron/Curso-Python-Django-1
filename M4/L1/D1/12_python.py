# Ejemplo 12: Versión sin encapsulamiento (mala) vs con encapsulamiento (mejor)

class CuentaSinEncapsular:
    def __init__(self, saldo):
        self.saldo = saldo  # público

c_mala = CuentaSinEncapsular(100)
c_mala.saldo = -999999  # estado inválido

class CuentaEncapsulada:
    def __init__(self, saldo):
        self.__saldo = saldo

    def set_saldo(self, saldo):
        if saldo < 0:
            raise ValueError("Saldo no puede ser negativo")
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

c_buena = CuentaEncapsulada(100)
# c_buena.set_saldo(-10)  # lanzaría error
print(c_buena.get_saldo())