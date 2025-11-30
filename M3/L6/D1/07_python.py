# 7) Parámetros *args
def sumar_todo(*numeros):
    total = 0
    for n in numeros:
        total += n
    return total

print(sumar_todo(1, 2, 3, 4))
