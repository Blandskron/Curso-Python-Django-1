# 46) Cálculo de suma y promedio con un solo for
valores = [10, 20, 30, 40]
suma = 0

for v in valores:
    suma += v

promedio = suma / len(valores)
print("Suma:", suma, "Promedio:", promedio)
