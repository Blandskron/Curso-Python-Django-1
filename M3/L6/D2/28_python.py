# 28) Función integrada vs personalizada
print(len([1, 2, 3]))

def largo_manual(lista):
    c = 0
    for _ in lista:
        c += 1
    return c

print(largo_manual([1, 2, 3]))
