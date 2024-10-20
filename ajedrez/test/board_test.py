import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.rook import Rook 
from piezas.king import King
from piezas.queen import Queen
from piezas.pawn import Pawn 
from piezas.knight import Knight
from piezas.bishop import Bishop
from tablero.board import Board


class TestBoard(unittest.TestCase):
    """Unit tests for the Board class."""

    def setUp(self):
        """Initialize a Board instance before each test."""
        self.board = Board()

    def test_initialization(self):
        """Test that the board is correctly initialized."""
        self.assertIsNotNone(self.board)
        self.assertEqual(len(self.board.squares), 8)
        for row in self.board.squares:
            self.assertEqual(len(row), 8)

    def test_piece_placement(self):
        """Test that pieces are in their initial positions."""
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertIsInstance(self.board.get_piece(0, 1), Knight)
        self.assertIsInstance(self.board.get_piece(0, 2), Bishop)
        self.assertIsInstance(self.board.get_piece(0, 3), Queen)
        self.assertIsInstance(self.board.get_piece(0, 4), King)
        self.assertIsInstance(self.board.get_piece(1, 0), Pawn)
        self.assertIsInstance(self.board.get_piece(6, 0), Pawn)
        self.assertIsInstance(self.board.get_piece(7, 0), Rook)

    def test_get_piece(self):
        """Test that the correct piece is retrieved from the board."""
        piece = self.board.get_piece(0, 0)
        self.assertIsInstance(piece, Rook)
        self.assertEqual(piece.get_color(), "BLACK")

    def test_set_piece(self):
        """Test that a piece can be placed on the board."""
        new_rook = Rook(4, 4, "WHITE")
        self.board.set_piece(4, 4, new_rook)
        self.assertIs(self.board.get_piece(4, 4), new_rook)
 
    def test_is_within_board(self):
        """Test if given coordinates are within the bounds of the board."""
        self.assertTrue(self.board.is_within_board(0, 0))
        self.assertTrue(self.board.is_within_board(7, 7))
        self.assertFalse(self.board.is_within_board(-1, 0))
        self.assertFalse(self.board.is_within_board(8, 8))
        
    def test_invalid_move(self):
        """Test that an invalid move does not change the state of the board."""
        original_piece = self.board.get_piece(0, 0)
        self.board.move_piece((0, 0), (0, 1))  # Invalid move for a rook
        self.assertIs(self.board.get_piece(0, 0), original_piece)  # The original piece should remain in place

    def test_get_state(self):
        """Test that the state of the board is returned correctly."""
        state = self.board.get_state()
        self.assertEqual(len(state), 8)
        self.assertEqual(len(state[0]), 8)

    def test_set_state(self):
        """Test that the state of the board can be set correctly."""
        state = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
        ]
        self.board.set_state(state)
        self.assertIsNone(self.board.get_piece(0, 0))  # Check that the position is empty

if __name__ == '__main__':
    unittest.main()
