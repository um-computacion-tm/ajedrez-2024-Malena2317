import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez')
from piezas.pieza import Piece

class King(Piece):
  
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.symbol = "♔" if color == "WHITE" else "♚"
        self.color = color

    def is_valid_move(self, to_row, to_col, board):
        start_row, start_col = self.get_coordinates()
        # Verificar que el movimiento sea de una casilla vecina 
        if abs(to_row - start_row) <= 1 and abs(to_col - start_col) <= 1:
            # Verificar si la casilla destino tiene una pieza del mismo color
            return self.can_move_to(to_row, to_col, board)
        print("Movimiento inválido para el Rey.")
        return False

  def is_valid_move(self, to_row, to_col, board):
        start_row, start_col = self.get_coordinates()
        # Verificar que el movimiento sea de una casilla vecina 
        if abs(to_row - start_row) <= 1 and abs(to_col - start_col) <= 1:
            # Verificar si la casilla destino tiene una pieza del mismo color
            return self.can_move_to(to_row, to_col, board)
        print("Movimiento inválido para el Rey.")
        return False

    def move(self, to_row, to_col, board):
        if self.is_valid_move(to_row, to_col, board):
            # Si el movimiento es válido, actualiza la posición del rey
            self.update_coordinates(to_row, to_col)
            board[to_row][to_col] = self
            return True
        else:
            # Si el movimiento no es válido, devuelve False
            return False
      
