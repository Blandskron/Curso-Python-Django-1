# 37) Patrón de reintento con backoff exponencial
import time
import random

def conectar_servicio(max_intentos=5):
    intento = 0
    while intento < max_intentos:
        try:
            print(f"Intento {intento + 1} de conexión...")
            if random.random() < 0.8:
                raise ConnectionError("Fallo temporal")
            print("Conectado!")
            return True
        except ConnectionError as e:
            intento += 1
            if intento == max_intentos:
                print("Error fatal:", e)
                return False
            espera = 2 ** intento
            print(f"{e}. Reintentando en {espera} segundos...")
            time.sleep(espera)

# conectar_servicio()
