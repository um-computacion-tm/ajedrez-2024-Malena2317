
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.bishop import Alfil

class TestBishop(unittest.TestCase):

    def setUp(self):
        # Inicializa el tablero y la pieza
        self.tablero = [[None for _ in range(8)] for _ in range(8)]
        self.alfil = Alfil(1, 1, "blanco")
        self.tablero[1][1] = self.alfil

    def test_mover_diagonal_libre(self):
        # Test para mover el alfil en diagonal a una posición libre
        resultado = self.alfil.mover(3, 3, self.tablero)
        self.assertTrue(resultado, "El alfil debería poder moverse en diagonal a una posición libre")
        self.assertEqual((self.alfil.get_row(), self.alfil.get_col()), (3, 3), "El alfil debería estar en la posición (3, 3)")

    def test_mover_no_diagonal(self):
        # Test para intentar mover el alfil a una posición no diagonal
        resultado = self.alfil.mover(2, 3, self.tablero)
        self.assertFalse(resultado, "El alfil no debería poder moverse a una posición que no está en diagonal")
        self.assertEqual((self.alfil.get_row(), self.alfil.get_col()), (1, 1), "El alfil debería seguir en la posición (1, 1)")

    def test_mover_posicion_ocupada(self):
        # Test para intentar mover el alfil a una posición ocupada
        otra_pieza = Alfil(3, 3, "negro")
        self.tablero[3][3] = otra_pieza
        resultado = self.alfil.mover(3, 3, self.tablero)
        self.assertFalse(resultado, "El alfil no debería poder moverse a una posición ocupada por otra pieza")
        self.assertEqual((self.alfil.get_row(), self.alfil.get_col()), (1, 1), "El alfil debería seguir en la posición (1, 1)")

if __name__ == '__main__':
    unittest.main()



