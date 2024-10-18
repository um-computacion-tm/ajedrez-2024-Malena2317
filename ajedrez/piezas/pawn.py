import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez') 
from piezas.pieza import Piece 


class Pawn(Piece):

    def __init__(self, color):
        super().__init__(0, 0, color)  # Inicializa la posición en (0, 0)
        self.simbolo = '♙' if color == "WHITE" else '♟'
        self.has_moved = False

    def move(self, to_row, to_col, board):
        if self.is_valid_move(to_row, to_col, board):
            return super().move(to_row, to_col, board)
        return False

    def is_valid_move(self, to_row, to_col, board):
    current_row, current_col = self.get_coordinates()
    direction = 1 if self.get_color() == "WHITE" else -1  # Blancas hacia adelante, negras hacia atrás

    # Check forward movement
    if self.is_forward_move(current_row, to_row, current_col, to_col, direction, board):
        return True

    
    # Check capture motion
    if self.is_capture_move(current_row, current_col, to_row, to_col, direction, board):
        return True

    return False

    def is_forward_move(self, from_pos, to_pos, direction, board):
    current_row, current_col = from_pos
    to_row, to_col = to_pos

        # Move forward one square
        if current_col == to_col:
            if to_row == current_row + direction and board.get_piece(to_row, to_col) is None:
                return True
            # Movement of two squares from the initial position
            if (current_row == 1 and self.get_color() == "WHITE" or
                current_row == 6 and self.get_color() == "BLACK"):
                if (to_row == current_row + 2 * direction and
                    board.get_piece(to_row, to_col) is None and
                    board.get_piece(current_row + direction, to_col) is None):
                    return True
    
        return False

   def is_capture_move(self, from_pos, to_pos, direction, board):
        current_row, current_col = from_pos
        to_row, to_col = to_pos
        
        # Diagonal capture movement
        if abs(current_col - to_col) == 1 and to_row == current_row + direction:
            piece_at_destination = board.get_piece(to_row, to_col)
            if piece_at_destination and piece_at_destination.get_color() != self.get_color():
                return True
        
        return False

        
  
