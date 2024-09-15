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

    def Mover_y_Verificar(self, start_pos, end_pos, expected_result, expected_pos):
        "Auxiliar para mover el caballo y verificar el resultado."
        result = self.knight.move(start_pos[0], start_pos[1], end_pos[0], end_pos[1], self.board)
        self.assertEqual(result, expected_result)
        self.assertEqual((self.knight.row, self.knight.col), expected_pos)

    def place_piece(self, row, col, color):
        "Colocar una pieza en el tablero."
        self.board[row][col] = Knight(row, col, color)

    def test_move_L_shape(self):
        "Probar movimiento en 'L' a (3, 2)."
        self.move_and_check((1, 1), (3, 2), True, (3, 2))

    def test_move_not_L_shape(self):
        "Probar movimiento que no es en 'L' a (4, 4)."
        self.move_and_check((1, 1), (4, 4), False, (1, 1))

    def test_move_to_same_color_piece(self):
        "Probar mover el caballo a donde ya hay otra pieza blanca en (3, 2)."
        self.place_piece(3, 2, "white")
        self.move_and_check((1, 1), (3, 2), False, (1, 1))

if __name__ == '__main__':
    unittest.main()
