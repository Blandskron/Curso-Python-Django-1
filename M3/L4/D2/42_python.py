# 42) Combinación de break, continue y else en un mismo patrón
for n in range(2, 20):
    if n % 2 == 0:
        continue  # ignorar pares
    for divisor in range(3, n, 2):
        if n % divisor == 0:
            print(f"{n} es compuesto ({divisor})")
            break
    else:
        print(f"{n} es primo impar")
