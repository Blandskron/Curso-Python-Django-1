# 40) Función iterativa equivalente
def factorial_iter(n):
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r

print(factorial_iter(5))
