import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.pawn import Pawn


class TestPawn(unittest.TestCase):

    def setUp(self):
        self.peon_blanco = Pawn("WITHE")
        self.peon_negro = Pawn("BLACK")
        self.tablero = [[None] * 8 for _ in range(8)]

    def test_mover_peon_blanco_hacia_adelante(self):
        self.tablero[3][3] = self.peon_blanco
        resultado = self.peon_blanco.mover(self.tablero, 3, 3, 4, 3)
        self.assertEqual(resultado, True, "El peon blanco debería poder moverse hacia adelante")

    def test_mover_peon_negro_hacia_adelante(self):
        self.tablero[4][4] = self.peon_negro
        resultado = self.peon_negro.mover(self.tablero, 4, 4, 3, 4)
        self.assertEqual(resultado, True, "El peon negro debería poder moverse hacia adelante")

    def test_mover_peon_blanco_hacia_atras(self):
        self.tablero[3][3] = self.peon_blanco
        resultado = self.peon_blanco.mover(self.tablero, 3, 3, 2, 3)
        self.assertEqual(resultado, False, "El peon blanco no debería poder moverse hacia atrás")

    def test_mover_peon_negro_hacia_atras(self):
        self.tablero[4][4] = self.peon_negro
        resultado = self.peon_negro.mover(self.tablero, 4, 4, 5, 4)
        self.assertEqual(resultado, False, "El peon negro no debería poder moverse hacia atrás")

    def test_mover_peon_misma_fila(self):
        self.tablero[3][3] = self.peon_blanco
        resultado = self.peon_blanco.mover(self.tablero, 3, 3, 3, 4)
        self.assertEqual(resultado, False, "El peon no debería poder moverse a la misma fila")

    def test_mover_peon_diferente_columna(self):
        self.tablero[4][4] = self.peon_negro
        resultado = self.peon_negro.mover(self.tablero, 4, 4, 5, 5)
        self.assertEqual(resultado, False, "El peon no debería poder moverse a una columna diferente")
    
if __name__ == '__main__':
    unittest.main()