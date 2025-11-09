# 7.3 – Resolución de conflictos de merge

Un **conflicto** ocurre cuando dos ramas cambian la **misma parte** del mismo archivo.

Ejemplo típico:

- `main` cambia la línea 10 de `index.html`.
- `feature/header` también cambia la línea 10 de `index.html`.
- Al hacer `git merge feature/header` desde `main`, Git no sabe cuál versión dejar.

---

## 1. Detectar el conflicto

Al hacer merge:

```bash
git merge feature/header
```

Git mostrará algo como:

```txt
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.
```

---

## 2. Ver el conflicto en el archivo

Dentro de `index.html` verás bloques especiales:

```txt
<<<<<<< HEAD
<h1>Sitio web de ventas</h1>
=======
<h1>Sitio web institucional</h1>
>>>>>>> feature/header
```

Significa:

- Entre `<<<<<<< HEAD` y `=======` está la versión de la rama donde estás (por ejemplo, `main`).
- Entre `=======` y `>>>>>>> feature/header` está la versión de la rama que estás uniendo.

---

## 3. Resolver el conflicto

Edita el archivo y deja SOLO la versión correcta. Por ejemplo:

```html
<h1>Sitio web institucional</h1>
```

Luego:

```bash
git add index.html
git commit -m "Resuelve conflicto en el título del header"
```

El merge queda completado.

---

## 4. Resumen para explicar en clase

1. Un conflicto NO es un error grave, es una situación que requiere decisión humana.
2. Git marca las partes en conflicto dentro del archivo.
3. El desarrollador elige qué quedará en la versión final.
4. Se hace `add` y luego `commit` para finalizar el merge.
