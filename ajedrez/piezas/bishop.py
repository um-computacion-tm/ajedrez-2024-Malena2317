import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.pieza import Piece 

      
class Alfil(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.symbol = "♗" if color == "WHITE" else "♝"

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
