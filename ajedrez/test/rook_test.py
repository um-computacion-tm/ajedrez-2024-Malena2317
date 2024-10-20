import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.rook import Rook
from tablero.board import Board




class TestRook(unittest.TestCase):
    """
    Test cases for the Rook chess piece. 
    """

    def setUp(self):
        """
        Sets up the test environment before each test case.

        This includes creating a board and placing a rook in the initial position.
        """
        self.board = Board()
        self.rook = Rook(1, 1, "WHITE")
        self.board.set_piece(1, 1, self.rook)

    def Rook_Move(self, rook, to_row, to_col, expected_result):
        """
        Tests the movement of the rook to the specified position.

        Args:
            rook (Rook): The rook piece to be moved.
            to_row (int): The target row position for the move.
            to_col (int): The target column position for the move.
            expected_result (bool): Expected validity of the move (True for valid, False for invalid).
        """
        result = rook.move(to_row, to_col, self.board)
        self.assertEqual(result, expected_result)
        
        if expected_result:
            # Verify that the rook has moved to the new position
            self.assertIsNone(self.board.get_piece(1, 1))  # Changed to get_piece
            self.assertEqual(self.board.get_piece(to_row, to_col), rook)  # Changed to get_piece
        else:
            # Verify that the rook remains in its original position
            self.assertEqual(self.board.get_piece(1, 1), rook)  # Changed to get_piece
            if 0 <= to_row < 8 and 0 <= to_col < 8:
                self.assertNotEqual(self.board.get_piece(to_row, to_col), rook)  # Changed to get_piece

    def set_piece_and_test_move(self, row, col, color, expected_result):
        """
        Helper to set a piece and test rook movement.

        Args:
            row (int): The row position to set the piece.
            col (int): The column position to set the piece.
            color (str): The color of the piece ('WHITE' or 'BLACK').
            expected_result (bool): Expected validity of the rook's move (True or False).
        """
        self.board.set_piece(row, col, Rook(row, col, color))
        self.Rook_Move(self.rook, row, col, expected_result)
        
    def test_move_rook_out_of_board(self):
        """
        Tests attempting to move the rook out of the board.
        """
        self.Rook_Move(self.rook, 8, 1, False)

    def test_move_rook_horizontal(self):
        """
        Tests moving the rook horizontally on the board.
        """
        self.board.set_piece(1, 2, None) 
        self.Rook_Move(self.rook, 1, 3, True)

    def test_move_rook_vertical(self):
        """
        Tests moving the rook vertically on the board.
        """
        self.Rook_Move(self.rook, 3, 1, True)

    def test_move_rook_diagonal(self):
        """
        Tests attempting to move the rook diagonally.
        """
        self.Rook_Move(self.rook, 3, 3, False)

    def test_move_rook_out_of_board_negative(self):
        """
        Tests attempting to move the rook out of the board negatively.
        """
        self.Rook_Move(self.rook, -1, 1, False)

    def test_move_rook_to_occupied_square(self):
        """
        Tests moving the rook to a square occupied by a piece of the same color.
        """
        self.set_piece_and_test_move(3, 1, "WHITE", False)

    def test_move_rook_to_occupied_square_different_color(self):
        """
        Tests moving the rook to a square occupied by a piece of a different color.
        """
        self.set_piece_and_test_move(3, 1, "BLACK", True)

    def test_move_rook_with_obstacle(self):
        """
        Tests moving the rook when there is an obstacle between the rook and the target position.
        """
        self.board.set_piece(2, 1, Rook(2, 1, "WHITE"))
        self.Rook_Move(self.rook, 3, 1, False)

if __name__ == '__main__':
    unittest.main()