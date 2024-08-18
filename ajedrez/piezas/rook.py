from piezas import Piece


class Rook(Piece):
    def __init__(self, color):
        self.__color__ = color
        if color == "WHITE" :
            self.symbol = "R"
        else: 
            self.symbol = "r"
    def move( self, board, start_row, start_col, end_row, end_col):
        if self.is_valid_move(board, start_row, start_col, end_row, end_col):
            board.set_piece(end_row, end_col, self)
            board.set_piece(start_row, start_col, None)
            return True
        else:
            return False