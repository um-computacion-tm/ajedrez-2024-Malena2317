import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez')
from piezas.piece import Piece


class Rook(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
    
    def get_symbol(self):
        # Return the symbol for the rook based on its color
        return '♖' if self.get_color() == "WHITE" else '♜'  

    def move(self, to_row, to_col, board):
         # Attempt to move the rook to the target position
        if self.is_valid_move(to_row, to_col, board):
            current_row, current_col = self.get_coordinates()
            # Clear the current position on the board
            board.set_piece(current_row, current_col, None) 
            # Update the rook's coordinates and place it on the new position
            self.update_coordinates(to_row, to_col)
            board.set_piece(to_row, to_col, self) 
            return True
        return False
        
        
    def is_valid_move(self, to_row, to_col, board):
        current_row, current_col = self.get_coordinates()
        
        # Check if the move is in a straight line
        if current_row == to_row or current_col == to_col:
            # Check if the path is clear
            if self._is_path_clear(current_row, current_col, to_row, to_col, board):
                # Check if the destination is empty or has a piece of a different color
                destination_piece = board.get_piece(to_row, to_col)
                return destination_piece is None or destination_piece.get_color() != self.get_color()
        
        return False

    def _is_path_clear(self, from_row, from_col, to_row, to_col, board): 
        # Determine the direction of movement
        step_row = 0 if from_row == to_row else (1 if to_row > from_row else -1)
        step_col = 0 if from_col == to_col else (1 if to_col > from_col else -1)

        # Iterate through intermediate positions
        row, col = from_row + step_row, from_col + step_col
        while row != to_row or col != to_col:
            if board[row][col] is not None:
                return False
            row += step_row
            col += step_col
        return True

