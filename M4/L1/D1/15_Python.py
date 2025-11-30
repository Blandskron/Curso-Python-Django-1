# Ejemplo 15: Abstracción con clase base "interfaz"

from abc import ABC, abstractmethod

class RepositorioUsuarios(ABC):
    @abstractmethod
    def guardar(self, usuario):
        ...

    @abstractmethod
    def obtener(self, id_usuario):
        ...

class RepoMemoria(RepositorioUsuarios):
    def __init__(self):
        self._datos = {}

    def guardar(self, usuario):
        self._datos[usuario["id"]] = usuario

    def obtener(self, id_usuario):
        return self._datos.get(id_usuario)

class RepoArchivo(RepositorioUsuarios):
    def __init__(self, ruta):
        self._ruta = ruta

    def guardar(self, usuario):
        import json, os
        datos = {}
        if os.path.exists(self._ruta):
            with open(self._ruta, "r", encoding="utf8") as f:
                datos = json.load(f)
        datos[usuario["id"]] = usuario
        with open(self._ruta, "w", encoding="utf8") as f:
            import json
            json.dump(datos, f)

    def obtener(self, id_usuario):
        import json, os
        if not os.path.exists(self._ruta):
            return None
        with open(self._ruta, "r", encoding="utf8") as f:
            datos = json.load(f)
        return datos.get(id_usuario)

def procesar_repo(repo: RepositorioUsuarios):
    repo.guardar({"id": "1", "nombre": "Ana"})
    print(repo.obtener("1"))

procesar_repo(RepoMemoria())
# procesar_repo(RepoArchivo("usuarios.json"))
