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
    pass