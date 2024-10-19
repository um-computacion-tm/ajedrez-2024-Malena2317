import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.knight import Knight
from tablero.board import Board

 
class TestKnight(unittest.TestCase):

    def setUp(self):
        self.board = Board ()
        self.knight = Knight(1, 1, "white")
        self.board[1][1] = self.knight

    def place_piece(self, row, col, color):
        # Colocar una pieza en el tablero
        self.board[row][col] = Knight(row, col, color)
    
    def assert_valid_move(self, row, col, expected):
        result = self.knight.is_valid_move(row, col, self.board)
        print(f"Testing move to ({row}, {col}): expected {expected}, got {result}")
        self.assertEqual(result, expected)

    def test_invalid_moves(self):
        # Test invalid moves (not in L-shape)
        invalid_moves = [(0, 0), (1, 1), (3, 3), (4, 4)]
        for move in invalid_moves:
            with self.subTest(move=move):
                self.assert_valid_move(move[0], move[1], False)

    def test_knight_movement(self):
        # Test that the horse moves correctly to a valid position
        self.knight.move(3, 2, self.board)
        self.assertEqual((self.knight.get_coordinates()[0], self.knight.get_coordinates()[1]), (3, 2))

    def test_move_to_occupied_square(self): 
        # Try moving to a square occupied by a piece of the same color
        self.place_piece(3, 2, "white")
        self.assert_valid_move(3, 2, False)  # No debe poder mover

    def test_move_to_enemy_piece(self):
        # Try movement to a square occupied by an enemy piece
        self.place_piece(3, 2, "black")
        self.assert_valid_move(3, 2, True)  

    def test_move_to_same_position(self): 
        # Try moving to the same position   
        self.assert_valid_move(1, 1, False)

    def test_move_not_L_shape(self):
        # Try movement that is not in 'L' a (4, 4)
        self.assert_valid_move(4, 4, False)

    def test_valid_L_shape_moves(self):
        # Test valid L-shape moves
        valid_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        for move in valid_moves:
            new_row, new_col = self.knight.get_coordinates()[0] + move[0], self.knight.get_coordinates()[1] + move[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                with self.subTest(move=(new_row, new_col)):
                    self.assert_valid_move(new_row, new_col, True)

    
if __name__ == '__main__':
    unittest.main()
