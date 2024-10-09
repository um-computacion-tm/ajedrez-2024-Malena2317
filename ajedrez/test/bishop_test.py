import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.bishop import Alfil
from tablero.board import Board

class TestBishop(unittest.TestCase):

    def setUp(self):
        # Inicializa el tablero y la pieza
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.alfil = Alfil(1, 1, "blanco")
        self.board[1][1] = self.alfil

    def place_piece(self, row, col, color):
        # Colocar una pieza en el tablero
        self.board[row][col] = None
        self.board[row][col] = Alfil(row, col, color)

    def test_move_diagonal_free(self):
        # Test para mover el alfil en diagonal a una posición libre
        self.assertTrue(self.alfil.is_valid_move(3, 3, self.board))
        self.alfil.move(3, 3, self.board)
        self.assertEqual((self.alfil.get_coordinates()[0], self.alfil.get_coordinates()[1]), (3, 3))

    def test_move_to_occupied_position(self):
        # Test para intentar mover el alfil a una posición ocupada
        self.place_piece(3, 3, "BLACK")
        self.assertTrue(self.alfil.is_valid_move(3, 3, self.board))

    def test_move_out_of_board(self):
        # Test para intentar mover el alfil fuera del tablero
        self.assertFalse(self.alfil.is_valid_move(8, 8, self.board))

    def test_move_diagonal_up_left(self):
        # Test para mover el alfil en diagonal hacia arriba y hacia la izquierda
        self.assertTrue(self.alfil.is_valid_move(0, 0, self.board))
        self.alfil.move(0, 0, self.board)
        self.assertEqual((self.alfil.get_coordinates()[0], self.alfil.get_coordinates()[1]), (0, 0))

    def test_move_diagonal_up_right(self):
        # Test para mover el alfil en diagonal hacia arriba y hacia la derecha
        self.alfil.move(0, 0, self.board)
        self.alfil = Alfil(2, 2, "WHITE")
        self.board[2][2] = self.alfil
        self.assertTrue(self.alfil.is_valid_move(1, 3, self.board))

    def test_move_to_enemy_piece(self):
        # Test para intentar mover el alfil a una posición ocupada por una pieza enemiga
        self.place_piece(3, 3, "BLACK")
        self.assertTrue(self.alfil.is_valid_move(3, 3, self.board))
        self.alfil.move(3, 3, self.board)
        self.assertEqual((self.alfil.get_coordinates()[0], self.alfil.get_coordinates()[1]), (3, 3))

    def test_move_to_empty_space(self):
        # Test para mover el alfil a una posición vacía
        self.assertTrue(self.alfil.is_valid_move(3, 3, self.board))
        self.alfil.move(3, 3, self.board)
        self.assertEqual((self.alfil.get_coordinates()[0], self.alfil.get_coordinates()[1]), (3, 3))
    
    def test_move_to_same_color_piece(self):
        # Test para intentar mover el alfil a una posición ocupada por una pieza del mismo color
        self.place_piece(3, 3, "blanco")
        self.assertFalse(self.alfil.is_valid_move(3, 3, self.board))
        self.board[3][3] = None
        self.place_piece(3, 3, "negro")
        self.assertTrue(self.alfil.is_valid_move(3, 3, self.board))

if __name__ == '__main__':
    unittest.main()



