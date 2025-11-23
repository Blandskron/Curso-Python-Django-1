# Uso de match-case (Python 3.10+) como alternativa a largas cadenas de elif

comando = input("Ingrese comando (iniciar, detener, pausar): ")

match comando:
    case "iniciar":
        print("Sistema iniciando...")
    case "detener":
        print("Sistema deteniéndose...")
    case "pausar":
        print("Sistema en pausa.")
    case _:
        print("Comando no reconocido")