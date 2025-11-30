# 46) Función generadora
def contador_hasta(n):
    for i in range(n):
        yield i

for x in contador_hasta(5):
    print(x)
