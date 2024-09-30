import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez')
from piezas.pieza import Piece 

class Knight(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.symbol = '♘' if color == "WHITE" else '♞'


    def is_valid_move(self, to_row, to_col, board):
        row_diff = abs(to_row - self.get_coordinates()[0])
        col_diff = abs(to_col - self.get_coordinates()[1])
        return ((row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)) and self.can_move_to(to_row, to_col, board)

    def move(self, to_row, to_col, board):
        if self.is_valid_move(to_row, to_col, board):
            return super().move(to_row, to_col, board)
        return False

