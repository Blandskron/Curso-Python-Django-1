# Sistema de login con reintentos y bandera de estado

import sys

MAX_INTENTOS = 3
CONTRASENA_CORRECTA = "python123"

intentos = 0
autenticado = False

while intentos < MAX_INTENTOS and not autenticado:
    intento = input("Ingrese contraseña: ")
    if intento == CONTRASENA_CORRECTA:
        autenticado = True
        print("Inicio de sesión exitoso")
    else:
        intentos += 1
        print("Contraseña incorrecta. Intentos usados:", intentos)

if not autenticado:
    print("Demasiados intentos fallidos. Cerrando programa.")
    sys.exit(1)  # código de salida distinto de 0 indica error