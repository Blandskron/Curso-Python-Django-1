Actividad N° 2 – Implementación de Clases, Métodos y Relaciones
Módulo: Programación Avanzada en Python

Archivos incluidos
------------------

- poo_avanzado.py

Contenido de poo_avanzado.py
----------------------------

1) Clase Libro:

   - Atributos:
     * _titulo
     * _autor (objeto Autor)  -> relación de colaboración
     * _anio_publicacion
     * _editorial (objeto Editorial) -> relación de composición
   - Constructor __init__():
     * Recibe título, Autor, año de publicación, nombre y ciudad de la editorial.
     * Crea internamente la instancia de Editorial (composición).
   - Métodos accesadores y mutadores:
     * get_titulo() / set_titulo(nuevo_titulo)
     * get_anio_publicacion() / set_anio_publicacion(nuevo_anio)
   - Método mostrar_info():
     * Imprime título, año, nombre y país del autor,
       y nombre y ciudad de la editorial.
   - Método resumen(texto=None):
     * Si texto es None -> "Libro sin resumen disponible".
     * Si texto tiene contenido -> imprime el resumen.
     * Esto simula la sobrecarga de métodos usando un parámetro opcional.
2) Clase Autor:

   - Atributos: nombre, pais.
   - Método mostrar_autor() que devuelve un texto "nombre (pais)".
   - Se pasa como parámetro al constructor de Libro, representando
     una relación de colaboración, porque el autor es creado fuera
     y se reutiliza en el libro.
3) Clase Editorial:

   - Atributos: nombre, ciudad.
   - Método mostrar_editorial() que devuelve un texto con ambos datos.
   - La instancia se crea dentro del constructor de Libro, por lo que
     la relación es de composición (la editorial del libro "nace" y
     vive dentro del objeto Libro).
4) main():

   - Crea un Autor.
   - Crea un Libro usando ese Autor y datos de la editorial.
   - Muestra la información del libro.
   - Modifica el título y el año usando los setters.
   - Vuelve a mostrar la información para apreciar los cambios.
   - Llama a resumen() sin texto y con texto para demostrar la
     "sobrecarga" mediante parámetros por defecto.

Reflexión
----------

La relación que me pareció más fácil de implementar fue la COLABORACIÓN,
porque simplemente paso un objeto ya creado (Autor) al constructor de
Libro y lo guardo como un atributo. Esto se siente muy natural, ya que
puedo reutilizar el mismo autor en varios libros si lo necesito.

La COMPOSICIÓN requiere pensar un poco más en el ciclo de vida de los
objetos, porque la clase "contenedora" (Libro) es responsable de crear
la instancia interna (Editorial). Sin embargo, una vez entendido el
concepto, ayuda a modelar mejor los casos donde un objeto "forma parte"
de otro y no tiene mucho sentido por separado.
