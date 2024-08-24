from  piezas import Piece



class Rook(Piece):
    def __init__(self, color):
        self.__color__ = color
        if color == "WHITE" :
            self.symbol = "♜"
        else: 
            self.symbol = "♖"
    def move( self, board, start_row, start_col, to_row, to_col):
        if self.is_valid_move(board, start_row, start_col, to_row, to_col):
            board.get_piece(to_row, to_col, self)
            board.get_piece(start_row, start_col, None)
            return True
        else:
            return False
    def is_valid_move(self, board, start_row, start_col, to_row, to_col):
    # La torre solo puede moverse en línea recta
        if start_row != to_row and start_col != to_col:
            return False

    # Movimiento vertical
        if start_col == to_col:
            for row in range(min(start_row, to_row) + 1, max(start_row, to_row)):
                if board.get_piece(row, start_col) is not None:
                    return False

    # Movimiento horizontal
        if start_row == to_row:
            for col in range(min(start_col, to_col) + 1, max(start_col, to_col)):
                if board.get_piece(start_row, col) is not None:
                    return False

    # No se puede mover al mismo lugar
        if start_row == to_row and start_col == to_col:
            return False

        return True


  