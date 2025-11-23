# Ejemplo 18: Lambdas, map y filter
numeros = [1, 2, 3, 4, 5]
dobles = list(map(lambda n: n * 2, numeros))         # Aplica función anónima
mayores_que_dos = list(filter(lambda n: n > 2, numeros))  # Filtra valores
print(dobles, mayores_que_dos)
