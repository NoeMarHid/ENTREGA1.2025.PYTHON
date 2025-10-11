import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from entrega1.funciones import funcion1, funcion2, funcion3, funcion4, funcion5
import unittest


class TestFuncion1(unittest.TestCase):
    def test_FechaValida(self):
        self.assertTrue(funcion1(4, 7, 2005))
    def test_FechaNoeExiste(self):
        self.assertFalse(funcion1(30, 2, 1999))
    def test_Domingo(self):
        self.assertFalse(funcion1(12, 10, 2025))

class TestFuncion2(unittest.TestCase):
    def test_nMenorAk(self):
        with self.assertRaises(AssertionError):
            funcion2(1,2)
    def test_Solucion(self):
        self.assertEqual(funcion2(3,2),24)
    






if __name__ == "__main__":
    unittest.main()