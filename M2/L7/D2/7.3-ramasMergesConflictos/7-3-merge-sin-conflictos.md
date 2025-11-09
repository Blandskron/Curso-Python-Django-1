# 7.3 – Merge entre ramas (sin conflictos)

Supongamos:

- Rama principal: `main`
- Rama de trabajo: `feature/navbar`

---

## 1. Asegurarse de que `feature/navbar` está lista

En `feature/navbar`:

```bash
git status
git log --oneline
```

Confirma que todo está commiteado.

---

## 2. Volver a la rama principal

```bash
git checkout main
```

Traer cambios remotos (si corresponde):

```bash
git pull
```

---

## 3. Hacer el merge

```bash
git merge feature/navbar
```

Si no hay conflictos, verás algo como:

```txt
Updating 123abcd..789efgh
Fast-forward
 nav.html | 1 +
 1 file changed, 1 insertion(+)
```

La rama `main` ahora incluye todos los cambios de `feature/navbar`.

---

## 4. Opcional: borrar la rama de trabajo

```bash
git branch -d feature/navbar
```

Esto elimina la rama **local** (no la remota), cuando ya está fusionada.
