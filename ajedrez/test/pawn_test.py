import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.pawn import Pawn
from tablero.board import Board



class TestPawn(unittest.TestCase):

    def setUp(self):
        self.white_pawn = Pawn(1, 0, "WHITE")
        self.black_pawn = Pawn(6, 0, "BLACK")
        self.board = Board() 
        self.board.set_piece(1, 0, self.white_pawn)
        self.board.set_piece(6, 0, self.black_pawn)

        
    def move_pawn_and_verify (self, pawn, start_pos, to_pos, expect_result):
        self.board.set_piece(start_pos[0], start_pos[1], pawn)
        pawn.update_coordinates(start_pos[0], start_pos[1])
        resultado = pawn.move(to_pos[0], to_pos[1], self.board)
        self.assertEqual(resultado, expect_result)

    def test_move_white_pawn_forward(self):
        self.move_pawn_and_verify(self.white_pawn, (1, 0), (2, 0), True)

    def test_move_black_pawn_forward(self):
        self.move_pawn_and_verify(self.black_pawn, (6, 0), (4, 0), True)

    def test_move_white_pawn_two_spaces_forward(self):
        self.move_pawn_and_verify(self.white_pawn, (1, 0), (3, 0), True)

    def test_move_pawn_into_another_piece(self):
        # Colocar una pieza enemiga en la posición (2, 1)
        enemy_pawn = Pawn(2, 1, "BLACK")
        self.board.set_piece(2, 1, enemy_pawn)
        
        # Intentar que el peón blanco capture la pieza enemiga en la diagonal
        self.move_pawn_and_verify(self.white_pawn, (1, 0), (2, 1), True)


if __name__ == '__main__':
    unittest.main()
