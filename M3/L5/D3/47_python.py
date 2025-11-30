# 47) Convertir lista a set y de vuelta para deduplicar pero mantener orden
lista = ["a", "b", "a", "c", "b"]
vistos = set()
sin_duplicados = []

for item in lista:
    if item not in vistos:
        vistos.add(item)
        sin_duplicados.append(item)

print(sin_duplicados)  # ['a', 'b', 'c']
