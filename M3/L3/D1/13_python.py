# Buenas prácticas: nombres en snake_case y constantes

MAX_INTENTOS_LOGIN = 3  # constante en SCREAMING_SNAKE_CASE

nombre_usuario = "bastian"
es_usuario_activo = True
numero_intentos = 0

if es_usuario_activo and numero_intentos < MAX_INTENTOS_LOGIN:
    print("Puede intentar iniciar sesión")
else:
    print("No puede iniciar sesión")