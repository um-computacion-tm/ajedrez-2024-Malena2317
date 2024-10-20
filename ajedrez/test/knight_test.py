import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.knight import Knight
<<<<<<< HEAD
from tablero.board import Board 

class TestKnight(unittest.TestCase):
    """
    Unit test class for testing the Knight piece in a chess game.

    This class contains various test cases to validate the movement rules and behavior
    of the Knight piece on the chessboard, ensuring that it adheres to the game's 
    rules for valid and invalid moves.
    """

    def setUp(self):
        """
        Set up the test environment by creating an empty board and placing a Knight piece.

        This method initializes a Board instance and a Knight piece at the specified position (1, 1).
        """
        # Create an empty board and a knight
=======
from  tablero.board import Board

class TestKnight(unittest.TestCase):
    """
    Test cases for the Knight chess piece.
    """

    def setUp(self):
        
>>>>>>> 38bcfbf (entrega)
        self.board = Board()
        self.knight = Knight(1, 1, "white")
        self.board.set_piece(1, 1, self.knight)

    def place_piece(self, row, col, color):
        """
<<<<<<< HEAD
        Place a Knight piece on the board at the specified position.

        Args:
            row (int): The row index where the piece will be placed.
            col (int): The column index where the piece will be placed.
            color (str): The color of the Knight piece ("white" or "black").
        """
        # Place a piece on the board
=======
        Places a knight piece on the board at the specified position.

        Args:
            row (int): The row position to place the knight.
            col (int): The column position to place the knight.
            color (str): The color of the knight ('white' or 'black').
        """
>>>>>>> 38bcfbf (entrega)
        self.board.set_piece(row, col, Knight(row, col, color))
    
    def assert_valid_move(self, row, col, expected):
        """
<<<<<<< HEAD
        Assert that the Knight's move to the specified position is valid.

        Args:
            row (int): The row index for the move.
            col (int): The column index for the move.
            expected (bool): The expected result (True for valid, False for invalid).
=======
        Asserts that the knight's move to the specified position is valid.

        Args:
            row (int): The target row position for the move.
            col (int): The target column position for the move.
            expected (bool): Expected validity of the move (True for valid, False for invalid).
>>>>>>> 38bcfbf (entrega)
        """
        result = self.knight.is_valid_move(row, col, self.board)
        print(f"Testing move to ({row}, {col}): expected {expected}, got {result}")
        self.assertEqual(result, expected)

    def test_invalid_moves(self):
        """
<<<<<<< HEAD
        Test invalid moves that do not follow the L-shape movement of the Knight.
        """
        # Test invalid moves (not in L-shape)
=======
        Tests invalid moves for the knight that do not conform to L-shape movement.
        """
>>>>>>> 38bcfbf (entrega)
        invalid_moves = [(0, 0), (1, 1), (3, 3), (4, 4)]
        for move in invalid_moves:
            with self.subTest(move=move):
                self.assert_valid_move(move[0], move[1], False)

    def test_knight_movement(self):
        """
<<<<<<< HEAD
        Test that the Knight moves correctly to a valid position.
        """
        # Test that the knight moves correctly to a valid position
=======
        Tests that the knight can move correctly to a valid position.
        """
>>>>>>> 38bcfbf (entrega)
        self.knight.move(3, 2, self.board)
        self.assertEqual((self.knight.get_coordinates()[0], self.knight.get_coordinates()[1]), (3, 2))

    def test_move_to_occupied_square(self):
        """
<<<<<<< HEAD
        Test movement to a square occupied by a piece of the same color.
        """
        # Test movement to an occupied square by a piece of the same color
=======
        Tests moving the knight to a square occupied by a piece of the same color.
        """
>>>>>>> 38bcfbf (entrega)
        self.place_piece(3, 2, "white")
        self.assert_valid_move(3, 2, False)  # Should not be able to move

    def test_move_to_enemy_piece(self):
        """
<<<<<<< HEAD
        Test movement to a square occupied by an enemy piece.
        """
        # Test movement to a square occupied by an enemy piece
=======
        Tests moving the knight to a square occupied by an enemy piece.
        """
>>>>>>> 38bcfbf (entrega)
        self.place_piece(3, 2, "black")
        self.assert_valid_move(3, 2, True)  # The knight should be able to capture it

    def test_move_to_same_position(self):
        """
<<<<<<< HEAD
        Test movement to the same position.
        """
        # Test movement to the same position
=======
        Tests moving the knight to the same position.
        """
>>>>>>> 38bcfbf (entrega)
        self.assert_valid_move(1, 1, False)

    def test_move_not_L_shape(self):
        """
<<<<<<< HEAD
        Test movement that does not form an L-shape to (4, 4).
        """
        # Test movement that is not in 'L' to (4, 4)
=======
        Tests moving the knight in a non-L shape to (4, 4).
        """
>>>>>>> 38bcfbf (entrega)
        self.assert_valid_move(4, 4, False)

    def test_valid_L_shape_moves(self):
        """
<<<<<<< HEAD
        Test valid L-shape moves for the Knight piece.
        """
        # Test valid L-shape moves
=======
        Tests valid L-shape moves for the knight from its current position.
        """
>>>>>>> 38bcfbf (entrega)
        valid_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        for move in valid_moves:
            new_row, new_col = self.knight.get_coordinates()[0] + move[0], self.knight.get_coordinates()[1] + move[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                with self.subTest(move=(new_row, new_col)):
                    self.assert_valid_move(new_row, new_col, True)

<<<<<<< HEAD
    
if __name__ == '__main__':
    unittest.main()

=======
if __name__ == '__main__':
    unittest.main()
>>>>>>> 38bcfbf (entrega)
