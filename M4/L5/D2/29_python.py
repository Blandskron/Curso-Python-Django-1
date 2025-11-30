# Ejemplo 29: Excepción híbrida con herencia múltiple

class ErrorA(Exception):
    pass

class ErrorB(Exception):
    pass

class ErrorHibrido(ErrorA, ErrorB):
    pass

def lanzar_hibrido() -> None:
    raise ErrorHibrido("fallo combinado")
