
class Piece:
    def __init__(self, row, col, color):
        self.__row__ = row
        self.__col__ = col
        self.__color__ = color

    # Devuelve la posición de la pieza en forma de tupla (row, col)
    def get_coordinates(self):
        return (self.__row__, self.__col__)

    # Establece la nueva posición de la pieza.
    def update_coordinates(self, new_row, new_col):
        self.__row__ = new_row
        self.__col__ = new_col

    # Devuelve el color de la pieza.
    def get_color(self):
        return self.__color__

    #Devuelve el icono asociado al color de la pieza.
    def display_icon(self):
        if self.__color__ == "WHITE":
            return self.white_icon
        else:
            return self.black_icon

    #Verifica si una posición dada en el tablero
    def is_within_board(self, to_row, to_col):
        return 0 <= to_row < 8 and 0 <= to_col < 8


    #Verifica si se puede mover a la nueva posición
    def can_move_to(self, to_row, to_col, board):
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


    