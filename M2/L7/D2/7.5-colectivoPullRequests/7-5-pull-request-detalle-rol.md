# 7.5 – Rol de los Pull Requests en el trabajo en equipo

En un equipo, los Pull Requests ayudan a:

---

## 1. Revisar código (Code Review)

- Otra persona del equipo revisa:
  - Legibilidad
  - Correcta implementación
  - Estilo de código
- Se pueden dejar comentarios línea por línea.

---

## 2. Documentar decisiones

Cada PR:

- Tiene un título descriptivo.
- Explica qué problema soluciona.
- Puede estar ligado a un Issue de GitHub.

Ejemplo de título:

> `Agrega validación al formulario de registro (#42)`

---

## 3. Proteger la rama principal

En muchos equipos:

- No se permite hacer `push` directo a `main`.
- Solo se aceptan cambios vía Pull Requests.
- GitHub puede exigir:
  - Que haya al menos 1 o 2 revisores que aprueben.
  - Que las pruebas automáticas pasen (CI verde).

Esto mantiene la rama principal **estable y confiable**.
