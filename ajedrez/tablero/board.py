import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.rook import Rook
from piezas.rey import King
from piezas.reina import Queen
from piezas.pawn import Pawn 
from piezas.caballo import Knight
from piezas.bishop import Alfil 
from piezas.pieza import Piece 


class Board:
    def __init__(self):
        """Initializes the chessboard and places the pieces in their starting positions."""
        self.squares = self.initialize_board()

    def initialize_board(self):
        """Initializes the board with pieces in their initial positions.

        Returns:
            list: A 2D list representing the chessboard with pieces placed in their starting positions.
        """
        squares = []
        for i in range(8):
            row = []
            for j in range(8):
                row.append(None)
            squares.append(row)

        # Place the pieces in their initial positions
        squares[0][0] = Rook(0, 0, "BLACK")
        squares[0][7] = Rook(0, 7, "BLACK")
        squares[7][0] = Rook(7, 0, "WHITE")
        squares[7][7] = Rook(7, 7, "WHITE")

        # Place pawns in their initial positions
        for i in range(8):
            squares[6][i] = Pawn(6, i, "WHITE")  # Place white pawns in row 6
            squares[1][i] = Pawn(1, i, "BLACK")  # Place black pawns in row 1

        # Place the remaining pieces in their initial positions
        squares[0][1] = Knight(0, 1, "BLACK")
        squares[0][6] = Knight(0, 6, "BLACK")
        squares[7][1] = Knight(7, 1, "WHITE")
        squares[7][6] = Knight(7, 6, "WHITE")

        squares[0][2] = Bishop(0, 2, "BLACK")
        squares[0][5] = Bishop(0, 5, "BLACK")
        squares[7][2] = Bishop(7, 2, "WHITE")
        squares[7][5] = Bishop(7, 5, "WHITE")

        squares[0][3] = Queen(0, 3, "BLACK")
        squares[7][3] = Queen(7, 3, "WHITE")

        squares[0][4] = King(0, 4, "BLACK")
        squares[7][4] = King(7, 4, "WHITE")

        return squares

    def print_board(self):
        """Prints the current state of the board in a human-readable format."""
        print("    A    B    C    D    E    F    G    H")
        print("  +---------------------------------------+")
        for i in range(8):
            print(f"{8 - i} |", end=" ")
            for j in range(8):
                piece = self.squares[i][j]
                if piece:
                    print(f"{piece.symbol:<4}", end=" ")
                else:
                    print(".   ", end=" ")
            print("|")
        print("  +---------------------------------------+")
        print("    A    B    C    D    E    F    G    H")

    def get_piece(self, row, col):
        """Returns the piece at the specified position.

        Args:
            row (int): The row index of the piece.
            col (int): The column index of the piece.

        Returns:
            Piece or None: The piece at the specified position, or None if there is no piece.
        """
        if self.is_within_board(row, col):
            return self.squares[row][col]
        return None

    def set_piece(self, row, col, piece):
        """Sets a piece at the given position if it's within the board.

        Args:
            row (int): The row index to set the piece.
            col (int): The column index to set the piece.
            piece (Piece): The piece to place on the board.
        """
        if self.is_within_board(row, col):
            self.squares[row][col] = piece

    def get_piece_position(self, piece):
        """Returns the position of the given piece on the board.

        Args:
            piece (Piece): The piece to find.

        Returns:
            tuple or None: A tuple containing the row and column of the piece, or None if the piece is not found.
        """
        for row in range(8):
            for col in range(8):
                if self.squares[row][col] == piece:
                    return row, col
        return None

    def is_within_board(self, row, col):
        """Checks if the given coordinates are within the bounds of the board.

        Args:
            row (int): The row index to check.
            col (int): The column index to check.

        Returns:
            bool: True if the coordinates are within the board, False otherwise.
        """
        return 0 <= row < 8 and 0 <= col < 8
    
    def place_piece(self, piece, position):
        """Places a piece on the board at the specified position.

        Args:
            piece (Piece): The piece to place on the board.
            position (tuple): The (row, col) position to place the piece.

        Raises:
            ValueError: If the position is outside the bounds of the board.
        """
        row, col = position
        if self.is_within_board(row, col):
            self.squares[row][col] = piece  # Changed from self.board to self.squares
        else:
            raise ValueError("Position out of bounds of the board")

    def move_piece(self, origin, destination):
        """Moves a piece from the origin position to the destination position.

        Args:
            origin (tuple): The (row, col) position of the piece to move.
            destination (tuple): The (row, col) position to move the piece to.

        Returns:
            bool: True if the move was successful, False otherwise.
        """
        origin_row, origin_col = origin  # Decomposes the origin tuple
        dest_row, dest_col = destination 
        piece = self.get_piece(origin_row, origin_col)
    
        # Check if there is a piece at the origin position
        if piece is None:
            print("No piece at origin square")
            return False
        # Check if the move is valid
        if not piece.is_valid_move(dest_row, dest_col, self):
            print("Invalid move for this piece")
            return False
        # Perform the move
        self.squares[origin_row][origin_col] = None
        self.squares[dest_row][dest_col] = piece
        piece.update_coordinates(dest_row, dest_col)
        return True

    def get_state(self):
        """Returns the current state of the board as a list of lists.

        Each piece is represented by "COLOR_TYPE" (e.g., "WHITE_PAWN").

        Returns:
            list: A 2D list representing the state of the board.
        """
        return [[f"{piece.get_color()}_{piece.__class__.__name__.upper()}" if piece else None for piece in row] for row in self.squares]

    def set_state(self, state):
        """Sets the state of the board from a list of lists.

        Args:
            state (list): A 2D list representing the state of the board.

        This method maps piece types to their corresponding classes and creates pieces accordingly.
        """
        piece_classes = {
            "PAWN": Pawn,
            "ROOK": Rook,
            "KNIGHT": Knight,
            "BISHOP": Bishop,
            "QUEEN": Queen,
            "KING": King
        }
    
        # Set the board state from a list of lists
        for i in range(8):
            for j in range(8):
                piece_info = state[i][j]
                if piece_info:
                    color, piece_type = piece_info.split('_')  # For example, "WHITE_PAWN"
                    # Create the piece using the class dictionary
                    self.squares[i][j] = piece_classes[piece_type](i, j, color)
                else:
                    self.squares[i][j] = None

       
