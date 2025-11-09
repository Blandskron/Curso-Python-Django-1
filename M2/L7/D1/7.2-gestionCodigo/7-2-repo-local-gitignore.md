# 7.2 – Ignorando archivos con .gitignore

No todo lo que hay en tu carpeta debe ser parte del repositorio.

Ejemplos de cosas que NO quieres subir:

- Archivos temporales (`*.log`, `*.tmp`)
- Dependencias (`node_modules/`)
- Archivos de configuración local (por ejemplo, `.env` con claves privadas)

---

## 1. Crear un archivo .gitignore

En la raíz del proyecto:

```txt
.gitignore
index.html
css/
js/
```

Contenido básico del `.gitignore`:

```gitignore
# Ignorar node_modules
node_modules/

# Ignorar archivos de log
*.log

# Ignorar archivos de configuración local
.env
```

---

## 2. Cómo funciona

Cuando ejecutas:

```bash
git status
```

Git **no mostrará** los archivos y carpetas que coincidan con las reglas del `.gitignore`.

> Nota: si un archivo ya estaba trackeado antes de agregarlo al `.gitignore`, hay que quitarlo del índice con `git rm --cached archivo`.
