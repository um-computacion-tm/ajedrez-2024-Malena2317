import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.pawn import Pawn
from tablero.board import Board

class TestPawn(unittest.TestCase):

    def setUp(self):
        self.board = Board()  
        self.white_pawn = Pawn(1, 0, "WHITE") 
        self.black_pawn = Pawn(6, 0, "BLACK") 
        self.board.set_piece(1, 0, self.white_pawn)
        self.board.set_piece(6, 0, self.black_pawn)

    def move_pawn_and_verify(self, pawn, start_pos, to_pos, expect_result):
        """Auxiliary function to move a pawn and verify the result."""

        self.board.set_piece(start_pos[0], start_pos[1], pawn)
        # Check positions on the board before movement  
        for row in range(8):
            for col in range(8):
                piece = self.board.get_piece(row, col)
                print(f"Position ({row}, {col}): {piece}")

        resultado = pawn.move(to_pos[0], to_pos[1], self.board)
        print(f"Result of move: {resultado}, Expected: {expect_result}")

        self.assertEqual(resultado, expect_result)

    def test_move_pawn_invalid_forward(self):
        """Test of a pawn trying to move more than two spaces forward."""
        self.move_pawn_and_verify(self.white_pawn, (1, 0), (4, 0), False)
        self.move_pawn_and_verify(self.black_pawn, (6, 0), (3, 0), False)

    def test_move_black_pawn_invalid_forward(self):
        self.move_pawn_and_verify(self.black_pawn, (6, 0), (3, 0), False)
    
    def test_move_white_pawn_invalid_forward(self):
        self.move_pawn_and_verify(self.white_pawn, (1, 0), (4, 0), False)
    
if __name__ == '__main__':

    unittest.main()
