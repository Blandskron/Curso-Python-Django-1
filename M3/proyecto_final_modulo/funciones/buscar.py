def buscar_productos(cat: dict) -> None:
    texto = input("\nIngrese texto a buscar (nombre o categoría): ").lower()
    encontrados = False

    print("\n--- RESULTADOS DE BÚSQUEDA ---")
    for id_prod, datos in cat.items():
        if texto in datos["nombre"].lower() or texto in datos["categoria"].lower():
            print(
                f"ID: {id_prod} | "
                f"Nombre: {datos['nombre']} | "
                f"Categoría: {datos['categoria']} | "
                f"Precio: ${datos['precio']}"
            )
            encontrados = True

    if not encontrados:
        print("No se encontraron productos con ese criterio.")