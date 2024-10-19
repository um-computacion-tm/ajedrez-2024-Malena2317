import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.rook import Rook
from tablero.board import Board

class TestRook(unittest.TestCase):

    def setUp(self):
        self.board = Board ()
        self.rook = Rook(1, 1, "WHITE")
        self.board.set_piece(1, 1, self.rook)

    def Rook_Move(self, rook, to_row, to_col, expected_result):
        # Attempt to move the rook to the specified row and column on the board.
        result = rook.move(to_row, to_col, self.board)
        self.assertEqual(result, expected_result)
        
        if expected_result:
            self.assertIsNone(self.board.get_piece(1, 1))
            self.assertEqual(self.board.get_piece(to_row, to_col), rook)
        else:
            self.assertEqual(self.board.get_piece(1, 1), rook)
            if 0 <= to_row < 8 and 0 <= to_col < 8:
                self.assertNotEqual(self.board.get_piece(to_row, to_col), rook)

    def set_piece_and_test_move(self, row, col, color, expected_result):
            # Helper to set a piece and test rook movement
            self.board.set_piece(row, col, Rook(row, col, color))
            self.Rook_Move(self.rook, row, col, expected_result)

    def set_piece_and_test_move(self, row, col, color, expected_result):
        # Helper to set a piece and test rook movement
        self.board.set_piece(row, col, Rook(row, col, color))
        self.Rook_Move(self.rook, row, col, expected_result)

    def test_move_rook_out_of_bounds(self):
        self.Rook_Move(self.rook, 8, 1, False)

    def test_move_rook_horizontal(self):
        self.board.set_piece(1, 2, None)  
        self.Rook_Move(self.rook, 1, 3, True)

    def test_move_rook_vertical(self):
        self.Rook_Move(self.rook, 3, 1, True)

    def test_move_rook_diagonal(self):
        self.Rook_Move(self.rook, 3, 3, False)

    def test_move_rook_to_occupied_square(self):
        self.set_piece_and_test_move(3, 1, "WHITE", False)

    def test_move_rook_to_square_occupied_by_different_color(self):
        self.set_piece_and_test_move(3, 1, "BLACK", True)

    def test_move_rook_with_obstacle(self):
        self.board.set_piece(2, 1, Rook(2, 1, "WHITE"))
        self.Rook_Move(self.rook, 3, 1, False)

if __name__ == '__main__':
    unittest.main()


