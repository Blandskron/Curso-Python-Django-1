# Ejemplo 19: Context manager personalizado simple

class RecursoDemo:
    def __enter__(self):
        print("Abriendo recurso")
        return self

    def __exit__(self, tipo, valor, traza):
        print("Cerrando recurso")
        # False => propaga excepción si existe
        return False

    def usar(self) -> None:
        print("Usando recurso")


def usar_recurso() -> None:
    with RecursoDemo() as r:
        r.usar()
