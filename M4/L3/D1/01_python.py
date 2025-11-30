# Ejemplo 1: Clase simple según diagrama (Libro)
class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def get_info(self) -> str:
        return f"{self.isbn} - '{self.titulo}' ({self.autor})"
