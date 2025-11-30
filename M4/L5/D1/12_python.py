# Ejemplo 12: Relanzar (re-raise) la misma excepción

def procesar_pago() -> None:
    raise RuntimeError("Fallo de pago simulado")

def flujo_pago() -> None:
    try:
        procesar_pago()
    except RuntimeError as e:
        print(f"Registrando error: {e}")
        raise  # relanza
