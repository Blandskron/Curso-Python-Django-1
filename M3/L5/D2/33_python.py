# 33) Agrupamiento con defaultdict(list)
from collections import defaultdict

empleados = [
    ("IT", "Juan"),
    ("Ventas", "Ana"),
    ("IT", "Pedro"),
]

por_depto = defaultdict(list)

for depto, nombre in empleados:
    por_depto[depto].append(nombre)

print(dict(por_depto))
