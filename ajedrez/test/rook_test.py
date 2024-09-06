import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.rook import Rook
from tablero.board import Board

class TestRook(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.rook_blanca = Rook("WHITE")
        self.rook_negra = Rook("BLACK")

    def test_mover_torre_vertical(self):
        self.board.set_piece(0, 0, self.rook_blanca)
        resultado = self.rook_blanca.move(self.board, 0, 0, 4, 0)
        self.assertEqual(resultado, True)
        self.assertEqual(self.board.get_piece(0, 0), None)
        self.assertEqual(self.board.get_piece(4, 0), self.rook_blanca)

    def test_mover_torre_horizontal(self):
        self.board.set_piece(0, 0, self.rook_negra)
        resultado = self.rook_negra.move(self.board, 0, 0, 0, 5)
        self.assertEqual(resultado, True)
        self.assertEqual(self.board.get_piece(0, 0), None)
        self.assertEqual(self.board.get_piece(0, 5), self.rook_negra)

    def test_mover_torre_diagonal(self):
        self.board.set_piece(0, 0, self.rook_blanca)
        resultado = self.rook_blanca.move(self.board, 0, 0, 3, 3)
        self.assertEqual(resultado, False)
        self.assertEqual(self.board.get_piece(0, 0), self.rook_blanca)

    def test_mover_torre_con_obstaculo(self):
        self.board.set_piece(0, 0, self.rook_blanca)
        self.board.set_piece(2, 0, self.rook_negra)
        resultado = self.rook_blanca.move(self.board, 0, 0, 4, 0)
        self.assertEqual(resultado, False)
        self.assertEqual(self.board.get_piece(0, 0), self.rook_blanca)
        self.assertEqual(self.board.get_piece(2, 0), self.rook_negra)

    def test_mover_torre_al_mismo_lugar(self):
        self.board.set_piece(0, 0, self.rook_negra)
        resultado = self.rook_negra.move(self.board, 0, 0, 0, 0)
        self.assertEqual(resultado, False)
        self.assertEqual(self.board.get_piece(0, 0), self.rook_negra)

if __name__ == '__main__':
    unittest.main()

