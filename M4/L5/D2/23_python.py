# Ejemplo 23: Bloques try anidados para errores de archivo y línea

def procesar_configuracion(ruta: str) -> None:
    try:
        with open(ruta, encoding="utf-8") as f:
            for num, linea in enumerate(f, 1):
                linea = linea.strip()
                if not linea:
                    continue
                try:
                    valor = int(linea)
                    resultado = 1000 / valor
                    print(f"{num}: 1000 / {valor} = {resultado:.2f}")
                except ValueError:
                    print(f"Línea {num}: no es número válido")
                except ZeroDivisionError:
                    print(f"Línea {num}: división por cero")
    except FileNotFoundError:
        print(f"No se encontró {ruta}")
    except PermissionError:
        print(f"Sin permisos para {ruta}")
