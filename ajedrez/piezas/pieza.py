
class Piece:
    def __init__(self, row, col, color):
        self.__row__ = row
        self.__col__ = col
        self.__color__ = color

    def get_coordinates(self):
        return (self.__row__, self.__col__)

    def update_coordinates(self, new_row, new_col):
        self.__row__ = new_row
        self.__col__ = new_col

    def get_color(self):
        return self.__color__

    def is_within_board(self, to_row, to_col):
        return 0 <= to_row < 8 and 0 <= to_col < 8

    def can_move_to(self, to_row, to_col, board):
        # Verifica si se puede mover a la nueva posición
        if not self.is_within_board(to_row, to_col):
            print("Te saliste del tablero!!")
            return False
        if board[to_row][to_col] is None or board[to_row][to_col].get_color() != self.get_color():
            return True
        return False

    def move(self, to_row, to_col, board):
        if self.can_move_to(to_row, to_col, board):
            self.update_coordinates(to_row, to_col)
            board[to_row][to_col] = self
            return True
        return False

    def is_valid_move(self, to_row, to_col, board):
        raise NotImplementedError("Este método debe ser implementado por las subclases") 