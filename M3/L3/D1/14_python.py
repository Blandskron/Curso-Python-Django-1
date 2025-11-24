# Mala práctica vs buena práctica con booleanos

es_valido = True

# Mala práctica (no recomendado):
if es_valido == True:
    print("Mala práctica: comparación redundante")

# Buena práctica:
if es_valido:
    print("Buena práctica: usar el booleano directamente")