import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.rook import Rook
from tablero.board import Board



class TestRook(unittest.TestCase):

    def setUp(self):
        
        # Crear un tablero vacío y un caballo
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.rook = Rook(1, 1, "WHITE")
        self.board[1][1] = self.rook

    def Rook_Move(self, rook, to_row, to_col, expected_result):

        result = rook.move(to_row, to_col, self.board)
        self.assertEqual(result, expected_result)
        
        if expected_result:
            # Verifica que la torre se haya movido a la nueva posición
            self.assertIsNone(self.board[1][1])
            self.assertEqual(self.board[to_row][to_col], rook)
        else:
            # Verifica que la torre permanezca en su lugar original
            self.assertEqual(self.board[1][1], rook)
            if 0 <= to_row < 8 and 0 <= to_col < 8:
                self.assertNotEqual(self.board[to_row][to_col], rook)


    def test_mover_torre_a_casilla_ocupada(self):
        # Agrega una pieza del mismo color en la casilla destino
        self.board[3][1] = Rook(3, 1, "WHITE")
        self.Rook_Move(self.rook, 3, 1, False)

    def test_mover_torre_con_obstaculo(self):
        # Agrega una pieza obstáculo
        self.board[2][1] = Rook(2, 1, "WITHE")
        self.Rook_Move(self.rook, 3, 1, False)

    def test_mover_torre_fuera_del_tablero(self):
        # Intenta mover la torre fuera del tablero
        self.Rook_Move(self.rook, 8, 1, False)

    def test_mover_torre_horizontal(self):
        # Mover torre horizontalmente
        self.Rook_Move(self.rook, 1, 3, True)

    def test_mover_torre_vertical(self):
        # Mover torre verticalmente
        self.Rook_Move(self.rook, 3, 1, True)

    def test_mover_torre_diagonal(self):
        # Intenta mover la torre diagonalmente
        self.Rook_Move(self.rook, 3, 3, False)
    
    def test_mover_torre_a_casilla_ocupada_mismo_color(self):
        self.board[3][1] = Rook(3, 1, "WHITE")
        self.Rook_Move(self.rook, 3, 1, False)

    def test_mover_torre_a_casilla_ocupada_diferente_color(self):
        self.board[3][1] = Rook(3, 1, "BLACK")
        self.Rook_Move(self.rook, 3, 1, True)

    def test_mover_torre_fuera_del_tablero(self):
        self.Rook_Move(self.rook, -1, 1, False)

if __name__ == '__main__':
    unittest.main()


