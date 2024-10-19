import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez')
from piezas.piece import Piece

  
class Queen(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)

    def get_symbol(self):
        return '♕' if self.get_color() == "WHITE" else '♛'
    
    def is_valid_move(self, to_row, to_col, board):
        print(f"Verificando movimiento a ({to_row}, {to_col})")
        
        # Verifica que la posición esté dentro de los límites del tablero
        if not self.is_within_board(to_row, to_col):
            print(f"Movimiento a ({to_row}, {to_col}) es inválido: fuera del tablero.")
            return False
        
        # Verifica que no se intente mover a la misma posición
        if (to_row, to_col) == self.get_coordinates():
            print(f"Movimiento a ({to_row}, {to_col}) es inválido: misma posición.")
            return False

        # Check if the target position is occupied by a piece of the same color
        destination_piece = board.get_piece(to_row, to_col)
        if destination_piece is not None and destination_piece.get_color() == self.get_color():
            print(f"Movimiento a ({to_row}, {to_col}) es inválido: ocupada por la misma pieza.")
            return False

        # Calcular diferencias para determinar el tipo de movimiento
        row_diff = abs(to_row - self.get_coordinates()[0])
        col_diff = abs(to_col - self.get_coordinates()[1])

        # Una reina puede moverse diagonalmente, verticalmente o horizontalmente
        is_valid = (row_diff == col_diff or row_diff == 0 or col_diff == 0)
        print(f"Movimiento a ({to_row}, {to_col}) es {'válido' if is_valid else 'inválido'}.")

        return is_valid


    def check_obstacles(self, start_coords, to_row, to_col, board):
        start_row, start_col = start_coords
        row_diff = to_row - start_row
        col_diff = to_col - start_col

        step_row = (row_diff > 0) - (row_diff < 0)  # 1 si positivo, -1 si negativo
        step_col = (col_diff > 0) - (col_diff < 0)  # 1 si positivo, -1 si negativo

        current_row, current_col = start_row, start_col  # Comenzar en la posición inicial

        # Mover hasta la posición de destino, excluyendo la posición de destino
        while (current_row, current_col) != (to_row, to_col):
            current_row += step_row
            current_col += step_col
            
            if not self.is_within_board(current_row, current_col):
                print(f"Verificando obstáculos: ({current_row}, {current_col}) está fuera del tablero.")
                return True  # Fuera de los límites del tablero
            
            if board.get_piece(current_row, current_col) is not None:
                print(f"Verificando obstáculos: ({current_row}, {current_col}) está ocupado.")
                return True  # Hay un obstáculo
            
            # Depuración de las posiciones evaluadas
            print(f"Verificando posición: ({current_row}, {current_col}) está libre.")

        print("No se encontraron obstáculos.")
        return False  # No se encontraron obstáculos

    def move(self, to_row, to_col, board):
        print(f"Intentando mover a ({to_row}, {to_col})")
        if self.is_within_board(to_row, to_col) and self.is_valid_move(to_row, to_col, board):
            current_row, current_col = self.get_coordinates()
            print(f"Movimiento válido. Actualizando posición de ({current_row}, {current_col}) a ({to_row}, {to_col}).")
            board.set_piece(current_row, current_col, None) 
            self.update_coordinates(to_row, to_col)
            board.set_piece(to_row, to_col, self)
            return True
        print("Movimiento no permitido.")
        return False
