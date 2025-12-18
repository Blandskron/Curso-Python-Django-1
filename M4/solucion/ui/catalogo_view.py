"""
Vistas de consola para catálogo.
"""


def mostrar_catalogo(catalogo):
    items = catalogo.listar_items()

    if not items:
        print("Catálogo vacío.")
        return

    print("\n--- CATÁLOGO ---")
    for producto, stock in items:
        print(f"{producto} | Stock: {stock}")


def mostrar_resultados_busqueda(resultados):
    if not resultados:
        print("No se encontraron productos.")
        return

    print("\n--- RESULTADOS ---")
    for producto, stock in resultados:
        print(f"{producto} | Stock: {stock}")
