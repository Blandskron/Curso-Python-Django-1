# Ejemplo 29: Excepción híbrida con herencia múltiple

class ErrorA(Exception):
    pass

class ErrorB(Exception):
    pass

class ErrorHibrido(ErrorA, ErrorB):
    pass

def lanzar_hibrido() -> None:
    raise ErrorHibrido("fallo combinado")

# Ejemplo 30: Captura de excepción híbrida respetando MRO

def capturar_hibrido() -> None:
    try:
        lanzar_hibrido()
    except ErrorA:
        print("Capturado como ErrorA")
    except ErrorB:
        print("Capturado como ErrorB")
