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

    def test_mover_una_casilla_hacia_abajo(self):
        result = self.king.move(1, 4, self.board)
        self.assertTrue(result)
        if result == True:  # Verificar si el movimiento fue exitoso
            self.assertEqual(self.king.__row__, 1)
            self.assertEqual(self.king.__col__, 4)

    def test_mover_en_diagonal(self):
        result = self.king.move(1, 5, self.board)
        self.assertTrue(result)
        if result == True:
            self.assertEqual(self.king.__row__, 1)
            self.assertEqual(self.king.__col__, 5)

    def test_colocar_otra_pieza_y_moverla(self):
        another_king = King(1, 4, "white")
        self.board[1][4] = another_king
        result = self.king.move(1, 4, self.board)
        self.assertFalse(result)
        if result == False:
            self.assertEqual(self.king.__row__, 0)
            self.assertEqual(self.king.__col__, 4)

    def test_mover_pieza_negra(self):
        # Colocar una pieza negra y tratar de moverse allí
        another_king = King(1, 4, "black")
        self.board[1][4] = another_king
        result = self.king.move(1, 4, self.board)
        self.assertTrue(result)
        if result == True:
            self.assertEqual(self.king.__row__, 1)
            self.assertEqual(self.king.__col__, 4)

if __name__ == '__main__':
    unittest.main()
