import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez')
from piezas.pieza import Piece


class Queen(Piece):
    """
    Represents a Queen piece in a chess game.
    Inherits from the Piece class.
    """

    def __init__(self, row, col, color):
        """
        Initializes a Queen piece with its position and color.

        Args:
            row (int): The row position of the Queen on the board.
            col (int): The column position of the Queen on the board.
            color (str): The color of the Queen, either "WHITE" or "BLACK".
        """
        super().__init__(row, col, color)

    def get_symbol(self):
        """
        Returns the symbol for the Queen based on its color.

        Returns:
            str: The symbol representing the Queen ("♕" for white, "♛" for black).
        """
        return '♕' if self.get_color() == "WHITE" else '♛'

    def is_valid_move(self, to_row, to_col, board):
        """
        Checks if the move to the specified position is valid for the Queen.

        A Queen can move any number of squares in a straight line vertically, horizontally, or diagonally.

        Args:
            to_row (int): The target row position to move to.
            to_col (int): The target column position to move to.
            board (Board): The current game board to check for valid moves.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        print(f"Verificando movimiento a ({to_row}, {to_col})")
                
        # Check if the position is within the board limits
        if not self.is_within_board(to_row, to_col):
            print(f"Movimiento a ({to_row}, {to_col}) es inválido: fuera del tablero.")
            return False
                
        # Check if trying to move to the same position
        if (to_row, to_col) == self.get_coordinates():
            print(f"Movimiento a ({to_row}, {to_col}) es inválido: misma posición.")
            return False
        
        # Check if the target position is occupied by a piece of the same color
        destination_piece = board.get_piece(to_row, to_col)
        if destination_piece is not None and destination_piece.get_color() == self.get_color():
            print(f"Movimiento a ({to_row}, {to_col}) es inválido: ocupada por la misma pieza.")
            return False
        
        # Calculate differences to determine the type of move
        row_diff = abs(to_row - self.get_coordinates()[0])
        col_diff = abs(to_col - self.get_coordinates()[1])
        
        # A queen can move diagonally, vertically, or horizontally
        is_valid = (row_diff == col_diff or row_diff == 0 or col_diff == 0)
        print(f"Movimiento a ({to_row}, {to_col}) es {'válido' if is_valid else 'inválido'}.")
        
        return is_valid

    def check_obstacles(self, start_coords, to_row, to_col, board):
        """
        Checks if there are obstacles in the path from the starting coordinates to the target position.

        Args:
            start_coords (tuple): The starting coordinates (row, col) of the Queen.
            to_row (int): The target row position to move to.
            to_col (int): The target column position to move to.
            board (Board): The current game board to check for obstacles.

        Returns:
            bool: True if there are obstacles in the way, False otherwise.
        """
        start_row, start_col = start_coords
        row_diff = to_row - start_row
        col_diff = to_col - start_col

        step_row = (row_diff > 0) - (row_diff < 0)  # 1 if positive, -1 if negative
        step_col = (col_diff > 0) - (col_diff < 0)  # 1 if positive, -1 if negative

        current_row, current_col = start_row, start_col  # Start at the initial position

        # Move towards the target position, excluding the target position
        while (current_row, current_col) != (to_row, to_col):
            current_row += step_row
            current_col += step_col
            
            if not self.is_within_board(current_row, current_col):
                print(f"Verificando obstáculos: ({current_row}, {current_col}) está fuera del tablero.")
                return True  # Out of board limits
            
            if board.get_piece(current_row, current_col) is not None:
                print(f"Verificando obstáculos: ({current_row}, {current_col}) está ocupado.")
                return True  # There is an obstacle
            
            # Debugging the evaluated positions
            print(f"Verificando posición: ({current_row}, {current_col}) está libre.")

        print("No se encontraron obstáculos.")
        return False  # No obstacles found

    def move(self, to_row, to_col, board):
        """
        Moves the Queen to the specified position if the move is valid.

        Args:
            to_row (int): The target row position to move to.
            to_col (int): The target column position to move to.
            board (Board): The current game board to place the Queen.

        Returns:
            bool: True if the move was successful, False if the move was invalid.
        """
        print(f"Intentando mover a ({to_row}, {to_col})")
        if self.is_within_board(to_row, to_col) and self.is_valid_move(to_row, to_col, board):
            current_row, current_col = self.get_coordinates()
            print(f"Movimiento válido. Actualizando posición de ({current_row}, {current_col}) a ({to_row}, {to_col}).")
            board.set_piece(current_row, current_col, None) 
            self.update_coordinates(to_row, to_col)
            board.set_piece(to_row, to_col, self)
            return True
        print("Movimiento no permitido.")
        return False



