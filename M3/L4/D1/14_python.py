# 14) for con continue: saltar elementos
numeros = [0, 1, 2, 3, 4, 5]
for n in numeros:
    if n % 2 != 0:
        continue  # salta impares
    print("Par:", n)
