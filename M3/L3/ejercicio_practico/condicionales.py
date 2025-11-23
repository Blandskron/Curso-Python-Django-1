# -----------------------------------------------------------
# condicionales.py
# Actividad M3 - L3: Control de flujo con sentencias condicionales
# -----------------------------------------------------------
# Objetivos:
# - Usar if, elif y else para tomar decisiones.
# - Aplicar decisiones simples, múltiples y anidadas.
# - Usar nombres de variables con snake_case.
# -----------------------------------------------------------

# 1. DECISIÓN SIMPLE
# Pedimos un número al usuario y determinamos si es mayor o menor de edad.

print("=== 1) Decisión simple: Mayor o menor de edad ===")
edad = int(input("Ingresa tu edad: "))  # Convertimos la entrada a entero

if edad >= 18:
    # Este bloque se ejecuta si la edad es 18 o más
    print("Eres mayor de edad")
else:
    # Este bloque se ejecuta si la condición anterior NO se cumple
    print("Eres menor de edad")

print()  # Línea en blanco para separar secciones


# 2. DECISIÓN MÚLTIPLE CON ELIF
# Pedimos una calificación entre 1 y 7 y mostramos una evaluación textual.

print("=== 2) Decisión múltiple: Evaluación de calificación ===")
calificacion = int(input("Ingresa una calificación entre 1 y 7: "))

# Usamos if / elif / else para evaluar diferentes casos
if calificacion == 7:
    print("Excelente")
elif calificacion == 6:
    print("Muy bien")
elif calificacion == 5:
    print("Bien")
elif calificacion == 4:
    print("Suficiente")
elif calificacion < 4:
    # Cualquier valor menor que 4 se considera insuficiente
    print("Insuficiente")
else:
    # Este caso captura calificaciones fuera del rango 1–7
    print("Calificación fuera de rango (debe ser entre 1 y 7)")

print()  # Línea en blanco para separar secciones


# 3. CONDICIONES ANIDADAS
# Pedimos un número entero y usamos if dentro de otro if (anidado).

print("=== 3) Condiciones anidadas: Signo del número ===")
numero_entero = int(input("Ingresa un número entero (puede ser negativo, cero o positivo): "))

# Primera condición externa
if numero_entero >= 0:
    # Dentro del if principal, anidamos otro if
    if numero_entero == 0:
        print("Es cero")
    else:
        # Si es mayor o igual a 0 y no es cero, entonces es positivo
        print("Número positivo")
else:
    # Si no cumple la condición numero_entero >= 0, es negativo
    print("Número negativo")

print()  # Línea en blanco para separar secciones


# 4. CONDICIÓN DE BORDE
# Pedimos un número entre 1 y 100 y revisamos límites y rango.

print("=== 4) Condición de borde: Número entre 1 y 100 ===")
numero_rango = int(input("Ingresa un número entre 1 y 100: "))

# Primero verificamos si está dentro del rango básico 1–100
if 1 <= numero_rango <= 100:
    # Ahora revisamos si está exactamente en los límites
    if numero_rango == 1 or numero_rango == 100:
        print("Estás en un límite permitido")
    else:
        # Está dentro del rango, pero no en los extremos
        print("Dentro del rango")
else:
    # Cualquier número fuera de 1–100
    print("Fuera del rango")

print()
print("=== Fin del programa condicionales.py ===")
