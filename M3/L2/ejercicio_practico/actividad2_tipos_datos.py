# -----------------------------------------------------------
# Actividad M3 - L2 - Tipos de Datos y Listas
# Resolución completa del ejercicio
# -----------------------------------------------------------

# Listas base del ejercicio
a = [3, 7, 12, 5, 9, 20]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
d = ["perro", "gato", "jirafa", "elefante"]
e = [[5, 5, 3], [1, 2, 5], [5, 7, 5]]

print("\n=== Resultado del ejercicio ===\n")

# 1) a[2]
res1 = a[2]
print("a[2] =", res1, "| tipo:", type(res1))

# 2) b[9]
res2 = b[9]
print("b[9] =", res2, "| tipo:", type(res2))

# 3) c[1][2]
res3 = c[1][2]
print("c[1][2] =", res3, "| tipo:", type(res3))

# 4) e[0] == e[1]
res4 = e[0] == e[1]
print("e[0] == e[1] =", res4, "| tipo:", type(res4))

# 5) len(c)
res5 = len(c)
print("len(c) =", res5, "| tipo:", type(res5))

# 6) len(c[0])
res6 = len(c[0])
print("len(c[0]) =", res6, "| tipo:", type(res6))

# 7) len(e)
res7 = len(e)
print("len(e) =", res7, "| tipo:", type(res7))

# 8) c[-1]
res8 = c[-1]
print("c[-1] =", res8, "| tipo:", type(res8))

# 9) c[-1][+1]
res9 = c[-1][+1]
print("c[-1][+1] =", res9, "| tipo:", type(res9))

# 10) c[2:] + d[2:]
res10 = c[2:] + d[2:]
print("c[2:] + d[2:] =", res10, "| tipo:", type(res10))

# 11) a[3:10]
res11 = a[3:10]
print("a[3:10] =", res11, "| tipo:", type(res11))

# 12) a[3:10:2]
res12 = a[3:10:2]
print("a[3:10:2] =", res12, "| tipo:", type(res12))

# 13) d.index("jirafa")
res13 = d.index("jirafa")
print("d.index('jirafa') =", res13, "| tipo:", type(res13))

# 14) e[c[0][1]].count(5)
print("e[c[0][1]].count(5) → provoca error (IndexError) porque e solo tiene índices 0, 1 y 2")
try:
    res14 = e[c[0][1]].count(5)
    print("Resultado:", res14)
except Exception as err:
    print("Error:", err, "| tipo:", type(err))

# 15) sorted(a)[2]
res15 = sorted(a)[2]
print("sorted(a)[2] =", res15, "| tipo:", type(res15))

# 16) complex(b[0], b[1])
res16 = complex(b[0], b[1])
print("complex(b[0], b[1]) =", res16, "| tipo:", type(res16))

print("\n=== Fin de la actividad ===")
