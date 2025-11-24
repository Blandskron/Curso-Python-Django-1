# Leyes de De Morgan para reescribir condiciones

usuario_inactivo = False
clave_expirada = True

# Condición para bloquear acceso
if usuario_inactivo or clave_expirada:
    print("Acceso bloqueado")

# Condición inversa para permitir acceso usando De Morgan
if (not usuario_inactivo) and (not clave_expirada):
    print("Acceso permitido")
else:
    print("Acceso NO permitido (con De Morgan)")