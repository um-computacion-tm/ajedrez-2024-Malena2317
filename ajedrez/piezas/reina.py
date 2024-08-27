import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez')
from piezas.pieza import Piece

class Queen:
    def __init__(self, row, col, color):
        self.__row__ = row
        self.__col__ = col
        self.__color__ = color

    def move(self, to_row, to_col, board):
        # Movimientos horizontales o verticales
        if self.__row__ == to_row or self.__col__ == to_col:
            # Si la casilla está vacía o hay una pieza del otro color
            if board[to_row][to_col] == None or board[to_row][to_col].color != self.color:
                self.row = to_row
                self.col = to_col
                return True

        # Movimientos diagonales
        elif abs(self.row - to_row) == abs(self.col - to_col):
            if board[to_row][to_col] == None or board[to_row][to_col].color != self.color:
                self.row = to_row
                self.col = to_col
                return True

        # Si nada de lo anterior funciona, entonces no se puede mover
        return False


# Crear un tablero vacío
board = []
for i in range(8):
    board.append([None] * 8)

# Crear una Reina blanca en (0, 0)
queen = Queen(0, 0, "white")

# Intentar mover la Reina a varias posiciones
print(queen.move(0, 5, board))  # True
print(queen.move(5, 5, board))  # True
print(queen.move(2, 2, board))  # True
print(queen.move(4, 1, board))  # False
