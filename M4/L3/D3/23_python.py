# Ejemplo 23: Type Hints con Optional y List
from typing import Optional

class Nodo:
    def __init__(self, valor: int, siguiente: Optional["Nodo"] = None):
        self.valor = valor
        self.siguiente = siguiente  # lista enlazada simple
