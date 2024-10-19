import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.rook import Rook
from tablero.board import Board



class TestRook(unittest.TestCase):

    def setUp(self):
        
        # Crear un tablero vacío y un caballo
        self.board = Board ()
        self.rook = Rook(1, 1, "WHITE")
        self.board.set_piece(1, 1, self.rook)

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


    def set_piece_and_test_move(self, row, col, color, expected_result):
        # Helper to set a piece and test rook movement
        self.board.set_piece(row, col, Rook(row, col, color))
        self.Rook_Move(self.rook, row, col, expected_result)
        
    def test_mover_torre_fuera_del_tablero(self):
        # Intenta mover la torre fuera del tablero
        self.Rook_Move(self.rook, 8, 1, False)

    def test_mover_torre_horizontal(self):
        # Mover torre horizontalmente
        self.board.set_piece(1, 2, None) 
        self.Rook_Move(self.rook, 1, 3, True)

    def test_mover_torre_vertical(self):
        # Mover torre verticalmente
        self.Rook_Move(self.rook, 3, 1, True)

    def test_mover_torre_diagonal(self):
        # Intenta mover la torre diagonalmente
        self.Rook_Move(self.rook, 3, 3, False)

    def test_mover_torre_fuera_del_tablero(self):
        self.Rook_Move(self.rook, -1, 1, False)

    def test_mover_torre_a_casilla_ocupada(self):
        # Coloca una pieza del mismo color en la posición de destino
        self.set_piece_and_test_move(3, 1, "WHITE", False)

    def test_mover_torre_a_casilla_ocupada_diferente_color(self):
        # Coloca una pieza de diferente color en la posición de destino
        self.set_piece_and_test_move(3, 1, "BLACK", True)

    def test_mover_torre_con_obstaculo(self):
        # Coloca un obstáculo entre la torre y la posición de destino
        self.board.set_piece(2, 1, Rook(2, 1, "WHITE"))
        self.Rook_Move(self.rook, 3, 1, False)

    
if __name__ == '__main__':
    unittest.main()


