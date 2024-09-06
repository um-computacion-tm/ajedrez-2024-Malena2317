import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez')

from piezas.pieza import Piece



class Rook(Piece):
    def __init__(self, color):
        self.__color__ = color
        self.__symbol__ = "♜" if color == "WHITE"  else "♖"


    def move(self, board, start_row, start_col, to_row, to_col):
        # Verificar si la torre intenta moverse al mismo lugar
        if start_row == to_row and start_col == to_col:
            return False  # El movimiento al mismo lugar no es válido
        
        # Verificación de si el movimiento es válido (horizontal o vertical)
        if self.is_valid_move(board, start_row, start_col, to_row, to_col):
            # Realiza el movimiento
            board.set_piece(to_row, to_col, self)
            board.set_piece(start_row, start_col, None)  # Elimina la pieza de la posición inicial
            return True  # Devuelve True si el movimiento fue exitoso
        
        return False 
    
    def is_valid_move(self, board, start_row, start_col, to_row, to_col):
    # Verificar si el movimiento es vertical u horizontal 
        if start_row == to_row:  # Movimiento Horizontal
            return self._is_valid_horizontal_move(board, start_row, start_col, to_col)
        elif start_col == to_col:  # Movimiento Vertical 
            return self._is_valid_vertical_move(board, start_row, to_row, start_col)
        else:
            return False

    def _is_valid_horizontal_move(self, board, row, start_col, to_col):
        for col in range(min(start_col, to_col) + 1, max(start_col, to_col)):
            if board.get_piece(row, col) is not None:
                return False
        return True

    def _is_valid_vertical_move(self, board, start_row, to_row, col):
        for row in range(min(start_row, to_row) + 1, max(start_row, to_row)):
            if board.get_piece(row, col) is not None:
                return False
        return True

    


  