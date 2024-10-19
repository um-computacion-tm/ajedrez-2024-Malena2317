
# 77% chat 
class Piece:
    def __init__(self, row, col, color):
        # Stores the piece's coordinates and its color.
        self.__row__ = row
        self.__col__ = col
        self.__color__ = color
        self.symbol = self.get_symbol() # Each subclass defines its own symbol.

    def get_symbol(self):
        # Must be implemented by subclasses to return the piece's symbol.
        raise NotImplementedError("This method should be overridden in subclasses.")

    def get_coordinates(self):
        # Returns the current coordinates of the piece.
        return (self.__row__, self.__col__)

    def update_coordinates(self, new_row, new_col):
        # Updates the piece's coordinates.
        self.__row__ = new_row
        self.__col__ = new_col


    def get_color(self):
        # Returns the color of the piece (WHITE or BLACK).
        return self.__color__

    def is_within_board(self, to_row, to_col):
        # Checks if a position is within the board's boundaries.
        return 0 <= to_row < 8 and 0 <= to_col < 8

    def can_move_to(self, to_row, to_col, board):
        # Checks if the piece can move to the given position.
        # Allows movement if the destination square is empty or contains a piece of a different color.
        if not self.is_within_board(to_row, to_col):
            print("Movement out of the board.")
            return False
        destination_piece = board.get_piece(to_row, to_col)
        if destination_piece is None or destination_piece.get_color() != self.get_color():
            return True

                
        print("The position is occupied by a piece of the same color.")
        return False

    def move(self, to_row, to_col, board):
        # Attempts to move the piece to the given position if possible.
        if self.can_move_to(to_row, to_col, board):
            current_row, current_col = self.get_coordinates()
            # Removes the piece from its current position on the board.
            board.set_piece(current_row, current_col, None)
            # Updates the piece's coordinates.
            self.update_coordinates(to_row, to_col)
            # Places the piece in the new position.
            board.set_piece(to_row, to_col, self)
            return True
        return False

    def is_valid_move(self, to_row, to_col, board):
        # This method must be implemented by each subclass to check the validity of the move.
        raise NotImplementedError("Este método debe ser implementado por las subclases") 