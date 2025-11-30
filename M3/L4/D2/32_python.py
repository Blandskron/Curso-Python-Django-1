# 32) Verificación de número primo con for + else (no-break)
numero = 29

for i in range(2, int(numero ** 0.5) + 1):
    if numero % i == 0:
        print(f"{numero} no es primo, divisible por {i}")
        break
else:
    print(f"{numero} es primo")
