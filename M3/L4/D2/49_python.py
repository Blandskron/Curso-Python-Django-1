# 49) Filtrado y mapeo manual vs list comprehension
datos = [10, -3, 5, 0, 8]

# for clásico
positivos_dobles = []
for d in datos:
    if d > 0:
        positivos_dobles.append(d * 2)

# list comprehension
positivos_dobles_comp = [d * 2 for d in datos if d > 0]

print(positivos_dobles)
print(positivos_dobles_comp)
