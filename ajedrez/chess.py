from  tablero.board import Board
from  piezas.bishop import Alfil
from  piezas.caballo import Knight
from  piezas.pawn import Pawn
from  piezas.reina import Queen
from  piezas.rey import King
from  piezas.rook import Rook 

class Chess:
    def __init__(self):
        # Initialize the board and set the turn to white.
        self.board = Board()  # Board representation
        self.current_turn = "WHITE"  # White always starts
        self.game_over = False  # Flag to indicate if the game is over
        self.move_history = []  # Store the move history
    
    def start_game(self):
        print("Welcome to Chess! The game begins.")
        self.board.print_board()  # Mostrar el tablero inicial
        while not self.game_over:
            self.play_turn()
    
    def play_turn(self):
        # Check if the game is over before asking for the next move.
        if self.game_over:
            print("The game is over. Thanks for playing!")
            return

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
    

  
