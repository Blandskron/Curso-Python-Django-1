# 37) Grafo como diccionario de listas (lista de adyacencia)
grafo = {
    "A": ["B", "C"],
    "B": ["C"],
    "C": ["A"],
    "D": [],
}

for nodo, vecinos in grafo.items():
    print(nodo, "->", vecinos)
