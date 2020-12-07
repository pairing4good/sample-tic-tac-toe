import unittest
import os

from com.pairgood.game.Board import Board
from com.pairgood.game.Console import Console
from com.pairgood.game.Game import Game
from com.pairgood.game.TicTacToe import TicTacToe
from com.pairgood.game.player.Computer import Computer
from com.pairgood.game.player.Human import Human
from test.stub.StubBuiltInsWrapper import StubBuiltInsWrapper
from test.stub.StubChoiceWrapper import StubChoiceWrapper
from test.stub.StubTimeWrapper import StubTimeWrapper


class GameAcceptanceTest(unittest.TestCase):
    def test_full_game_that_ends_in_a_draw(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(dir_path + '/output/test-draw-output.txt', 'r') as file:
            expected = file.read()

        stub_built_ins_wrapper = StubBuiltInsWrapper(['bad', 'X', 'wrong', 'y', 'not a number', 5, 7, 2, 9, 6])
        stub_choice_wrapper = StubChoiceWrapper([])
        console = Console(stub_built_ins_wrapper)
        game = Game(TicTacToe(console, Board(console), Human(), Computer(), stub_built_ins_wrapper, stub_choice_wrapper,
                              StubTimeWrapper()))

        game.play()

        self.assertEqual(expected, stub_built_ins_wrapper.actual_console())

    def test_full_game_that_ends_in_a_loss(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(dir_path + '/output/test-loss-output.txt', 'r') as file:
            expected = file.read()

        stub_built_ins_wrapper = StubBuiltInsWrapper(['O', 'n', 9, 8, 7])
        stub_choice_wrapper = StubChoiceWrapper([0, 0])
        console = Console(stub_built_ins_wrapper)
        game = Game(TicTacToe(console, Board(console), Human(), Computer(), stub_built_ins_wrapper, stub_choice_wrapper,
                              StubTimeWrapper()))

        game.play()

        self.assertEqual(expected, stub_built_ins_wrapper.actual_console())

    def test_full_game_that_ends_in_a_win(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(dir_path + '/output/test-win-output.txt', 'r') as file:
            expected = file.read()

        stub_built_ins_wrapper = StubBuiltInsWrapper(['X', 'n', 4])
        stub_choice_wrapper = StubChoiceWrapper([])
        console = Console(stub_built_ins_wrapper)

        board = Board(console)

        comp = Computer.COMP
        human = Human.HUMAN

        board.board = [
        [human, 0, human],
        [0, comp, 0],
        [human, 0, comp],
    ]
        game = Game(TicTacToe(console, board, Human(), Computer(), stub_built_ins_wrapper, stub_choice_wrapper,
                              StubTimeWrapper()))

        game.play()

        self.assertEqual(expected, stub_built_ins_wrapper.actual_console())


if __name__ == '__main__':
    unittest.main()
