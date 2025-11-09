# 7.5 – ¿Qué es un Pull Request?

Un **Pull Request (PR)** es una propuesta de cambios que se envía a un repositorio remoto (por ejemplo, en GitHub).

Sirve para:

- Revisar código antes de mezclarlo con la rama principal (`main`).
- Discutir cambios (comentarios).
- Ejecutar pruebas automáticas (CI/CD).

---

## Flujo típico con Pull Requests

1. Crear una rama nueva:

   ```bash
   git checkout -b feature/form-contacto
   ```

2. Hacer cambios y commits en esa rama.

3. Enviar la rama a GitHub:

   ```bash
   git push -u origin feature/form-contacto
   ```

4. En GitHub:
   - Crear un **Pull Request** desde `feature/form-contacto` hacia `main`.
   - Asignar revisores.
   - Discutir y corregir si es necesario.

5. Cuando todo está OK:
   - Se hace **Merge** del PR.
   - La rama se puede borrar.

Este flujo permite mantener `main` siempre estable y revisada.
