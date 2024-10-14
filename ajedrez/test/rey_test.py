import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.rey import King

class TestKing(unittest.TestCase):
    def setUp(self):
        # Crear un tablero vacío
        self.board = []
        i = 0
        while i < 8:
            fila = []
            j = 0
            while j < 8:
                fila.append(None)
                j = j + 1
            self.board.append(fila)
            i = i + 1
        
        # Colocar el Rey blanco en (0, 4)
        self.king = King(0, 4, "white")
        self.board[0][4] = self.king

    def assert_king_position(self, row, col, result):
        if result:
            # Comprobar si el rey se movió a la posición correcta
            self.assertEqual(self.king.get_coordinates()[0], row)
            self.assertEqual(self.king.get_coordinates()[1], col)

    def move_and_assert(self, row, col, expected_result=True):
        # Mover el rey existente y verificar el resultado
        result = self.king.move(row, col, self.board)
        self.assertEqual(result, expected_result)
        self.assert_king_position(row, col, result)

    def place_piece_and_move(self, row, col, color, expected_result=True):
        """Coloca una pieza en el tablero y prueba si puede moverse"""
        
        if color == "white" and (row, col) == (self.king.get_coordinates()[0], self.king.get_coordinates()[1]):
            # Si es el mismo rey blanco en la misma posición, probar su movimiento
            result = self.king.move(row, col, self.board)
        else:
            # Colocar una nueva pieza (rey negro) y probar el movimiento
            another_king = King(row, col, color)
            self.board[row][col] = another_king  # Coloca el rey negro en el tablero
            result = self.king.move(row, col, self.board)  # Intenta mover el rey blanco (mover actual rey)
            
        self.assertEqual(result, expected_result)  # Compara resultado esperado

    def test_mover_una_casilla_hacia_abajo(self):
        self.move_and_assert(1, 4, True)

    def test_mover_en_diagonal(self):
        self.move_and_assert(1, 5, True)

    def test_colocar_otra_pieza_y_moverla(self):
        self.place_piece_and_move(1, 4, "white", False)

    def test_mover_pieza_negra(self):
        self.place_piece_and_move(1, 4, "black", True)

    def test_mover_fuera_del_tablero(self):
        self.move_and_assert(8, 4, False)

    def test_mover_a_una_posicion_invalida(self):
        self.move_and_assert(3, 4, False)

    def test_mover_en_horizontal(self):
        self.move_and_assert(0, 5, True)

    def test_mover_en_vertical(self):
        self.move_and_assert(1, 4, True)

    def test_mover_en_diagonal_hacia_la_izquierda(self):
        self.move_and_assert(1, 3, True)

    def test_mover_a_una_posicion_ocupada_por_una_pieza_del_mismo_color(self):
        self.place_piece_and_move(0, 4, "white", False)

    def test_mover_a_una_posicion_ocupada_por_una_pieza_de_diferente_color(self):
        self.place_piece_and_move(0, 4, "black", True)

    def test_mover_fuera_del_tablero_en_la_fila_superior(self):
        self.move_and_assert(-1, 4, False)

    def test_mover_fuera_del_tablero_en_la_columna_izquierda(self):
        self.move_and_assert(0, -1, False)

if __name__ == '__main__':
    unittest.main()
