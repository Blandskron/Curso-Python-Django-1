# 39) Búsqueda en lista vs set (patrón conceptual)
usuarios = list(range(1_000_000))
usuarios_set = set(usuarios)

objetivo = 900_000

# búsqueda en lista (O(N))
en_lista = objetivo in usuarios

# búsqueda en set (O(1) promedio)
en_set = objetivo in usuarios_set

print(en_lista, en_set)
