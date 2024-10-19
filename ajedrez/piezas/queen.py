import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez')
from piezas.piece import Piece

  
class Queen(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)

    def get_symbol(self):
        # Returns the queen symbol depending on its color.
        # '♕' represents the white queen and '♛' the black queen. 
        return '♕' if self.get_color() == "WHITE" else '♛'
    
    def is_valid_move(self, to_row, to_col, board):
        #Checks if a move to position (to_row, to_col) is valid.
        print(f"Verifying movement to ({to_row}, {to_col})")
    
        if not self.is_within_board(to_row, to_col):
            print(f"Movement to({to_row}, {to_col}) is invalid: off the board.")
            return False
        
        if (to_row, to_col) == self.get_coordinates():
            print(f"Movement to ({to_row}, {to_col}) is invalid: same position..")
            return False
        
        # Check if the target position is occupied by a piece of the same color
        destination_piece = board.get_piece(to_row, to_col)
        if destination_piece is not None and destination_piece.get_color() == self.get_color():
            print(f"Movement to({to_row}, {to_col}) is invalid: occupied by the same piece")
            return False

        row_diff = abs(to_row - self.get_coordinates()[0])
        col_diff = abs(to_col - self.get_coordinates()[1])

        # A queen can move diagonally, vertically or horizontally
        is_valid = (row_diff == col_diff or row_diff == 0 or col_diff == 0)
        print(f"Movement to({to_row}, {to_col}) es {'valid' if is_valid else 'invalid'}.")

        return is_valid


    def check_obstacles(self, start_coords, to_row, to_col, board):
        # Check if there are obstacles between the starting position and the target position.
        start_row, start_col = start_coords
        row_diff = to_row - start_row
        col_diff = to_col - start_col

        step_row = (row_diff > 0) - (row_diff < 0)  
        step_col = (col_diff > 0) - (col_diff < 0)  

        current_row, current_col = start_row, start_col  

        # Move to the target position, excluding the target position
        while (current_row, current_col) != (to_row, to_col):
            current_row += step_row
            current_col += step_col
            
            if not self.is_within_board(current_row, current_col):
                print(f"Checking obstacles: ({current_row}, {current_col}) is off the board.")
                return True # Out of bounds of the board
            
            if board.get_piece(current_row, current_col) is not None:
                print(f"Checking obstacles: ({current_row}, {current_col}) is busy.")
                return True  # There is an obstacle
            
            # Debugging of evaluated positions
            print(f"Checking position: ({current_row}, {current_col}) is free.")

        print("No obstacles found.")
        return False  

    def move(self, to_row, to_col, board): 
        print(f"Trying to move to ({to_row}, {to_col})")
        if self.is_within_board(to_row, to_col) and self.is_valid_move(to_row, to_col, board):
            current_row, current_col = self.get_coordinates()
            print(f"Valid move. Updating position from ({current_row}, {current_col}) to ({to_row}, {to_col}).")
            board.set_piece(current_row, current_col, None) 
            self.update_coordinates(to_row, to_col)
            board.set_piece(to_row, to_col, self)
            return True
        print("Movement not allowed.")
        return False
