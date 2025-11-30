# 44) Uso combinado list + dict: índice inverso
texto = "uno dos tres dos tres tres".split()
posiciones = {}

for i, palabra in enumerate(texto):
    posiciones.setdefault(palabra, []).append(i)

print(posiciones)
