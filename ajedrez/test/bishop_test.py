import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.bishop import Bishop
from tablero.board import Board
    # limpio 0%

class TestBishop(unittest.TestCase):

    def setUp(self):
        # # Initializes the board and the piece
        self.board = Board()
        self.bishop = Bishop(4, 4, "WHITE")
        self.board.set_piece(4, 4, self.bishop)


    def set_piece(self, row, col, color):
        # Place a piece on the board
        self.board.set_piece(row, col, Bishop(row, col, color))

    def _assert_move(self, row, col, expected_valid):
        if row < 0 or row >= 8 or col < 0 or col >= 8:
            self.assertFalse(expected_valid)
        else:
            valid_move = self.bishop.move(row, col, self.board)
            self.assertEqual(valid_move, expected_valid)

    def test_move_diagonal_free(self):
        self._assert_move(3, 3, True)

    def test_move_diagonal_up_left(self):
        self._assert_move(2, 2, True)

    def test_move_diagonal_up_right(self):
        self._assert_move(2, 6, True)

    def test_move_out_of_board(self):
        self._assert_move(8, 8, False)

    def test_move_to_empty_space(self):
        self._assert_move(3, 3, True)

    def test_move_to_enemy_piece(self):
        self.set_piece(3, 3, "BLACK")
        self._assert_move(3, 3, True)

    def test_move_to_occupied_position(self):
        self.set_piece(3, 3, "WHITE")
        self._assert_move(3, 3, False)

    def test_invalid_move_horizontal(self):
        self._assert_move(4, 5, False)

if __name__ == '__main__':
    unittest.main()


