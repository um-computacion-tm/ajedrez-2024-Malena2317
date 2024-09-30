import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez')
from piezas.pieza import Piece 

class Knight:
    def __init__(self, start_row, start_col,color):
        self.__row__ = start_row
        self.__col__ = start_col
        self.__color__ = color
    
    def get_row(self):
        return self.__row__

    def get_col(self):
        return self.__col__

    def set_row(self, row):
        self.__row__ = row

    def set_col(self, col):
        self.__col__ = col

    def get_color(self):
        return self.__color__

    def get_row(self):
        return self.__row__

    def get_col(self):
        return self.__col__

    def set_row(self, row):
        self.__row__ = row

    def set_col(self, col):
        self.__col__ = col

    def get_color(self):
        return self.__color__
    
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

