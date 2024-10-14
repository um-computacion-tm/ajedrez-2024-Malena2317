import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez') 
from piezas.pieza import Piece 


class Pawn(Piece):

    def __init__(self, color):
        super().__init__(0, 0, color)  # Inicializa la posición en (0, 0)
        self.simbolo = '♙' if color == "WHITE" else '♟'
        self.has_moved = False
    
    def move(self, to_row, to_col, board):
        if self.is_valid_move(to_row, to_col, board):
            return super().move(to_row, to_col, board)
        return False
        
    def is_valid_move(self, to_row, to_col, board):
        start_row, start_col = self.get_coordinates()
        print(f"Coordenadas actuales: ({start_row}, {start_col})")
        print(f"Intentando mover a: ({to_row}, {to_col})")
    
    
        # El peón solo se mueve en la misma columna
        if start_col != to_col:
                print("El peón solo se puede mover en la misma columna.")
                return False
         
        # Diferencia de filas
        row_diff = to_row - start_row if self.get_color() == "WHITE" else start_row - to_row
       
        # Verificar si el movimiento es válido
        if self.get_color() == "WHITE":
            if row_diff < 0 or row_diff > 2 or (row_diff == 2 and (self.has_moved or start_row != 1)):
                print("El peón blanco solo puede avanzar hacia adelante.")
                return False
        else:
            if row_diff > 0 or (row_diff < -2 and self.has_moved) or (row_diff == -2 and (self.has_moved or start_row != 6)) or (row_diff != -1 and self.has_moved):
                print("El peón negro solo puede avanzar hacia adelante.")
                return False

        # Verificar si puede moverse a la posición
        return self.can_move_to(to_row, to_col, board)