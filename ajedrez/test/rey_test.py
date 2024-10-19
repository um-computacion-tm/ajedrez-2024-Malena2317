import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.king import King
from tablero.board import Board

    
class TestKing(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.king = King(0, 4, "white")
        self.board[0][4] = self.king

    def assert_king_position(self, row, col, result):
        if result:
            # Check if the king moved to the correct position
            self.assertEqual(self.king.get_coordinates()[0], row)
            self.assertEqual(self.king.get_coordinates()[1], col)

    def move_and_assert(self, row, col, expected_result=True):
        #Move the king to the position (row, col) and check if the move was successfu
        result = self.king.move(row, col, self.board)
        self.assertEqual(result, expected_result)
        self.assert_king_position(row, col, result)

    def place_piece_and_move(self, row, col, color, expected_result=True):
        """Place a piece on the board and test if it can move"""
        
        if color == "white" and (row, col) == (self.king.get_coordinates()[0], self.king.get_coordinates()[1]):
            result = self.king.move(row, col, self.board)
        else:
            another_king = King(row, col, color)
            self.board[row][col] = another_king  
            result = self.king.move(row, col, self.board)  
            
        self.assertEqual(result, expected_result)  

    def test_move_one_square_down(self):
        self.move_and_assert(1, 4, True)

    def test_move_diagonally(self):
        self.move_and_assert(1, 5, True)

    def test_place_another_piece_and_move(self):
        self.place_piece_and_move(1, 4, "white", False)

    def test_move_black_piece(self):
        self.place_piece_and_move(1, 4, "black", True)

    def test_move_off_the_board(self):
        self.move_and_assert(8, 4, False)

    def test_move_to_an_invalid_position(self):
        self.move_and_assert(3, 4, False)

    def test_move_horizontally(self):
        self.move_and_assert(0, 5, True)

    def test_move_vertically(self):
        self.move_and_assert(1, 4, True)

    def test_move_diagonally_to_the_left(self):
        self.move_and_assert(1, 3, True)

    def test_move_to_a_position_occupied_by_a_piece_of_the_same_color(self):
        self.place_piece_and_move(0, 4, "white", False)

    def test_move_to_a_position_occupied_by_a_piece_of_different_color(self):
        self.place_piece_and_move(0, 4, "black", True)

    def test_move_off_the_board_at_the_top_row(self):
        self.move_and_assert(-1, 4, False)

    def test_move_off_the_board_at_the_left_column(self):
        self.move_and_assert(0, -1, False)


if __name__ == '__main__':
    unittest.main()
