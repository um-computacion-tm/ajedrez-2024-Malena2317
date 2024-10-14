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
            squares[1][i] = Pawn("WHITE")
            squares[6][i] = Pawn("BLACK")

        # Coloca las piezas restantes en su posición inicial
        squares[0][1] = Knight(0, 1, "BLACK")
        squares[0][6] = Knight(0, 6, "BLACK")
        squares[7][1] = Knight(7, 1, "WHITE")
        squares[7][6] = Knight(7, 6, "WHITE")

        squares[0][2] = Alfil(0, 2, "BLACK")
        squares[0][5] = Alfil(0, 5, "BLACK")
        squares[7][2] = Alfil(7, 2, "WHITE")
        squares[7][5] = Alfil(7, 5, "WHITE")

        squares[0][3] = Queen(0, 3, "BLACK")
        squares[7][3] = Queen(7, 3, "WHITE")

        squares[0][4] = King(0, 4, "BLACK")
        squares[7][4] = King(7, 4, "WHITE")

        return squares

        # Retorna la pieza en la posición (row, col)
    def get_piece(self, row, col):
        return self.squares[row][col]

    def set_piece(self, row, col, piece):
        self.squares[row][col] = piece

    def get_piece_position(self, piece):
        """Busca la posición de una pieza en el tablero y retorna (row, col)"""
        for row in range(8):
            for col in range(8):
                if self.get_piece(row, col) == piece:
                    return row, col
        return None, None

    def print_board(self):
        # Prints the board to the console
        print("  a b c d e f g h")
        for i in range(8):
            print(i + 1, end=" ")
            for j in range(8):
                if self.squares[i][j] is None:
                    print("-", end=" ")
                else:
                    print(self.squares[i][j], end=" ")
            print()

    def move_piece(self, origin, destination):
        # Mueve las piezas en el tablero
        x1, y1 = origin
        x2, y2 = destination
        piece = self.squares[x1][y1]
        if piece is not None:
            self.squares[x1][y1] = None
            self.squares[x2][y2] = piece
        else:
            print("No piece at origin square")

    def __str__(self):
        # Representa el tablero como una cadena de texto
        board_str = ""
        for row in self.squares:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)
                else:
                    board_str += " . "  # Representa una celda vacía
            board_str += "\n"
        return board_str