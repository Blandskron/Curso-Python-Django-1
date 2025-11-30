# 41) Expresión generadora (generator expression) en un for
numeros = (n * n for n in range(5))  # genera al vuelo
for valor in numeros:
    print("Cuadrado:", valor)
