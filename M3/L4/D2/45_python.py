# 45) Árbol de productos: recorrido anidado con for
categorias = {
    "libros": ["Python", "Django"],
    "cursos": ["Intro", "Avanzado"],
}

for categoria, items in categorias.items():
    print("Categoría:", categoria)
    for item in items:
        print(" -", item)
