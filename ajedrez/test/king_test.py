from textwrap import fill
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.king import King
from tablero.board import Board



class TestKing(unittest.TestCase):
    """
    Test cases for the King chess piece.
    """

    def setUp(self):
        """
        Sets up the test environment before each test case.

        This includes creating a board and placing a white king in the initial position.
        """
        self.board = Board()
        self.king = King(0, 4, "white")
        self.board.set_piece(0, 4, self.king)

    def assert_king_position(self, row, col, result):
        """
        Asserts that the king is at the specified position after a move.

        Args:
            row (int): The expected row position of the king.
            col (int): The expected column position of the king.
            result (bool): The result of the move attempt.
        """
        if result:
            # Check if the king moved to the correct position
            self.assertEqual(self.king.get_coordinates()[0], row)
            self.assertEqual(self.king.get_coordinates()[1], col)

    def move_and_assert(self, row, col, expected_result=True):
        """
        Moves the king to the specified position and asserts the result.

        Args:
            row (int): The target row position for the move.
            col (int): The target column position for the move.
            expected_result (bool): Expected result of the move (True for success, False for failure).
        """
        # Move the existing king and verify the result
        result = self.king.move(row, col, self.board)
        self.assertEqual(result, expected_result)
        self.assert_king_position(row, col, result)

    def place_piece_and_move(self, row, col, color, expected_result=True):
        """
        Places a piece on the board and tests if the king can move to that position.

        Args:
            row (int): The row position where another piece will be placed.
            col (int): The column position where another piece will be placed.
            color (str): The color of the other piece ('white' or 'black').
            expected_result (bool): Expected result of the move (True for success, False for failure).
        """
        if color == "white" and (row, col) == (self.king.get_coordinates()[0], self.king.get_coordinates()[1]):
            # If it's the same white king in the same position, test its movement
            result = self.king.move(row, col, self.board)
        else:
            # Place a new piece (black king) and test the movement
            another_king = King(row, col, color)
            self.board.set_piece(row, col, another_king)  # Place the black king on the board
            result = self.king.move(row, col, self.board)  # Attempt to move the white king
            
        self.assertEqual(result, expected_result)  # Compare with expected result

    def test_move_one_square_down(self):
        """
        Tests moving the king one square down.
        """
        self.move_and_assert(1, 4, True)

    def test_move_diagonally(self):
        """
        Tests moving the king diagonally.
        """
        self.move_and_assert(1, 5, True)

    def test_place_another_piece_and_move(self):
        """
        Tests placing another piece on the board and attempting to move the king to that position.
        """
        self.place_piece_and_move(1, 4, "white", False)

    def test_move_to_black_piece(self):
        """
        Tests moving the king to a position occupied by a black piece.
        """
        self.place_piece_and_move(1, 4, "black", True)

    def test_move_out_of_board(self):
        """
        Tests attempting to move the king outside the bounds of the board.
        """
        self.move_and_assert(8, 4, False)

    def test_move_to_invalid_position(self):
        """
        Tests moving the king to an invalid position.
        """
        self.move_and_assert(3, 4, False)

    def test_move_horizontal(self):
        """
        Tests moving the king horizontally to the right.
        """
        self.move_and_assert(0, 5, True)

    def test_move_vertical(self):
        """
        Tests moving the king vertically down.
        """
        self.move_and_assert(1, 4, True)

    def test_move_diagonally_left(self):
        """
        Tests moving the king diagonally to the left.
        """
        self.move_and_assert(1, 3, True)

    def test_move_to_occupied_by_same_color(self):
        """
        Tests moving the king to a position occupied by another piece of the same color.
        """
        self.place_piece_and_move(0, 4, "white", False)

    def test_move_to_occupied_by_different_color(self):
        """
        Tests moving the king to a position occupied by an opponent's piece.
        """
        self.place_piece_and_move(0, 4, "black", True)

    def test_move_out_of_board_top_row(self):
        """
        Tests attempting to move the king outside the bounds of the board at the top.
        """
        self.move_and_assert(-1, 4, False)

    def test_move_out_of_board_left_column(self):
        """
        Tests attempting to move the king outside the bounds of the board on the left.
        """
        self.move_and_assert(0, -1, False)

if __name__ == '__main__':
    unittest.main()