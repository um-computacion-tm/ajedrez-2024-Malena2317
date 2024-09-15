import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez') 
from piezas.pieza import Piece 


class Pawn(Piece):
    def __init__(self, color):
        self.__color__ = color
        if color == "WHITE":
            self.simbolo = "P"
        else:
            self.simbolo = "p"
  
class Position:
    def __init__(self, row, col):
        self.__row__ = row
        self.__col__ = col
        
    def move(self, start_pos, to_pos, board):  #Verifica si el peón se puede mover de la posición start_pos a to_pos en el tablero.

    
        movimiento_valido = True  # Variable para rastrear si el movimiento es válido o no
    
        # Verificar si se mueve en la misma fila
        if start_pos.row == to_pos.row:
            print("No puedes mover el peón a la misma fila")
            movimiento_valido = False
    
        # Verificar si se mueve en la columna
        if start_pos.col != to_pos.col:
            print("El peón solo se puede mover en columnas")
            movimiento_valido = False

        # Verificar si el peón blanco va para adelante
        if self.__color__ == "WHITE":
            if to_pos.row > start_pos.row:
                print("El peón blanco solo se puede mover hacia adelante")
                movimiento_valido= False

        # Verificar si el peón negro va para adelante
        if self.__color__ == "BLACK":
            if to_pos.row < start_pos.row:
                print("El peón negro solo se puede mover hacia adelante")
                movimiento_valido= False

        # Devuelve el resultado final
        return movimiento_valido
    
     # Si todas las verificaciones pasan, mueve el peón
        board[to_pos.row][to_pos.col] = self
        board[start_pos.row][start_pos.col] = None
        return True



