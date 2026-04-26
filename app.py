# app.py — Lógica del verificador de contraseñas

def verificar_contrasena(contrasena: str) -> dict:
    """
    Verifica si una contraseña cumple con los requisitos de seguridad.

    Reglas:
      - Mínimo 8 caracteres
      - Al menos una letra mayúscula
      - Al menos un número
      - Al menos un carácter especial (!@#$%^&*)

    Retorna un dict con 'valida' (bool) y 'errores' (list).
    """
    errores = []

    if len(contrasena) < 8:
        errores.append("Debe tener al menos 8 caracteres.")

    if not any(c.isupper() for c in contrasena):
        errores.append("Debe contener al menos una mayúscula.")

    if not any(c.isdigit() for c in contrasena):
        errores.append("Debe contener al menos un número.")

    caracteres_especiales = "!@#$%^&*"
    if not any(c in caracteres_especiales for c in contrasena):
        errores.append("Debe contener al menos un carácter especial (!@#$%^&*).")

    return {
        "valida": len(errores) == 0,
        "errores": errores
    }