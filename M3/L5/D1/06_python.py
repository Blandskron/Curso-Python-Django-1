# 6) List comprehension: transformar + filtrar
numeros = list(range(10))
cuadrados_pares = [n**2 for n in numeros if n % 2 == 0]
print(cuadrados_pares)
