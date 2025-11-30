Actividad N° 6 – Lectura y Escritura de Archivos en Python
Módulo: Programación Avanzada en Python

Archivos incluidos
------------------

- manejo_archivos.py
- datos.txt (generado por el propio script)

Descripción de manejo_archivos.py
----------------------------------

El script implementa en orden los 5 puntos de la actividad:

1) Escribir en un archivo (write, modo "w")

   - Función: escribir_archivo_inicial()
   - Crea (o sobrescribe) datos.txt.
   - Escribe 3 líneas usando write().
   - Se usa with open(..., "w", ...) para asegurar el cierre automático.
2) Leer el archivo completo

   - Función: leer_archivo_completo()
   - Abre datos.txt en modo lectura ("r").
   - Usa read() para leer todo el contenido y lo muestra por pantalla.
3) Leer línea por línea

   - Función: leer_linea_por_linea()
   - Abre datos.txt en modo lectura.
   - Usa readline() para leer solo la primera línea.
   - Luego recorre el resto del archivo con un ciclo for para mostrar
     línea por línea.
4) Añadir contenido (modo append)

   - Función: agregar_con_append()
   - Abre datos.txt en modo append ("a") y agrega una nueva línea.
   - Después abre el archivo en modo lectura para comprobar que la línea
     se agregó correctamente y muestra todo el contenido actualizado.
5) Atributos y cierre de archivo

   - Función: mostrar_atributos_y_cierre()
   - Abre datos.txt de forma "manual" (sin with).
   - Muestra:
     * f.name
     * f.mode
     * f.closed (antes de cerrar)
   - Llama a f.close() y vuelve a mostrar f.closed para evidenciar
     que el archivo quedó cerrado correctamente.

Preguntas teóricas
-------------------

1. ¿Qué diferencia notaste entre write() y append()?

- write() (cuando se usa con el modo "w"):

  * Crea el archivo si no existe.
  * Si el archivo ya existe, BORRA el contenido previo y escribe desde cero.
  * Es útil cuando queremos "empezar de nuevo" el archivo.
- append() (modo "a"):

  * Crea el archivo si no existe.
  * Si el archivo existe, CONSERVA todo su contenido y solo agrega
    texto al final.
  * Es útil para llevar registros (logs, bitácoras, historiales) en los
    que no queremos perder lo ya escrito.

En la práctica, la diferencia clave es que "w" sobrescribe el archivo,
mientras que "a" mantiene lo anterior y solo añade más información.

2. ¿Qué ventaja tiene usar with open(...) frente a abrir y cerrar manualmente?

Usar with open(...) tiene varias ventajas:

- Cierre automático del archivo:
  No tenemos que preocuparnos de llamar a close(). Cuando el bloque
  with termina, Python cierra el archivo automáticamente, incluso si
  ocurre una excepción dentro del bloque.
- Menos errores de programación:
  Es fácil olvidarse de cerrar un archivo al usar la forma manual
  (f = open(...); f.close()). Con with se reduce el riesgo de dejar
  archivos abiertos, lo que puede causar problemas de recursos
  (muchos archivos abiertos al mismo tiempo) o bloqueos de acceso.
- Código más limpio y legible:
  El patrón with deja claro dónde empieza y termina el uso del recurso
  (el archivo), haciendo el código más fácil de entender y mantener.

Por estas razones, with open(...) se considera una buena práctica para
la gran mayoría de operaciones de lectura/escritura de archivos.
