# 7.4 – Conflictos al sincronizar con repositorios remotos

Es posible tener conflictos al hacer:

- `git pull`
- `git push`

---

## 1. Conflictos al hacer `git pull`

Situación típica:

1. Hiciste commits locales en `main`.
2. Alguien más hizo commits en `main` y los subió a GitHub.
3. Sin actualizar, intentas hacer `git push`.

Git responde algo como:

```txt
To https://github.com/usuario/mi-proyecto.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs
```

Solución:

```bash
git pull
```

Si hay cambios incompatibles, puede aparecer un **conflicto** de merge, que se resuelve igual que en el punto 7.3.

---

## 2. Conflictos al hacer `git push`

Si alguien subió cambios antes que tú:

- Git te pedirá **actualizar primero** (`git pull`).
- Luego de resolver conflictos y hacer commit, podrás:

```bash
git push
```

---

## 3. Buenas prácticas para evitar problemas

- Hacer `git pull` al comenzar a trabajar.
- Hacer commits pequeños y con mensajes claros.
- No trabajar muchas personas directamente sobre `main`; usar ramas y Pull Requests.
