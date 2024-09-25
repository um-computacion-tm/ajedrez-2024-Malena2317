import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez') 
from piezas.pieza import Piece 





class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col


class Pawn(Piece):

    def __init__(self, color):
        self.__color__ = color
        self.simbolo = "P" if color == "WHITE" else "p"
    
    def move(self, start_pos, to_pos, board):  # Este método debe ser parte de la clase Pawn
        movimiento_valido = True

        # Verificar si se mueve en la misma fila
        if start_pos.row == to_pos.row:
            print("No puedes mover el peón a la misma fila")
            movimiento_valido = False

        # Verificar si se mueve en la columna
        if start_pos.col != to_pos.col:
            print("El peón solo se puede mover en columnas")
            movimiento_valido = False

        # Verificar si el peón blanco va para adelante
        if self.__color__ == "WHITE":
            if to_pos.row <  start_pos.row:
                print("El peón blanco solo se puede mover hacia adelante")
                movimiento_valido = False

        # Verificar si el peón negro va para adelante
        if self.__color__ == "BLACK":
            if to_pos.row > start_pos.row:
                print("El peón negro solo se puede mover hacia adelante")
                movimiento_valido = False

        # Si todas las verificaciones pasan, mueve el peón
        if movimiento_valido:
            board[to_pos.row][to_pos.col] = self
            board[start_pos.row][start_pos.col] = None
            return True
        
        return False  # Si no es válido, devuelve False
    
        board[to_pos.row][to_pos.col] = self
        board[start_pos.row][start_pos.col] = None
        return True