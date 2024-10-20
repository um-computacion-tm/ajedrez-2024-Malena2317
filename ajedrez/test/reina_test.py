import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.queen import Queen
from tablero.board import Board

class TestQueen(unittest.TestCase):
    """
    Unit test class for testing the Queen piece in a chess game.

    This class contains various test cases to validate the movement rules and behavior
    of the Queen piece on the chessboard, ensuring that it adheres to the game's 
    rules for valid and invalid moves.
    """
    
    def setUp(self):
        """
        Set up the test environment by initializing the Queen and the board.

        This method creates a Board instance and places a Queen piece at the specified position (0, 0).
        """
        # Initialize the queen and the board
        self.board = Board()
        self.queen = Queen(0, 0, "white")
        self.board.set_piece(0, 0, self.queen)

    def auxiliar_move(self, row, col, expected_result):
        """
        Attempt to move the Queen to the specified position and assert the result.

        Args:
            row (int): The target row index for the move.
            col (int): The target column index for the move.
            expected_result (bool): The expected result of the move (True for successful, False for failed).
        """
        # Attempt to move the Queen
        result = self.queen.move(row, col, self.board)
        print(f"Result: {result}, Expected: {expected_result}")
        print(self.board)
        self.assertEqual(result, expected_result)

    def auxiliar_move_to_occupied(self, row, col, color, expected_result):
        """
        Place another Queen on the specified position and attempt to move the original Queen.

        Args:
            row (int): The row index of the occupied square.
            col (int): The column index of the occupied square.
            color (str): The color of the piece occupying the square ("white" or "black").
            expected_result (bool): The expected result of the move (True for successful, False for failed).
        """
        # Place another Queen in the position
        other_piece = Queen(row, col, color)
        self.board.set_piece(row, col, other_piece)
        self.auxiliar_move(row, col, expected_result)

    def test_move_horizontal(self):
        """
        Test the Queen's ability to move horizontally across the board.
        """
        self.auxiliar_move(0, 5, True)

    def test_move_vertical(self):
        """
        Test the Queen's ability to move vertically across the board.
        """
        self.auxiliar_move(5, 0, True)

    def test_move_diagonal(self):
        """
        Test the Queen's ability to move diagonally across the board.
        """
        self.auxiliar_move(5, 5, True)

    def test_move_to_occupied_by_same_color(self):
        """
        Test the Queen's attempt to move to a square occupied by a piece of the same color.
        """
        self.auxiliar_move_to_occupied(0, 5, "white", False)
        self.board.set_piece(0, 5, Queen(0, 5, "white")) 

    def test_move_to_occupied_by_opponent(self):
        """
        Test the Queen's ability to move to a square occupied by an opponent's piece.
        """
        self.auxiliar_move_to_occupied(5, 5, "black", True)
   
    def test_move_out_of_board(self):
        """
        Test the Queen's attempts to move out of the board's boundaries.
        """
        self.auxiliar_move(8, 0, False)
        self.auxiliar_move(0, 8, False)

    def test_move_to_same_position(self):
        """
        Test the Queen's attempt to move to the same position.
        """
        self.auxiliar_move(0, 0, False)

    def test_move_up_left(self):
        """
        Test the Queen's ability to move diagonally up to the left.
        """
        self.auxiliar_move(1, 1, True)

    def test_move_up_right(self):
        """
        Test the Queen's ability to move diagonally up to the right.
        """
        self.auxiliar_move(0, 6, True)

    def test_move_down_left(self):
        """
        Test the Queen's ability to move diagonally down to the left.
        """
        self.auxiliar_move(6, 0, True)

    def test_move_down_right(self):
        """
        Test the Queen's ability to move diagonally down to the right.
        """
        self.auxiliar_move(7, 7, True)

if __name__ == '__main__':
    unittest.main()
