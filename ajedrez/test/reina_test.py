import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.reina import Queen

class TestQueen(unittest.TestCase):
    
    def setUp(self):
        # Inicializa la reina y el tablero
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.queen = Queen(0, 0, "white")
        self.board[0][0] = self.queen

    def auxiliar_move(self, row, col, expected_result):
    # Intento mover la Reina
        resultado = self.queen.move(row, col, self.board)
        self.assertEqual(resultado, expected_result)
        self.assertEqual(self.queen.__row__, row if expected_result else 0)
        self.assertEqual(self.queen.__col__, col if expected_result else 0)

    def auxiliar_move_to_occupied(self, row, col, color, expected_result):
        # Pongo otra Reina en el lugar
        otra_reina = Queen(row, col, color)
        self.board[row][col] = otra_reina
        self.auxiliar_move(row, col, expected_result)

    def test_move_horizontal(self):
        self.auxiliar_move(0, 5, True)

    def test_move_vertical(self):
        self.auxiliar_move(5, 0, True)

    def test_move_diagonal(self):
        self.auxiliar_move(5, 5, True)

    def test_invalid_move(self):
        self.auxiliar_move(4, 1, False)

    def test_move_to_occupied_by_same_color(self):
        self.auxiliar_move_to_occupied(0, 5, "white", False)

    def test_move_to_occupied_by_opponent(self):
        self.auxiliar_move_to_occupied(5, 5, "black", True)
   
if __name__ == '__main__':
    unittest.main()
