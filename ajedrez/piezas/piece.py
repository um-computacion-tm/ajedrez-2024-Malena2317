

class Piece:
    """
    A class representing a chess piece. This serves as a base class for all chess pieces,
    providing common properties and methods for movement and validation.

    Attributes:
        __row__ (int): The row position of the piece on the board.
        __col__ (int): The column position of the piece on the board.
        __color__ (str): The color of the piece, either "WHITE" or "BLACK".
        symbol (str): The symbol representing the piece, defined in subclasses.
    """
    
    def __init__(self, row, col, color):
        """
        Initializes a chess piece with its position and color.

        Args:
            row (int): The initial row of the piece.
            col (int): The initial column of the piece.
            color (str): The color of the piece, either "WHITE" or "BLACK".
        """
        self.__row__ = row
        self.__col__ = col
        self.__color__ = color
        self.symbol = self.get_symbol()  # Each subclass defines its own symbol.

    def get_symbol(self):
        """
        Retrieves the symbol of the chess piece.

        Must be implemented by subclasses to return the piece's specific symbol.

        Raises:
            NotImplementedError: If the method is not overridden in a subclass.
        """
        raise NotImplementedError("This method should be overridden in subclasses.")

    def get_coordinates(self):
        """
        Returns the current coordinates of the piece on the board.

        Returns:
            tuple: A tuple containing the row and column of the piece.
        """
        return (self.__row__, self.__col__)

    def update_coordinates(self, new_row, new_col):
        """
        Updates the piece's position to the new coordinates.

        Args:
            new_row (int): The new row position for the piece.
            new_col (int): The new column position for the piece.
        """
        self.__row__ = new_row
        self.__col__ = new_col

    def get_color(self):
        """
        Retrieves the color of the piece.

        Returns:
            str: The color of the piece, either "WHITE" or "BLACK".
        """
        return self.__color__

    def is_within_board(self, to_row, to_col):
        """
        Checks if the specified coordinates are within the boundaries of the chess board.

        Args:
            to_row (int): The row to check.
            to_col (int): The column to check.

        Returns:
            bool: True if the coordinates are within the board, False otherwise.
        """
        return 0 <= to_row < 8 and 0 <= to_col < 8

    def can_move_to(self, to_row, to_col, board):
        """
        Determines if the piece can move to the specified coordinates.

        Args:
            to_row (int): The target row for the move.
            to_col (int): The target column for the move.
            board (Board): The current state of the game board.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        # Check if the move is within the board boundaries
        if not self.is_within_board(to_row, to_col):
            print("You are out of the board!!")
            return False
        destination_piece = board.get_piece(to_row, to_col)
        # Allow the move if the destination square is empty or contains a piece of a different color
        if destination_piece is None or destination_piece.get_color() != self.get_color():
            return True
                
        print("The position is occupied by a piece of the same color.")
        return False

    def move(self, to_row, to_col, board):
        """
        Moves the piece to the specified coordinates if the move is valid.

        Args:
            to_row (int): The target row for the move.
            to_col (int): The target column for the move.
            board (Board): The current state of the game board.

        Returns:
            bool: True if the move was successful, False otherwise.
        """
        current_row, current_col = self.get_coordinates()
        if self.can_move_to(to_row, to_col, board):
            self.update_coordinates(to_row, to_col)
            board.set_piece(current_row, current_col, None)
            board.set_piece(to_row, to_col, self)
            return True
        return False

    def is_valid_move(self, to_row, to_col, board):
        """
        Validates whether a move to the specified coordinates is valid.

        This method must be implemented by subclasses.

        Args:
            to_row (int): The target row for the move.
            to_col (int): The target column for the move.
            board (Board): The current state of the game board.

        Raises:
            NotImplementedError: If the method is not overridden in a subclass.
        """
        raise NotImplementedError("This method must be implemented by subclasses")
