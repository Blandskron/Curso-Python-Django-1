# Ejemplo simple de "código espagueti" vs versión estructurada

# Versión poco clara (simulada, no usar este estilo):
opcion = "b"

if opcion == "a":
    print("Elegiste A")
else:
    if opcion == "b":
        print("Elegiste B")
    else:
        if opcion == "c":
            print("Elegiste C")
        else:
            print("Opción desconocida")

# Versión estructurada con if/elif/else:
if opcion == "a":
    print("Elegiste A (estructurado)")
elif opcion == "b":
    print("Elegiste B (estructurado)")
elif opcion == "c":
    print("Elegiste C (estructurado)")
else:
    print("Opción desconocida (estructurado)")