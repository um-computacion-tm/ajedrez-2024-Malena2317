import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez')
from piezas.pieza import Piece

class Queen(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.symbol = "♕" if color == "WHITE" else "♛"
        

    def is_valid_move(self, to_row, to_col, board):
        current_row, current_col = self.get_coordinates()
        row_diff = abs(to_row - current_row)
        col_diff = abs(to_col - current_col)
        if row_diff == col_diff or current_row == to_row or current_col == to_col:
            return True
        return False

    def move(self, to_row, to_col, board):  
        if self.is_valid_move(to_row, to_col, board):
            return super().move(to_row, to_col, board)
        return False
