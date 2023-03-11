# ==============================
# Sergi Bordes Lloria
# Actividad 02 - Tests
# Archivo test con PYTEST
# ==============================

import funciones as fun
import pytest


def test_suma():
    assert fun.suma(2, 3) == 5
    assert fun.suma(-2, 3) == 1
    assert fun.suma(0, 0) == 0

def test_resta():
    assert fun.resta(5, 3) == 2
    assert fun.resta(5, 5) == 0
    assert fun.resta(-5, 3) == -8

def test_multiplicacion():
    assert fun.multiplicacion(5, 3) == 15
    assert fun.multiplicacion(5, 0) == 0
    assert fun.multiplicacion(-5, 3) == -15

def test_division():
    assert fun.division(10, 2) == 5
    assert fun.division(10, 3) == 3.3333333333333335
    with pytest.raises(ZeroDivisionError):
        fun.division(10, 0)

def test_potencia():
    assert fun.potencia(2, 3) == 8
    assert fun.potencia(2, 0) == 1
    assert fun.potencia(2, -3) == 0.125
    
#if __name__ == '__main__':
    #pytest.main()