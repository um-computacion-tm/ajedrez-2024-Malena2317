import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.bishop import Alfil
from tablero.board import Board

class TestBishop(unittest.TestCase):

    def setUp(self):
        # Inicializa el tablero y la pieza
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.place_piece(1, 1, "WHITE")
        self.alfil = Alfil(1, 1, "WHITE")

    def place_piece(self, row, col, color):
        # Colocar una pieza en el tablero
        self.board[row][col] = Alfil(row, col, color)

    def _assert_move(self, row, col, expected_valid):
        if row < 0 or row >= 8 or col < 0 or col >= 8:
            self.assertFalse(expected_valid)
        else:
            try:
                self.alfil.move(row, col, self.board)
                self.assertIsInstance(self.board[row][col], Alfil)
                self.assertTrue(expected_valid)
            except ValueError:
                self.assertFalse(expected_valid)

    def test_move_diagonal_free(self):
        self._assert_move(3, 3, True)

    def test_move_diagonal_up_left(self):
        self._assert_move(0, 0, True)

    def test_move_diagonal_up_right(self):
        self._assert_move(1, 3, True)

    def test_move_out_of_board(self):
        self._assert_move(8, 8, False)

    def test_move_to_empty_space(self):
        self._assert_move(3, 3, True)

    def test_move_to_enemy_piece(self):
        self.place_piece(3, 3, "BLACK")
        self._assert_move(3, 3, True)

    def test_move_to_occupied_position(self):
        self.place_piece(3, 3, "WHITE")
        self._assert_move(3, 3, True)

    def test_invalid_move_horizontal(self):
        self._assert_move(1, 1, False)

if __name__ == '__main__':
    unittest.main()



