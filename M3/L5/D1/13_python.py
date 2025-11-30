# 13) Lista vs tupla: secuencia mutable vs inmutable
lista = [1, 2, 3]
tupla = (1, 2, 3)

lista[0] = 99   # OK
print(lista)

# tupla[0] = 99  # TypeError: 'tuple' object does not support item assignment
