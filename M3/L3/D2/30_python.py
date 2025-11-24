# Manejo cuidadoso de rangos y errores off-by-one

nota = int(input("Ingrese nota (0-100): "))

if 0 <= nota <= 100:
    if nota == 0:
        print("Nota mínima")
    elif nota == 100:
        print("Nota máxima")
    else:
        print("Nota dentro del rango normal")
else:
    print("Nota fuera de rango (error de entrada)")