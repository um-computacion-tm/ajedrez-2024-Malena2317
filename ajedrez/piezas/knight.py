import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez')
from piezas.piece import Piece 



class Knight(Piece):
    """
    Represents a Knight piece in a chess game.
    Inherits from the Piece class.
    """

    def __init__(self, row, col, color):
        """
        Initializes a Knight piece with its position and color.

        Args:
            row (int): The row position of the Knight on the board.
            col (int): The column position of the Knight on the board.
            color (str): The color of the Knight, either "WHITE" or "BLACK".
        """
        super().__init__(row, col, color)

    def get_symbol(self):
        """
        Returns the symbol for the Knight based on its color.

        Returns:
            str: The symbol representing the Knight ("♘" for white, "♞" for black).
        """
        return '♘' if self.get_color() == "WHITE" else '♞' 

    def is_valid_move(self, to_row, to_col, board):
        """
        Checks if the move to the specified position is valid for the Knight.

        A Knight moves in an L-shape: two squares in one direction and one square perpendicular.

        Args:
            to_row (int): The target row position to move to.
            to_col (int): The target column position to move to.
            board (Board): The current game board to check for valid moves.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        row_diff = abs(to_row - self.get_coordinates()[0])
        col_diff = abs(to_col - self.get_coordinates()[1])
        return ((row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)) and self.can_move_to(to_row, to_col, board)


