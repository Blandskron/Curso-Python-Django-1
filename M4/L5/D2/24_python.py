# Ejemplo 24: Uso peligroso de 'except:' desnudo

def ocultar_todo() -> None:
    try:
        1 / 0
    except:  # no recomendado
        print("Algo falló, pero no sabemos qué")
