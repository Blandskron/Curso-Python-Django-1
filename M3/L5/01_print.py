# 01_print.py
# Demo "nivel hacker" combinando múltiples efectos en consola solo con print

import time
import random
import os
import sys


# ----------------- UTILIDADES BÁSICAS -----------------

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def typing(texto: str, delay: float = 0.03):
    """Imprime texto como máquina de escribir."""
    for ch in texto:
        print(ch, end="", flush=True)
        time.sleep(delay)
    # no agrega salto de línea extra, lo manejas desde fuera si quieres


# ----------------- EFECTOS INDIVIDUALES -----------------

def fake_login():
    clear_screen()
    print("login:", end=" ", flush=True)
    time.sleep(0.8)
    print("root")

    print("password:", end=" ", flush=True)
    time.sleep(1.2)
    print("********")

    time.sleep(0.8)
    print("\n\033[92m✔ Acceso concedido\033[0m")
    time.sleep(1.2)


def loader_bar():
    barra = ["■", "■", "■", "■", "■"]
    for i in range(len(barra) + 1):
        print(f"[{''.join(barra[:i]):<5}] Inicializando módulos...", end="\r", flush=True)
        time.sleep(0.4)
    print("[#####] Módulos listos           ")


def borrar_reescribir():
    print("DESCARGANDO DATOS   ", end="", flush=True)
    time.sleep(0.8)

    for _ in range(3):
        # borrar "...":
        print("\b\b\b   \b\b\b", end="", flush=True)
        time.sleep(0.25)
        print("...", end="", flush=True)
        time.sleep(0.25)

    print("\n\033[92mDatos descargados correctamente\033[0m")
    time.sleep(0.7)


def scanner_line():
    for i in range(30):
        print(f"[{'=' * i}>{' ' * (30 - i)}] ESCANEANDO PUERTOS", end="\r", flush=True)
        time.sleep(0.03)
    print("\n\033[92mESCANEO COMPLETADO 🔍\033[0m")
    time.sleep(0.8)


def matrix_rain(lines: int = 25, width: int = 60, delay: float = 0.03):
    chars = "01"
    for _ in range(lines):
        line = "".join(random.choice(chars) for _ in range(width))
        print(f"\033[92m{line}\033[0m")
        time.sleep(delay)


def glitch_text(texto: str = "CONEXIÓN SEGURA", repeticiones: int = 10):
    for _ in range(repeticiones):
        glitch = "".join(
            c if random.random() > 0.3 else random.choice("@#$%&")
            for c in texto
        )
        print(glitch, end="\r", flush=True)
        time.sleep(0.08)
    print(texto + " " * 10)
    time.sleep(0.7)


def countdown_injection():
    for i in range(5, 0, -1):
        print(f"\033[91mINYECCIÓN EN {i}...\033[0m", end="\r", flush=True)
        time.sleep(0.8)
    print("\033[92m✔ INYECCIÓN COMPLETADA          \033[0m")
    time.sleep(0.8)


def tracing_packets():
    for i in range(40):
        puntos = "." * (i % 5)
        print(f"TRAZANDO PAQUETES{puntos:<5}", end="\r", flush=True)
        time.sleep(0.2)
    print("TRAZANDO PAQUETES... OK   ")
    time.sleep(0.7)


def dashboard_live(iteraciones: int = 20):
    for _ in range(iteraciones):
        cpu = random.randint(1, 100)
        ram = random.randint(1, 100)

        panel = f"""
╔══════════════════════╗
║  SISTEMA ACTIVO      ║
║  CPU: {cpu:3}%            ║
║  RAM: {ram:3}%            ║
╚══════════════════════╝
"""
        print(panel, end="\r", flush=True)
        time.sleep(0.25)
    print(panel)


def progress_vertical():
    print("\n\033[94mDescargando módulos adicionales:\033[0m")
    for i in range(1, 11):
        print("█" * i)
        time.sleep(0.15)
    time.sleep(0.5)


def moving_snake():
    for i in range(30):
        print(" " * i + "🐍", end="\r", flush=True)
        time.sleep(0.03)
    print()
    time.sleep(0.4)


def alert_flashing(veces: int = 6):
    for _ in range(veces):
        print("\033[91m⚠ ALERTA DE SEGURIDAD DETECTADA ⚠\033[0m", end="\r", flush=True)
        time.sleep(0.3)
        print(" " * 40, end="\r", flush=True)
        time.sleep(0.3)
    print("\033[93mRevisión completada...\033[0m")
    time.sleep(0.7)


def mini_scene():
    mensajes = [
        "Iniciando protocolo SIGMA...",
        "Bypassing firewall...",
        "Inyectando payload...",
        "Escalando privilegios...",
        "Acceso ROOT ✔"
    ]
    for m in mensajes:
        typing(m)
        print()
        time.sleep(0.6)


# ----------------- SECUENCIA PRINCIPAL -----------------

def main():
    clear_screen()

    # 1. Login falso
    fake_login()
    time.sleep(0.5)

    # 2. Título con typing
    print()
    typing("Accediendo al sistema central...\n", delay=0.04)
    time.sleep(0.7)

    # 3. Loader y borrado/reescritura
    loader_bar()
    borrar_reescribir()

    # 4. Scanner lineal
    scanner_line()

    # 5. Lluvia estilo Matrix
    clear_screen()
    print("\033[92m[MODO MONITOR MATRIX ACTIVADO]\033[0m")
    time.sleep(0.5)
    matrix_rain()
    time.sleep(0.5)

    # 6. Glitch de texto
    glitch_text("TÚ NO DEBERÍAS ESTAR AQUÍ")

    # 7. Conteo regresivo de "inyección"
    countdown_injection()

    # 8. Trazado de paquetes
    tracing_packets()

    # 9. Dashboard de sistema
    clear_screen()
    print("\033[96m[MONITOREO DE RECURSOS]\033[0m")
    dashboard_live()

    # 10. Progreso vertical
    progress_vertical()

    # 11. Snake móvil
    print("\nMoviendo payload por la red:")
    moving_snake()

    # 12. Alerta intermitente
    alert_flashing()

    # 13. Mini escena final con narrativa
    print()
    mini_scene()

    # 14. Pantalla final tipo banner
    clear_screen()
    print("""
██████╗  ██████╗  ██████╗████████╗
██╔══██╗██╔═══██╗██╔════╝╚══██╔══╝
██████╔╝██║   ██║██║        ██║   
██╔══██╗██║   ██║██║        ██║   
██║  ██║╚██████╔╝╚██████╗   ██║   
╚═╝  ╚═╝ ╚═════╝  ╚═════╝   ╚═╝   

   SISTEMA COMPROMETIDO
""")
    typing("Demo hacker finalizada. Presiona ENTER para salir...", delay=0.04)
    input()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[91mInterrumpido por el usuario.\033[0m")
        sys.exit(0)
