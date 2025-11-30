# Ejemplo 32 corregido: API que devuelve resultado o lanza excepción

class RecursoNoDisponibleError(Exception):
    pass


def obtener_usuario(id_usuario: int) -> dict:
    datos = {1: {"nombre": "Ana"}}
    try:
        return datos[id_usuario]
    except KeyError:
        raise RecursoNoDisponibleError("Usuario no encontrado")
