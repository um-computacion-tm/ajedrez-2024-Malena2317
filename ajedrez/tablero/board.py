import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from piezas.rook import Rook

class Board:
    def __init__(self):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        self.__positions__[0][0] = Rook("BLACK") # Black
        self.__positions__[0][7] = Rook("BLACK") # Black
        self.__positions__[7][7] = Rook("WHITE") # White
        self.__positions__[7][0] = Rook("WHITE") # White

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