import unittest
import os

from com.pairgood.game.Console import Console
from com.pairgood.game.Game import Game
from com.pairgood.game.TicTacToe import TicTacToe


class GameAcceptanceTest(unittest.TestCase):
    def test_full_game(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(dir_path + '/test-output.txt', 'r') as file:
            expected = file.read()

        stub_built_ins_wrapper = StubBuiltInsWrapper(['bad', 'X', 'wrong', 'y', 'not a number', 5, 7, 2, 9, 6])
        game = Game(TicTacToe(Console(stub_built_ins_wrapper)))

        game.play()

        self.assertEqual(expected, stub_built_ins_wrapper.actual_console())


if __name__ == '__main__':
    unittest.main()


class StubBuiltInsWrapper:
    console = ''
    recorded_inputs = []

    def __init__(self, recorded_inputs):
        self.recorded_inputs = recorded_inputs

    def wrapped_print(self, value):
        self.console += (value + '\n')

    def wrapped_print_no_return(self, value):
        self.console += value

    def wrapped_input(self, value):
        out = self.recorded_inputs.pop(0)
        self.console += (value + str(out) + '\n')
        return out

    def wrapped_exit(self):
        return

    def actual_console(self):
        return self.console
