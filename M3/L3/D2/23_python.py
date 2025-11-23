# Flujo de autenticación con condicionales anidados

usuario_existe = True
password_correcta = False

if usuario_existe:
    if password_correcta:
        print("Acceso concedido")
    else:
        print("Contraseña incorrecta")
else:
    print("El usuario no existe")
