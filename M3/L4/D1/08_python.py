# 8) while para aproximar raíz cuadrada (método de Newton)
numero = 25
estimacion = 1.0
tolerancia = 0.0001

while abs(estimacion * estimacion - numero) > tolerancia:
    estimacion = (estimacion + numero / estimacion) / 2

print("Raíz aproximada:", estimacion)
