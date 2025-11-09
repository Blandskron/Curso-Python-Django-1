# 7.2 – Restaurar archivos y deshacer cambios con Git

Además de guardar versiones, Git nos permite **volver atrás**.

---

## 1. Ver qué cambió

```bash
git status
```

Si un archivo aparece como `modified`:

```bash
git diff nombre-del-archivo
```

Muestra línea por línea qué cambió.

---

## 2. Deshacer cambios SIN haber hecho commit

Si modificaste un archivo y quieres volver a la última versión confirmada:

```bash
git restore nombre-del-archivo
```

Esto deja el archivo como estaba en el último commit.

---

## 3. Recuperar un archivo borrado

Si borraste un archivo y todavía no hiciste commit:

```bash
git restore nombre-borrado.ext
```

Git lo trae de vuelta desde el último commit.

---

## 4. Volver un proyecto entero a un commit anterior (soft)

Ver historial:

```bash
git log --oneline
```

Elegir un commit (ejemplo: `abc1234`) y:

```bash
git reset --soft abc1234
```

- Mantiene los archivos como estaban en ese commit.
- Deja los cambios posteriores “preparados” para volver a commitearlos distinto, si quieres.

> Importante: para enseñanza inicial normalmente usamos `git restore` y `git reset --soft` o `--mixed`. `--hard` se deja para más adelante porque borra cambios sin posibilidad de recuperación fácil.
