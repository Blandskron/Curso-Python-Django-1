# Espacio para practicar y aprender sobre variables en Python
c = [[1,2],[3,4,5],[6,7]]
c = [[1, 2], [3, 4, 5], [6, 7]]

# ¿Qué es c[-1]?
resultado = c[-1]
print(f"El resultado de c[-1] es: {resultado}")

# ¿Qué es c[-1][+1]?
# El +1 es lo mismo que 1.
resultado_2 = c[-1][+1]
print(f"El resultado de c[-1][+1] es: {resultado_2}")

d = ['perro', 'gato', 'jirafa', 'elefante']

# ¿Qué es c[2:] + d[2:]?
resultado_3 = c[2:] + d[2:]
print(f"El resultado de c[2:] + d[2:] es: {resultado_3}")

a = [5, 1, 4, 9, 0]

# ¿Qué es a[3:10]?
# El índice 10 no existe, pero Python no da error, solo llega hasta el final.
resultado_4 = a[3:10]
print(f"El resultado de a[3:10] es: {resultado_4}")

# ¿Qué es a[3:10:2]?
# Esto significa: empieza en el 3, ve hasta el 10, pero dando saltos de 2 en 2.
resultado_5 = a[3:10:2]
print(f"El resultado de a[3:10:2] es: {resultado_5}")

# ¿Qué es d.index('jirafa')?
# .index() pregunta: "¿En qué número de vagón está X?"
resultado_6 = d.index('jirafa')
print(f"El resultado de d.index('jirafa') es: {resultado_6}")

e = ['a', a, 2 * a]

# ¿Qué es e[c[0][1]].count(5)?
# Esto es como una búsqueda del tesoro en varios pasos.
resultado_7 = e[c[0][1]].count(5)
print(f"El resultado de e[c[0][1]].count(5) es: {resultado_7}")

# ¿Qué es sorted(a)[2]?
# sorted() ordena la lista de menor a mayor sin cambiar la original.
resultado_8 = sorted(a)[2]
print(f"El resultado de sorted(a)[2] es: {resultado_8}")

# ¿Qué es complex(b[0], b[1])?
# Primero intentamos crear b.
try:
    b = range(3, 10) + range(20, 23)
    resultado_9 = complex(b[0], b[1])
    print(f"El resultado de complex(b[0], b[1]) es: {resultado_9}")
except TypeError:
    print("Error: No se pueden sumar rangos (range) directamente. ¡Explotó! 💥")

# ¿Pero qué es complex?
# Imagina un número con dos partes: una parte Real y una parte Imaginaria.
# complex(3, 5) crea el número: 3 + 5j
numero_magico = complex(3, 5)
print(f"Ejemplo de complex(3, 5): {numero_magico}")

# ¿Qué es c[-1][1]?
