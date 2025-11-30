# 31) Contar frecuencias con dict.get()
palabras = ["a", "b", "a", "c", "b", "a"]
frecuencias = {}

for p in palabras:
    frecuencias[p] = frecuencias.get(p, 0) + 1

print(frecuencias)
