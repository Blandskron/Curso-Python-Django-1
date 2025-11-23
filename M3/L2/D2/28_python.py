# 28_python.py
# conjuntos (set): evitar duplicados

valores = [1, 2, 2, 3, 3, 3]
conjunto = set(valores)

print("Original:", valores)
print("Sin duplicados:", conjunto)

conjunto.add(4)
conjunto.discard(2)

print("Actualizado:", conjunto)
print("¿3 está?", 3 in conjunto)
print("¿10 está?", 10 in conjunto)
