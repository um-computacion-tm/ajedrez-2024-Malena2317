import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez')
from piezas.piece import Piece



class Rook(Piece):
    """
    Represents a rook chess piece.

    A rook can move any number of squares along a row or column,
    but cannot jump over other pieces.
    """

    def __init__(self, row, col, color):
        """
        Initializes a rook piece.

        Args:
            row (int): The initial row position of the rook on the board.
            col (int): The initial column position of the rook on the board.
            color (str): The color of the rook, either 'WHITE' or 'BLACK'.
        """
        super().__init__(row, col, color)
        
    def get_symbol(self):
        """
        Returns the symbol representing the rook.

        Returns:
            str: The symbol for the rook, '♖' for white and '♜' for black.
        """
        return "♖" if self.get_color() == "WHITE" else "♜"
        
    def move(self, to_row, to_col, board):
        """
        Moves the rook to a specified position on the board.

        Args:
            to_row (int): The target row position to move to.
            to_col (int): The target column position to move to.
            board (Board): The board on which the rook is moving.

        Returns:
            bool: True if the move was successful, False otherwise.
        """
        if self.is_valid_move(to_row, to_col, board):
            current_row, current_col = self.get_coordinates()
            board.set_piece(current_row, current_col, None)
            self.update_coordinates(to_row, to_col)
            board.set_piece(to_row, to_col, self) 
            return True
        return False

    def is_valid_move(self, to_row, to_col, board):
        """
        Checks if a move to a specified position is valid for the rook.

        Args:
            to_row (int): The target row position to check.
            to_col (int): The target column position to check.
            board (Board): The board on which the move is being validated.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        print(f"Verificando movimiento de ({self.get_coordinates()}) a ({to_row}, {to_col})")
        # Verify if the position is within the board
        if not self.is_within_board(to_row, to_col):
            print("Movimiento fuera del tablero.")
            return False

        current_row, current_col = self.get_coordinates()
        # Check if the movement is in a straight line
        if current_row == to_row or current_col == to_col:
            # Check if the path is clear
            if self._is_path_clear(current_row, current_col, to_row, to_col, board):
                # Check if the destination position is empty or has a piece of a different color
                destination_piece = board.get_piece(to_row, to_col)  
                if destination_piece is None or destination_piece.get_color() != self.get_color():
                    return True
        return False
        

    def _is_path_clear(self, from_row, from_col, to_row, to_col, board):
        """
        Checks if the path between the current position and the target position is clear.

        Args:
            from_row (int): The starting row position.
            from_col (int): The starting column position.
            to_row (int): The target row position.
            to_col (int): The target column position.
            board (Board): The board on which the path is being checked.

        Returns:
            bool: True if the path is clear, False if there are obstacles.
        """
        # Determine the direction of movement
        step_row = 0 if from_row == to_row else (1 if to_row > from_row else -1)
        step_col = 0 if from_col == to_col else (1 if to_col > from_col else -1)

        # Iterate through the intermediate positions
        row, col = from_row + step_row, from_col + step_col
        while row != to_row or col != to_col:
            print(f"Verificando posición ({row}, {col})")
            if board.get_piece(row, col) is not None:
                print(f"Obstáculo encontrado en ({row}, {col})")
                return False
            row += step_row
            col += step_col
        return True
