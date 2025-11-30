# 38) Grafo con sets para evitar aristas duplicadas
grafo = {
    "A": {"B", "C"},
    "B": {"C"},
    "C": {"A"},
}

grafo["A"].add("D")
grafo["A"].add("C")  # ya existía, no se duplica
print(grafo["A"])
