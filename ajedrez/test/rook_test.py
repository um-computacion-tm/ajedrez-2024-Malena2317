import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.rook import Rook
from tablero.board import Board

class TestRook(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.rook_blanca = Rook("WHITE")
        self.rook_negra = Rook("BLACK")

    def Test_Move(self, rook, start_row, start_col, to_row, to_col, expected_result):
        # Coloca la pieza en la posición inicial
        self.board.set_piece(start_row, start_col, rook)
        
        # Realiza el movimiento
        result = rook.move(self.board, start_row , start_col, to_row, to_col )
        
        # Verifica el resultado del movimiento
        self.assertEqual(result, expected_result)
        
        if expected_result:
            # Verifica que la pieza se haya movido a la nueva posición
            self.assertEqual(self.board.get_piece(start_row , start_col), None)
            self.assertEqual(self.board.get_piece(to_row, to_col ), rook)
        else:
            # Verifica que la pieza permanezca en su lugar original
            self.assertEqual(self.board.get_piece(start_row , start_col), rook)
            # Verifica que la nueva posición siga vacía
            self.assertEqual(self.board.get_piece(to_row , to_col), None)

    def test_mover_torre_vertical(self):
        self.Test_Move(self.rook_blanca, 0, 0, 4, 0, True)

    def test_mover_torre_horizontal(self):
        self.Test_Move(self.rook_negra, 0, 0, 0, 5, True)

    def test_mover_torre_diagonal(self):
        self.Test_Move(self.rook_blanca, 0, 0, 3, 3, False)

    def test_mover_torre_con_obstaculo(self):
        self.board.set_piece(2, 0, self.rook_negra)
        self.Test_Move(self.rook_blanca, 0, 0, 4, 0, False)


if __name__ == '__main__':
    unittest.main()


