# 7.2 – Flujo básico de trabajo en un repositorio local

En este ejemplo se muestra el flujo típico al trabajar con Git **solo en tu máquina** (sin GitHub todavía).

---

## 1. Crear un repositorio local

Dentro de la carpeta de tu proyecto:

```bash
git init
```

Este comando:

- Crea una carpeta oculta `.git/`.
- Comienza a seguir el historial de ese proyecto.

---

## 2. Ver el estado de los archivos

```bash
git status
```

Muestra:

- Archivos nuevos (untracked)
- Archivos modificados
- Ramas actuales

---

## 3. Agregar archivos al área de preparación (staging)

```bash
git add index.html
git add css/estilos.css
# o agregar todo:
git add .
```

Git ahora sabe **qué archivos** quieres incluir en el próximo commit.

---

## 4. Crear un commit

```bash
git commit -m "Crea estructura básica del sitio"
```

El commit guarda una **foto** del estado actual de esos archivos.

---

## 5. Ver el historial

```bash
git log
```

Salida típica:

```txt
commit 1a2b3c4d (HEAD -> main)
Author: Tu Nombre <tu@mail.com>
Date:   2025-11-01

    Crea estructura básica del sitio
```

Esta es la “línea de tiempo” de tu proyecto.
