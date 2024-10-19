import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unittest.mock import patch, MagicMock
from chess import Chess
from cli import CommandLineInterface


@patch('builtins.input', side_effect=['D2', 'D4'])  # Simulating moves
@patch('builtins.print')  # To capture print statements
@patch('cli.Chess')
class TestCommandLineInterface(unittest.TestCase):

    def setUp(self, mock_chess, mock_print, mock_input):
        """Common setup for all test cases."""
        self.mock_chess = mock_chess
        self.mock_print = mock_print
        self.mock_input = mock_input

        # Common setup for the chess game instance
        self.mock_chess_instance = self.mock_chess.return_value
        self.mock_chess_instance.game_over = False

        self.cli = CommandLineInterface()
        self.cli.chess_game = self.mock_chess_instance

    def setUp_play_turn(self, move_result, expected_print):
        """Helper method to test play_turn with different outcomes."""
        self.mock_chess_instance.attempt_move = MagicMock(return_value=move_result)

        # Run the CLI method that initiates the game.
        self.cli.initiate()

        # Assert that attempt_move was called once.
        self.mock_chess_instance.attempt_move.assert_called_once()

        # Assert the expected print statement was executed.
        self.mock_print.assert_any_call(expected_print)

    def test_play_turn_valid_move(self):
        self.setUp_play_turn(
            move_result=True,
            expected_print="Scores: White - 0, Black - 0"  # Adjust according to your score logic
        )

    def test_play_turn_invalid_move(self):
        self.setUp_play_turn(
            move_result=False,
            expected_print="Invalid move. Try again."
        )

if __name__ == '__main__':
    unittest.main()
