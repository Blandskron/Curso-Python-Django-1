# 41) Función como elemento de estructura
def suma(a, b): return a + b
def resta(a, b): return a - b

operaciones = {
    "+": suma,
    "-": resta
}

print(operaciones["+"](5, 3))
