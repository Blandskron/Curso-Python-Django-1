# Truthiness: valores considerados verdaderos o falsos

usuarios = []  # lista vacía
mensaje = ""   # cadena vacía
contador = 0   # número cero

if usuarios:
    print("Hay usuarios registrados")
else:
    print("No hay usuarios registrados")

if mensaje:
    print("El mensaje no está vacío")
else:
    print("El mensaje está vacío")

if contador:
    print("El contador es distinto de cero")
else:
    print("El contador es cero (Falsey)")