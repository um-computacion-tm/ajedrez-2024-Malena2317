import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from exception import is_valid_diagonal_move








class Alfil:
    def __init__(self, row, col, color, board = None):
        self.__row__ = row
        self.__col__ = col
        self.__color__ = color
        self.board = board
        self.symbol = "♗" if color == "WHITE" else "♝"

        # Verifica si el movimiento es diagonal y si la casilla de destino está vacía.
         
    def mover(self, to_row, to_col, board):
        # Utiliza la función is_valid_diagonal_move desde exceptions
        if not is_valid_diagonal_move(self.__row__, self.__col__, to_row, to_col, self.board):
            raise InvalidMoveBishop((to_row, to_col))
    
    def get_row(self):
        return self.__row__
    
    def get_col(self):
        return self.__col__
    
tablero = [[None for _ in range(8)] for _ in range(8)]
alfil = Alfil(1, 1, "blanco")
print(alfil.mover(3, 3, tablero))  # True
print(alfil.get_row(), alfil.get_col())  # 3, 3

