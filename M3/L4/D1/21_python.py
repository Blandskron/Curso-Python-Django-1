# 21) Iteradores manuales con iter() y next()
lista = [10, 20, 30]
it = iter(lista)

try:
    while True:
        valor = next(it)
        print("Valor del iterador:", valor)
except StopIteration:
    print("Iterador agotado")
