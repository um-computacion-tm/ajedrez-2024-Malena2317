import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from typing import List
from plistlib import InvalidFileException



# EXCEPCION FICHAS ------------------------------------------------------------------------------------------------------

class InvalidMoveRookMove():
    
    def move(self, board, start_row, start_col, to_row, to_col):
    # Verifica si el movimiento es válido
        valid_move = self.is_valid_move(board, start_row, start_col, to_row, to_col)
        if not valid_move:
        # Error si el movimiento no es válido
            print("Error: Movimiento inválido para la torre.")
        return
    
class InvalidMoveBishop(Exception):

    def __init__(self, position, message="Movimiento no válido para el alfil"):
        # Se guarda la posición y se crea el mensaje básico
        self.position = position
        self.message = message + " en la posición " + str(position)
        super().__init__(self.message)  # Llamada al constructor de Exception

    def __str__(self):
        # Se retorna el mensaje formateado
        return "Error: " + self.message

    def is_valid_diagonal_move(start_row, start_col, to_row, to_col, board):
        # Verifica si el movimiento es diagonal
        if abs(start_row - to_row) != abs(start_col - to_col):
            raise InvalidMoveDiagonal((to_row, to_col))

    # Verifica si la casilla de destino está ocupada
        if board[to_row][to_col] is not None:
            raise InvalidMoveDiagonal((to_row, to_col), message="La casilla de destino está ocupada")
    
    # Si pasa todas las verificaciones, el movimiento es válido
        return True



class InvalidMoveKnight(Exception):
    def __init__(self, position, message="El caballo no se puede mover así"):
        # Guardar la posición donde ocurrió el error
        self.position = position
        # Crear el mensaje de error con la posición
        self.message = message + " en " + str(position)
        # Llamar a la superclase Exception
        super(InvalidMoveKnight, self).__init__(self.message)

    def __str__(self):
        # Mostrar el mensaje de error
        return "Error: " + self.message

    def mover_caballo(caballo, to_row, to_col, tablero):
    # Calcular las diferencias en filas y columnas usando métodos getter
        diferencia_filas = abs(caballo.get_row() - to_row)
        diferencia_columnas = abs(caballo.get_col() - to_col)
    
    # Comprobar si el movimiento es válido para el caballo
        if not (diferencia_filas == 2 and diferencia_columnas == 1) and not (diferencia_filas == 1 and diferencia_columnas == 2):
        # Lanzar error si el movimiento no es válido
            raise InvalidMoveKnight((to_row, to_col))
    
    # Comprobar si la casilla destino está vacía
        if tablero[to_row][to_col] is None:
        # Mover el caballo a la nueva posición
            caballo.set_row(to_row)
            caballo.set_col(to_col)
            return True
    
        # Retornar False si la casilla está ocupada
        return False



#---------------------------------------------------------------------------------------------------------------------------------

#EXCEPCIONES GENERALES --------------------------------------------------------------------------------------------------------------

class InvalidMove(Exception):
    
    def verificar_si_posicion_ocupada(board, to_row, to_col, pieza):
    # Buscar la pieza en la posición
        pieza_en_destino = board.get_piece(to_row, to_col)
    
    # Si hay algo en esa posición
        if pieza_en_destino != None:
        # Si es del mismo color
            if pieza_en_destino.__color__ == pieza.__color__:
                print("Error: La posición está ocupada por una pieza del mismo color.")
            return True  # Está ocupada, así que devolver True
    
    # Si no hay pieza o es de otro color
        return False  # No está ocupada por una pieza del mismo color

class PieceNotFoundException(Exception):
    def __init__(self, position, message="No hay ninguna pieza en la posición especificada"):
        # Se guarda la posición y se crea el mensaje básico
        self.position = position
        self.message = message + " en la posición " + str(position)
        Exception.__init__(self, self.message)  # Llamada directa al constructor de Exception

    def __str__(self):
        # Se retorna el mensaje tal cual, sin mucho formato
        return "Error: " + self.message

# Función para obtener la pieza en una posición del tablero
    def get_piece_at(board, position):
    # Verificar si hay una pieza en la posición dada
        if board[position[0]][position[1]] == None:
        # Lanza la excepción si no hay ninguna pieza
            raise PieceNotFoundException(position)
    # Retorna la pieza en esa posición (si la hay)
        return board[position[0]][position[1]]
    

class InvalidMoveNoPiec():
      
      def __init__(self, message="Movimiento no válido"):
        self.message = message
        super().__init__(self.message)
    
#----------------------------------------------------------------------------------------------------------------------------------------------