# 24) Bucles anidados: matriz identidad 3x3
n = 3
identidad = []

for i in range(n):
    fila = []
    for j in range(n):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    identidad.append(fila)

print("Matriz identidad:")
for fila in identidad:
    print(fila)
