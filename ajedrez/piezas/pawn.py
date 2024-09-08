import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez') 
from piezas.pieza import Piece 


class Pawn(Piece):
    def __init__(self, color):
        self.__color__ = color
        if color == "WHITE":
            self.simbolo = "P"
        else:
            self.simbolo = "p"
  
class Position:
    def __init__(self, row, col):
        self.__row__ = row
        self.__col__ = col
        
    def mover(self, start_pos, to_pos, board):
        # Verifica si el peón se está moviendo en la misma fila
        if start_pos.row == to_pos.row:
            print("No puedes mover el peón a la misma fila")
            return False
        
        # Verifica que el peón solo se mueva en la columna correcta
        if start_pos.col != to_pos.col:
            print("El peón solo se puede mover en columnas")
            return False

        # Verifica que el peón blanco solo se mueva hacia adelante
        if self.__color__ == "WHITE" and to_pos.row > start_pos.row:
            print("El peón blanco solo se puede mover hacia adelante")
            return False

        # Verifica que el peón negro solo se mueva hacia adelante
        if self.__color__ == "BLACK" and to_pos.row < start_pos.row:
            print("El peón negro solo se puede mover hacia adelante")
            return False

        # Si todas las verificaciones pasan, mueve el peón
        board[to_pos.row][to_pos.col] = self
        board[start_pos.row][start_pos.col] = None
        return True



