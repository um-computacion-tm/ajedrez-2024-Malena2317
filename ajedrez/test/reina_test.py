import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.reina import Queen

class TestQueen(unittest.TestCase):

    def setUp(self):
        self.queen = Queen(0, 0, "white")  # Initialize the queen attribute
        # Armo un tablero de ajedrez con None
        self.board = []
        for i in range(8):
            self.board.append([None] * 8)

    def verificar_movimiento(self, row, col, expected_result, oponente=None):
    # Si hay una pieza oponente, la colocamos en el tablero
        if oponente:
            self.board[oponente.__row__][oponente.__col__] = oponente

    # Intento mover la Reina y verifico los resultados
        resultado = self.queen.move(row, col, self.board)
        self.assertEqual(resultado, expected_result)
        self._assert_move(resultado, row, col)

    def _assert_move(self, resultado, row, col):
        self.assertEqual(self.queen.__row__, row)
        self.assertEqual(self.queen.__col__, col)

    def test_move(self, row, col, expected_result):
        self.verificar_movimiento(row, col, expected_result)

    def test_move_to_occupied(self, row, col, expected_result, color):
        self.test_move(row, col, expected_result)

    def test_move_horizontal(self):
        self.test_move(0, 5, True)

    def test_move_vertical(self):
        self.test_move(5, 0, True)

    def test_move_diagonal(self):
        self.test_move(5, 5, True)

    def test_invalid_move(self):
        self.test_move(4, 1, False)

    def test_move_to_occupied(self, row, col, expected_result, color):
        otra_reina = Queen(row, col, color)
        self.board[row][col] = otra_reina
        self.test_move(row, col, expected_result)

    def test_move_to_occupied_by_same_color(self):
        self.test_move_to_occupied(0, 5, False, "white")

    def test_move_to_occupied_by_opponent(self):
        self.test_move_to_occupied(5, 5, True, "black")

if __name__ == '__main__':
    unittest.main()
