import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.piece import Piece 


class Bishop(Piece):
    def __init__(self, row, col, color):
        # Initializes the bishop at its starting position.
        super().__init__(row, col, color)

    def get_symbol(self):
        # Returns the bishop's symbol based on its color.
        return "♗" if self.get_color() == "WHITE" else "♝"
    
    def move(self, to_row, to_col, board):
        if self.is_valid_move(to_row, to_col, board):
            current_row, current_col = self.get_coordinates()
            # Remueve la pieza de su posición actual en el tablero.
            board.set_piece(current_row, current_col, None)
            # Actualiza las coordenadas de la pieza.
            self.update_coordinates(to_row, to_col)
            # Coloca la pieza en la nueva posición.
            board.set_piece(to_row, to_col, self)
            return True
        return False
    
    def is_valid_move(self, to_row, to_col, board):
        row_diff = abs(to_row - self.get_coordinates()[0])
        col_diff = abs(to_col - self.get_coordinates()[1])
        return row_diff == col_diff and self.can_move_to(to_row, to_col, board)

    def _is_path_clear(self, to_row, to_col, board):
        # Checks if the diagonal to the destination position is free of obstacles.
        current_row, current_col = self.get_coordinates()
        step_row = 1 if to_row > current_row else -1
        step_col = 1 if to_col > current_col else -1

        while (current_row, current_col) != (to_row - step_row, to_col - step_col):
            current_row += step_row
            current_col += step_col
            if board.get_piece(current_row, current_col) is not None:
                return False
        return True

  

