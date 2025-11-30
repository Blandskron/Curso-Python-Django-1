# 31) while True + break: sistema de comandos (máquina de estados simple)
estado = "MENU"

while True:
    if estado == "MENU":
        opcion = input("1. Jugar  2. Salir: ")
        if opcion == "1":
            estado = "JUGANDO"
        elif opcion == "2":
            print("Saliendo...")
            break
    elif estado == "JUGANDO":
        comando = input("Escribe 'fin' para terminar la partida: ")
        if comando == "fin":
            estado = "MENU"
        else:
            print("Juegando...")
