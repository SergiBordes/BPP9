# ==============================
# Sergi Bordes Lloria
# Actividad 02 - Tests
# Archivo test con UNNITEST
# ==============================

import funciones as fun
import unittest

class TestFunciones(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(fun.suma(2, 3), 5)
        self.assertEqual(fun.suma(-2, 3), 1)
        self.assertEqual(fun.suma(0, 0), 0)

    def test_resta(self):
        self.assertEqual(fun.resta(5, 3), 2)
        self.assertEqual(fun.resta(5, 5), 0)
        self.assertEqual(fun.resta(-5, 3), -8)

    def test_multiplicacion(self):
        self.assertEqual(fun.multiplicacion(5, 3), 15)
        self.assertEqual(fun.multiplicacion(5, 0), 0)
        self.assertEqual(fun.multiplicacion(-5, 3), -15)

    def test_division(self):
        self.assertEqual(fun.division(10, 2), 5)
        self.assertEqual(fun.division(10, 3), 3.3333333333333335)
        self.assertRaises(ZeroDivisionError, fun.division, 10, 0)

    def test_potencia(self):
        self.assertEqual(fun.potencia(2, 3), 8)
        self.assertEqual(fun.potencia(2, 0), 1)
        self.assertEqual(fun.potencia(2, -3), 0.125)

if __name__ == '__main__':
    unittest.main()