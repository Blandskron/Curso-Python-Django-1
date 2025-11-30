# Ejemplo 19: Violación del LSP (no recomendado)

class Ave:
    def emitir_sonido(self) -> str:
        return "Pío"

    def volar(self) -> str:
        return "Estoy volando"


class Avestruz(Ave):
    def volar(self) -> str:
        raise NotImplementedError("Las avestruces no vuelan")  # rompe expectativas

# Ejemplo 20: Diseño alternativo respetando LSP

class AveNoVoladora(Ave):
    def volar(self) -> str:
        return "Camino, no vuelo"


class AvestruzCorrecta(AveNoVoladora):
    pass
