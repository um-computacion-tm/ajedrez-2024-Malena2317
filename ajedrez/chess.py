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
     
        """
        Initialize the chess game with a board and sets the initial turn to white.
        """
        self.board = Board()  # Board representation
        self.current_turn = "WHITE"  # Starts with the white player's turn
        self.game_over = False  # Indicates if the game has ended
        self.white_score = 0
        self.black_score = 0

    def save_game(self, filename="chess_game.json"):
        """
        Saves the current state of the game to a JSON file.
        
        Args:
            filename (str): The name of the file where the game state will be saved.
        """
        game_state = {
            "board": self.board.get_state(),  # Implement get_state in Board to retrieve the board state

            "current_turn": self.current_turn,
            "game_over": self.game_over
        }
        with open(filename, 'w') as f:
            json.dump(game_state, f)
        print("Game saved.")

    def save_game_state(self):
        """
        Save the game state using the save_game method.
        """
        self.save_game()
        print("Game state saved.")

    def load_game(self, filename="chess_game.json"):
        """
        Loads a saved game state from a JSON file.
        
        Args:
            filename (str): The name of the file from which the game state will be loaded.
        """
        try:
            with open(filename, 'r') as f:
                game_state = json.load(f)
                self.board.set_state(game_state["board"])  # Implement set_state in Board to set the board state

                self.current_turn = game_state["current_turn"]
                self.game_over = game_state["game_over"]
            print("Game loaded successfully.")
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except json.JSONDecodeError:
            print("Error reading the game file.")

    def check_if_player_has_pieces(self, player_color):
        """
        Check if a player has any pieces left on the board.
        
        Args:
            player_color (str): The color of the player to check.
        
        Returns:
            bool: True if the player has pieces left, False otherwise.
        """

        for row in self.board.squares:
            for piece in row:
                if piece and piece.get_color() == player_color:
                    return True
        return False

    def declare_winner(self, winner_color):
        """
        Declare the winner and end the game.
        
        Args:
            winner_color (str): The color of the winning player.
        """
        print(f"{winner_color} wins the game. Congratulations!")
        self.game_over = True

    def calculate_score(self, piece):
        """
        Calculate the score based on the type of captured piece.
        
        Args:
            piece (Piece): The captured piece.
        
        Returns:
            int: The score corresponding to the captured piece.
        """
        score_mapping = {
            "PAWN": 1,
            "KNIGHT": 3,
            "BISHOP": 3,
            "ROOK": 5,
            "QUEEN": 9,
            "KING": 0  # El rey no tiene puntuación
        }
        return score_mapping.get(piece.__class__.__name__.upper(), 0)


    def start_game(self):
        """
        Starts the game and displays the initial board state.
        """
        print("Welcome to Chess! The game begins.")
        load_choice = input("Would you like to load a saved game? (Y/N): ").strip().upper()
        if load_choice == "Y":
            self.load_game()  # Load the saved game
        
        self.board.print_board()  # Display the initial board
        while not self.game_over:
            self.play_turn()
        print("The game has ended. Thank you for playing!")

    
    def play_turn(self):
        """
        Execute a player's turn, validate input, and make moves.
        
        Returns:
            bool: True if the game is over after the turn, False otherwise.
        """
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
            # Update scores if the move is successful.
            piece_moved = self.board.get_piece(destination_row, destination_column)
            if piece_moved:
                # Update the score based on the captured piece.
                if piece_moved.get_color() == "WHITE":
                    self.black_score += self.calculate_score(piece_moved)
                else:
                    self.white_score += self.calculate_score(piece_moved)

            self.switch_turn()
            self.board.print_board()  # Show the updated board

            # Display scores after the move.
            print(f"Scores: White - {self.white_score}, Black - {self.black_score}")

            self.save_game()  # Save the game after each move
        else:
            print("Invalid move. Try again.")

    def switch_turn(self):
        """
        Change the current turn to the other player.
        """
        self.current_turn = "BLACK" if self.current_turn == "WHITE" else "WHITE"
    
    def get_user_input(self, prompt):
        """
        Validate the user's input for board positions.
        
        Args:
            prompt (str): The prompt to display to the user.
        
        Returns:
            str: The validated user input.
        """

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
        """
        Convert chess notation to board coordinates.
        
        Args:
            notation (str): The notation (e.g., 'D2').
        
        Returns:
            tuple: A tuple with row and column indices.
        """
        columns = "ABCDEFGH"
        row = 8 - int(notation[1])  # Convert chess row (2-8) to array indices (7-0).
        column = columns.index(notation[0])  # Convert chess column (A-H) to array indices (0-7).
        print(f"Notation {notation} converted to coordinates: ({row}, {column})")
        return row, column
    
    def attempt_move(self, origin_row, origin_column, destination_row, destination_column):
        """
        Attempt to move a piece on the board and validate the move.
        
        Args:
            origin_row (int): The row of the piece's starting position.
            origin_column (int): The column of the piece's starting position.
            destination_row (int): The row of the piece's destination.
            destination_column (int): The column of the piece's destination.
        
        Returns:
            bool: True if the move is successful, False otherwise.
        """
        move_successful = False

        if not (self.board.is_within_board(origin_row, origin_column) and 
                self.board.is_within_board(destination_row, destination_column)):
            print("The move is outside the board limits.")
        else:
            piece = self.board.get_piece(origin_row, origin_column)
            if not piece:
                print("There is no piece at the origin position.")
            elif piece.get_color() != self.current_turn:
                print(f"It is {self.current_turn.lower()}'s turn, not {piece.get_color().lower()}'s.")
            else:
                move_successful = self.board.move_piece((origin_row, origin_column), (destination_row, destination_column))
                if move_successful:
                    print("Move successful.")
                    if isinstance(piece, Pawn) and (destination_row == 0 or destination_row == 7):
                        self.check_pawn_promotion()

        return move_successful
    
  
    def check_pawn_promotion(self):
        """
        Check if any pawn has reached the end of the board and needs promotion.
        """
        for column in range(8):
            pawn = self.board.get_piece(0, column)  # For white pawns in row 0
            if isinstance(pawn, Pawn) and pawn.get_color() == "WHITE":
                self.promote_pawn(0, column)
            pawn = self.board.get_piece(7, column)  # For black pawns in row 7
            if isinstance(pawn, Pawn) and pawn.get_color() == "BLACK":
                self.promote_pawn(7, column)

    def promote_pawn(self, row, column):
        """
        Promote a pawn that has reached the end of the board.
        
        Args:
            row (int): The row of the pawn.
            column (int): The column of the pawn.
        """
        piece_color = self.board.get_piece(row, column).get_color()
        promotion_choice = input("Choose a piece to promote your pawn (Q for Queen, R for Rook, B for Bishop, N for Knight): ").strip().upper()

        new_piece = None
        if promotion_choice == "Q":
            new_piece = Queen(row, column, piece_color)  
        elif promotion_choice == "R":
            new_piece = Rook(row, column, piece_color)  
        elif promotion_choice == "B":
            new_piece = Bishop(row, column, piece_color)  
        elif promotion_choice == "N":
            new_piece = Knight(row, column, piece_color) 

        if new_piece:
            self.board.set_piece(row, column, new_piece)
            print(f"Pawn promoted to {new_piece.__class__.__name__}.")
        else:
            print("Invalid choice. The pawn will remain as it is.")

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
    game.save_game("mi_partida.json")  # Guarda la partida
    game.load_game("mi_partida.json")  # Carga la partida

 
 
 
