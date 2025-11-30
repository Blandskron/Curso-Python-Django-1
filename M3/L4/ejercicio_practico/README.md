Actividad N° 4 – Estructuras Repetitivas en Python
Módulo: Fundamentos de Programación en Python

1. ¿Cuál fue la diferencia principal que notaste entre for y while?

La diferencia principal es que el ciclo for normalmente se usa cuando conocemos
de antemano la cantidad de iteraciones (por ejemplo, recorrer una lista, un
rango de números o cualquier colección). El for “sabe” cuántos elementos hay y
se detiene automáticamente cuando los recorre todos.

En cambio, while se usa con más frecuencia cuando no conocemos exactamente
cuántas veces se repetirá el ciclo y dependemos de una condición lógica que
puede cambiar dentro del propio ciclo. En while es responsabilidad del
programador asegurarse de que la condición llegue a ser falsa en algún
momento, para evitar ciclos infinitos.

2. ¿Te pareció útil el uso de break y continue? ¿Por qué?

Sí, break y continue son muy útiles porque permiten controlar el flujo de los
ciclos de forma más precisa:

- break permite “cortar” un ciclo antes de que termine de forma natural,
  por ejemplo, cuando encontramos un valor especial o una condición que indica
  que no es necesario seguir iterando.
- continue permite saltar una iteración específica sin detener todo el ciclo.
  Es útil cuando queremos omitir ciertos casos (por ejemplo, un valor
  prohibido o un dato que no queremos procesar) pero queremos seguir con las
  demás iteraciones.

Gracias a break y continue el código se vuelve más expresivo y es más fácil
modelar la lógica real de los problemas que resolvemos.
