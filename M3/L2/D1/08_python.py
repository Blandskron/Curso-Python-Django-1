# 08_python.py
# conversión explícita entre tipos

texto_entero = "123"
texto_decimal = "3.14"
texto_booleano = "True"

entero = int(texto_entero)
decimal = float(texto_decimal)
booleano = texto_booleano == "True"  # conversión manual

print(entero, type(entero))
print(decimal, type(decimal))
print(booleano, type(booleano))

print(str(999), type(str(999)))
