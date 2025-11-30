# Ejemplo 18: Modelo estructurado del mismo problema (menos modular)

libros = {
    "1984": {"autor": "Orwell", "disponible": True},
}

prestamos = []

def prestar_libro(nombre_usuario, titulo):
    libro = libros[titulo]
    if not libro["disponible"]:
        raise RuntimeError("No disponible")
    libro["disponible"] = False
    prestamos.append((nombre_usuario, titulo))

def devolver_libro(titulo):
    libros[titulo]["disponible"] = True
    # prestamos global no se limpia, ejemplo de estado disperso

prestar_libro("Ana", "1984")
devolver_libro("1984")
