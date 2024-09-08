class Piece:
    def __init__(self , color, start_):
        self.__color__ =  color 

        
def __str__(self):
        if self.__color__ == "WHITE":
            return self.white_str
        else:
            return self.black_str
        
def move(self, start_pos, to_pos, board):
        # Intenta mover la pieza de start_pos a to_pos en el tablero
        if not to_pos.is_within_board():
            print("¡Ouch! Te saliste del tablero!")
            return False

            
class Position:
    def __init__(self, row, col):
        # Inicializa una posición en el tablero de ajedrez
        self.row = row
        self.col = col

    def is_within_board(self):
        # Verifica si la posición está dentro del tablero
        if 0 <= self.row < 8 and 0 <= self.col < 8:
            return True
        return False




    