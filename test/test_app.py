# test/test_app.py — Tests automatizados con pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import verificar_contrasena


# ✅ CASO EXITOSO
def test_contrasena_valida():
    resultado = verificar_contrasena("Segura1!")
    assert resultado["valida"] == True
    assert resultado["errores"] == []


# ❌ CASO DE ERROR — sin mayúscula
def test_sin_mayuscula():
    resultado = verificar_contrasena("segura1!")
    assert resultado["valida"] == False
    assert "Debe contener al menos una mayúscula." in resultado["errores"]


# ❌ CASO DE ERROR — sin número
def test_sin_numero():
    resultado = verificar_contrasena("Segura!!")
    assert resultado["valida"] == False
    assert "Debe contener al menos un número." in resultado["errores"]


# ❌ CASO DE ERROR — sin carácter especial
def test_sin_especial():
    resultado = verificar_contrasena("Segura12")
    assert resultado["valida"] == False
    assert "Debe contener al menos un carácter especial (!@#$%^&*)." in resultado["errores"]


# ❌ CASO DE ERROR — muy corta
def test_contrasena_muy_corta():
    resultado = verificar_contrasena("Ab1!")
    assert resultado["valida"] == False
    assert "Debe tener al menos 8 caracteres." in resultado["errores"]


# 🔲 CASO BORDE — contraseña vacía (los 4 errores juntos)
def test_contrasena_vacia():
    resultado = verificar_contrasena("")
    assert resultado["valida"] == False
    assert len(resultado["errores"]) == 4


# 🔲 CASO BORDE — exactamente 8 caracteres válidos
def test_longitud_exacta():
    resultado = verificar_contrasena("Abc1!xyz")
    assert resultado["valida"] == True