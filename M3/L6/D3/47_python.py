# 47) Generador con estado interno
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(6):
    print(next(fib))
