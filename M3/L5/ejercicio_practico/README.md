Actividad N° 5 – Explorando Estructuras de Datos
Módulo: Fundamentos de Programación en Python

1. ¿Cuál estructura te pareció más flexible?

La estructura que me pareció más flexible es la LISTA (list), porque:

- Permite agregar, eliminar y modificar elementos fácilmente.
- Mantiene el orden de inserción, por lo que puedo acceder a elementos
  por índice (posición).
- Acepta tipos de datos mixtos si es necesario (por ejemplo, números
  y cadenas en la misma lista).
- Tiene muchos métodos útiles (append, remove, insert, sort, etc.) que
  facilitan el trabajo con colecciones de datos.

En resumen, la lista es muy versátil y se adapta bien a una gran variedad
de problemas donde necesito una colección ordenada y mutable.

2. ¿Para qué tipo de problema usarías un diccionario en lugar de una lista?

Usaría un diccionario en lugar de una lista cuando necesito:

- Asociar un valor a una CLAVE descriptiva (por ejemplo "nombre",
  "edad", "correo") y no solo a una posición numérica.
- Buscar información de manera rápida a partir de una clave, sin tener
  que recorrer toda la estructura.
- Modelar registros o entidades con varios atributos, como un estudiante
  (nombre, edad, carrera, promedio) o un producto (id, precio, stock, etc.).

Por ejemplo, para guardar y acceder a datos de usuarios por su id, un
diccionario es mucho más apropiado que una lista, porque puedo hacer
algo como usuarios[id_usuario] y obtener directamente la información
asociada a esa clave.
