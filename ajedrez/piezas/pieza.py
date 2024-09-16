
class Piece:
    def __init__(self, row, col, color):
        self.__row__ = row
        self.__col__ = col
        self.__color__ = color


        
    def __str__(self):
            if self.__color__ == "WHITE":
                return self.white_str
            else:
                return self.black_str

    def move(self, to_position, board):
        # Utiliza la lógica de la clase Position para moverse
        return self.position.move(to_position, board, self.color)
        
class Position:
    def __init__(self, row, col):
        # Inicializa una posición en el tablero de ajedrez
        self.__row__ = row
        self.__col__ = col

    def is_within_board(self):
        # Verifica si la posición está dentro del tablero
        return 0 <= self.row < 8 and 0 <= self.col < 8

    def move(self, start_pos, to_pos, board):
        # Intenta mover la pieza de start_pos a to_pos en el tablero
        if not to_pos.is_within_board():
            print("Te saliste del tablero!!")
            return False
        if self.can_move_to(to_pos, board, color):
            self.row = to_pos.row
            self.col = to_pos.col
            return True
        return False

    def is_valid_move(self, to_row, to_col, board):
        return board[to_row][to_col] is None or board[to_row][to_col].color != self.color

    def make_move(self, to_row, to_col, board):
        if self.is_valid_move(to_row, to_col, board):
            self.row = to_row
            self.col = to_col
            return True
        return False
    