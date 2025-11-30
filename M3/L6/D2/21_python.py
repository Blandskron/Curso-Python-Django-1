# 20) Función como objeto
def doble(n):
    return n * 2

f = doble
print(f(5))

# 21) Función como parámetro
def aplicar(func, valor):
    return func(valor)

print(aplicar(doble, 6))
