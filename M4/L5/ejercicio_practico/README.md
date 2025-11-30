Actividad N° 5 – Captura y Control de Errores en Python
Módulo: Programación Avanzada en Python

Archivos incluidos
------------------

- manejo_errores.py

Descripción de manejo_errores.py
---------------------------------

El archivo implementa cuatro partes principales:

1) Captura básica de errores

   - Función: dividir_numeros()
   - Pide dos números al usuario y los divide.
   - Usa try/except para capturar:
     * ZeroDivisionError: si el segundo número es 0.
     * ValueError: si el usuario no ingresa un número válido.
   - Usa else para mostrar el resultado cuando no hay errores.
   - Usa finally para indicar que la operación de división finalizó.
2) Múltiples excepciones

   - Dentro de dividir_numeros() se manejan explícitamente:
     * ValueError (entrada no numérica).
     * ZeroDivisionError (división por cero).
   - Esto permite mensajes de error más claros para cada caso.
3) Excepciones personalizadas

   - Clase: EdadInvalidaError (hereda de Exception).
   - Función: validar_edad(edad)
     * Lanza EdadInvalidaError si edad < 0.
   - Función: demo_validar_edad()
     * Pide una edad al usuario.
     * Maneja:
       - ValueError (si no se ingresa un entero).
       - EdadInvalidaError (si la edad es negativa).
4) Limpieza de recursos con finally

   - Función: demo_archivo_simulado()
   - Simula la apertura de un archivo con:
     * print("Abriendo archivo...")
   - Dentro del bloque try puede ocurrir un error simulado (RuntimeError).
   - El bloque finally siempre ejecuta:
     * print("Cerrando archivo...")
   - De esta forma se representa la limpieza de recursos aunque haya error.

Preguntas del README
--------------------

1. ¿Qué tipo de error crees que es más común en programas reales?

En programas reales, los errores más comunes suelen ser:

- ValueError o errores de validación de datos:
  Muchas veces el usuario ingresa información en formatos incorrectos
  (texto donde se esperaba un número, fechas mal escritas, etc.) o
  los datos provenientes de archivos / APIs no cumplen las reglas
  de negocio.
- Errores de tipo (TypeError):
  Intentar operar con tipos incompatibles (por ejemplo, sumar texto
  con número) también es muy frecuente en código con poca validación.
- Errores de índice o clave (IndexError, KeyError):
  Ocurren al acceder a posiciones que no existen en listas o claves
  ausentes en diccionarios, sobre todo cuando se asume que los datos
  siempre estarán completos.

La división por cero (ZeroDivisionError) también es común en cierto
tipo de cálculos, pero en la práctica el conjunto de errores de
validación de datos suele ser el más frecuente.

2. ¿Por qué es importante manejar excepciones?

Manejar excepciones es importante porque:

- Evita que el programa termine de forma brusca:
  Si una excepción no se captura, Python detiene la ejecución y
  muestra un traceback. Esto puede ser aceptable en un script
  de pruebas, pero no en una aplicación que usan otras personas.
- Permite entregar mensajes claros al usuario:
  En lugar de mostrar errores técnicos, podemos informar en lenguaje
  comprensible qué salió mal (por ejemplo, "No se puede dividir por
  cero" o "Debes ingresar un número").
- Mejora la robustez del software:
  Un programa que anticipa escenarios de error (entradas inválidas,
  fallos de red, archivos inexistentes, etc.) y los maneja de forma
  apropiada es más confiable y profesional.
- Facilita la limpieza de recursos:
  Con bloques finally y context managers (with) podemos asegurarnos
  de cerrar archivos, conexiones o liberar recursos aunque ocurra
  una excepción, evitando fugas de recursos o bloqueos.

En resumen, el manejo de excepciones es una parte esencial para crear
programas seguros, estables y amigables para el usuario final.
