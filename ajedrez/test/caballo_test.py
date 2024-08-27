import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.caballo import Knight

class TestKnight(unittest.TestCase):

    def setUp(self):
        # Crear un tablero vacío y un caballo
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.knight = Knight(1, 1, "white")
        self.board[1][1] = self.knight

    def test_move_L_shape(self):
        # Probar movimiento en "L" a (3, 2)
        result = self.knight.move(1, 1, 3, 2, self.board)
        self.assertTrue(result)
        self.assertEqual(self.knight.row, 3)
        self.assertEqual(self.knight.col, 2)

    def test_move_not_L_shape(self):
        # Probar movimiento que no es en "L" a (4, 4)
        result = self.knight.move(1, 1, 4, 4, self.board)
        self.assertFalse(result)
        self.assertEqual(self.knight.row, 1)
        self.assertEqual(self.knight.col, 1)

    def test_move_to_same_color_piece(self):
        # Probar mover el caballo a donde ya hay otra pieza blanca en (3, 2)
        another_knight = Knight(3, 2, "white")
        self.board[3][2] = another_knight
        result = self.knight.move(1, 1, 3, 2, self.board)
        self.assertFalse(result)
        self.assertEqual(self.knight.row, 1)
        self.assertEqual(self.knight.col, 1)

    def test_move_to_opponent_piece(self):
        # Probar mover el caballo a donde hay una pieza negra en (3, 2)
        another_knight = Knight(3, 2, "black")
        self.board[3][2] = another_knight
        result = self.knight.move(1, 1, 3, 2, self.board)
        self.assertTrue(result)
        self.assertEqual(self.knight.row, 3)
        self.assertEqual(self.knight.col, 2)

if __name__ == '__main__':
    unittest.main()
