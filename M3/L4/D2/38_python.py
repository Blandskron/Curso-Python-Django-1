# 38) Sistema simple de notas con while, for, if, break, continue
def sistema_notas():
    estudiantes = []

    while True:
        print("\n--- GESTIÓN ACADÉMICA ---")
        print("1. Agregar estudiante y nota")
        print("2. Mostrar reporte")
        print("3. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            try:
                nota = float(input("Nota (0-100): "))
            except ValueError:
                print("Nota inválida")
                continue

            if not (0 <= nota <= 100):
                print("Fuera de rango")
                continue

            for est in estudiantes:
                if est["nombre"] == nombre:
                    est["notas"].append(nota)
                    print("Nota agregada")
                    break
            else:
                estudiantes.append({"nombre": nombre, "notas": [nota]})
                print("Estudiante creado")

        elif opcion == "2":
            if not estudiantes:
                print("No hay datos")
                continue

            for est in estudiantes:
                suma = 0
                for n in est["notas"]:
                    suma += n
                promedio = suma / len(est["notas"])
                estado = "APROBADO" if promedio >= 60 else "REPROBADO"
                print(f"{est['nombre']} -> {promedio:.2f} ({estado})")

        elif opcion == "3":
            print("Cerrando sistema...")
            break
        else:
            print("Opción no reconocida")

# sistema_notas()
