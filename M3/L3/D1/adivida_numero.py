import random

def juego_adivina_numero():
    print(" Bienvenido al juego de adivinar el número")
    print("Estoy pensando en un número del 1 al 100...")

    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    while not adivinado:
        try:
            intento = int(input(" Ingresa tu número: "))
            intentos += 1

            if intento < numero_secreto:
                print(" El número secreto es MÁS grande.")
            elif intento > numero_secreto:
                print(" El número secreto es MÁS pequeño.")
            else:
                print(f" ¡Correcto! El número era {numero_secreto}.")
                print(f" Lo lograste en {intentos} intentos.")
                adivinado = True

        except ValueError:
            print(" Por favor, ingresa un número válido (solo dígitos).")

if __name__ == "__main__":
    juego_adivina_numero()
