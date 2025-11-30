# Ejemplo 33: Manejo de KeyboardInterrupt explícito

def bucle_infinito() -> None:
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Ejecución interrumpida por el usuario")
