import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez')
from piezas.pieza import Piece




class Rook(Piece):

    def __init__(self,row, col, color):
        super().__init__(row, col, color)
        self.__symbol__ = "♜" if color == "WHITE"  else "♖"
        
    def move(self, to_row, to_col, board):
        if self.is_valid_move(to_row, to_col, board):
            current_row, current_col = self.get_coordinates()
            board[current_row][current_col] = None
            self.update_coordinates(to_row, to_col)
            board[to_row][to_col] = self
            return True
        return False

    def is_valid_move(self, to_row, to_col, board):
        # Verificar si la posición está dentro del tablero
        if not self.is_within_board(to_row, to_col):
            return False

        current_row, current_col = self.get_coordinates()
        # Verificar movimiento en línea recta
        if current_row == to_row or current_col == to_col:
            # Verificar si el camino está libre
            if self._is_path_clear(current_row, current_col, to_row, to_col, board):
                # Verificar si la posición de destino está vacía o tiene una pieza de otro color
                destination_piece = board[to_row][to_col]
                if destination_piece is None or destination_piece.get_color() != self.get_color():
                    return True
        return False
        
  def _is_path_clear(self, from_row, from_col, to_row, to_col, board):
          # Verifica si hay obstaculos en el camino
          step_row = 1 if to_row > from_row else -1
          step_col = 1 if to_col > from_col else -1
          if from_row == to_row:  # Horizontal
              for col in range(from_col + step_col, to_col, step_col):
                  if board[from_row][col] is not None:
                      return False
          else:  # Vertical
              for row in range(from_row + step_row, to_row, step_row):
                  if board[row][from_col] is not None:
                      return False
          return True
   