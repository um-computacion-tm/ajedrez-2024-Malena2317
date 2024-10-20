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
        self.chess_game = Chess()  
        print("Chess game initialized.")

    def initiate(self):
        """
        Start the command-line interface and handle game flow.
        """
        print("Starting the command line interface...")
        while not self.chess_game.game_over:
            print(f"Turn for {self.chess_game.current_turn}.")
            self.chess_game.play_turn()  
            print("Turn completed.")

def main():
    """
    Main function to start the command line interface for the chess game.
    """
    cli = CommandLineInterface()  
    cli.initiate() 

if __name__ == '__main__':
    main()  
