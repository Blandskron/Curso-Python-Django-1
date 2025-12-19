"""
Módulo usuario.

Define las clases relacionadas con los usuarios del sistema de e-commerce:
- Usuario: clase base común
- Cliente: usuario con carrito de compras
- Admin: usuario administrador del sistema
"""

import re
from ..carrito import Carrito


class Usuario:
    """
    Clase base que representa a un usuario del sistema.
    """

    def __init__(self, nombre, email):
        self.nombre = str(nombre)

        if not self._email_valido(email):
            raise ValueError("Email inválido.")

        self.email = str(email)

    def _email_valido(self, email: str) -> bool:
        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(patron, email) is not None


class Cliente(Usuario):
    """
    Representa a un cliente del e-commerce.

    Hereda de Usuario y agrega un carrito de compras.
    """

    def __init__(self, nombre, email):
        """
        Inicializa un cliente con un carrito vacío.

        Args:
            nombre (str): Nombre del cliente.
            email (str): Email del cliente.
        """
        # Inicialización de atributos heredados
        super().__init__(nombre, email)

        # Cada cliente posee su propio carrito
        self.carrito = Carrito()


class Admin(Usuario):
    """
    Representa a un usuario administrador del sistema.

    Por ahora no agrega comportamiento adicional,
    pero existe para diferenciar roles y permisos.
    """

    def __init__(self, nombre, email):
        """
        Inicializa un administrador.

        Args:
            nombre (str): Nombre del administrador.
            email (str): Email del administrador.
        """
        super().__init__(nombre, email)
