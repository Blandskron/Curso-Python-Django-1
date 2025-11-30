# 15) Retornar múltiples valores con tupla
def dividir(dividendo, divisor):
    cociente = dividendo // divisor
    resto = dividendo % divisor
    return cociente, resto  # tupla

q, r = dividir(17, 5)
print(q, r)
