from  tablero.board import Board
from  piezas.bishop import Bishop
from  piezas.knight import Knight
from  piezas.pawn import Pawn
from  piezas.queen import Queen
from  piezas.king import King
from  piezas.rook import Rook 
import json


class Chess:
    def __init__(self):
        self.board = Board()  
        self.current_turn = "WHITE" 
        self.game_over = False  
        self.white_score = 0
        self.black_score = 0
    

    def save_game(self, filename="chess_game.json"):
        #Saves the current game state to a JSON file.
        game_state = {
            "board": self.board.get_state(),  # Implementar get_state en Board para obtener el estado del tablero
            "current_turn": self.current_turn,
            "game_over": self.game_over
        }
        with open(filename, 'w') as f:
            json.dump(game_state, f)
        print("Game saved.")

    def save_game_state(self):
        #Saves the game state and confirms the action.
        self.save_game()
        print("Game state saved.")


    def load_game(self, filename="chess_game.json"):
        #Loads the game state from a JSON file, handling errors if the file is not found or if there are JSON issues.
        try:
            with open(filename, 'r') as f:
                game_state = json.load(f)
                self.board.set_state(game_state["board"])  # Implementar set_state en Board para configurar el estado del tablero
                self.current_turn = game_state["current_turn"]
                self.game_over = game_state["game_over"]
            print("Game loaded successfully.")
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except json.JSONDecodeError:
            print("Error reading the game file.")

    def check_if_player_has_pieces(self, player_color):
        # Check if a player has any pieces left.
        for row in self.board.squares:
            for piece in row:
                if piece and piece.get_color() == player_color:
                    return True
        return False

    def declare_winner(self, winner_color):
        # Declare the winner and end the game.
        print(f"{winner_color} wins the game. Congratulations!")
        self.game_over = True

    def calculate_score(self, piece):     
        # Calculate score based on part type
        score_mapping = {
            "PAWN": 1,
            "KNIGHT": 3,
            "BISHOP": 3,
            "ROOK": 5,
            "QUEEN": 9,
            "KING": 0  
        }
        return score_mapping.get(piece.__class__.__name__.upper(), 0)


    def start_game(self):
        # Starts the game and displays the initial board
        print("Welcome to Chess! The game begins.")
        load_choice = input("Would you like to load a saved game? (Y/N): ").strip().upper()
        if load_choice == "Y":
            self.load_game() 
        
        self.board.print_board()  
        while not self.game_over:
            self.play_turn()
        print("The game has ended. Thank you for playing!")

    def play_turn(self):
        #Executes a player's turn in the chess game by prompting for move input, validating the move, updating scores if a piece is captured, switching turns, printing the board, and saving the game state.
        if self.game_over:
            print("The game is over. Thanks for playing!")
            return True 

        print(f"{self.current_turn}'s turn. Think carefully...")
        self.board.print_board()

        origin_position = self.get_user_input("Enter the origin position (e.g., D2): ")
        if origin_position is None:
            return

        destination_position = self.get_user_input("Enter the destination position (e.g., D4): ")
        if destination_position is None:
            return

        origin_row, origin_column = self.get_positions_from_notation(origin_position)
        destination_row, destination_column = self.get_positions_from_notation(destination_position)

        if self.attempt_move(origin_row, origin_column, destination_row, destination_column):
            piece_moved = self.board.get_piece(destination_row, destination_column)
            if piece_moved:
                # Increase player's score according to the captured piece
                if piece_moved.get_color() == "WHITE":
                    self.black_score += self.calculate_score(piece_moved)
                else:
                    self.white_score += self.calculate_score(piece_moved)

            self.switch_turn()
            self.board.print_board()  

            
            # Show scores after move
            print(f"Scores: White - {self.white_score}, Black - {self.black_score}")

            self.save_game()  # Save the game in Redis after each move
        else:
            print("Invalid move. Try again.")


    def switch_turn(self):
        # Change the current turn to the other player.
        self.current_turn = "BLACK" if self.current_turn == "WHITE" else "WHITE"
    
    def get_user_input(self, prompt):
        # Validate the user input.
        while True:
            user_input = input(prompt).strip().upper()
            if user_input == "END":
                print("The game ends by mutual agreement.")
                self.game_over = True
                return None
            if len(user_input) == 2 and user_input[0] in "ABCDEFGH" and user_input[1].isdigit():
                return user_input
            print("Invalid input. Remember, it should be something like 'D2'. Try again.")

    def get_positions_from_notation(self, notation):
        columns = "ABCDEFGH"
        row = 8 - int(notation[1])  # Convert chess row (1-8) to array indices (7-0).
        column = columns.index(notation[0])  # Convert chess column (A-H) to array indices (0-7)
        print(f"Notación {notation} convertida a coordenadas: ({row}, {column})")
        return row, column
    
    

    def attempt_move(self, origin_row, origin_column, destination_row, destination_column):
        # Initially we assume that the move is not successfu
        move_successful = False

        # Validate that the positions are within the board.
        if not (self.board.is_within_board(origin_row, origin_column) and 
                self.board.is_within_board(destination_row, destination_column)):
            print("The move is outside the board boundaries.")
        
        else:
            # Get the piece at the origin position.
            piece = self.board.get_piece(origin_row, origin_column)
            if not piece:
                print("There is no piece in the origin position")
                
            
            # Check if it's the correct turn.
            elif piece.get_color() != self.current_turn:
                print(f"Es el turno de {self.current_turn.lower()}, no de {piece.get_color().lower()}.")
            
            # Attempt to move the piece.
            else:
                move_successful = self.board.move_piece(origin_row, origin_column, destination_row, destination_column)
                if move_successful:
                    print("Movimiento exitoso.")
                    
                    # Check for pawn promotion if the piece is a pawn and it's in the promotion row
                    if isinstance(piece, Pawn) and (destination_row == 0 or destination_row == 7):
                        self.check_pawn_promotion()
        
        return move_successful


    def check_pawn_promotion(self):
        # Check if any pawn has reached the other end of the board and needs to be promoted.
        for column in range(8):
            # Check if there are white pawns that need to be promoted.
            pawn = self.board.get_piece(0, column)  
            if isinstance(pawn, Pawn) and pawn.get_color() == "WHITE":
                self.promote_pawn(0, column)
            
            # Check if there are black pawns that need to be promoted.
            pawn = self.board.get_piece(7, column)  
            if isinstance(pawn, Pawn) and pawn.get_color() == "BLACK":
                self.promote_pawn(7, column)

    def promote_pawn(self, row, column):
       
    # Ask the user to choose the piece to promote their pawn to.
        while True:
            print(f"Promote your pawn in {chr(column + ord('A'))}{8 - row}.")
            choice = input("Elige (Q)ueen, (R)ook, (B)ishop o (N)ight: ").strip().upper()
            if choice in {"Q", "R", "B", "N"}:
                break
            print("Invalid choice. Please choose Q, R, B or N.")

        # Replace the pawn with the chosen piece.
        if choice == "Q":
            self.board.set_piece(row, column, Queen(self.current_turn, row, column))
        elif choice == "R":
            self.board.set_piece(row, column, Rook(self.current_turn, row, column))
        elif choice == "B":
            self.board.set_piece(row, column, Bishop(self.current_turn, row, column))
        elif choice == "N":
            self.board.set_piece(row, column, Knight(self.current_turn, row, column))

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
    game.save_game("mi_partida.json")  
    game.load_game("mi_partida.json")  