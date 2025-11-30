# 47) Simulación de intentos de login con while y contador
MAX_INTENTOS = 3
intentos = 0

while intentos < MAX_INTENTOS:
    password = input("Password: ")
    if password == "secreto":
        print("Acceso concedido")
        break
    print("Password incorrecto")
    intentos += 1
else:
    print("Cuenta bloqueada por demasiados intentos")
