import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.bishop import Bishop
from tablero.board import Board

class TestBishop(unittest.TestCase):
    """
    Test cases for the Bishop chess piece.
    """

    def setUp(self):
        """
        Sets up the test environment before each test case.

        This includes creating a board and placing a white bishop in the center.
        """
        self.board = Board()
        self.bishop = Bishop(4, 4, "WHITE")
        self.board.set_piece(4, 4, self.bishop)

    def set_piece(self, row, col, color):
        """
        Places a new bishop piece on the board at the specified position.

        Args:
            row (int): The row position to place the bishop.
            col (int): The column position to place the bishop.
            color (str): The color of the bishop ('WHITE' or 'BLACK').
        """
        # Here we set a piece on the board.
        self.board.set_piece(row, col, Bishop(row, col, color))

    def _assert_move(self, row, col, expected_valid):
        """
        Asserts whether the bishop can move to the specified position.

        Args:
            row (int): The target row position for the move.
            col (int): The target column position for the move.
            expected_valid (bool): Expected validity of the move.
        """
        if row < 0 or row >= 8 or col < 0 or col >= 8:
            self.assertFalse(expected_valid)
        else:
            valid_move = self.bishop.move(row, col, self.board)
            self.assertEqual(valid_move, expected_valid)

    def test_move_diagonal_free(self):
        """
        Tests moving the bishop to a diagonal position that is free.
        """
        self._assert_move(3, 3, True)

    def test_move_diagonal_up_left(self):
        """
        Tests moving the bishop to an empty diagonal position at the corner of the board.
        """
        self._assert_move(0, 0, True)

    def test_move_out_of_board(self):
        """
        Tests moving the bishop to a position outside the board.
        """
        self._assert_move(8, 8, False)

    def test_move_to_empty_space(self):
        """
        Tests moving the bishop to an empty diagonal space.
        """
        self._assert_move(3, 3, True)

    def test_move_to_enemy_piece(self):
        """
        Tests moving the bishop to a space occupied by an enemy piece.
        """
        self.set_piece(3, 3, "BLACK")
        self._assert_move(3, 3, True)

    def test_move_to_occupied_position(self):
        """
        Tests moving the bishop to a space occupied by a piece of the same color.
        """
        self.set_piece(3, 3, "WHITE")
        self._assert_move(3, 3, False)

    def test_invalid_move_horizontal(self):
        """
        Tests moving the bishop horizontally, which should be invalid.
        """
        self._assert_move(4, 6, False)

if __name__ == '__main__':
    unittest.main()