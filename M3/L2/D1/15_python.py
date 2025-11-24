# 15_python.py
# for recorriendo lista y calculando suma y promedio

numeros = [10, 5, 8, 3, 9]
suma = 0

for n in numeros:
    suma += n

promedio = suma / len(numeros)

print("Números:", numeros)
print("Suma:", suma)
print("Promedio:", promedio)
