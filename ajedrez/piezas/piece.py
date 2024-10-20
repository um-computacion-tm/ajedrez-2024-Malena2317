
class Piece:
    """
    Represents a generic chess piece.
    This class serves as a base class for all specific piece types (e.g., King, Knight).
    """

    def __init__(self, row, col, color):
        """
        Initializes a chess piece with its position and color.

        Args:
            row (int): The row position of the piece on the board.
            col (int): The column position of the piece on the board.
            color (str): The color of the piece, either "WHITE" or "BLACK".
        """
        self.__row__ = row
        self.__col__ = col
        self.__color__ = color
        self.symbol = self.get_symbol()  # Each subclass defines its own symbol.

    def get_symbol(self):
        """
        Must be implemented by subclasses to return the piece's symbol.

        Raises:
            NotImplementedError: This method should be overridden in subclasses.
        """
        raise NotImplementedError("This method should be overridden in subclasses.")

    def get_coordinates(self):
        """
        Returns the current coordinates of the piece.

        Returns:
            tuple: A tuple containing the row and column of the piece (row, col).
        """
        return (self.__row__, self.__col__)

    def update_coordinates(self, new_row, new_col):
        """
        Updates the position of the piece to the new coordinates.

        Args:
            new_row (int): The new row position of the piece.
            new_col (int): The new column position of the piece.
        """
        self.__row__ = new_row
        self.__col__ = new_col

    def get_color(self):
        """
        Returns the color of the piece.

        Returns:
            str: The color of the piece ("WHITE" or "BLACK").
        """
        return self.__color__

    def is_within_board(self, to_row, to_col):
        """
        Checks if the specified coordinates are within the bounds of the chessboard.

        Args:
            to_row (int): The row position to check.
            to_col (int): The column position to check.

        Returns:
            bool: True if the coordinates are within the board, False otherwise.
        """
        return 0 <= to_row < 8 and 0 <= to_col < 8

    def can_move_to(self, to_row, to_col, board):
        """
        Checks if the piece can move to the specified position.

        Args:
            to_row (int): The target row position to move to.
            to_col (int): The target column position to move to.
            board (Board): The current game board to check for valid moves.

        Returns:
            bool: True if the piece can move to the specified position, False otherwise.
        """
        if not self.is_within_board(to_row, to_col):
            print("You are out of the board!!")
            return False
        destination_piece = board.get_piece(to_row, to_col)
        # Allows the move if the destination square is empty or contains a piece of a different color
        if destination_piece is None or destination_piece.get_color() != self.get_color():
            return True
                
        print("The position is occupied by a piece of the same color.")
        return False

    def move(self, to_row, to_col, board):
        """
        Moves the piece to the specified position if the move is valid.

        Args:
            to_row (int): The target row position to move to.
            to_col (int): The target column position to move to.
            board (Board): The current game board to place the piece.

        Returns:
            bool: True if the move was successful, False if the move was invalid.
        """
        if self.can_move_to(to_row, to_col, board):
            current_row, current_col = self.get_coordinates()
            self.update_coordinates(to_row, to_col)
            board.set_piece(current_row, current_col, None)
            board.set_piece(to_row, to_col, self)
            return True
        return False

    def is_valid_move(self, to_row, to_col, board):
        """
        Checks if the move to the specified position is valid for the piece.

        This method must be implemented by subclasses.

        Args:
            to_row (int): The target row position to move to.
            to_col (int): The target column position to move to.
            board (Board): The current game board to check for valid moves.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        raise NotImplementedError("This method must be implemented by subclasses")