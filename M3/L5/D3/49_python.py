# 49) Ordenar diccionario por valor
puntuaciones = {"Ana": 80, "Luis": 95, "Marta": 70}

ordenado = sorted(
    puntuaciones.items(),
    key=lambda par: par[1],
    reverse=True,
)
print(ordenado)
