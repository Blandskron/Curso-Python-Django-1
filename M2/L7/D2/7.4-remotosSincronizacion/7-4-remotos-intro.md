# 7.4 – Repositorios locales y remotos

Hasta ahora hemos usado Git solo en la máquina local.

Con **GitHub** podemos:

- Tener una copia remota del repositorio.
- Colaborar con otras personas.
- Hacer copias de seguridad.

---

## 1. Ver repositorios remotos configurados

```bash
git remote -v
```

Si no hay nada, significa que `origin` u otros remotos no están configurados.

---

## 2. Agregar un remoto (origin)

Después de crear un repo vacío en GitHub (sin README):

```bash
git remote add origin https://github.com/usuario/mi-proyecto.git
```

Ahora `origin` apunta al repositorio remoto en GitHub.

---

## 3. Enviar cambios al remoto (push)

```bash
git push -u origin main
```

- `push`: envía los commits locales al remoto.
- `-u origin main`: deja configurada la rama `main` para que quede asociada a `origin/main`.

Para siguientes pushes:

```bash
git push
```

---

## 4. Traer cambios del remoto (pull)

Cuando hay cambios nuevos en GitHub:

```bash
git pull
```

`git pull` = `git fetch` + `git merge`
