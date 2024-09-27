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


    def _mover_alfil(self, to_row, to_col, expected_result, expected_position):
        resultado = self.alfil.mover(to_row, to_col, self.tablero)
        self.assertEqual(resultado, expected_result)
        self.assertEqual((self.alfil.get_row(), self.alfil.get_col()), expected_position)

    def test_mover_diagonal_libre(self):
        # Test para mover el alfil en diagonal a una posición libre
        self._mover_alfil(3, 3, True, (3, 3))

    def test_mover_no_diagonal(self):
        # Test para intentar mover el alfil a una posición no diagonal
        self._mover_alfil(2, 3, False, (1, 1))

    def test_mover_posicion_ocupada(self):
        # Test para intentar mover el alfil a una posición ocupada
        otra_pieza = Alfil(3, 3, "negro")
        self.tablero[3][3] = otra_pieza
        self._mover_alfil(3, 3, False, (1, 1))

if __name__ == '__main__':
    unittest.main()



