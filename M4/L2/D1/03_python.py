# =====================================
# Ejemplo 3: Agregación ("tiene un" débil)
# =====================================

class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre

class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.profesores: list[Profesor] = []  # profesores pueden vivir fuera

    def agregar_profesor(self, profesor: Profesor):
        self.profesores.append(profesor)

dep = Departamento("Informática")
p1 = Profesor("Juan")
dep.agregar_profesor(p1)   # el profesor podría pertenecer a otro depto o existir sin el depto
