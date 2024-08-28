import sys
sys.path.insert(0, '/home/meli/Escritorio/computacion/ajedrez-2024-Malena2317/ajedrez')
from piezas.pieza import Piece

class King:
    def __init__(self, row, col, color):
        self.__row__ = row
        self.__col__ = col
        self.__color__ = color

    def move(self, to_row, to_col, board):
        # Verifica si el rey se mueve una casilla en cualquier dirección
        if to_row == self.__row__ + 1 or to_row == self.__row__ - 1 or to_row == self.__row__:
            if to_col == self.__col__ + 1 or to_col == self.__col__ - 1 or to_col == self.__col__:
                # Verifica si la casilla está vacía o tiene una pieza del color contrario
                if board[to_row][to_col] == None:
                    self.__row__ = to_row
                    self.__col__ = to_col
                    return True
                elif board[to_row][to_col] != None and board[to_row][to_col].color != self.__color__:
                    self.__row__= to_row
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
print(king.move(1, 4, board))  # Debería ser True, mover abajo
print(king.move(2, 4, board))  # Debería ser False, movimiento inválido
print(king.move(1, 5, board))  # Debería ser True, mover en diagonal