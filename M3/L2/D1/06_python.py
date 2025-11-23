# 06_python.py
# operadores lógicos y truthiness

edad = 20
tiene_licencia = True

puede_conducir = edad >= 18 and tiene_licencia
print("¿Puede conducir?", puede_conducir)

usuario = ""
nombre_mostrar = usuario or "Invitado"  # valor por defecto
print("Nombre a mostrar:", nombre_mostrar)

print("not True:", not True)
print("not False:", not False)
