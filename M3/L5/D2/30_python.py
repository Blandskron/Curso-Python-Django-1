# 30) Dict comprehension
cuadrados = {n: n**2 for n in range(5)}
print(cuadrados)

cuadrados2 = {}

for n in range(5):
    cuadrados2[n] = n ** 2
    
print(cuadrados2)