import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.caballo import Knight
from tablero.board import Board 

class TestKnight(unittest.TestCase):

    def setUp(self):
        # Crear un tablero vacío y un caballo
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.knight = Knight(1, 1, "white")
        self.board[1][1] = self.knight

    def place_piece(self, row, col, color):
        # Colocar una pieza en el tablero
        self.board[row][col] = Knight(row, col, color)

    def test_move_L_shape(self):
        # Probar movimiento en 'L' a (3, 2)
        self.assertTrue(self.knight.is_valid_move(3, 2, self.board))
        self.knight.move(3, 2, self.board)
        self.assertEqual((self.knight.get_coordinates()[0], self.knight.get_coordinates()[1]), (3, 2))

    def test_move_not_L_shape(self):
        # Probar movimiento que no es en 'L' a (4, 4)
        self.assertFalse(self.knight.is_valid_move(4, 4, self.board))

    def test_move_to_same_color_piece(self):
        # Probar mover el caballo a donde ya hay otra pieza blanca en (3, 2)
        self.place_piece(3, 2, "white")
        self.assertFalse(self.knight.is_valid_move(3, 2, self.board))

    def test_move_to_empty_space(self):
        # Probar mover el caballo a un espacio vacío en (3, 2)
        self.assertTrue(self.knight.is_valid_move(3, 2, self.board))
        self.knight.move(3, 2, self.board)
        self.assertEqual((self.knight.get_coordinates()[0], self.knight.get_coordinates()[1]), (3, 2))

    def test_move_out_of_board(self):
        # Probar mover el caballo fuera del tablero en (8, 8)
        self.assertFalse(self.knight.is_valid_move(8, 8, self.board))

    def test_move_L_shape_up_left(self):
        # Probar movimiento en 'L' hacia arriba y hacia la izquierda
        self.knight.move(0, 3, self.board)
        self.assertEqual((self.knight.get_coordinates()[0], self.knight.get_coordinates()[1]), (0, 3))

    def test_move_L_shape_up_right(self):
        # Probar movimiento en 'L' hacia arriba y hacia la derecha
        self.knight.move(0, 0, self.board)
        self.knight = Knight(2, 1, "white")
        self.board[2][1] = self.knight
        self.knight.move(0, 3, self.board)
        self.assertEqual((self.knight.get_coordinates()[0], self.knight.get_coordinates()[1]), (0, 3))

    def test_move_L_shape_down_right(self):
        # Probar movimiento en 'L' hacia abajo y hacia la derecha
        self.assertTrue(self.knight.is_valid_move(3, 2, self.board))
        self.knight.move(3, 2, self.board)
        self.assertEqual((self.knight.get_coordinates()[0], self.knight.get_coordinates()[1]), (3, 2))

    def test_move_L_shape_down_left(self):
        # Probar movimiento en 'L' hacia abajo y hacia la izquierda
        self.assertTrue(self.knight.is_valid_move(3, 2, self.board))
        self.knight.move(3, 2, self.board)
        self.assertEqual((self.knight.get_coordinates()[0], self.knight.get_coordinates()[1]), (3, 2))

    def test_move_to_enemy_piece(self):
        # Probar movimiento a una casilla ocupada por una pieza enemiga
        self.place_piece(1, 0, "white")
        self.assertFalse(self.knight.is_valid_move(1, 0, self.board))

if __name__ == '__main__':
    unittest.main()
