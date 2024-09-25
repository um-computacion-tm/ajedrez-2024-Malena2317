import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.pawn import Pawn
from piezas.pawn import Position


class TestPawn(unittest.TestCase):

    def setUp(self):
        self.peon_blanco = Pawn("WHITE")
        self.peon_negro = Pawn("BLACK")
        self.tablero = [[None] * 8 for _ in range(8)]
        
    def mover_peon_y_verificar(self, pawn, start_pos, to_pos, expect_result):
        # Creamos las posiciones inicial y final
        start_position = Position(start_pos[0], start_pos[1])
        to_position = Position(to_pos[0], to_pos[1])
        
        # Colocamos el peón en la posición inicial del tablero
        self.tablero[start_pos[0]][start_pos[1]] = pawn
        
        # Llamamos al método mover del peón
        resultado = pawn.move(start_position, to_position, self.tablero)
        
        # Verificamos si el resultado es el esperado
        self.assertEqual(resultado, expect_result)

    def test_mover_peon_blanco_hacia_adelante(self):
        self.mover_peon_y_verificar(self.peon_blanco, (3, 3), (4, 3), True)

    def test_mover_peon_negro_hacia_adelante(self):
        self.mover_peon_y_verificar(self.peon_negro, (4, 4), (3, 4), True)

    def test_mover_peon_blanco_hacia_atras(self):
        self.mover_peon_y_verificar(self.peon_blanco, (3, 3), (2, 3), False)

    def test_mover_peon_negro_hacia_atras(self):
        self.mover_peon_y_verificar(self.peon_negro, (4, 4), (5, 4), False)

    def test_mover_peon_misma_fila(self):
        self.mover_peon_y_verificar(self.peon_blanco, (3, 3), (3, 4), False)

    def test_mover_peon_diferente_columna(self):
        self.mover_peon_y_verificar(self.peon_negro, (4, 4), (5, 5), False)

    
if __name__ == '__main__':
    unittest.main()