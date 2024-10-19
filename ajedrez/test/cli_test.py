import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unittest.mock import patch, MagicMock
from chess import Chess
from cli import CommandLineInterface

class TestCommandLineInterface(unittest.TestCase):
    
    @patch('cli.Chess')
    def test_initiate(self, mock_chess):
        # Mock the game over condition
        mock_chess_instance = mock_chess.return_value
        mock_chess_instance.game_over = False
        
        cli = CommandLineInterface()
        cli.chess_game = mock_chess_instance  # Use the mocked chess instance

        # Simulate a turn
        mock_chess_instance.play_turn = MagicMock(side_effect=lambda: setattr(mock_chess_instance, 'game_over', True))

        # Run the CLI
        cli.initiate()

        # Assert that play_turn was called once
        mock_chess_instance.play_turn.assert_called_once()

    @patch('builtins.input', side_effect=['D2', 'D4'])  # Simulating moves
    @patch('builtins.print')  # To capture print statements
    @patch('cli.Chess')
    def test_play_turn_valid_move(self, mock_chess, mock_print, mock_input):
        mock_chess_instance = mock_chess.return_value
        mock_chess_instance.game_over = False
        mock_chess_instance.attempt_move = MagicMock(return_value=True)

        cli = CommandLineInterface()
        cli.chess_game = mock_chess_instance
        
        cli.initiate()

        # Assert that attempt_move was called
        mock_chess_instance.attempt_move.assert_called_once()

        # Check if the appropriate print statements were executed
        mock_print.assert_any_call("Scores: White - 0, Black - 0")  # Change according to your score logic

    @patch('builtins.input', side_effect=['D2', 'D4'])  # Simulating moves
    @patch('builtins.print')  # To capture print statements
    @patch('cli.Chess')
    def test_play_turn_invalid_move(self, mock_chess, mock_print, mock_input):
        mock_chess_instance = mock_chess.return_value
        mock_chess_instance.game_over = False
        mock_chess_instance.attempt_move = MagicMock(return_value=False)

        cli = CommandLineInterface()
        cli.chess_game = mock_chess_instance
        
        cli.initiate()

        # Assert that attempt_move was called
        mock_chess_instance.attempt_move.assert_called_once()

        # Check if the appropriate error message was printed
        mock_print.assert_any_call("Invalid move. Try again.")

if __name__ == '__main__':
    unittest.main()
