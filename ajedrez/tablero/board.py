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
            squares[1][i] = Pawn(1, i, "WHITE")  # Añadido: fila y columna
            squares[6][i] = Pawn(6, i, "BLACK")  # Añadido: fila y columna

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
        self.squares[row][col] = piece

    def get_piece_position(self, piece):
        if self.is_within_board(row, col):
            return self.board[row][col]
        return None

    def is_within_board(self, row, col):
            # Verifica si las coordenadas están dentro del rango del tablero.
            return 0 <= row < 8 and 0 <= col < 8
        
    def move_piece(self, origin, destination):
         piece = self.get_piece(origin_row, origin_col)
        # Verificar si hay una pieza en la posición inicial
        if piece is None:
            print("No piece at origin square")
            return False
        # Verificar si el movimiento es válido
        if not piece.is_valid_move(dest_row, dest_col, self.squares):
            print("Invalid move for this piece")
            return False
        # Realizar el movimiento
        self.squares[origin_row][origin_col] = None
        self.squares[dest_row][dest_col] = piece
        piece.update_coordinates(dest_row, dest_col)
        return True
        
       
