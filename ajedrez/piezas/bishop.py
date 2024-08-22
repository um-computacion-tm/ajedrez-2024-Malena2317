from piezas.piezas import Piece

class Alfil:
    def __init__(self, row, col, color):
        self.__row__ = row
        self.__col__ = col
        self.__color__ = color

    def mover(self, to_row, to_col, tablero):
        if abs(self.__row__ - to_row) == abs(self.__col__ - to_col):
            if tablero[to_row][to_col] is None:
                self.__row__ = to_row
                self.__col__ = to_col
                return True
        return False  
    
    def get_row(self):
        return self.__row__
    
    def get_col(self):
        return self.__col__
    
tablero = [[None for _ in range(8)] for _ in range(8)]
alfil = Alfil(1, 1, "blanco")
print(alfil.mover(3, 3, tablero))  # True
print(alfil.get_row(), alfil.get_col())  # 3, 3

