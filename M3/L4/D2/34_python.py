# 34) Bubblesort con ciclos anidados, break de optimización
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        intercambio = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True
        if not intercambio:
            break
    return lista

datos = [5, 1, 4, 2, 8]
print("Ordenado:", bubble_sort(datos))
