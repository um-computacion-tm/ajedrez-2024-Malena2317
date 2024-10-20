from chess import Chess

class CommandLineInterface:
    """
    CommandLineInterface class for interacting with the chess game through a command-line interface.
    """

    def __init__(self):
        """
        Initialize the command-line interface and the chess game.
        """
        print("Initializing the chess game...")
        self.chess_game = Chess()  # Creates an instance of the Chess game.
        print("Chess game initialized.")

    def initiate(self):
        """
        Start the command-line interface and handle game flow.
        """
        print("Starting the command line interface...")
        # Loop until the game is over.
        while not self.chess_game.game_over:
            print(f"Turn for {self.chess_game.current_turn}.")
            self.chess_game.play_turn()  # Let the current player play their turn.
            print("Turn completed.")

def main():
    """
    Main function to start the command line interface for the chess game.
    """
    cli = CommandLineInterface()  # Create an instance of the CommandLineInterface.
    cli.initiate()  # Start the command line interface.

if __name__ == '__main__':
    main()  # Run the main function if the script is executed directly.
