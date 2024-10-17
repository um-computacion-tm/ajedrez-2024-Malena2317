from  tablero.board import Board
from  piezas.bishop import Bishop
from  piezas.knight import Knight
from  piezas.pawn import Pawn
from  piezas.queen import Queen
from  piezas.king import King
from  piezas.rook import Rook 


class Chess:
    def __init__(self):
        # Initialize the board and set the turn to white.
        self.__board__ = Board() # Board representation
        self.__turn__ = "WHITE"# Empieza el turno con el jugador blanco
        self.game_over = False  # Indica si el juego ha terminado
        self.move_history = []  # Store the move history

    def start_game(self):
        # Starts the game and displays the initial board
        print("Welcome to Chess! The game begins.")
        self.board.print_board()  # Mostrar el tablero inicial
        while not self.game_over:
            self.play_turn()

        
    def play_turn(self):
         # Check if the game is over before asking for the next move.
        if self.game_over:
            print("The game is over. Thanks for playing!")
            return True 

        print(f"{self.current_turn}'s turn. Think carefully...")
        self.board.print_board()

        # Ask for the origin and destination positions.
        origin_position = self.get_user_input("Enter the origin position (e.g., D2): ")
        destination_position = self.get_user_input("Enter the destination position (e.g., D4): ")

        # Convert the input positions to coordinates.
        origin_row, origin_column = self.get_positions_from_notation(origin_position)
        destination_row, destination_column = self.get_positions_from_notation(destination_position)

            # Attempt to make the move.
        if self.attempt_move(origin_row, origin_column, destination_row, destination_column):
            # If the move is successful, switch turns and update the board.
            self.switch_turn()
            self.board.print_board()  # Display the updated board.
        else:
            print("Invalid move. Try again.")
        

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
    def promote_pawn(self, row, column):
        # Ask the user to choose the piece to promote their pawn to.
        while True:
            print(f"Promote your pawn at {chr(column + ord('A'))}{8 - row}.")
            choice = input("Choose (Q)ueen, (R)ook, (B)ishop, or (N)ight: ").strip().upper()
            if choice in {"Q", "R", "B", "N"}:
                break
            print("Invalid choice. Please choose Q, R, B, or N.")

        # Replace the pawn with the chosen piece.
        if choice == "Q":
            self.board.board[row][column] = Queen(self.current_turn, row, column)
        elif choice == "R":
            self.board.board[row][column] = Rook(self.current_turn, row, column)
        elif choice == "B":
            self.board.board[row][column] = Bishop(self.current_turn, row, column)
        elif choice == "N":
            self.board.board[row][column] = Knight(self.current_turn, row, column)

        print("Pawn successfully promoted!")

    def declare_winner(self):
        # Declare the winner and end the game
        print(f"{self.current_turn} wins the game. Congratulations!")
        self.game_over = True

    def start_game(self):
        # Main game loop
        print("Welcome to Chess! The game begins.")
        while not self.game_over:
            self.play_turn()
        print("The game has ended. Thank you for playing!")

if __name__ == "__main__":
    game = Chess()
    game.start_game()

 
