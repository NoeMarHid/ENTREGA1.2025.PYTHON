import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import math
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

class TestFuncion3(unittest.TestCase):
    def test_kEsCero(self):
        with self.assertRaises(AssertionError):
            funcion3(2,2,0)
    def test_kMenorACEro(self):
        with self.assertRaises(AssertionError):
            funcion3(2,2,-1)
    def test_Solucion3(self):
        self.assertEqual(funcion3(3, 5, 2), 45)
        
class TestFuncion4(unittest.TestCase):
    def test_nMenorAk(self):
        with self.assertRaises(AssertionError):
            funcion4(9,10)
    def test_Solucion4(self):
        self.assertEqual(funcion4(4, 2), 6)
        
class TestFuncion5(unittest.TestCase):
    def test_Solucion5(self):
        self.assertEqual(funcion5(4, 2), 22.5)
    def test_nMenorAk(self):
        with self.assertRaises(AssertionError):
            funcion5(3,4)






if __name__ == "__main__":
    unittest.main()