"""
Módulo 4 – Programación Avanzada en Python
Actividad N° 6 – Lectura y Escritura de Archivos en Python

Este script resuelve:

1. Escribir en un archivo (write, modo "w").
2. Leer el archivo completo (read).
3. Leer línea por línea (readline + for).
4. Añadir contenido (append, modo "a").
5. Mostrar atributos (.name, .closed, .mode) y cierre correcto.
"""

NOMBRE_ARCHIVO = "datos.txt"


# ============================================================
# 1. ESCRIBIR EN UN ARCHIVO (write, modo "w")
# ============================================================

def escribir_archivo_inicial() -> None:
    """
    Crea (o sobrescribe) datos.txt y escribe al menos 3 líneas usando write().
    """
    print("=== 1) Creando y escribiendo datos.txt con write() ===")
    with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as f:
        f.write("Línea 1: Este es el inicio del archivo.\n")
        f.write("Línea 2: Practicando lectura y escritura en Python.\n")
        f.write("Línea 3: El modo 'w' sobrescribe el contenido existente.\n")
    print("Archivo creado y escrito correctamente.\n")


# ============================================================
# 2. LEER EL ARCHIVO COMPLETO (read)
# ============================================================

def leer_archivo_completo() -> None:
    """
    Abre datos.txt en modo lectura y muestra todo el contenido usando read().
    """
    print("=== 2) Leyendo archivo completo con read() ===")
    with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as f:
        contenido = f.read()
    print("Contenido de datos.txt:")
    print(contenido)
    print()


# ============================================================
# 3. LEER LÍNEA POR LÍNEA (readline + for)
# ============================================================

def leer_linea_por_linea() -> None:
    """
    Usa readline() para leer la primera línea y luego un for para el resto.
    """
    print("=== 3) Leer primera línea con readline() y resto con for ===")
    with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as f:
        primera = f.readline()
        print("Primera línea (readline):")
        print(primera, end="")  # ya trae '\n'

        print("\nResto de las líneas (for sobre el archivo):")
        for linea in f:
            print(linea, end="")
    print("\n")


# ============================================================
# 4. AÑADIR CONTENIDO (append, modo "a")
# ============================================================

def agregar_con_append() -> None:
    """
    Abre datos.txt en modo append, agrega una nueva línea, y verifica el resultado.
    """
    print("=== 4) Añadiendo una nueva línea con append (modo 'a') ===")
    with open(NOMBRE_ARCHIVO, "a", encoding="utf-8") as f:
        f.write("Línea 4: Esta línea fue agregada usando el modo 'a'.\n")

    print("Verificando contenido después del append:")
    with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as f:
        print(f.read())
    print()


# ============================================================
# 5. ATRIBUTOS Y CIERRE (.name, .closed, .mode)
# ============================================================

def mostrar_atributos_y_cierre() -> None:
    """
    Muestra nombre, modo y estado cerrado del archivo.
    Usa apertura manual + close() para ver el cambio en .closed.
    """
    print("=== 5) Atributos del archivo y cierre correcto ===")
    f = open(NOMBRE_ARCHIVO, "r", encoding="utf-8")  # apertura manual
    print(f"Nombre del archivo (.name): {f.name}")
    print(f"Modo de apertura (.mode): {f.mode}")
    print(f"¿Está cerrado antes de close()? (.closed): {f.closed}")

    # Cerramos manualmente
    f.close()
    print(f"¿Está cerrado después de close()? (.closed): {f.closed}\n")


# ============================================================
# PROGRAMA PRINCIPAL (EJECUCIÓN SECUENCIAL DE LOS PASOS)
# ============================================================

def main() -> None:
    escribir_archivo_inicial()
    leer_archivo_completo()
    leer_linea_por_linea()
    agregar_con_append()
    mostrar_atributos_y_cierre()
    print("Script manejo_archivos.py finalizado.")


if __name__ == "__main__":
    main()
