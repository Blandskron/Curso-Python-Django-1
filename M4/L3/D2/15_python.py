# Ejemplo 13: Biblioteca adquiriendo libros (composición)
class LibroBiblioteca:
    def __init__(self, titulo: str, autor: str, isbn: str):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

class Biblioteca:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self._catalogo: list[LibroBiblioteca] = []

    def adquirir_libro(self, titulo: str, autor: str, isbn: str) -> None:
        nuevo = LibroBiblioteca(titulo, autor, isbn)
        self._catalogo.append(nuevo)

# Ejemplo 14: Biblioteca registrando socios (agregación)
class Socio:
    def __init__(self, nombre: str, numero: int):
        self.nombre = nombre
        self.numero = numero

class BibliotecaSocios:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self._socios: list[Socio] = []

    def registrar_socio(self, socio: Socio) -> None:
        if socio not in self._socios:
            self._socios.append(socio)

# Ejemplo 15: Biblioteca generando Ticket (dependencia)
from datetime import datetime

class Ticket:
    def __init__(self, detalle: str):
        self.detalle = detalle
        self.fecha = datetime.now()

    def imprimir(self) -> None:
        print(self.fecha, "-", self.detalle)

class BibliotecaPrestamo:
    def gestionar_prestamo(self, socio: Socio, libro: LibroBiblioteca) -> Ticket | None:
        if not libro.disponible:
            return None
        libro.disponible = False
        detalle = f"Préstamo '{libro.titulo}' a {socio.nombre}"
        return Ticket(detalle)   # objeto efímero
