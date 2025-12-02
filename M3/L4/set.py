conjunto = {1, 2, 3, 4}

otro_set =          {4, 5, 6, 7, 8}

union = conjunto.union(otro_set)
interseccion = conjunto.intersection(otro_set)
diferencia = conjunto.difference(otro_set)
diferencia2 = otro_set.difference(conjunto)
simetrica = conjunto.symmetric_difference(otro_set)
es_subconjunto = conjunto.issubset(otro_set)
es_superconjunto = conjunto.issuperset(otro_set)
es_disjunto = conjunto.isdisjoint({100, 200})

print("SET:", union)
print("SET:", interseccion)
print("SET:", diferencia)
print("SET:", diferencia2)
print("SET:", simetrica)
print("SET:", es_subconjunto)
print("SET:", es_superconjunto)
print("SET:", es_disjunto)