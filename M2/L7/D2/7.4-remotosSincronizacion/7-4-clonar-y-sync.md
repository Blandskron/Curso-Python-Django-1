# 7.4 – Clonar un repositorio y sincronizar cambios

Cuando un repo ya existe en GitHub, lo más común es **clonarlo**.

---

## 1. Clonar

```bash
git clone https://github.com/usuario/mi-proyecto.git
```

Esto:

- Crea una carpeta `mi-proyecto/`.
- Configura el remoto `origin` automáticamente.
- Descarga todo el historial de Git.

---

## 2. Trabajar normalmente

Dentro de la carpeta clonada:

```bash
cd mi-proyecto
git status
# editar archivos...
git add .
git commit -m "Agrega sección de testimonios"
```

---

## 3. Enviar cambios al remoto

```bash
git push
```

Si Git pregunta por la rama:

```bash
git push -u origin main
```

---

## 4. Actualizarse con lo último del remoto

Antes de empezar a trabajar un nuevo día:

```bash
git pull
```

Esto trae los cambios realizados por otras personas y los mezcla con tu rama local.
