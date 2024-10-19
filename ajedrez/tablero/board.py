import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.rook import Rook
from piezas.king import King
from piezas.queen import Queen
from piezas.pawn import Pawn 
from piezas.knight import Knight
from piezas.bishop import Bishop
from piezas.piece import Piece 


 
class Board:
    def __init__(self):
        # Initializes the board and places pieces in their starting positions
        self.squares = self.initialize_board()

    def initialize_board(self):
        # Initializes the board with pieces in their starting positions
        squares = []
        for i in range(8):
            row = [None] * 8
            squares.append(row)  # Creates an empty 8x8 board

        # Places pieces 
        squares[0][0] = Rook(0, 0, "BLACK")
        squares[0][7] = Rook(0, 7, "BLACK")
        squares[7][0] = Rook(7, 0, "WHITE")
        squares[7][7] = Rook(7, 7, "WHITE")

        # Places pawns in their starting positions
        for i in range(8):
            squares[1][i] = Pawn(1, i, "BLACK")  # Peones negros deben estar en la fila 1 (desde el punto de vista del código)
            squares[6][i] = Pawn(6, i, "WHITE")  # Peones blancos deben estar en la fila 6 (desde el punto de vista del código)


         # Places remaining pieces
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
    
    def __getitem__(self, index):
        # Permite acceder a las filas del tablero usando el formato board[row]
        return self.squares[index]

    def print_board(self):
        # Prints the current state of the board to the console
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
        # Returns the piece at the given position
        if self.is_within_board(row, col):
            return self.squares[row][col]
        return None

    def set_piece(self, row, col, piece):
        # Sets a piece at the given position if it's within the board
        if self.is_within_board(row, col):
            self.squares[row][col] = piece
        

    def get_piece_position(self, piece):
        # Returns the piece in the given position.
        for row in range(8):
            for col in range(8):
                if self.squares[row][col] == piece:
                    return row, col
        return None

    def is_within_board(self, row, col):    
        # Check if the coordinates are within the range of the board.
        return 0 <= row < 8 and 0 <= col < 8
        

    def move_piece(self, origin_row, origin_col, dest_row, dest_col):
        # Attempts to move a piece from the origin position to the destination position
        piece = self.get_piece(origin_row, origin_col)

        # Checks if there's a piece at the origin position
        if piece is None:
            print(f"No piece at origin square ({origin_row}, {origin_col})")
            return False

        # Checks if the move is valid
        if not piece.is_valid_move(dest_row, dest_col, self):
            print("Invalid move for this piece")
            return False

        # Makes the move
        if self.get_piece(dest_row, dest_col) and self.get_piece(dest_row, dest_col).get_color() == piece.get_color():
            print("Cannot capture your own piece.")
            return False
        
        # Updates the board with movemen
        self.squares[origin_row][origin_col] = None
        self.squares[dest_row][dest_col] = piece
        piece.update_coordinates(dest_row, dest_col)
        print(f"Piece moved from ({origin_row}, {origin_col}) to ({dest_row}, {dest_col})")
        return True

    def get_state(self):
        # Devuelve el estado del tablero como una lista de listas
        # donde cada pieza se representa por "COLOR_TIPO" (por ejemplo, "WHITE_PAWN").
        return [[f"{piece.get_color()}_{piece.__class__.__name__.upper()}" if piece else None for piece in row] for row in self.squares]


    def set_state(self, state):
        # Establece el estado del tablero desde una lista de listas
        for i in range(8):
            for j in range(8):
                piece_info = state[i][j]
                if piece_info:
                    color, piece_type = piece_info.split('_')  # Por ejemplo, "WHITE_PAWN"
                    # Crear la pieza según el tipo y el color
                    if piece_type == "PAWN":
                        self.squares[i][j] = Pawn(i, j, color)
                    elif piece_type == "ROOK":
                        self.squares[i][j] = Rook(i, j, color)
                    elif piece_type == "KNIGHT":
                        self.squares[i][j] = Knight(i, j, color)
                    elif piece_type == "BISHOP":
                        self.squares[i][j] = Bishop(i, j, color)
                    elif piece_type == "QUEEN":
                        self.squares[i][j] = Queen(i, j, color)
                    elif piece_type == "KING":
                        self.squares[i][j] = King(i, j, color)
                else:
                    self.squares[i][j] = None




  