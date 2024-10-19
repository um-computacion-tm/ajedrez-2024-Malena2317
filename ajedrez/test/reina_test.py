import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.queen import Queen
from tablero.board import Board

class TestQueen(unittest.TestCase):

    def setUp(self):
        # Inicializa la reina y el tablero
        self.board = Board()
        self.queen = Queen(0, 0, "white")
        self.board.set_piece(0, 0, self.queen)

    def auxiliar_move(self, row, col, expected_result):
        print(f"Probando movimiento a ({row}, {col}), se espera {'éxito' if expected_result else 'fallo'}.")
        result = self.queen.move(row, col, self.board)
        print(f"Resultado: {result}, Expected: {expected_result}")
        self.assertEqual(result, expected_result)

    def auxiliar_move_to_occupied(self, row, col, color, expected_result):
        print(f"Colocando una pieza de color {color} en ({row}, {col}).")
        other_piece = Queen(row, col, color)
        self.board.set_piece(row, col, other_piece)
        self.auxiliar_move(row, col, expected_result)

    def test_move_horizontal(self):
        self.auxiliar_move(0, 5, True)  # Mover a la derecha en la fila 0

    def test_move_vertical(self):
        self.auxiliar_move(5, 0, True)  # Mover hacia abajo en la columna 0

    def test_move_diagonal(self):
        self.auxiliar_move(5, 5, True)  # Mover diagonalmente hacia abajo a la derecha

    def test_move_out_of_board(self):
        self.auxiliar_move(8, 0, False)  # Fuera de los límites del tablero
        self.auxiliar_move(0, 8, False)  # Fuera de los límites del tablero

    def test_move_to_occupied_by_same_color(self):
        print("Probando movimiento a posición ocupada por la misma pieza.")
        self.board.set_piece(0, 5, Queen(0, 5, "white"))  # Coloca una pieza del mismo color
        self.auxiliar_move(0, 5, False)

    def test_move_to_occupied_by_opponent(self):
        self.auxiliar_move_to_occupied(5, 5, "black", True)  # Debe poder capturar

    def test_move_to_same_position(self):
        self.auxiliar_move(0, 0, False)  # No se puede mover a la misma posición

    def test_move_up_left(self):
        self.auxiliar_move(1, 1, True)  # Mover diagonalmente hacia arriba a la izquierda

    def test_move_up_right(self):
        self.auxiliar_move(0, 6, True)  # Mover diagonalmente hacia arriba a la derecha

    def test_move_down_left(self):
        self.auxiliar_move(6, 0, True)  # Mover diagonalmente hacia abajo a la izquierda

    def test_move_down_right(self):
        self.auxiliar_move(7, 7, True)  # Mover diagonalmente hacia abajo a la derecha

if __name__ == '__main__':
    unittest.main()
