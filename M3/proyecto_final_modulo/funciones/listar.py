def listar_productos(cat: dict) -> None:
    print("\n--- CATÁLOGO DE PRODUCTOS ---")
    for id_prod, datos in cat.items():
        print(
            f"ID: {id_prod} | "
            f"Nombre: {datos['nombre']} | "
            f"Categoría: {datos['categoria']} | "
            f"Precio: ${datos['precio']}"
        )