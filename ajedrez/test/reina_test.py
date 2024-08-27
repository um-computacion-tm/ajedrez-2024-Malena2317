import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.reina import Queen

class TestQueen(unittest.TestCase):

    def setUp(self):
        # Armo un tablero de ajedrez con None
        self.board = []
        for i in range(8):
            self.board.append([None] * 8)
        
        # Pongo una Reina en (0, 0) que es blanca
        self.queen = Queen(0, 0, "white")
        self.board[0][0] = self.queen

    def test_move_horizontal(self):
        # Intento mover la Reina horizontalmente
        resultado = self.queen.move(0, 5, self.board)
        self.assertTrue(resultado)
        self.assertEqual(self.queen.__row__, 0)
        self.assertEqual(self.queen.__col__, 5)

    def test_move_vertical(self):
        # Intento mover la Reina verticalmente
        resultado = self.queen.move(5, 0, self.board)
        self.assertTrue(resultado)
        self.assertEqual(self.queen.__row__, 5)
        self.assertEqual(self.queen.__col__, 0)

    def test_move_diagonal(self):
        # Intento mover la Reina en diagonal
        resultado = self.queen.move(5, 5, self.board)
        self.assertTrue(resultado)
        self.assertEqual(self.queen.__row__, 5)
        self.assertEqual(self.queen.__col__, 5)

    def test_invalid_move(self):
        # Intento un movimiento inválido
        resultado = self.queen.move(4, 1, self.board)
        self.assertFalse(resultado)
        self.assertEqual(self.queen.__row__, 0)
        self.assertEqual(self.queen.__col__, 0)

    def test_move_to_occupied_by_same_color(self):
        # Pongo otra Reina blanca en el lugar y pruebo mover la primera Reina ahí
        otra_reina = Queen(0, 5, "white")
        self.board[0][5] = otra_reina
        resultado = self.queen.move(0, 5, self.board)
        self.assertFalse(resultado)
        self.assertEqual(self.queen.__row__, 0)
        self.assertEqual(self.queen.__col__, 0)

    def test_move_to_occupied_by_opponent(self):
        # Pongo una Reina negra en el lugar y pruebo mover la Reina blanca ahí
        otra_reina = Queen(5, 5, "black")
        self.board[5][5] = otra_reina
        resultado = self.queen.move(5, 5, self.board)
        self.assertTrue(resultado)
        self.assertEqual(self.queen.__row__, 5)
        self.assertEqual(self.queen.__col__, 5)

if __name__ == '__main__':
    unittest.main()
