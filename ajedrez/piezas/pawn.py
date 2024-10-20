import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez') 
from piezas.piece import Piece 


class Pawn(Piece):
    """
    A class representing a pawn piece in a chess game. The pawn can move forward and capture diagonally.

    Attributes:
        has_moved (bool): Indicates whether the pawn has moved from its initial position.
    """

    def __init__(self, row, col, color):
        """
        Initializes a pawn with its position and color.

        Args:
            row (int): The initial row of the pawn.
            col (int): The initial column of the pawn.
            color (str): The color of the pawn, either "WHITE" or "BLACK".
        """
        super().__init__(row, col, color)  # Initializes the position
        self.has_moved = False

    def get_symbol(self):
        """
        Retrieves the symbol of the pawn based on its color.

        Returns:
            str: The symbol representing the pawn, '♙' for white and '♟' for black.
        """
        # Returns the pawn's symbol based on its color.
        return '♙' if self.get_color() == "WHITE" else '♟'

    def move(self, to_row, to_col, board):
        """
        Moves the pawn to the specified coordinates if the move is valid.

        Args:
            to_row (int): The target row for the move.
            to_col (int): The target column for the move.
            board (Board): The current state of the game board.

        Returns:
            bool: True if the move was successful, False otherwise.
        """
        if self.is_valid_move(to_row, to_col, board):
            result = super().move(to_row, to_col, board)
            if result:
                self.has_moved = True
                self.update_coordinates(to_row, to_col)
            return result
        return False

    def is_valid_move(self, to_row, to_col, board):
        """
        Validates whether a move to the specified coordinates is valid for the pawn.

        Args:
            to_row (int): The target row for the move.
            to_col (int): The target column for the move.
            board (Board): The current state of the game board.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        current_row, current_col = self.get_coordinates()
        direction = -1 if self.get_color() == "WHITE" else 1
        print(f"Trying to move from ({current_row}, {current_col}) to ({to_row}, {to_col})")
    
        # Forward move
        if self.is_forward_move((current_row, current_col), (to_row, to_col), direction, board):
            print("Forward move is valid")
            return True
    
        # Diagonal capture move
        if self.is_capture_move((current_row, current_col), (to_row, to_col), direction, board):
            print("Capture move is valid")
            return True
    
        print("Move is not valid")
        return False

    def is_forward_move(self, from_pos, to_pos, direction, board):
        """
        Checks if the move is a valid forward move for the pawn.

        Args:
            from_pos (tuple): The current position of the pawn (row, column).
            to_pos (tuple): The target position for the move (row, column).
            direction (int): The direction in which the pawn moves (-1 for white, 1 for black).
            board (Board): The current state of the game board.

        Returns:
            bool: True if the forward move is valid, False otherwise.
        """
        current_row, current_col = from_pos
        to_row, to_col = to_pos
    
        print(f"Current Position: ({current_row}, {current_col}), Target Position: ({to_row}, {to_col}), Direction: {direction}")
    
        # One square forward move
        if current_col == to_col:
            if to_row == current_row + direction and board.get_piece(to_row, to_col) is None:
                return True
    
            # Two squares forward move from the initial position
            if not self.has_moved and to_row == current_row + 2 * direction:
                if board.get_piece(to_row, to_col) is None and board.get_piece(current_row + direction, to_col) is None:
                    return True
    
        return False

    def is_capture_move(self, from_pos, to_pos, direction, board):
        """
        Checks if the move is a valid capture move for the pawn.

        Args:
            from_pos (tuple): The current position of the pawn (row, column).
            to_pos (tuple): The target position for the move (row, column).
            direction (int): The direction in which the pawn moves (-1 for white, 1 for black).
            board (Board): The current state of the game board.

        Returns:
            bool: True if the capture move is valid, False otherwise.
        """
        current_row, current_col = from_pos
        to_row, to_col = to_pos
                
        # Diagonal capture
        if abs(current_col - to_col) == 1 and to_row == current_row + direction:
            piece_at_destination = board.get_piece(to_row, to_col)
            if piece_at_destination and piece_at_destination.get_color() != self.get_color():
                return True
                
        return False


