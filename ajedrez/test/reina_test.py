import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.reina import Queen
from tablero.board import Board

class TestQueen(unittest.TestCase):
    
    def setUp(self):
         # Inicializa la reina y el tablero
        self.board = Board()
        self.queen = Queen(0, 0, "white")
        self.board.set_piece(0, 0, self.queen)
    

    def auxiliar_move(self, row, col, expected_result):
    # Intento mover la Reina
        resultado = self.queen.move(row, col, self.board)
        print(f"Resultado: {resultado}, Expected: {expected_result}")
        print(self.board)
        self.assertEqual(resultado, expected_result)

    def auxiliar_move_to_occupied(self, row, col, color, expected_result):
        # Pongo otra Reina en el lugar
        other_piece = Queen(row, col, color)
        self.board.set_piece(row, col, other_piece)
        self.auxiliar_move(row, col, expected_result)

    def test_move_horizontal(self):
        self.auxiliar_move(0, 5, True)

    def test_move_vertical(self):
        self.auxiliar_move(5, 0, True)

    def test_move_diagonal(self):
        self.auxiliar_move(5, 5, True)

    def test_move_to_occupied_by_same_color(self):
        self.auxiliar_move_to_occupied(0, 5, "white", False)
        self.board.set_piece(0, 5, Queen(0, 5, "white")) 

    def test_move_to_occupied_by_opponent(self):
        self.auxiliar_move_to_occupied(5, 5, "black", True)
   
    def test_move_out_of_board(self):
        self.auxiliar_move(8, 0, False)
        self.auxiliar_move(0, 8, False)
        
    def test_move_to_same_position(self):
        self.auxiliar_move(0, 0, False)

    def test_move_up_left(self):
        self.auxiliar_move(1, 1, True)

    def test_move_up_right(self):
        self.auxiliar_move(0, 6, True)

    def test_move_down_left(self):
        self.auxiliar_move(6, 0, True)

    def test_move_down_right(self):
        self.auxiliar_move(7, 7, True)

if __name__ == '__main__':
    unittest.main()
