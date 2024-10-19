import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez') 
from piezas.piece import Piece 


class Pawn(Piece):

    def __init__(self, row, col, color):
        # Initializes the pawn at its starting position with a flag indicating if it has moved.
        super().__init__(row, col, color)  
        self.has_moved = False

    def get_symbol(self):
         # Returns the pawn's symbol based on its color.
        return '♙' if self.get_color() == "WHITE" else '♟'

    def move(self, to_row, to_col, board):
        if self.is_valid_move(to_row, to_col, board):
            result = super().move(to_row, to_col, board)
            if result:
                self.has_moved = True
                self.update_coordinates(to_row, to_col)
            return result
        return False

    def is_valid_move(self, to_row, to_col, board):
        current_row, current_col = self.get_coordinates()
        direction = -1 if self.get_color() == "WHITE" else 1
        print(f"Trying to move from ({current_row}, {current_col}) to ({to_row}, {to_col})")

        # Movimiento hacia adelante
        if self.is_forward_move((current_row, current_col), (to_row, to_col), direction, board):
            print("Forward move is valid")
            return True

        # Movimiento de captura en diagonal
        if self.is_capture_move((current_row, current_col), (to_row, to_col), direction, board):
            print("Capture move is valid")
            return True

        print("Move is not valid")
        return False

    def is_forward_move(self, from_pos, to_pos, direction, board):
        current_row, current_col = from_pos
        to_row, to_col = to_pos

        print(f"Current Position: ({current_row}, {current_col}), Target Position: ({to_row}, {to_col}), Direction: {direction}")

        # Movimiento de un espacio hacia adelante
        if current_col == to_col:
            if to_row == current_row + direction and board.get_piece(to_row, to_col) is None:
                return True

            # Movimiento de dos espacios hacia adelante desde la posición inicial
            if not self.has_moved and to_row == current_row + 2 * direction:
                if board.get_piece(to_row, to_col) is None and board.get_piece(current_row + direction, to_col) is None:
                    return True

        return False


    def is_capture_move(self, from_pos, to_pos, direction, board):
        current_row, current_col = from_pos
        to_row, to_col = to_pos
        
        # Captura en diagonal
        if abs(current_col - to_col) == 1 and to_row == current_row + direction:
            piece_at_destination = board.get_piece(to_row, to_col)
            if piece_at_destination and piece_at_destination.get_color() != self.get_color():
                return True
        
        return False

 