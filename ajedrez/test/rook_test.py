import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.rook import Rook
from tablero.board import Board
from piezas.pieza import Piece

class TestRook(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.rook_blanca = Rook("WHITE")
        self.rook_negra = Rook("BLACK")

        # Coloca las piezas en el tablero
        self.board.set_piece(0, 0, self.rook_blanca)
        self.board.set_piece(7, 7, self.rook_negra)

    def Rook_Move(self, rook, to_row, to_col, expected_result):
        # Obtener la posición inicial de la torre
        start_row, start_col = self.board.get_piece_position(rook)
        
        if start_row is None or start_col is None:
            self.fail("Start row or column is None")

        # Realiza el movimiento
        result = rook.move(self.board, to_row, to_col)
        
        # Verifica el resultado del movimiento
        self.assertEqual(result, expected_result)
        
        if expected_result:
            # Verifica que la pieza se haya movido a la nueva posición
            self.assertEqual(self.board.get_piece(start_row, start_col), None)
            self.assertEqual(self.board.get_piece(to_row, to_col), rook)
        else:
            # Verifica que la pieza permanezca en su lugar original
            self.assertEqual(self.board.get_piece(start_row, start_col), rook)
            self.assertEqual(self.board.get_piece(to_row, to_col), None)

    def test_mover_torre_vertical(self):
        self.Rook_Move(self.rook_blanca, 4, 0, True)

    def test_mover_torre_horizontal(self):
        self.Rook_Move(self.rook_negra, 7, 5, True)  # Mover torre negra horizontalmente


    def test_mover_torre_diagonal(self):
        self.Rook_Move(self.rook_blanca, 3, 3, False)

    def test_mover_torre_con_obstaculo(self):
        self.board.set_piece(2, 0, Piece(2, 0, "WHITE"))  # Agrega una pieza obstáculo
        self.Rook_Move(self.rook_blanca, 4, 0, False)


if __name__ == '__main__':
    unittest.main()


