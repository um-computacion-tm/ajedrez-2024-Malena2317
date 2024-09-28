import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))




class Alfil:
    def __init__(self, row, col, color, board=None):
        self.__row__ = row
        self.__col__ = col
        self.__color__ = color
        self.board = board if board is not None else [[None for _ in range(8)] for _ in range(8)]
        self.symbol = "♗" if color == "WHITE" else "♝"
         
    def is_valid_diagonal_move(self, from_row, from_col, to_row, to_col, board):
        # verifica que el movimeinto sea en diagonal 
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)
        if row_diff != col_diff:
            return False

        # verifica si la casilla de destino est vacia 
        if board[to_row][to_col] is not None:
            return False

        return True

    def mover(self, to_row, to_col, board):
        if not self.is_valid_diagonal_move(self.__row__, self.__col__, to_row, to_col, board):
            return False
        else:
            # actualiza la posicion de la pieza
            self.__row__ = to_row
            self.__col__ = to_col
            board[to_row][to_col] = self
            board[self.__row__][self.__col__] = None
            return True
    
    def _mover_alfil(self, to_row, to_col, expected_result, expected_position):
        resultado = self.alfil.mover(to_row, to_col, self.tablero)
        self.assertEqual(resultado, expected_result)
        self.assertEqual((self.alfil.get_row(), self.alfil.get_col()), expected_position)
        
    def get_row(self):
        return self.__row__
    
    def get_col(self):
        return self.__col__
    
tablero = [[None for _ in range(8)] for _ in range(8)]
alfil = Alfil(1, 1, "blanco")
print(alfil.mover(3, 3, tablero))  # True
print(alfil.get_row(), alfil.get_col())  # 3, 3

