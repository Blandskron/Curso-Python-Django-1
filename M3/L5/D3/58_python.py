# 58) Tuplas como filas de una tabla y lista como tabla
tabla = [
    ("id", "nombre", "edad"),
    (1, "Ana", 30),
    (2, "Luis", 25),
]

for fila in tabla[1:]:
    id_, nombre, edad = fila
    print(id_, nombre, edad)
