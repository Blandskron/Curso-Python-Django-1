# Ejemplo 9: Composición (Libro crea sus Paginas)
class Pagina:
    def __init__(self, numero: int, contenido: str = ""):
        self.numero = numero
        self.contenido = contenido

class LibroCompuesto:
    def __init__(self, titulo: str, total_paginas: int):
        self.titulo = titulo
        # las páginas nacen y mueren con el libro
        self.paginas = [Pagina(n) for n in range(1, total_paginas + 1)]
