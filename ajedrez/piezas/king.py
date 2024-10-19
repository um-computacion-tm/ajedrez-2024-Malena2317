import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez')
from piezas.piece import Piece

class King(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        
    def get_symbol(self):
        # Return the symbol for the king based on its color
        return "♔" if self.get_color() == "WHITE" else "♚"

    def is_valid_move(self, to_row, to_col, board):
        # Get the current coordinates of the king
        start_row, start_col = self.get_coordinates()
     
        # Check if the target position is within one square of the current position
        if abs(to_row - start_row) <= 1 and abs(to_col - start_col) <= 1:
            # Check if the target position is not occupied by a piece of the same color
            return self.can_move_to(to_row, to_col, board)
        return False

    def move(self, to_row, to_col, board):
        # Check if the target position is valid for movement
        if self.is_valid_move(to_row, to_col, board):
            # Update the king's coordinates and place it on the new position
            self.update_coordinates(to_row, to_col)
            board[to_row][to_col] = self
            return True
        else:
            return False
      
        
    