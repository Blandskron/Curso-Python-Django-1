"""
Actividad N° 5 – Explorando Estructuras de Datos
Módulo: Fundamentos de Programación en Python

Este archivo resuelve todos los ejercicios solicitados:
1) Crear estructuras (lista, tupla, set y diccionario).
2) Acceder a elementos.
3) Contar e iterar.
4) Modificar estructuras.
"""


# ============================================
# 1. CREAR ESTRUCTURAS
# ============================================

# Lista: estructura ordenada y MUTABLE (se puede modificar).
lista_numeros = [10, 20, 30]

# Tupla: estructura ordenada pero INMUTABLE (no se puede modificar).
tupla_colores = ("rojo", "verde", "azul")

# Conjunto (set): colección NO ordenada, SIN elementos duplicados.
conjunto_frutas = {"manzana", "plátano", "naranja"}

# Diccionario: pares CLAVE-VALOR, acceso por clave (no por índice).
diccionario_estudiante = {
    "nombre": "Ana",
    "edad": 21,
    "carrera": "Informática",
}

print("=== 1) CREAR ESTRUCTURAS ===")
print("Lista:", lista_numeros)
print("Tupla:", tupla_colores)
print("Set:", conjunto_frutas)
print("Diccionario:", diccionario_estudiante)
print()  # línea en blanco para separar secciones


# Comentario general de diferencias principales (muy resumido):
# - Lista: ordenada + mutable.
# - Tupla: ordenada + inmutable.
# - Set: no ordenado + sin duplicados.
# - Diccionario: clave-valor + acceso por clave.


# ============================================
# 2. ACCEDER A ELEMENTOS
# ============================================

print("=== 2) ACCEDER A ELEMENTOS ===")

# Imprimir el segundo elemento de la lista (índice 1).
segundo_lista = lista_numeros[1]
print("Segundo elemento de la lista:", segundo_lista)

# Imprimir una clave y su valor desde el diccionario.
clave = "nombre"
valor = diccionario_estudiante[clave]
print(f"Clave '{clave}' en diccionario:", valor)

# Por qué no se puede acceder por índice a un set:
# Un 'set' es una colección NO ordenada, por lo tanto
# no existe posición fija (índices) como en una lista o tupla.
# Acceder por índice implicaría asumir un orden que no está garantizado.


print()  # línea en blanco para separar secciones


# ============================================
# 3. CONTAR E ITERAR
# ============================================

print("=== 3) CONTAR E ITERAR ===")

# Usar len() para mostrar la cantidad de elementos en cada estructura.
print("Cantidad en lista:", len(lista_numeros))
print("Cantidad en tupla:", len(tupla_colores))
print("Cantidad en set:", len(conjunto_frutas))
print("Cantidad en diccionario:", len(diccionario_estudiante))

print("\n--- Iterar lista ---")
for numero in lista_numeros:
    print("Elemento lista:", numero)

print("\n--- Iterar tupla ---")
for color in tupla_colores:
    print("Elemento tupla:", color)

print("\n--- Iterar set ---")
for fruta in conjunto_frutas:
    # El orden al iterar un set NO está garantizado.
    print("Elemento set:", fruta)

print("\n--- Iterar diccionario (claves y valores) ---")
for clave, valor in diccionario_estudiante.items():
    print(f"{clave} -> {valor}")

print()  # línea en blanco para separar secciones


# ============================================
# 4. MODIFICAR ESTRUCTURAS
# ============================================

print("=== 4) MODIFICAR ESTRUCTURAS ===")

# Agregar un nuevo elemento a la lista.
lista_numeros.append(40)
print("Lista después de agregar 40:", lista_numeros)

# Agregar un nuevo elemento al conjunto.
# Si el elemento ya existe, el set simplemente lo ignora (no duplica).
conjunto_frutas.add("pera")
print("Set después de agregar 'pera':", conjunto_frutas)

# Borrar un elemento de la lista (por valor).
# Si no existe, lanzaría ValueError (en un caso real, conviene verificar).
lista_numeros.remove(20)
print("Lista después de eliminar 20:", lista_numeros)

# Agregar una nueva clave al diccionario.
diccionario_estudiante["promedio"] = 6.5
print("Diccionario después de agregar 'promedio':", diccionario_estudiante)

print()

# Intentar modificar la tupla.
print("Tupla original:", tupla_colores)

# Las tuplas son INMUTABLES: no podemos hacer algo como tupla_colores[0] = "amarillo".
# Para ilustrarlo sin interrumpir el programa, usamos un try/except.
try:
    # Esto lanza TypeError porque las tuplas no permiten asignación por índice.
    tupla_colores[0] = "amarillo"  # type: ignore[assignment]
except TypeError as e:
    print("Intento de modificar tupla_colores[0] produjo TypeError:")
    print("Mensaje de error:", e)

print()
print("Fin de estructuras.py")
