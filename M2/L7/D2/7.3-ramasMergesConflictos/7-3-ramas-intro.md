# 7.3 – Introducción a las ramas

Una **rama** es una línea de desarrollo dentro del mismo repositorio.

La rama principal suele llamarse:

- `main` o
- `master` (nombre más antiguo)

---

## 1. Ver ramas existentes

```bash
git branch
```

Muestra algo como:

```txt
* main
```

El asterisco indica la rama actual.

---

## 2. Crear y cambiar a una nueva rama

```bash
git branch feature/navbar
git checkout feature/navbar
```

Atajo:

```bash
git checkout -b feature/navbar
```

Esto crea la rama `feature/navbar` y te mueve a ella.

---

## 3. Trabajar en una rama

A partir de aquí:

- Editas archivos
- Haces commits normalmente

```bash
git add .
git commit -m "Agrega navbar responsive"
```

Los cambios quedan registrados en la rama `feature/navbar`, sin afectar `main` hasta que hagas un **merge**.
