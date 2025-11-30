# 47) Generador con estado interno
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(6):
    print(next(fib))

# 48) Función que consume generador
def sumar_gen(gen, limite):
    total = 0
    for i in range(limite):
        total += next(gen)
    return total

fib = fibonacci()
print(sumar_gen(fib, 5))
