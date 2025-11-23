# Ejemplo 13: List comprehension (programación funcional ligera)
numeros = [1, 2, 3, 4, 5]
cuadrados = [n ** 2 for n in numeros]       # Crea nueva lista con n^2
pares = [n for n in numeros if n % 2 == 0]  # Filtra solo los pares
print(cuadrados, pares)
