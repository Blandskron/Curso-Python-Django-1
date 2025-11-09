# 7.5 – Ejemplo de flujo de trabajo colaborativo con Git y GitHub

Imaginemos un equipo de 3 personas trabajando en el mismo repositorio.

---

## 1. Preparación inicial

1. La persona que lidera el proyecto crea el repo en GitHub.
2. El resto del equipo clona el repositorio:

   ```bash
   git clone https://github.com/empresa/proyecto-web.git
   ```

---

## 2. Trabajo diario (por cada integrante)

1. Actualizar la rama principal:

   ```bash
   git checkout main
   git pull
   ```

2. Crear una rama para una nueva tarea:

   ```bash
   git checkout -b feature/validar-login
   ```

3. Hacer cambios y commits:

   ```bash
   git add .
   git commit -m "Agrega validación básica al formulario de login"
   ```

4. Enviar la rama a GitHub:

   ```bash
   git push -u origin feature/validar-login
   ```

5. Crear un Pull Request en GitHub desde `feature/validar-login` → `main`.

---

## 3. Revisión y merge

- Otro integrante revisa el PR:
  - Comenta si ve problemas.
  - Sugiere mejoras.
- El autor corrige y hace nuevos commits en la misma rama.
- Finalmente, alguien aprueba el PR y hace **Merge**.

---

## 4. Actualización para todos

Después del merge:

```bash
git checkout main
git pull
```

Todos reciben los cambios integrados a `main`.

---

Este flujo:

- Evita que se rompa `main`.
- Registra claramente quién hizo cada cambio.
- Deja un historial limpio de qué PR introdujo qué funcionalidad.
