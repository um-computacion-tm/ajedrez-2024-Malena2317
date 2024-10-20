import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.queen import Queen
from tablero.board import Board



class TestQueen(unittest.TestCase):
    """
    Test cases for the Queen chess piece.
    """

    def setUp(self):
        self.board = Board()
        self.queen = Queen(0, 0, "white")
        self.board.set_piece(0, 0, self.queen)

    def auxiliar_move(self, row, col, expected_result):
        """
        Attempts to move the queen to the specified position and asserts the result.

        Args:
            row (int): The target row position for the move.
            col (int): The target column position for the move.
            expected_result (bool): Expected result of the move (True for success, False for failure).
        """
        # Attempt to move the Queen
        result = self.queen.move(row, col, self.board)
        print(f"Result: {result}, Expected: {expected_result}")
        print(self.board)
        self.assertEqual(result, expected_result)

    def auxiliar_move_to_occupied(self, row, col, color, expected_result):
        """
        Places another queen on the specified position and attempts to move the original queen.

        Args:
            row (int): The row position where the other queen is placed.
            col (int): The column position where the other queen is placed.
            color (str): The color of the other queen ('white' or 'black').
            expected_result (bool): Expected result of the move (True for success, False for failure).
        """
        # Place another Queen in the position
        other_piece = Queen(row, col, color)
        self.board.set_piece(row, col, other_piece)
        self.auxiliar_move(row, col, expected_result)

    def test_move_horizontal(self):
        """
        Tests moving the queen horizontally across the board.
        """
        self.auxiliar_move(0, 5, True)

    def test_move_vertical(self):
        """
        Tests moving the queen vertically down the board.
        """
        self.auxiliar_move(5, 0, True)

    def test_move_diagonal(self):
        """
        Tests moving the queen diagonally across the board.
        """
        self.auxiliar_move(5, 5, True)

    def test_move_to_occupied_by_same_color(self):
        """
        Tests moving the queen to a position occupied by another piece of the same color.
        """
        self.auxiliar_move_to_occupied(0, 5, "white", False)
        self.board.set_piece(0, 5, Queen(0, 5, "white"))

    def test_move_to_occupied_by_opponent(self):
        """
        Tests moving the queen to a position occupied by an opponent's piece.
        """
        self.auxiliar_move_to_occupied(5, 5, "black", True)

    def test_move_out_of_board(self):
        """
        Tests attempting to move the queen outside the bounds of the board.
        """
        self.auxiliar_move(8, 0, False)
        self.auxiliar_move(0, 8, False)

    def test_move_to_same_position(self):
        """
        Tests moving the queen to its current position, which should be invalid.
        """
        self.auxiliar_move(0, 0, False)

    def test_move_up_left(self):
        """
        Tests moving the queen diagonally up to the left.
        """
        self.auxiliar_move(1, 1, True)

    def test_move_up_right(self):
        """
        Tests moving the queen horizontally to the right.
        """
        self.auxiliar_move(0, 6, True)

    def test_move_down_left(self):
        """
        Tests moving the queen diagonally down to the left.
        """
        self.auxiliar_move(6, 0, True)

    def test_move_down_right(self):
        """
        Tests moving the queen diagonally down to the right.
        """
        self.auxiliar_move(7, 7, True)

if __name__ == '__main__':
    unittest.main()
