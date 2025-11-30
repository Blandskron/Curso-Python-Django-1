# Ejemplo 17: Modelo de dominio inspirado en la realidad (biblioteca)

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        if not self.disponible:
            raise RuntimeError("No disponible")
        self.disponible = False

    def devolver(self):
        self.disponible = True

class UsuarioBiblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self._prestamos: list[Libro] = []

    def tomar_prestado(self, libro: Libro):
        libro.prestar()
        self._prestamos.append(libro)

    def devolver_todo(self):
        for libro in self._prestamos:
            libro.devolver()
        self._prestamos.clear()

libro = Libro("1984", "Orwell")
usuario = UsuarioBiblioteca("Ana")
usuario.tomar_prestado(libro)
usuario.devolver_todo()
