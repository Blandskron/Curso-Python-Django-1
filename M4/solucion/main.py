"""
Punto de entrada principal de la aplicación.

Este módulo inicia la ejecución del sistema de e-commerce
por consola, delegando el control a la clase Tienda.
"""

from models.tienda import Tienda


def main():
    """
    Función principal que inicia la aplicación.
    """
    tienda = Tienda()
    tienda.ejecutar()


# --- Ejecutar ---
if __name__ == "__main__":
    main()
