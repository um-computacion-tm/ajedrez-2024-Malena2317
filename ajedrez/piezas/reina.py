import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez')
from piezas.pieza import Piece

class Queen(Piece):

    """Class representing a Queen chess piece."""

    def __init__(self, row, col, color):

        """Initialize a Queen.
        
        Args:
            row (int): Initial row position.
            col (int): Initial column position.
            color (str): Color of the Queen.
        """

        super().__init__(row, col, color)
        self.symbol = "♕" if color == "WHITE" else "♛"
        self.color = color
        

    def is_valid_move(self, to_row, to_col, board):

        """Check if the Queen can move to a specified position.
        
        Args:
            to_row (int): Target row.
            to_col (int): Target column.
            board (list): The chess board.
        
        Returns:
            bool: True if the move is valid, False otherwise.
        """
        
        if not self.is_within_board(to_row, to_col) or (to_row, to_col) == self.get_coordinates():
            return False

        if board[to_row][to_col] is not None and board[to_row][to_col].color == self.color:
            return False

        # Comprobar si la reina puede moverse a la posición dada
        row_diff = abs(to_row - self.get_coordinates()[0])
        col_diff = abs(to_col - self.get_coordinates()[1])

        is_valid = (row_diff == col_diff or row_diff == 0 or col_diff == 0)
        is_valid &= not self.check_obstacles(self.get_coordinates(), to_row, to_col, board)
        return is_valid

    def check_obstacles(self, start_coords, to_row, to_col, board):
        start_row, start_col = start_coords
        row_diff = to_row - start_row
        col_diff = to_col - start_col

        if row_diff == 0:  # Movimiento horizontal
            step_row = 0
            step_col = 1 if col_diff > 0 else -1
        elif col_diff == 0:  # Movimiento vertical
            step_row = 1 if row_diff > 0 else -1
            step_col = 0
        else:  # Movimiento diagonal
            step_row = 1 if row_diff > 0 else -1
            step_col = 1 if col_diff > 0 else -1

        current_row, current_col = start_row + step_row, start_col + step_col
        while (current_row, current_col ) != (to_row, to_col):
            if not self.is_within_board(current_row, current_col):
                return True  # Fuera del tablero
            if board[current_row][current_col] is not None:
                return True  # Hay un obstáculo
            current_row += step_row
            current_col += step_col
                    
        return False  # No hay obstáculos

    def move(self, to_row, to_col, board):
        # Comprobar si la posición está dentro del tablero
        if self.is_within_board(to_row, to_col) and self.is_valid_move(to_row, to_col, board) and self.can_move_to(to_row, to_col, board):
                current_row, current_col = self.get_coordinates()
                if board[current_row][current_col] == self:
                    board[current_row][current_col] = None
                self.update_coordinates(to_row, to_col)
                board[to_row][to_col] = self
                return True
        return False