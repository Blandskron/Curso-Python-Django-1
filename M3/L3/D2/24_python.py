# Registro con varias validaciones anidadas

email = "alguien@example.com"
password = "12345678"
edad = 20
terms_accepted = False

if "@" in email and "." in email:
    print("✓ Email válido")
    if len(password) >= 8:
        print("✓ Contraseña suficientemente larga")
        if edad >= 18:
            print("✓ Edad válida")
            if terms_accepted:
                print("✓ Términos aceptados")
                print("Registro completado exitosamente")
            else:
                print("✗ Debe aceptar los términos")
        else:
            print("✗ Debe ser mayor de 18 años")
    else:
        print("✗ Contraseña muy corta (mínimo 8 caracteres)")
else:
    print("✗ Email inválido")