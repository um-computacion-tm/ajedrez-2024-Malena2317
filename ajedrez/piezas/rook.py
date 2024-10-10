import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez')
from piezas.pieza import Piece



class Rook(Piece):

    def __init__(self, color):
        self.__color__ = color
        self.__symbol__ = "♜" if color == "WHITE"  else "♖"

        
    def is_valid_move(self, to_row, to_col, board):
        current_row, current_col = self.get_coordinates()
        if current_row == to_row or current_col == to_col:
            return self._is_path_clear(current_row, current_col, to_row, to_col, board)
        return False

    def _is_path_clear(self, start_row, start_col, to_row, to_col, board):
        # Verifica si hay obstaculos en el camino
        step_row = to_row - start_row
        step_col = to_col - start_col
  
        # Determinar la dirección del movimiento
        step_row = 1 if delta_row > 0 else (-1 if delta_row < 0 else 0)
        step_col = 1 if delta_col > 0 else (-1 if delta_col < 0 else 0)

        # Recorre el camino desde la posición actual hasta la de destino
        current_row, current_col = from_row + step_row, from_col + step_col
        while current_row != to_row or current_col != to_col:
            if board[current_row][current_col] is not None:
                return False
            current_row += step_row
            current_col += step_col
            
        return True

    def _get_step(self, delta):
        
        if delta > 0:
            return 1
        elif delta < 0:
            return -1
        else:
            return 0