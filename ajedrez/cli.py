from chess import Chess


class CommandLineInterface:
    def __init__(self):
        # Initialize the chess game instance.
        self.chess_game = Chess()

    def initiate(self):
        # Run the game until the game is declared finished.        
        while not self.chess_game.game_over:
            # Call `play_turn` to have the current player make his move.
            # `play_turn` should control when the game ends and change turns.
            self.chess_game.play_turn()

            # No need to check the return value of `play_turn` here,
            # since the loop depends directly on `self.chess_game.game_over`
            
def main():
    # Start the command line interface for the chess game.
    cli = CommandLineInterface()
    cli.initiate()

if __name__ == '__main__':
    main()
