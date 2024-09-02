class Piece:
    def __init__(self , color, start_):
        self.__color__ =  color 

def __str__(self):
        if self.__color__ == "WHITE":
            return self.white_str
        else:
            return self.black_str
        
def move(self, start_row, start_col, to_row, to_col, board):
        # Chequear si las filas y columnas están dentro del tablero
    if to_row < 0 or to_row >= 8 or to_col < 0 or to_col >= 8:
            # Si la posición está fuera del tablero, lanzar error
        print ("¡Ouch! Te saliste del tablero!")

    