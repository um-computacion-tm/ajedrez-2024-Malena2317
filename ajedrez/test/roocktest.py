import unittest
from piezas.rook import Rook
from tablero.board import Board


class TestRook(unittest.TestCase):
    def setUp(self):
        self.white_rook = Rook("WHITE")
        self.black_rook = Rook("BLACK")
        self.board = Board()

    def test_rook_initialization(self):
        self.assertEqual(self.white_rook.symbol, "R")
        self.assertEqual(self.black_rook.symbol, "r")

    def test_rook_valid_move_horizontal(self):
        self.board.set_piece(0, 0, self.white_rook)
        result = self.white_rook.move(self.board, 0, 0, 0, 7)
        self.assertTrue(result)
        self.assertIsNone(self.board.get_piece(0, 0))
        self.assertEqual(self.board.get_piece(0, 7), self.white_rook)

    def test_rook_valid_move_vertical(self):
        self.board.set_piece(0, 0, self.white_rook)
        result = self.white_rook.move(self.board, 0, 0, 7, 0)
        self.assertTrue(result)
        self.assertIsNone(self.board.get_piece(0, 0))
        self.assertEqual(self.board.get_piece(7, 0), self.white_rook)

    def test_rook_invalid_move(self):
        self.board.set_piece(0, 0, self.white_rook)
        result = self.white_rook.move(self.board, 0, 0, 1, 1)
        self.assertFalse(result)
        self.assertEqual(self.board.get_piece(0, 0), self.white_rook)
        self.assertIsNone(self.board.get_piece(1, 1))

if __name__ == '__main__':
    unittest.main()
