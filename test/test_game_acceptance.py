import unittest
import os

from com.pairgood.game.Board import Board
from com.pairgood.game.Console import Console
from com.pairgood.game.Game import Game
from com.pairgood.game.TicTacToe import TicTacToe
from com.pairgood.game.player.Human import Human
from test.StubBuiltInsWrapper import StubBuiltInsWrapper
from test.StubChoiceWrapper import StubChoiceWrapper


class GameAcceptanceTest(unittest.TestCase):
    def test_full_game(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(dir_path + '/test-output.txt', 'r') as file:
            expected = file.read()

        stub_built_ins_wrapper = StubBuiltInsWrapper(['bad', 'X', 'wrong', 'y', 'not a number', 5, 7, 2, 9, 6])
        stub_choice_wrapper = StubChoiceWrapper([])
        console = Console(stub_built_ins_wrapper)
        game = Game(TicTacToe(console, Board(console), Human(), stub_built_ins_wrapper, stub_choice_wrapper))

        game.play()

        self.assertEqual(expected, stub_built_ins_wrapper.actual_console())


if __name__ == '__main__':
    unittest.main()
