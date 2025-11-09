# 7.1 – ¿Qué es un Sistema de Control de Versiones?

Un **Sistema de Control de Versiones (VCS)** es una herramienta que nos permite:

- Guardar el **historial** de cambios de un proyecto.
- Recuperar versiones anteriores cuando algo sale mal.
- Trabajar **en equipo** sin pisar el trabajo de los demás.
- Saber **quién cambió qué y cuándo**.

El sistema de control de versiones que usaremos es **Git**.

---

## ¿Por qué NO alcanza con guardar archivos sueltos?

Mala práctica típica:

- `index.html`
- `index_final.html`
- `index_final_ahora_sí.html`
- `index_final_definitivo_2.html`

Problemas de este enfoque:

1. No hay historial claro de cambios.
2. No sabemos qué cambió entre archivos.
3. Es fácil borrar o sobreescribir cosas importantes.
4. Es muy difícil trabajar con otras personas en el mismo proyecto.

---

## ¿Qué nos da un VCS como Git?

- **Histórico de cambios** en forma de _commits_.
- Poder hacer **experimentos** en ramas sin romper la versión estable.
- Volver a una versión anterior si un cambio rompe el proyecto.
- Mezclar (hacer *merge*) el trabajo de distintas personas.
- Resolver conflictos de forma controlada.

---

## Conceptos clave

- **Repositorio**: carpeta del proyecto donde Git guarda el historial.
- **Commit**: “foto” del estado de los archivos en un momento dado.
- **Rama (branch)**: línea de desarrollo paralela (por ejemplo, `main` y `feature/login`).
- **Merge**: unión de dos ramas.
- **Conflicto**: cuando dos cambios tocan la misma parte del mismo archivo.

Git no solo guarda archivos: guarda **la historia completa del proyecto**.
