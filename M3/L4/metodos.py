# =========================
# LISTAS (list)
# =========================

lista = [1, 2, 3, 4, 5]

lista.append(6)                   # agrega al final
lista.extend([7, 8])              # agrega múltiples
lista.insert(0, 0)                # inserta por índice
lista.remove(3)                   # elimina por valor
ultimo = lista.pop()              # elimina y retorna último
lista.pop(0)                      # elimina por índice
indice = lista.index(4)           # obtiene índice
conteo = lista.count(2)           # cuenta apariciones
lista.sort()                      # ordena
lista.reverse()                   # invierte
copia_lista = lista.copy()        # copia superficial
longitud = len(lista)             # tamaño
lista.clear()                     # vacía la lista

print("LISTA:", lista, indice, conteo, ultimo, copia_lista, longitud)


# =========================
# TUPLAS (tuple)
# =========================

tupla = (1, 2, 3, 4, 2)

indice_t = tupla.index(3)         # índice
conteo_t = tupla.count(2)         # conteo
longitud_t = len(tupla)           # tamaño

# conversión para modificación
tupla_a_lista = list(tupla)
tupla_a_lista.append(5)
tupla_nueva = tuple(tupla_a_lista)

print("TUPLA:", tupla, indice_t, conteo_t, longitud_t, tupla_nueva)


# =========================
# CONJUNTOS (set)
# =========================

conjunto = {1, 2, 3, 4}

conjunto.add(5)                   # agrega elemento
conjunto.update([6, 7])            # agrega múltiples
conjunto.remove(3)                # elimina (error si no existe)
conjunto.discard(10)               # elimina sin error
elemento = conjunto.pop()         # elimina aleatorio
copia_set = conjunto.copy()       # copia
longitud_set = len(conjunto)      # tamaño

otro_set = {4, 5, 6, 7, 8}

union = conjunto.union(otro_set)
interseccion = conjunto.intersection(otro_set)
diferencia = conjunto.difference(otro_set)
simetrica = conjunto.symmetric_difference(otro_set)
es_subconjunto = conjunto.issubset(otro_set)
es_superconjunto = conjunto.issuperset(otro_set)
es_disjunto = conjunto.isdisjoint({100, 200})

conjunto.clear()                  # vacía

print("SET:", union, interseccion, diferencia, simetrica,
      es_subconjunto, es_superconjunto, es_disjunto, copia_set, longitud_set)


# =========================
# DICCIONARIOS (dict)
# =========================

dic = {"a": 1, "b": 2, "c": 3}

dic["d"] = 4                      # agregar
dic.update({"e": 5})              # actualizar
valor = dic.get("a")              # obtener valor
valor_defecto = dic.get("z", 0)   # valor por defecto
eliminado = dic.pop("b")          # elimina por clave
ultimo = dic.popitem()            # elimina último
claves = dic.keys()               # claves
valores = dic.values()            # valores
items = dic.items()               # pares clave-valor
copia_dic = dic.copy()            # copia
longitud_dic = len(dic)           # tamaño

dic.clear()                       # vacía

print("DICT:", valor, valor_defecto, eliminado, ultimo,
      list(claves), list(valores), list(items), copia_dic, longitud_dic)
