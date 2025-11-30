# 44) Simulación de servidor con while True (bucle infinito controlado)
def servidor():
    while True:
        peticion = input("Escribe 'salir' para apagar servidor: ")
        if peticion == "salir":
            print("Servidor apagado")
            break
        print("Procesando petición:", peticion)

# servidor()
