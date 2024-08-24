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

    def test_mover_torre_vertical(self):
        self.board.__positions__[0][0] = self.rook_blanca
        resultado = self.rook_blanca.move(self.board, 0, 0, 4, 0)
        self.assertEqual(resultado, True)
        # Verificar si la antigua posición está vacía
        self.assertEqual(self.board.get_piece(0, 0), None)
        # Verificar si la torre está en la nueva posición
        self.assertEqual(self.board.get_piece(4, 0), self.rook_blanca)

    def test_mover_torre_horizontal(self):
        # Colocar la torre negra en (0, 0)
        self.board.__positions__[0][0] = self.rook_negra
        # Moverla a (0, 5)
        resultado = self.rook_negra.move(self.board, 0, 0, 0, 5)
        # Verificar si el movimiento es True
        self.assertEqual(resultado, True)
        # Comprobar si la antigua posición está vacía
        self.assertEqual(self.board.get_piece(0, 0), None)
        # Verificar si la torre está en la nueva posición
        self.assertEqual(self.board.get_piece(0, 5), self.rook_negra)

    def test_mover_torre_diagonal(self):
        # Colocar la torre blanca en (0, 0)
        self.board.__positions__[0][0] = self.rook_blanca
        # Intentar moverla a (3, 3) en diagonal
        resultado = self.rook_blanca.move(self.board, 0, 0, 3, 3)
        # Comprobar si el movimiento es False (debería fallar)
        self.assertEqual(resultado, False)
        # Verificar si la torre no se movió
        self.assertEqual(self.board.get_piece(0, 0), self.rook_blanca)

    def test_mover_torre_con_obstaculo(self):
        # Colocar la torre blanca en (0, 0)
        self.board.__positions__[0][0] = self.rook_blanca
        # Colocar una torre negra en (2, 0) como obstáculo
        self.board.__positions__[2][0] = self.rook_negra
        # Intentar mover la torre blanca a (4, 0)
        resultado = self.rook_blanca.move(self.board, 0, 0, 4, 0)
        # Verificar si el movimiento es False (debería fallar)
        self.assertEqual(resultado, False)
        # Verificar si la torre blanca no se movió
        self.assertEqual(self.board.get_piece(0, 0), self.rook_blanca)
        # Verificar si la torre negra sigue en su lugar
        self.assertEqual(self.board.get_piece(2, 0), self.rook_negra)

    def test_mover_torre_al_mismo_lugar(self):
        # Colocar la torre negra en (0, 0)
        self.board.__positions__[0][0] = self.rook_negra
        # Intentar moverla a (0, 0) (mismo lugar)
        resultado = self.rook_negra.move(self.board, 0, 0, 0, 0)
        # Verificar si el movimiento es False (debería fallar)
        self.assertEqual(resultado, False)
        # Verificar si la torre negra sigue en su lugar
        self.assertEqual(self.board.get_piece(0, 0), self.rook_negra)

if __name__ == '__main__':
    unittest.main()
