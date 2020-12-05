import unittest
import os

from com.pairgood.game.Console import Console
from com.pairgood.game.Game import Game
from com.pairgood.game.TicTacToe import TicTacToe
from test.StubBuiltInsWrapper import StubBuiltInsWrapper


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
