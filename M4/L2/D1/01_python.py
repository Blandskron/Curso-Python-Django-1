# =====================================
# Ejemplo 1: Asociación simple ("conoce a")
# =====================================

class Libro:
    def __init__(self, titulo):
        self.titulo = titulo

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

    def leer(self, libro: Libro):
        print(f"{self.nombre} lee {libro.titulo}")

libro = Libro("POO con Python")
alumno = Estudiante("Ana")
alumno.leer(libro)  # asociación: Estudiante conoce Libro
