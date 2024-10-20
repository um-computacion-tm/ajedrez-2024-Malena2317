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
        self.squares = self.initialize_board()

    def initialize_board(self):
        # Inicializa el tablero con las piezas en su posición inicial
        squares = []
        for i in range(8):
            row = []
            for j in range(8):
                row.append(None)
            squares.append(row)

        # Coloca las piezas en su posición inicial
        squares[0][0] = Rook(0, 0, "BLACK")
        squares[0][7] = Rook(0, 7, "BLACK")
        squares[7][0] = Rook(7, 0, "WHITE")
        squares[7][7] = Rook(7, 7, "WHITE")

        # Coloca los peones en su posición inicial
        for i in range(8):
           squares[6][i] = Pawn(6, i, "WHITE")  # Los peones blancos deben estar en la fila 2 (índice 6)
           squares[1][i] = Pawn(1, i, "BLACK") 

        # Coloca las piezas restantes en su posición inicial
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

        # Retorna la pieza en la posición (row, col)
    def get_piece(self, row, col):
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
            # Verifica si las coordenadas están dentro del rango del tablero.
            return 0 <= row < 8 and 0 <= col < 8
        
    def move_piece(self, origin, destination):
        origin_row, origin_col = origin  # Descompone la tupla de origen
        dest_row, dest_col = destination 
        
        piece = self.get_piece(origin_row, origin_col)
        # Verificar si hay una pieza en la posición inicial
        if piece is None:
            print("No piece at origin square")
            return False
        # Verificar si el movimiento es válido
        if not piece.is_valid_move(dest_row, dest_col, self):
            print("Invalid move for this piece")
            return False
        # Realizar el movimiento
        self.squares[origin_row][origin_col] = None
        self.squares[dest_row][dest_col] = piece
        piece.update_coordinates(dest_row, dest_col) 
        return True

    def get_state(self):
            # Devuelve el estado del tablero como una lista de listas
            # donde cada pieza se representa por "COLOR_TIPO" (por ejemplo, "WHITE_PAWN").
            return [[f"{piece.get_color()}_{piece.__class__.__name__.upper()}" if piece else None for piece in row] for row in self.squares]


    def set_state(self, state):
        # Diccionario para mapear tipos de piezas a sus clases correspondientes
            piece_classes = {
                "PAWN": Pawn,
                "ROOK": Rook,
                "KNIGHT": Knight,
                "BISHOP": Bishop,
                "QUEEN": Queen,
                "KING": King
            }
    
            # Establece el estado del tablero desde una lista de listas
            for i in range(8):
                for j in range(8):
                    piece_info = state[i][j]
                    if piece_info:
                        color, piece_type = piece_info.split('_')  # Por ejemplo, "WHITE_PAWN"
                        # Crear la pieza usando el diccionario de clases
                        self.squares[i][j] = piece_classes[piece_type](i, j, color)
                    else:
                        self.squares[i][j] = None