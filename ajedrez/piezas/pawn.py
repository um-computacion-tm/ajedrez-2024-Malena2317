from piezas import Piece


class Pawn(Piece):
   def __init__(self, color):
     self.__color__ = color
     if color == "WITHE":
      self.simbolo = "P"
     else:
      self.simbolo = "p"
      
   def mover(self, tablero, start_row, start_col, to_row, to_col ):
     if start_row == to_row:
       print("No puedes mover el peon a la misma fila")
       return False
     if start_col != to_col:
       print("El peon solo se puede mover en columnas")
       return False
     if self.color == "blanco" and to_row > start_row:
       print("El peon blanco solo se puede mover hacia adelante")
       return False
     if self.color == "negro" and to_row < start_row:
       print("El peon negro solo se puede mover hacia adelante")
       return False
     tablero[to_row][to_col] = self
     tablero[start_row][start_col] = None
     return True

