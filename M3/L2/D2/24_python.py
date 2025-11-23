# 24_python.py
# función con condición (par o impar)

def es_par(numero):
    # True si el número es par
    return numero % 2 == 0


for n in range(6):
    if es_par(n):
        print(n, "es par")
    else:
        print(n, "es impar")
