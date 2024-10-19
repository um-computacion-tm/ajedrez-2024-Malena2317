import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez')
from piezas.piece import Piece 

class Knight(Piece):
     # Initializes the knight at its starting position.
    def __init__(self, row, col, color):
        super().__init__(row, col, color) 

    def get_symbol(self):
        # Returns the knight's symbol based on its color.
        return '♘' if self.get_color() == "WHITE" else '♞' 

    def is_valid_move(self, to_row, to_col, board):
        # The knight moves in an L-shape: two squares in one direction and one square perpendicular.
        row_diff = abs(to_row - self.get_coordinates()[0])
        col_diff = abs(to_col - self.get_coordinates()[1])
        return ((row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)) and self.can_move_to(to_row, to_col, board)



