# 39) List comprehension vs for clásico
# cuadrados pares con for
cuadrados = []
for x in range(10):
    if x % 2 == 0:
        cuadrados.append(x ** 2)

# cuadrados pares con list comprehension
cuadrados_comp = [x ** 2 for x in range(10) if x % 2 == 0]

print("for clásico:", cuadrados)
print("list comprehension:", cuadrados_comp)
