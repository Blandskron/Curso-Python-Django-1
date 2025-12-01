# =========================
# TIPOS DE DATOS EN PYTHON
# =========================

# -------------------------
# Tipos básicos (escalares)
# -------------------------

entero = 10                  # int
decimal = 3.14               # float
complejo = 2 + 3j            # complex
booleano = True              # bool
texto = "Hola Python"        # str
nulo = None                  # NoneType

# -------------------------
# Tipos de colección
# -------------------------

# Lista (mutable, ordenada, admite duplicados)
lista = [1, 2, 3, "texto", True]

# Tupla (inmutable, ordenada, admite duplicados)
tupla = (1, 2, 3, "texto", True)

# Conjunto / Set (mutable, no ordenado, no admite duplicados)
conjunto = {1, 2, 3, 3, 4}

# Conjunto inmutable
conjunto_inmutable = frozenset({1, 2, 3, 4})

# Diccionario (clave-valor, mutable)
diccionario = {
    "nombre": "Bastián",
    "edad": 35,
    "activo": True
}

# -------------------------
# Tipos de rango
# -------------------------

rango = range(1, 6)

# -------------------------
# Tipos binarios
# -------------------------

bytes_data = b"Hola"
byte_array = bytearray(b"Hola")
memoria = memoryview(b"Hola")

# -------------------------
# Tipos numéricos avanzados
# -------------------------

# Notación científica
cientifico = 1.2e3

# -------------------------
# Ejemplos de conversión de tipos
# -------------------------

numero_str = "100"
numero_int = int(numero_str)
numero_float = float(numero_str)

lista_a_tupla = tuple(lista)
tupla_a_lista = list(tupla)
lista_a_set = set(lista)

# -------------------------
# Verificación de tipos
# -------------------------

print(type(entero))
print(type(decimal))
print(type(complejo))
print(type(booleano))
print(type(texto))
print(type(nulo))
print(type(lista))
print(type(tupla))
print(type(conjunto))
print(type(conjunto_inmutable))
print(type(diccionario))
print(type(rango))
print(type(bytes_data))
print(type(byte_array))
print(type(memoria))

# -------------------------
# Estructuras anidadas
# -------------------------

estructura_compleja = {
    "usuarios": [
        {"id": 1, "roles": ("admin", "editor")},
        {"id": 2, "roles": ("viewer",)}
    ],
    "tags": {"python", "backend", "educacion"}
}
