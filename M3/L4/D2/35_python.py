# 35) Fibonacci recursivo ingenuo (no eficiente)
def fib_recursivo(n):
    if n <= 1:
        return n
    return fib_recursivo(n - 1) + fib_recursivo(n - 2)

print([fib_recursivo(i) for i in range(10)])
