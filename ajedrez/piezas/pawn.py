import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez') 
from piezas.pieza import Piece 


class Pawn(Piece):

    def __init__(self, color):
        super().__init__(0, 0, color)  # Inicializa la posición en (0, 0)
        self.simbolo = '♙' if color == "WHITE" else '♟'
    
        
    def is_valid_move(self, to_row, to_col, board):
        start_row, start_col = self.get_coordinates()
        is_valid = True

        if start_col != to_col:
                print("El peón solo se puede mover en la misma columna.")
                is_valid = False
        row_diff = to_row - start_row

        if (self.get_color() == "WHITE" and row_diff <= 0) or (self.get_color() == "BLACK" and row_diff >= 0):
            print("El peón solo puede avanzar hacia adelante.")
            is_valid = False
        elif abs(row_diff) > 1:
            print("El peón solo puede avanzar una casilla.")
            is_valid = False
            
        if is_valid:
            is_valid = self.can_move_to(to_row, to_col, board)

        return is_valid

        if self.get_color() == "BLACK":
            if to_row >= start_row:
                print("El peón negro solo puede avanzar hacia adelante.")
                return False
            elif start_row - to_row > 1:
                print("El peón negro solo puede avanzar una casilla.")
                return False

        return self.can_move_to(to_row, to_col, board)


