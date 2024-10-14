import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez') 
from piezas.pieza import Piece 


class Pawn(Piece):

    def __init__(self, color):
        super().__init__(0, 0, color)  # Inicializa la posición en (0, 0)
        self.simbolo = '♙' if color == "WHITE" else '♟'
        self.has_moved = False
    
        
    def is_valid_move(self, to_row, to_col, board):
        start_row, start_col = self.get_coordinates()
        print(f"Coordenadas actuales: ({start_row}, {start_col})")
        print(f"Intentando mover a: ({to_row}, {to_col})")
        is_valid = True
        

        # El peón solo se mueve en la misma columna
        if start_col != to_col:
                print("El peón solo se puede mover en la misma columna.")
                is_valid = False
        if self.get_color() == "WHITE":
            row_diff = to_row - start_row  # Diferencia de filas para peones blancos
        else:
            row_diff = start_row - to_row  # Diferencia de filas para peones negros


        # Peón blanco avanza hacia adelante (filas crecientes y Peón negro avanza hacia atrás (filas decrecientes)
        if self.get_color() == "WHITE":
            if row_diff < 0 or row_diff > 2:
                print("El peón solo puede avanzar hacia adelante.")
                is_valid = False

            elif row_diff == 2 and (self.has_moved or start_row != 1):
                print("El peón blanco solo puede avanzar dos casillas en su primer movimiento.")
                is_valid = False

        elif self.get_color() == "BLACK":
            if row_diff > 0 or (row_diff < -2 and self.has_moved) or (row_diff == -2 and (self.has_moved or start_row != 6)):
                print("El peón solo puede avanzar hacia adelante.")
                is_valid = False

            elif row_diff == -2 and (self.has_moved or start_row != 6):
                print("El peón negro solo puede avanzar dos casillas en su primer movimiento.")
                is_valid = False

            elif row_diff != -1 and self.has_moved:
                print("El peón negro solo puede avanzar una casilla en movimientos subsiguientes.")
                is_valid = False

        #Verificar si puede moverse a la posición
        if is_valid:
            is_valid = self.can_move_to(to_row, to_col, board)

        return is_valid

