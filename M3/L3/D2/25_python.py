# Reescritura del ejemplo anterior con guard clauses (más plano)

def registrar_usuario(email: str, password: str, edad: int, terms_accepted: bool) -> None:
    """Ejemplo de refactorización con condiciones de salida temprana."""
    if "@" not in email or "." not in email:
        print("✗ Email inválido")
        return

    if len(password) < 8:
        print("✗ Contraseña muy corta (mínimo 8 caracteres)")
        return

    if edad < 18:
        print("✗ Debe ser mayor de 18 años")
        return

    if not terms_accepted:
        print("✗ Debe aceptar los términos")
        return

    print("Todos los datos son válidos. Registro completado exitosamente")


registrar_usuario("alguien@example.com", "12345678", 20, True)
