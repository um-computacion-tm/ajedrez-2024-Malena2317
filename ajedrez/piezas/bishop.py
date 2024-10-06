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

   

