# Ejemplo 31: Herencia de excepción personalizada

class ErrorDominio(Exception):
    pass


class ErrorPagoInvalido(ErrorDominio):
    pass
