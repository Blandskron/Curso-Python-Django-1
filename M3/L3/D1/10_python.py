# Precedencia de operadores con paréntesis

a = 5
b = 3
c = 8

# Sin paréntesis, se respeta la precedencia lógica
resultado1 = a > b or c < a and not (b == 3)

# Con paréntesis explícitos para cambiar el significado
resultado2 = (a > b or c < a) and not (b == 3)

print("Resultado1:", resultado1)
print("Resultado2:", resultado2)