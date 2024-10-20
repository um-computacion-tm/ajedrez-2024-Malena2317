import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.king import King
from tablero.board import Board





class TestKing(unittest.TestCase):
    """Unit tests for the King class."""

    def setUp(self):
        """Initialize a Board instance and place a white king on it before each test."""
        self.board = Board()
        self.king = King(0, 4, "white")
        self.board.set_piece(0, 4, self.king)

    def assert_king_position(self, row, col, result):
        """Check if the king is at the specified coordinates after a move.

        Args:
            row (int): The expected row of the king.
            col (int): The expected column of the king.
            result (bool): Whether the move was successful.
        """
        if result:
            # Check if the king moved to the correct position
            self.assertEqual(self.king.get_coordinates()[0], row)
            self.assertEqual(self.king.get_coordinates()[1], col)

    def move_and_assert(self, row, col, expected_result=True):
        """Move the king to the specified coordinates and assert the result.

        Args:
            row (int): The row to move the king to.
            col (int): The column to move the king to.
            expected_result (bool): The expected result of the move.
        """
        # Move the existing king and verify the result
        result = self.king.move(row, col, self.board)
        self.assertEqual(result, expected_result)
        self.assert_king_position(row, col, result)

    def place_piece_and_move(self, row, col, color, expected_result=True):
        """Place a piece on the board and test if the king can move.

        Args:
            row (int): The row where the piece is placed.
            col (int): The column where the piece is placed.
            color (str): The color of the piece being placed.
            expected_result (bool): The expected result of the move.
        """
        if color == "white" and (row, col) == self.king.get_coordinates():
            # If it's the same white king in the same position, test its movement
            result = self.king.move(row, col, self.board)
        else:
            # Place a new piece (black king) and test the movement
            another_king = King(row, col, color)
            self.board.place_piece(another_king, (row, col))  # Place the black king on the board
            result = self.king.move(row, col, self.board)  # Attempt to move the white king
            
        self.assertEqual(result, expected_result)  # Compare the expected result

    def test_move_one_square_down(self):
        """Test moving the king one square down."""
        self.move_and_assert(1, 4, True)

    def test_move_diagonally(self):
        """Test moving the king diagonally."""
        self.move_and_assert(1, 5, True)

    def test_place_another_piece_and_move(self):
        """Test placing another piece and moving the king."""
        self.place_piece_and_move(1, 4, "white", False)

    def test_move_black_piece(self):
        """Test moving a black piece onto the square occupied by the king."""
        self.place_piece_and_move(1, 4, "black", True)

    def test_move_out_of_bounds(self):
        """Test moving the king out of the board's boundaries."""
        self.move_and_assert(8, 4, False)

    def test_move_to_an_invalid_position(self):
        """Test moving the king to an invalid position."""
        self.move_and_assert(3, 4, False)

    def test_move_horizontally(self):
        """Test moving the king horizontally."""
        self.move_and_assert(0, 5, True)

    def test_move_vertically(self):
        """Test moving the king vertically."""
        self.move_and_assert(1, 4, True)

    def test_move_diagonally_to_the_left(self):
        """Test moving the king diagonally to the left."""
        self.move_and_assert(1, 3, True)

    def test_move_to_a_square_occupied_by_own_piece(self):
        """Test moving to a square occupied by a piece of the same color."""
        self.move_and_assert(0, 4, False)  

    def test_move_out_of_bounds_at_upper_row(self):
        """Test moving the king out of bounds at the upper row."""
        self.move_and_assert(-1, 4, False)

    def test_move_out_of_bounds_at_left_column(self):
        """Test moving the king out of bounds at the left column."""
        self.move_and_assert(0, -1, False)

if __name__ == '__main__':
    unittest.main()
