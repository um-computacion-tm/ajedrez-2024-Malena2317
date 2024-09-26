import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez')
from piezas.pieza import Piece

class King:
    def __init__(self, row, col, color):
        self.__row__ = row
        self.__col__ = col
        self.__color__ = color




    def move_valid(self, to_row, to_col, board):
        # Verifica si el movimiento es válido
        if abs(to_row - self.__row__) <= 1 and abs(to_col - self.__col__) <= 1:
            if board[to_row][to_col] is None or board[to_row][to_col].__color__ != self.__color__:
                return True
        return False

    def move(self, to_row, to_col, board):
        # Si el movimiento es válido, actualiza la posición
        if self.move_valid(to_row, to_col, board):
            self.__row__ = to_row
            self.__col__ = to_col
            return True
        return False


    
# Creo un tablero vacío
board = []
for i in range(8):
    fila = []
    for j in range(8):
        fila.append(None)
    board.append(fila)

# Coloco un Rey blanco en la posición (0, 4)
king = King(0, 4, "white")
board[0][4] = king

# Intento mover el Rey a diferentes posiciones
print(king.move_valid(1, 4, board))  # Debería ser True, mover abajo
print(king.move_valid(2, 4, board))  # Debería ser False, movimiento inválido
print(king.move_valid(1, 5, board))  # Debería ser True, mover en diagonal