"""
Módulo 4 – Programación Avanzada en Python
Actividad N° 2 – Implementación de Clases, Métodos y Relaciones

Contenido:
1. Clase Libro con constructor y método mostrar_info().
2. Métodos accesadores (get_) y mutadores (set_) para título y año.
3. Simulación de sobrecarga de métodos con resumen().
4. Colaboración entre objetos (Libro <-> Autor).
5. Composición (Libro -> Editorial).
"""


# ============================================================
# 4. COLABORACIÓN ENTRE OBJETOS
# ============================================================
# Clase Autor: será usada por Libro como relación de colaboración.
# La COLABORACIÓN ocurre porque Libro recibe un Autor ya creado desde afuera.


class Autor:
    def __init__(self, nombre: str, pais: str) -> None:
        self.nombre = nombre
        self.pais = pais

    def mostrar_autor(self) -> str:
        return f"{self.nombre} ({self.pais})"


# ============================================================
# 5. COMPOSICIÓN
# ============================================================
# Clase Editorial: Libro CREARÁ internamente una instancia de Editorial.
# Esta es una relación de COMPOSICIÓN porque la Editorial del libro
# "nace" en el constructor de Libro y está fuertemente ligada a él.


class Editorial:
    def __init__(self, nombre: str, ciudad: str) -> None:
        self.nombre = nombre
        self.ciudad = ciudad

    def mostrar_editorial(self) -> str:
        return f"{self.nombre} - {self.ciudad}"


# ============================================================
# 1, 2 y 3. CLASE LIBRO: CONSTRUCTOR, GET/SET Y RESUMEN
# ============================================================


class Libro:
    """
    Clase que representa un libro con:
      - título
      - autor (objeto Autor)  -> colaboración
      - año de publicación
      - editorial (objeto Editorial) -> composición
    """

    def __init__(
        self,
        titulo: str,
        autor: Autor,
        anio_publicacion: int,
        nombre_editorial: str,
        ciudad_editorial: str,
    ) -> None:
        # Atributos "internos" con convención de subrayado
        self._titulo = titulo
        self._autor = autor
        self._anio_publicacion = anio_publicacion

        # COMPOSICIÓN: el objeto Editorial se crea DENTRO del constructor
        self._editorial = Editorial(nombre_editorial, ciudad_editorial)

    # --------------------------------------------------------
    # 2. MÉTODOS ACCESADORES (GET) Y MUTADORES (SET)
    # --------------------------------------------------------
    def get_titulo(self) -> str:
        return self._titulo

    def set_titulo(self, nuevo_titulo: str) -> None:
        # Podríamos validar aquí largo mínimo, etc.
        self._titulo = nuevo_titulo

    def get_anio_publicacion(self) -> int:
        return self._anio_publicacion

    def set_anio_publicacion(self, nuevo_anio: int) -> None:
        # Validación mínima de año: ejemplo, no aceptar negativos.
        if nuevo_anio > 0:
            self._anio_publicacion = nuevo_anio

    # --------------------------------------------------------
    # 1. MÉTODO mostrar_info()
    # --------------------------------------------------------
    def mostrar_info(self) -> None:
        """
        Muestra toda la información del libro,
        incluyendo colaboración (autor) y composición (editorial).
        """
        print("=== Información del Libro ===")
        print(f"Título: {self._titulo}")
        print(f"Año de publicación: {self._anio_publicacion}")
        # Colaboración: se usa el objeto Autor que viene de fuera
        print(f"Autor: {self._autor.mostrar_autor()}")
        # Composición: se usa el objeto Editorial creado internamente
        print(f"Editorial: {self._editorial.mostrar_editorial()}")

    # --------------------------------------------------------
    # 3. "SOBRECARGA" DE MÉTODO resumen()
    # --------------------------------------------------------
    def resumen(self, texto: str | None = None) -> None:
        """
        Simula sobrecarga de métodos:
          - Sin parámetro -> mensaje por defecto.
          - Con texto -> imprime el resumen.
        """
        if texto is None:
            print("Libro sin resumen disponible.")
        else:
            print("Resumen del libro:")
            print(texto)


# ============================================================
# PROGRAMA PRINCIPAL (DEMO)
# ============================================================


def main() -> None:
    # Crear un autor (colaboración)
    autor_principal = Autor(nombre="Gabriel García Márquez", pais="Colombia")

    # Crear un libro utilizando:
    # - autor_principal (colaboración)
    # - datos de editorial (composición dentro del constructor)
    libro_1 = Libro(
        titulo="Cien años de soledad",
        autor=autor_principal,
        anio_publicacion=1967,
        nombre_editorial="Editorial Sudamericana",
        ciudad_editorial="Buenos Aires",
    )

    # Mostrar información inicial
    libro_1.mostrar_info()
    print()

    # Uso de getters y setters (accesadores y mutadores)
    print("Título actual (get_titulo):", libro_1.get_titulo())
    print("Año actual (get_anio_publicacion):", libro_1.get_anio_publicacion())

    print("\nModificando título y año usando set_titulo y set_anio_publicacion...")
    libro_1.set_titulo("Cien años de soledad (Edición Aniversario)")
    libro_1.set_anio_publicacion(2017)

    # Mostrar nuevamente la información del libro para ver cambios
    print()
    libro_1.mostrar_info()
    print()

    # Demostración de la "sobrecarga" de resumen()
    print("--- Demostración de resumen() sin texto ---")
    libro_1.resumen()

    print("\n--- Demostración de resumen() con texto ---")
    texto_resumen = (
        "Novela que narra la historia de la familia Buendía a lo largo de varias "
        "generaciones en el mítico pueblo de Macondo."
    )
    libro_1.resumen(texto_resumen)


if __name__ == "__main__":
    main()
