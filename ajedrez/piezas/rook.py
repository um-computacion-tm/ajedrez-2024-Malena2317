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

    def _is_path_clear(self, board, fixed, start, end, is_horizontal):
        step = 1 if end > start else -1
        for pos in range(start + step, end, step):
            if is_horizontal:
                if board.get_piece(fixed, pos) is not None:
                    return False
            else:
                if board.get_piece(pos, fixed) is not None:
                    return False
        return True