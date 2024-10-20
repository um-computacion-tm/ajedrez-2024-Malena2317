import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.piece import Piece


      
class Bishop(Piece):
    """Class representing a bishop in the chess game."""

    def __init__(self, row, col, color):
        """Initializes the bishop with its position and color.

        Args:
            row (int): The row where the bishop is located.
            col (int): The column where the bishop is located.
            color (str): The color of the bishop ('WHITE' or 'BLACK').
        """
        super().__init__(row, col, color)

    def get_symbol(self):
        """Returns the bishop's symbol based on its color.

        Returns:
            str: The symbol of the bishop.
        """
        return "♗" if self.get_color() == "WHITE" else "♝"
    
    def move(self, to_row, to_col, board):
        """Attempts to move the bishop to a new position.

        Args:
            to_row (int): The target row.
            to_col (int): The target column.
            board (Board): The board on which the bishop is located.

        Returns:
            bool: True if the move was successful, False otherwise.
        """
        if self.is_valid_move(to_row, to_col, board):
            current_row, current_col = self.get_coordinates()
            board.get_piece(current_row, current_col)
            self.update_coordinates(to_row, to_col)
            board.set_piece(to_row, to_col, self)
            return True
        return False

    def is_valid_move(self, to_row, to_col, board):
        """Checks if the bishop's move is valid.

        Args:
            to_row (int): The target row.
            to_col (int): The target column.
            board (Board): The board on which the bishop is located.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        row_diff = abs(to_row - self.get_coordinates()[0])
        col_diff = abs(to_col - self.get_coordinates()[1])
        return row_diff == col_diff and self.can_move_to(to_row, to_col, board)

    def _is_path_clear(self, to_row, to_col, board):
        """Checks if the path to the destination position is free of obstacles.

        Args:
            to_row (int): The target row.
            to_col (int): The target column.
            board (Board): The board on which the bishop is located.

        Returns:
            bool: True if the path is clear, False otherwise.
        """
        current_row, current_col = self.get_coordinates()
        step_row = 1 if to_row > current_row else -1
        step_col = 1 if to_col > current_col else -1
          
        while (current_row, current_col) != (to_row - step_row, to_col - step_col):
            current_row += step_row
            current_col += step_col
            if board.get_piece(current_row, current_col) is not None:
                return False
        return True