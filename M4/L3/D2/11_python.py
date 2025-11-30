# Ejemplo 11: Dependencia a través de parámetro (Documento usa Impresora)
class Impresora:
    def imprimir(self, texto: str) -> None:
        print(texto)

class Documento:
    def __init__(self, contenido: str):
        self.contenido = contenido

    def imprimir_en(self, impresora: Impresora) -> None:
        impresora.imprimir(self.contenido)  # dependencia efímera
