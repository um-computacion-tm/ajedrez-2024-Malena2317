import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez')
from piezas.pieza import Piece

class King(Piece):
    """
    Represents a King piece in a chess game.
    Inherits from the Piece class.
    """

    def __init__(self, row, col, color):
        """
        Initializes a King piece with its position and color.

        Args:
            row (int): The row position of the King on the board.
            col (int): The column position of the King on the board.
            color (str): The color of the King, either "WHITE" or "BLACK".
        """
        super().__init__(row, col, color)

    def get_symbol(self):
        """
        Returns the symbol for the King based on its color.

        Returns:
            str: The symbol representing the King ("♔" for white, "♚" for black).
        """
        return "♔" if self.get_color() == "WHITE" else "♚"

    def is_valid_move(self, to_row, to_col, board):
        """
        Checks if the move to the specified position is valid for the King.

        A King can move to any adjacent square (one square in any direction).

        Args:
            to_row (int): The target row position to move to.
            to_col (int): The target column position to move to.
            board (Board): The current game board to check for valid moves.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        start_row, start_col = self.get_coordinates()
        # Check that the move is to an adjacent square
        if abs(to_row - start_row) <= 1 and abs(to_col - start_col) <= 1:
            # Check if the destination square has a piece of the same color
            return self.can_move_to(to_row, to_col, board)
        print("Invalid move for the King.")
        return False

    def move(self, to_row, to_col, board):
        """
        Moves the King to the specified position if the move is valid.

        Args:
            to_row (int): The target row position to move to.
            to_col (int): The target column position to move to.
            board (Board): The current game board to place the King.

        Returns:
            bool: True if the move was successful, False if the move was invalid.
        """
        if self.is_valid_move(to_row, to_col, board):
            # If the move is valid, update the King's position
            self.update_coordinates(to_row, to_col)
            board.place_piece(self, (to_row, to_col))
            return True
        else:
            # If the move is invalid, return False
            return False
            
      
