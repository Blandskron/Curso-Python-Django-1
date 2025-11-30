# Ejemplo 28: Implementación directa de diagrama de Biblioteca simplificado

class Libro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor

class Socio:
    def __init__(self, nombre: str, numero: int):
        self.nombre = nombre
        self.numero = numero

class BibliotecaSimple:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.libros: list[Libro] = []
        self.socios: list[Socio] = []

    def registrar_libro(self, libro: Libro) -> None:
        self.libros.append(libro)

    def registrar_socio(self, socio: Socio) -> None:
        self.socios.append(socio)
