import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.pawn import Pawn
from tablero.board import Board

from tablero.board import Board



class TestPawn(unittest.TestCase):
    """
    Test cases for the Pawn chess piece.
    """

    def setUp(self):
        self.white_pawn = Pawn(1, 0, "WHITE")
        self.black_pawn = Pawn(6, 0, "BLACK")
        self.board = Board() 
        self.board.set_piece(1, 0, self.white_pawn)
        self.board.set_piece(6, 0, self.black_pawn)

    def move_pawn_and_verify(self, pawn, start_pos, to_pos, expect_result):
        """
        Helper function to move a pawn and verify the result.

        Args:
            pawn (Pawn): The pawn piece to move.
            start_pos (tuple): The starting position of the pawn (row, col).
            to_pos (tuple): The target position for the move (row, col).
            expect_result (bool): Expected validity of the move (True for valid, False for invalid).
        """
        # Place the pawn at the starting position
        self.board.set_piece(start_pos[0], start_pos[1], pawn)

        # Debug: Print the board state before the move
        for row in range(8):
            for col in range(8):
                piece = self.board.get_piece(row, col)
                print(f"Position ({row}, {col}): {piece}")

        # Perform the move and verify the result
        result = pawn.move(to_pos[0], to_pos[1], self.board)
        print(f"Result of move: {result}, Expected: {expect_result}")

        self.assertEqual(result, expect_result)
        self.white_pawn = Pawn(1, 0, "WHITE")
        self.black_pawn = Pawn(6, 0, "BLACK")
        self.board = Board() 
        self.board.set_piece(1, 0, self.white_pawn)
        self.board.set_piece(6, 0, self.black_pawn)

        
    def move_pawn_and_verify(self, pawn, start_pos, to_pos, expect_result):
        """Función auxiliar para mover un peón y verificar el resultado."""

        # Establecer el peón en su posición inicial
        self.board.set_piece(start_pos[0], start_pos[1], pawn)

        # Verificar posiciones en el tablero antes del movimiento
        for row in range(8):
            for col in range(8):
                piece = self.board.get_piece(row, col)
                print(f"Position ({row}, {col}): {piece}")

        resultado = pawn.move(to_pos[0], to_pos[1], self.board)
        print(f"Result of move: {resultado}, Expected: {expect_result}")

        self.assertEqual(resultado, expect_result)

    def test_move_pawn_invalid_forward(self):
        """
        Test a pawn attempting to move more than two spaces forward.
        """
        self.move_pawn_and_verify(self.white_pawn, (1, 0), (4, 0), False)
        self.move_pawn_and_verify(self.black_pawn, (6, 0), (3, 0), False)
    def test_move_pawn_invalid_forward(self):
        """Test de un peón intentando moverse más de dos espacios hacia adelante."""
        self.move_pawn_and_verify(self.white_pawn, (1, 0), (4, 0), False)
        self.move_pawn_and_verify(self.black_pawn, (6, 0), (3, 0), False)

    def test_move_black_pawn_invalid_forward(self):
        """
        Test a black pawn attempting to move more than two spaces forward.
        """
        self.move_pawn_and_verify(self.black_pawn, (6, 0), (3, 0), False)
    
    def test_move_white_pawn_invalid_forward(self):
        """
        Test a white pawn attempting to move more than two spaces forward.
        """
        self.move_pawn_and_verify(self.white_pawn, (1, 0), (4, 0), False)
    def test_move_black_pawn_invalid_forward(self):
        """Test de un peón negro intentando moverse más de dos espacios hacia adelante."""
        self.move_pawn_and_verify(self.black_pawn, (6, 0), (3, 0), False)
    
    def test_move_white_pawn_invalid_forward(self):
        """Test de un peón blanco intentando moverse más de dos espacios hacia adelante."""
        self.move_pawn_and_verify(self.white_pawn, (1, 0), (4, 0), False)
    
if __name__ == '__main__':

    unittest.main()
