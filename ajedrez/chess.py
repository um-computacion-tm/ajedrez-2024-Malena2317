from  tablero.board import Board

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"# Empieza el turno con el jugador blanco
        self.game_over = False  # Indica si el juego ha terminado
    


    def move(self, from_row, from_col, to_row, to_col):
        "Gestiona el movimiento de una pieza"
        piece = self.__board__.get_piece(from_row, from_col)
        if piece and self.is_valid_move(piece, to_row, to_col):
            self.__board__.move_piece(from_row, from_col, to_row, to_col)
            self.change_turn()
        else:
            print("Movimiento inválido, intenta de nuevo.")


    def is_valid_move(self, piece, to_row, to_col):
        "Valida si el movimiento es legal dentro del tablero"
        return piece.move(to_row, to_col, self.__board__.squares)
        
    def play_turn(self):
        if self.game_over:  # Si el juego ha terminado, no se puede jugar
            return False
            self.board.print_board()  # Muestra el tablero
            print("Es el turno de " + self.current_turn)  # Indica de quién es el turno

           # Entrada de origen del movimiento
            origin = input("Ingrese la posición de origen (Ej: D2) o 'q' para rendirse: ")
            if origin.lower() == 'q':
                print("El jugador " + self.current_turn + " se ha rendido.")
                self.game_over = True
                return False
                # Entrada de destino del movimiento
                destination = input("Ingrese la posición de destino (Ej: D3): ")
                origin_coords = self.convert_position(origin)
                destination_coords = self.convert_position(destination)

            if origin_coords and destination_coords:
                from_row, from_col = origin_coords
                to_row, to_col = destination_coords
                self.move(from_row, from_col, to_row, to_col)
            else:
                print("Posiciones inválidas. Intenta de nuevo.")

 def switch_turn(self):
        # Change the current turn to the other player.
        self.current_turn = "BLACK" if self.current_turn == "WHITE" else "WHITE"
    
    def get_user_input(self, prompt):
        # Validate the user input.
        while True:
            user_input = input(prompt).strip().upper()
            if len(user_input) == 2 and user_input[0] in "ABCDEFGH" and user_input[1].isdigit():
                return user_input
            print("Invalid input. Remember, it should be something like 'D2'. Try again.")

    def get_positions_from_notation(self, notation):
        columns = "ABCDEFGH"
        row = 8 - int(notation[1])  # Convert chess row (2-8) to array indices (7-0).
        column = columns.index(notation[0])  # Convert chess column (A-H) to array indices (0-7
        print(f"Notación {notation} convertida a coordenadas: ({row}, {column})")
        return row, column

    def attempt_move(self, origin_row, origin_column, destination_row, destination_column):
        # Validate that the positions are within the board.
        if not self.board.is_within_board(origin_row, origin_column) or not self.board.is_within_board(destination_row, destination_column):
            print("El movimiento está fuera de los límites del tablero.")
            print(f"Intentando mover de ({origin_row}, {origin_column}) a ({destination_row}, {destination_column})")
            return False

        # Get the part at the origin position.
        piece = self.board.get_piece(origin_row, origin_column)
        if not piece:
            print("There is no piece in the home position.")
            return False
        if piece.get_color() != self.current_turn:
            print(f"It's the turn of {self.current_turn.lower()}, not of {piece.get_color().lower()}.")
            return False
        # Try to move the piece on the board.
        if self.board.move_piece(origin_row, origin_column, destination_row, destination_column):
            print("Successful move.")
            return True
        print("Movimiento no válido según el método move_piece.")
        return False

    def check_pawn_promotion(self):
            # Check if any pawn has reached the other end of the board and needs to be promoted.
            for column in range(8):
                # Check if there are white pawns that need to be promoted.
                if isinstance(self.board.get_piece(0, column), Pawn) and self.board.get_piece(0, column).color == "WHITE":
                    self.promote_pawn(0, column)
                # Check if there are black pawns that need to be promoted.
                elif isinstance(self.board.get_piece(7, column), Pawn) and self.board.get_piece(7, column).color == "BLACK":
                    self.promote_pawn(7, column)

 
