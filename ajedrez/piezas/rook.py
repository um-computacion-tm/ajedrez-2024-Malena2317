import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez')

from piezas.pieza import Piece



class Rook(Piece):
    def __init__(self, color):
        self.__color__ = color
        self.__symbol__ = "♜" if color == "WHITE"  else "♖"


    
    def move(self, board, to_row, to_col):
        # Obtener la posición actual desde el tablero
        start_row, start_col = board.get_piece_position(self)

        # Realiza las validaciones del movimiento
        if self.is_valid_move(board, start_row, start_col, to_row, to_col):
            # Mueve la torre si es válido
            board.set_piece(start_row, start_col, None)  # Quitar de la posición actual
            board.set_piece(to_row, to_col, self)  # Colocar en la nueva posición
            return True
        return False

    def is_valid_move(self, board, start_row, start_col, to_row, to_col):
        # Verificar si el movimiento es vertical u horizontal
        if start_row == to_row or start_col == to_col:
            if start_row == to_row:  # Movimiento Horizontal
                return self._is_valid_horizontal_move(board, start_row, start_col, to_col)
            else:  # Movimiento Vertical
                return self._is_valid_vertical_move(board, start_row, to_row, start_col)
        else:
            return False

    def _is_valid_horizontal_move(self, board, row, start_col, to_col):
        step = 1 if to_col > start_col else -1
        for col in range(start_col + step, to_col, step):
            if board.get_piece(row, col) is not None:
                return False
        return True

    def _is_valid_vertical_move(self, board, start_row, to_row, col):
        step = 1 if to_row > start_row else -1
        for row in range(start_row + step, to_row, step):
            if board.get_piece(row, col) is not None:
                return False
        return True