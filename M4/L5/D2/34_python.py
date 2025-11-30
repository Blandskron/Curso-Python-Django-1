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
