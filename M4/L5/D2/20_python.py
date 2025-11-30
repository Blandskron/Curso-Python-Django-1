# Ejemplo 20: Context manager que suprime la excepción

class IgnorarErrores:
    def __enter__(self):
        return self

    def __exit__(self, tipo, valor, traza):
        # True => suprime cualquier excepción
        return True


def demo_ignorar() -> None:
    with IgnorarErrores():
        1 / 0  # no se propaga
