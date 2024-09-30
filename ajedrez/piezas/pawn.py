import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez') 
from piezas.pieza import Piece 


class Pawn(Piece):

    def __init__(self, color):
        self.__color__ = color
        self.simbolo = '♙' if color == "WHITE" else '♟'
    
    def move(self, to_row, to_col, board):
        if self.is_valid_move(to_row, to_col, board):
            return super().move(to_row, to_col, board)
        return False
        
    def is_valid_move(self, to_row, to_col, board):
        start_row, start_col = self.get_coordinates()
        if start_col != to_col:
            print("El peón solo se puede mover en la misma columna.")
            return False

        if self.get_color() == "WHITE":
            if to_row <= start_row:
                print("El peón blanco solo puede avanzar hacia adelante.")
                return False
            elif to_row - start_row > 1:
                print("El peón blanco solo puede avanzar una casilla.")
                return False

        if self.get_color() == "BLACK":
            if to_row >= start_row:
                print("El peón negro solo puede avanzar hacia adelante.")
                return False
            elif start_row - to_row > 1:
                print("El peón negro solo puede avanzar una casilla.")
                return False

        return self.can_move_to(to_row, to_col, board)