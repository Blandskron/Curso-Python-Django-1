# 7.1 – Analogías para entender Git

A veces Git se entiende mejor con analogías del mundo real.

---

## Git como máquina del tiempo

Imagina que tu proyecto es un documento importante.

- Cada cierto tiempo, sacas una **foto** del documento y la guardas con fecha.
- Si rompes el original, puedes volver a una foto anterior.

En Git, esas “fotos” son los **commits**.

```txt
commit 1 → Versión inicial de index.html
commit 2 → Agregué estilos CSS
commit 3 → Corregí el formulario de contacto
```

Puedes viajar en el tiempo a cualquiera de esos commits.

---

## Git como “historial de cambios super avanzado”

Comparado con el historial de Word o Google Docs:

- Git guarda cambios de **muchos archivos** a la vez.
- Cada cambio tiene:
  - Autor
  - Fecha
  - Mensaje descriptivo
- Puedes ver exactamente qué líneas cambiaron.

---

## Git como “coordinador de equipo”

En un equipo:

- Cada persona trabaja en su **rama**.
- Git ayuda a **mezclar cambios** sin perder trabajo.
- Si dos personas cambian la misma parte del archivo, Git marca un **conflicto** para que alguien lo resuelva a mano.

Control de versiones = herramienta **obligatoria** cuando hay más de una persona tocando el mismo código.
