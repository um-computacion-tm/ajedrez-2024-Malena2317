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

    def setUp(self, mock_chess, mock_print, mock_input):
        """
        Common setup for all test cases. It initializes the mock objects and the CLI instance.
        """
        self.mock_chess = mock_chess
        self.mock_print = mock_print
        self.mock_input = mock_input

        # Set up a mock instance of the Chess game
        self.mock_chess_instance = self.mock_chess.return_value
        self.mock_chess_instance.game_over = False

        # Create an instance of CommandLineInterface using the mocked Chess instance
        self.cli = CommandLineInterface()
        self.cli.chess_game = self.mock_chess_instance

    def setUp_play_turn(self, move_result, expected_print):
        """
        Helper method to test the `play_turn` method of the CommandLineInterface with different outcomes.
        """
        # Mock the `attempt_move` method to return the specified move_result
        self.mock_chess_instance.attempt_move = MagicMock(return_value=move_result)

        # Run the `initiate` method to simulate game play
        self.cli.initiate()

        # Verify that `attempt_move` was called once during the turn
        self.mock_chess_instance.attempt_move.assert_called_once()

        # Check that the expected message was printed to the console
        self.mock_print.assert_any_call(expected_print)

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