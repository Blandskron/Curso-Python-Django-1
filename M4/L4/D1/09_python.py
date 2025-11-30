# Ejemplo 9: Llamada cooperativa con super() (recomendado)

class PadreCooperativo:
    def __init__(self) -> None:
        super().__init__()
        self.valor = 1


class HijoCooperativo(PadreCooperativo):
    def __init__(self) -> None:
        super().__init__()
        self.valor *= 2
