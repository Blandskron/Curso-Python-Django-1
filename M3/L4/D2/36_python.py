# 36) Fibonacci iterativo eficiente con for
def fib_iterativo(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print([fib_iterativo(i) for i in range(10)])
