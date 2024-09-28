import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.rook import Rook




class Board:

    def __init__(self):
        self.squares = self.initialize_board()

    def initialize_board(self):
        # Inicializa el tablero conlas piezas en su posicion inicial 
        squares = []
        for i in range(8):
            row = []
            for j in range(8):
                row.append(None)
            squares.append(row)
        squares[0][0] = Rook("BLACK") 
        squares[0][7] = Rook("BLACK") 
        squares[7][7] = Rook("WHITE") 
        squares[7][0] = Rook("WHITE") 
        return squares

    def get_piece(self, row, col):
        # Retorna la pieza en la posición (row, col)
        return self.__positions__[row][col]


    def set_piece(self, row, col, piece):
        self.__positions__[row][col] = piece
    

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
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)
                else:
                    board_str += " . "  # Representa una celda vacía
            board_str += "\n"
        return board_str