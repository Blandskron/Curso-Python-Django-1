# Ejemplo 31: Asociación muchos a muchos Autor <-> Libro
class Autor:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.libros: set["LibroAutor"] = set()

class LibroAutor:
    def __init__(self, titulo: str):
        self.titulo = titulo
        self.autores: set[Autor] = set()

    def agregar_autor(self, autor: Autor) -> None:
        self.autores.add(autor)
        autor.libros.add(self)
