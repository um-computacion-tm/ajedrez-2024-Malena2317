import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez')
from piezas.pieza import Piece 

class Knight:
    def __init__(self, start_row, start_col,color):
        self.__row__ = start_row
        self.__col__ = start_col
        self.__color__ = color

    def move(self, start_row, start_col, to_row, to_col, board):
        # Calcular la diferencia en filas y columnas
        row_diff = abs(to_row - start_row)
        col_diff = abs(to_col - start_col)

        # El caballo se mueve en forma de "L": 2 casillas en una dirección y 1 en la otra
        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            # Verificar si la casilla destino está vacía o ocupada por una pieza del otro color
            if board[to_row][to_col] is None or board[to_row][to_col].color != self.color:
                # Mover el caballo
                self.row = to_row
                self.col = to_col
                return True
        return False

# Crear un tablero vacío
board = [[None for _ in range(8)] for _ in range(8)]

# Crear un caballo blanco en la posición (1, 1)
knight = Knight("white", 1, 1)

# Intentar mover el caballo a (3, 2)
print(knight.move(1, 1, 3, 2, board))  # Debería imprimir True si el movimiento es válido

# Imprimir la nueva posición del caballo
print(knight.row, knight.col)  # Debería imprimir 3, 2 si el movimiento fue exitoso
