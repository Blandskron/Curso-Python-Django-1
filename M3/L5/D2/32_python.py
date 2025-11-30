# 32) Agrupamiento con dict.setdefault()
alumnos = [
    ("A", "math"),
    ("B", "math"),
    ("A", "physics"),
    ("C", "math"),
]

grupos = {}
for nombre, curso in alumnos:
    grupos.setdefault(curso, []).append(nombre)

print(grupos)
