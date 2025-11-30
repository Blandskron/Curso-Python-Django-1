# 25) Salir de múltiples bucles anidados usando flag
encontrado = False
for i in range(5):
    for j in range(5):
        if i * j == 6:
            print("Par encontrado:", i, j)
            encontrado = True
            break
    if encontrado:
        break
