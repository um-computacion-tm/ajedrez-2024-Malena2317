class InvalidMoveNoPiec():
      
      def __init__(self, message="Movimiento no válido"):
        self.message = message
        super().__init__(self.message)

class InvalidMoveRookMove():

    def move(self, board, start_row, start_col, to_row, to_col):
    # Verifica si el movimiento es válido
        valid_move = self.is_valid_move(board, start_row, start_col, to_row, to_col)
        if not valid_move:
        # Error si el movimiento no es válido
            print("Error: Movimiento inválido para la torre.")
        return
    
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