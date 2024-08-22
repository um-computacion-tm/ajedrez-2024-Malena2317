import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.rook import Rook
from tablero.board import Board


class TestRook(unittest.TestCase):
    
    def setUp(self):
        self.rook_blanco = Rook("WHITE")
        self.rook_negro = Rook("BLACK")
        self.board = Board()

    def test_mover_torre_en_linea_recta_vertical(self):
        self.board.__positions__[0][0] = self.rook_blanco
        resultado = self.rook_blanco.move(self.board, 0, 0, 4, 0)
        self.assertEqual(resultado, True, "La torre blanca debería poder moverse en línea recta vertical")
        self.assertIsNone(self.board.get_piece(0, 0), "La posición inicial debería estar vacía")
        self.assertEqual(self.board.get_piece(4, 0), self.rook_blanco, "La torre blanca debería estar en la nueva posición (4, 0)")
    
    def test_mover_torre_en_linea_recta_horizontal(self):
        self.board.__positions__[0][0] = self.rook_negro
        resultado = self.rook_negro.move(self.board, 0, 0, 0, 5)
        self.assertEqual(resultado, True, "La torre negra debería poder moverse en línea recta horizontal")

    def test_mover_torre_diagonal(self):
        self.board.__positions__[0][0] = self.rook_blanco
        resultado = self.rook_blanco.move(self.board, 0, 0, 3, 3)
        self.assertEqual(resultado, False, "La torre no debería poder moverse en diagonal")

    def test_mover_torre_obstaculo(self):
        self.board.__positions__[0][0] = self.rook_blanco
        self.board.__positions__[2][0] = Rook("BLACK")  # Colocando una pieza en el camino
        resultado = self.rook_blanco.move(self.board, 0, 0, 4, 0)
        self.assertEqual(resultado, False, "La torre no debería poder moverse si hay una pieza en su camino")

    def test_mover_torre_mismo_lugar(self):
        self.board.__positions__[0][0] = self.rook_negro
        resultado = self.rook_negro.move(self.board, 0, 0, 0, 0)
        self.assertEqual(resultado, False, "La torre no debería poder moverse al mismo lugar")

if __name__ == '__main__':
    unittest.main()

