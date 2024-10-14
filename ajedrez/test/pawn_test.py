import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.pawn import Pawn


class TestPawn(unittest.TestCase):

    def setUp(self):
        self.white_pawn = Pawn("WHITE")
        self.black_pawn = Pawn("BLACK")
        self.board = [[None] * 8 for _ in range(8)]
        
    def move_pawn_and_verify (self, pawn, start_pos, to_pos, expect_result):
        self.board[start_pos[0]][start_pos[1]] = pawn
        print(f"Tablero antes del movimiento: {self.board}")
        resultado = pawn.move(to_pos[0], to_pos[1], self.board)
        print(f"Resultado del movimiento: {resultado}")
        self.assertEqual(resultado, expect_result)

    def test_move_white_pawn_forward(self):
        self.move_pawn_and_verify(self.white_pawn, (0, 0), (1, 0), True)

    def test_move_black_pawn_forward(self):
        self.move_pawn_and_verify(self.black_pawn, (6,0), (4,0), True)

    def test_move_white_pawn_backward(self):
        self.move_pawn_and_verify(self.white_pawn, (0, 0), (-1, 0), False)

    def test_move_black_pawn_backward(self):
        self.move_pawn_and_verify(self.black_pawn, (7, 0), (8, 0), False)

    def test_move_pawn_same_row(self):
        self.move_pawn_and_verify(self.white_pawn, (0, 0), (0, 1), False)

    def test_move_pawn_different_column(self):
        self.move_pawn_and_verify(self.black_pawn, (7, 0), (6, 1), False)

    def test_move_white_pawn_two_spaces_forward(self):
        self.move_pawn_and_verify(self.white_pawn, (0, 0), (2, 0), False)

    def test_move_black_pawn_two_spaces_forward(self):
        self.move_pawn_and_verify(self.black_pawn, (7, 0), (6, 1), False)

    def test_move_pawn_off_board(self):
        self.move_pawn_and_verify(self.white_pawn, (0, 0), (-1, 0), False)
        self.move_pawn_and_verify(self.black_pawn, (7, 0), (8, 0), False)

    def test_move_pawn_into_another_piece(self):
        # Place another piece on the destination square
        self.board[1][0] = Pawn("WHITE")
        self.move_pawn_and_verify(self.white_pawn,(0, 0), (1, 0), False)

if __name__ == '__main__':
    unittest.main()