import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez')
from piezas.piece import Piece

class King(Piece):
    """
    Represents a king chess piece.

    A king can move one square in any direction.
    """

    def __init__(self, row, col, color):
        """
        Initializes a king piece.

        Args:
            row (int): The initial row position of the king on the board.
            col (int): The initial column position of the king on the board.
            color (str): The color of the king, either 'WHITE' or 'BLACK'.
        """
        super().__init__(row, col, color)

    def get_symbol(self):
        """
        Returns the symbol representing the king.

        Returns:
            str: The symbol for the king, '♔' for white and '♚' for black.
        """
        # Return the symbol for the king based on its color
        return "♔" if self.get_color() == "WHITE" else "♚"

    def is_valid_move(self, to_row, to_col, board):
        """
        Checks if a move to a specified position is valid for the king.

        Args:
            to_row (int): The target row position to check.
            to_col (int): The target column position to check.
            board (Board): The board on which the move is being validated.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        start_row, start_col = self.get_coordinates()
        # Check that the movement is to an adjacent square
        if abs(to_row - start_row) <= 1 and abs(to_col - start_col) <= 1:
            # Check if the destination square has a piece of the same color
            return self.can_move_to(to_row, to_col, board)
        print("Movimiento inválido para el Rey.")
        return False

    def move(self, to_row, to_col, board):
        """
        Moves the king to a specified position on the board.

        Args:
            to_row (int): The target row position to move to.
            to_col (int): The target column position to move to.
            board (Board): The board on which the king is moving.

        Returns:
            bool: True if the move was successful, False otherwise.
        """
        if self.is_valid_move(to_row, to_col, board):
            # If the move is valid, update the king's position
            self.update_coordinates(to_row, to_col)
            board.set_piece(to_row, to_col, self)
            return True
        else:
            # If the move is not valid, return False
            return False

      