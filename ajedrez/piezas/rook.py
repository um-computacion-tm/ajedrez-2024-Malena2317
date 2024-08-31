import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez')

from piezas.pieza import Piece



class Rook(Piece):
    def __init__(self, color):
        self.__color__ = color
        self.__symbol__ = "♜" if color == "WHITE"  else "♖"


    def move( self, board, start_row, start_col, to_row, to_col):
            if self.is_valid_move(board, start_row, start_col, to_row, to_col) == False:
                 raise ValueError("Movimiento inválido")
    
            board.get_piece(to_row, to_col, self)
            board.get_piece(start_row, start_col, None)
    
    def is_valid_move(self, board, start_row, start_col, to_row, to_col):
    # La torre solo puede moverse en línea recta
        if start_row != to_row and start_col != to_col:
    # Movimiento horizontal
            if start_row == to_row: 
                for col in range(min(start_col, to_col) + 1, max(start_col, to_col)):
                    if board.get_piece(start_row, col) != None:
                        return False
    # Movimiento vertical
            if start_col == to_col:
                for row in range(min(start_row, to_row) + 1, max(start_row, to_row)):
                    if board.get_piece(row, start_col) != None:
                        return False
            return True

        return False

    


  