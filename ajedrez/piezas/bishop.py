import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.pieza import Piece 

      
class Alfil(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.symbol = "♗" if color == "WHITE" else "♝"

    def is_valid_move(self, to_row, to_col, board):
        if to_row < 0 or to_row >= len(board) or to_col < 0 or to_col >= len(board[0]):
            return False
        row_diff = abs(to_row - self.get_coordinates()[0])
        col_diff = abs(to_col - self.get_coordinates()[1])
        if board[to_row][to_col] is not None:
            if board[to_row][to_col].get_color() == self.get_color():
                return False
        return row_diff == col_diff

