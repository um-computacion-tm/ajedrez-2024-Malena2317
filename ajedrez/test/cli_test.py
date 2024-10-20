import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unittest.mock import MagicMock
from unittest.mock import patch
from chess import Chess
from cli import CommandLineInterface


@patch('builtins.input', side_effect=['D2', 'D4'])  # Simulate user input for moves
@patch('builtins.print')  # Mock the print function to capture output
@patch('cli.Chess')  # Mock the Chess class to control its behavior
class TestCommandLineInterface(unittest.TestCase):
    """
    Unit test class for testing the Command Line Interface of the chess game.

    This class uses mocks to simulate user input and the Chess game instance, allowing for testing
    of various scenarios without requiring actual user interaction or a running chess game.
    """

    def setUp(self, mock_chess, mock_print, mock_input):
        """
        Common setup for all test cases. It initializes the mock objects and the CLI instance.
        
        Args:
            mock_chess (MagicMock): Mocked Chess class instance.
            mock_print (MagicMock): Mocked print function to capture output.
            mock_input (MagicMock): Mocked input function to simulate user input.

        Common setup for all test cases. It initializes the mock objects and the CLI instance. 

        """
        self.mock_chess = mock_chess
        self.mock_print = mock_print
        self.mock_input = mock_input

        # Common setup for the chess game instance
        self.mock_chess_instance = self.mock_chess.return_value
        self.mock_chess_instance.game_over = False

        # Set up a mock instance of the Chess game
        self.mock_chess_instance = self.mock_chess.return_value
        self.mock_chess_instance.game_over = False

        # Create an instance of CommandLineInterface using the mocked Chess instance
        self.cli = CommandLineInterface()
        self.cli.chess_game = self.mock_chess_instance

    def setUp_play_turn(self, move_result, expected_print):
        """
        Helper method to test play_turn with different outcomes.
        
        Args:
            move_result (bool): The result of the move attempt (True for success, False for failure).
            expected_print (str): The expected output to be printed based on the move result.
        """
        self.mock_chess_instance.attempt_move = MagicMock(return_value=move_result)

        # Run the CLI method that initiates the game.
        self.cli.initiate()

        # Assert that attempt_move was called once.
        self.mock_chess_instance.attempt_move.assert_called_once()

        # Assert the expected print statement was executed.
        self.mock_print.assert_any_call(expected_print)

    def test_play_turn_valid_move(self):
        """
        Test case for a valid move scenario.
        """
        self.setUp_play_turn(
            move_result=True,
            expected_print="Scores: White - 0, Black - 0"  # Adjust according to your score logic
        )

    def test_play_turn_valid_move(self):
        """
        Test case for a valid move scenario.
        """
        self.setUp_play_turn(
            move_result=True,
            expected_print="Scores: White - 0, Black - 0"  # Adjust the message to match your game logic
        )

    def test_play_turn_invalid_move(self):
        """
        Test case for an invalid move scenario.
        """
        self.setUp_play_turn(
            move_result=False,
            expected_print="Invalid move. Try again."
        )

if __name__ == '__main__':
    unittest.main()

