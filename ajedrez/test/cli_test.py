import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unittest.mock import patch
from chess import Chess
from cli import play


class TestCli(unittest.TestCase):
    def _setup_patches(self, input_side_effect):
        with patch('builtins.input', side_effect=input_side_effect) as mock_input, \
             patch('builtins.print') as mock_print, \
             patch.object(Chess, 'move') as mock_chess_move:
            yield mock_input, mock_print, mock_chess_move

    def _run_test(self, input_side_effect, input_calls, print_calls, move_calls):
        with self._setup_patches(input_side_effect) as (mock_input, mock_print, mock_chess_move):
            chess = Chess()
            play(chess)
            self.assertEqual(mock_input.call_count, input_calls)
            self.assertEqual(mock_print.call_count, print_calls)
            self.assertEqual(mock_chess_move.call_count, move_calls)

    def test_happy_path(self):
        self._run_test(['1', '1', '2', '2'], 4, 2, 1)

    def test_not_happy_path(self):
        self._run_test(['hola', '1', '2', '2'], 1, 3, 0)

    def test_more_not_happy_path(self):
        self._run_test(['1', '1', '2', 'hola'], 4, 3, 0)

    # @patch(  # este patch controla lo que hace el input
    #     'builtins.input',
    #     side_effect=['1', '1', '2', '1'], # estos son los valores que simula lo que ingresaria el usuario
    # )
    # @patch('builtins.print') # este patch controla lo que hace el print
    # @patch.object(
    #     Chess,
    #     'move',
    #     side_effect=InvalidMove(),
    # )
    # def test_invalid_move(
    #     self,
    #     mock_chess_move,
    #     mock_print,
    #     mock_input,
    # ): #
    #     chess = Chess()
    #     play(chess)
    #     self.assertEqual(mock_input.call_count, 4)
    #     self.assertEqual(mock_print.call_count, 2)
    #     self.assertEqual(mock_chess_move.call_count, 1)