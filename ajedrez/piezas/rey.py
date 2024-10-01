import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez')
from piezas.pieza import Piece

class King(Piece):
    SYMBOLS = {"WHITE": "♔", "BLACK": "♚"}

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.symbol = self.SYMBOLS[color]

    def is_valid_move(self, to_row, to_col, board):
        start_row, start_col = self.get_coordinates()
        if abs(to_row - start_row) <= 1 and abs(to_col - start_col) <= 1:
            return self.can_move_to(to_row, to_col, board)
        print("Movimiento inválido para el Rey.")
        return False

    def move(self, to_row, to_col, board):
        return super().move(to_row, to_col, board) if self.is_valid_move(to_row, to_col, board) else False

    