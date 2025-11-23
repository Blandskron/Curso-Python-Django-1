# Truthiness con cuidado: distinguir 0 de None

puntuacion = 0      # valor válido
puntuacion2 = None  # sin valor

if puntuacion is not None:
    print("Puntuación válida (puede ser 0):", puntuacion)
else:
    print("Puntuación no definida")

if puntuacion2 is not None:
    print("Puntuación2 válida:", puntuacion2)
else:
    print("Puntuación2 no definida")