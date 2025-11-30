# Ejemplo 34: finally asegurando liberación de lock

from threading import Lock

lock_global = Lock()

def seccion_critica() -> None:
    lock_global.acquire()
    try:
        # trabajo crítico
        ...
    finally:
        lock_global.release()

# Ejemplo 35: with con manager personalizado para locks

class LockManager:
    def __init__(self, lock: Lock):
        self.lock = lock

    def __enter__(self):
        self.lock.acquire()
        return self.lock

    def __exit__(self, tipo, valor, traza):
        self.lock.release()
        return False


def seccion_critica_with() -> None:
    with LockManager(lock_global):
        # trabajo crítico
        ...
