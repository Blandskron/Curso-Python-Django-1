"""
Módulo: Programación Avanzada en Python
Actividad N° 1 – Introducción a la Programación Orientada a Objetos

Este archivo resuelve los puntos:
1) Exploración teórica
2) Definición de una clase simple
3) Diferenciar conceptos
4) Principios de POO (abstracción y encapsulamiento)
"""

# ============================================================
# 1. EXPLORACIÓN TEÓRICA
# ============================================================
# ¿Qué es la programación orientada a objetos?
# Es un paradigma de programación que organiza el código en torno a
# "objetos" que combinan datos (atributos) y funciones (métodos).
# Cada objeto representa una entidad del mundo real o del dominio del
# problema, con sus características y comportamientos asociados.
#
# ¿En qué se diferencia de la programación estructurada?
# La programación estructurada se organiza principalmente en funciones
# y estructuras de control (if, while, for) que operan sobre datos
# separados, mientras que en la programación orientada a objetos los
# datos y las operaciones se agrupan dentro de clases y objetos.
# Esto facilita la modularidad, la reutilización de código y el
# mantenimiento de proyectos más grandes.
#
# Ejemplo de la vida cotidiana donde se vea reflejado el concepto de objeto:
# Un "Auto" es un objeto: tiene atributos como color, marca, modelo,
# año, y métodos o comportamientos como arrancar(), frenar(),
# acelerar(), girar().


# ============================================================
# 2. DEFINICIÓN DE UNA CLASE SIMPLE
# ============================================================

class Perro:
    """
    Versión inicial de la clase Perro (sin encapsulamiento estricto).
    Más abajo se verá una versión modificada con atributos "protegidos".
    """

    def __init__(self, nombre: str, edad: int, raza: str) -> None:
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

    def ladrar(self) -> None:
        print("¡Guau!")


# Crear una instancia de la clase Perro y llamar al método ladrar()
perro_1 = Perro(nombre="Firulais", edad=3, raza="Mestizo")
perro_1.ladrar()


# ============================================================
# 3. DIFERENCIAR CONCEPTOS
# ============================================================
# Clase, instancia y objeto:
# - Clase: es el "molde" o plantilla que define qué atributos y
#   métodos tendrán los objetos (por ejemplo, la clase Perro).
# - Instancia: es un objeto concreto creado a partir de una clase.
#   Cuando hacemos Perro("Firulais", 3, "Mestizo") estamos creando
#   una instancia.
# - Objeto: en este contexto es sinónimo de instancia; es la entidad
#   individual que existe en memoria y que tiene su propio estado.
#
# Atributo y estado:
# - Atributo: es una variable asociada a un objeto o clase que guarda
#   datos (por ejemplo, nombre, edad, raza).
# - Estado: es el conjunto de valores actuales de los atributos de un
#   objeto en un momento dado (por ejemplo, nombre="Firulais",
#   edad=3, raza="Mestizo").
#
# Método y comportamiento:
# - Método: es una función definida dentro de una clase que describe
#   una operación que el objeto puede realizar (por ejemplo, ladrar()).
# - Comportamiento: es la forma en que un objeto actúa o reacciona,
#   y se manifiesta a través de la ejecución de sus métodos.


# ============================================================
# 4. PRINCIPIOS DE POO: ENCAPSULAMIENTO Y ABSTRACCIÓN
# ============================================================

class PerroEncapsulado:
    """
    Versión de la clase Perro con atributos encapsulados mediante
    el prefijo de convención _ (atributos "protegidos").
    """

    def __init__(self, nombre: str, edad: int, raza: str) -> None:
        # Encapsulamiento básico usando el prefijo _
        self._nombre = nombre
        self._edad = edad
        self._raza = raza

    def ladrar(self) -> None:
        print("¡Guau!")

    def mostrar_info(self) -> str:
        """
        Devuelve el estado del objeto en forma de texto.
        """
        return f"Perro(nombre={self._nombre}, edad={self._edad}, raza={self._raza})"


perro_2 = PerroEncapsulado(nombre="Luna", edad=5, raza="Labrador")
print(perro_2.mostrar_info())


# Abstracción (comentario teórico):
# La abstracción consiste en resaltar solo las características
# importantes de un objeto y ocultar los detalles internos que no
# son necesarios para el usuario de la clase.
#
# En este ejemplo:
# - Como usuario de la clase PerroEncapsulado solo necesito saber cómo
#   crear un perro (qué datos pasar al constructor) y cómo interactuar
#   con él a través de métodos como ladrar() o mostrar_info().
# - No necesito conocer cómo están almacenados internamente los
#   atributos ni cómo exactamente se construye la cadena de texto en
#   mostrar_info().
# - De esta forma, la clase abstrae los detalles internos y expone una
#   interfaz sencilla para trabajar con el objeto.
