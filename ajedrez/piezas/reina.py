import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez')
from piezas.pieza import Piece

class Queen(Piece):

    def __init__(self, row, col, color):
        self.__row__ = row
        self.__col__ = col
        self.color = color  # Add this line
        super().__init__(row, col, color)

    def is_valid_move(self, to_row, to_col, board):
        return board[to_row][to_col] is None or board[to_row][to_col].color != self.color


    def make_move(self, to_row, to_col, board):
        if self.is_valid_move(to_row, to_col, board) and (board[to_row][to_col] is None or board[to_row][to_col].color != self.color):
            self.__row__ = to_row
            self.__col__ = to_col
            board[to_row][to_col] = self  # Update the board to reflect the queen's new position
            return True
        return False

    def move(self, to_row, to_col, board):
        if self.is_horizontal_or_vertical(to_row, to_col) or self.is_diagonal(to_row, to_col):
            return self.make_move(to_row, to_col, board)
        return False

    def is_horizontal_or_vertical(self, to_row, to_col):
        return self.__row__ == to_row or self.__col__ == to_col

    def is_diagonal(self, to_row, to_col):
        return abs(self.__row__ - to_row) == abs(self.__col__ - to_col)


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
