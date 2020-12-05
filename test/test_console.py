import unittest

from com.pairgood.game.Console import Console
from test.StubBuiltInsWrapper import StubBuiltInsWrapper


class ConsoleTest(unittest.TestCase):

    console: Console
    wrapper: StubBuiltInsWrapper

    def setUp(self):
        self.wrapper = StubBuiltInsWrapper([1])
        self.console = Console(self.wrapper)

    def test_should_display_bad_choice(self):
        self.assertEqual('', self.wrapper.actual_console())

        self.console.display_bad_choice()

        self.assertEqual('Bad choice\n', self.wrapper.actual_console())

    def test_should_display_bad_move(self):
        self.assertEqual('', self.wrapper.actual_console())

        self.console.display_bad_move()

        self.assertEqual('Bad move\n', self.wrapper.actual_console())

    def test_should_display_bye(self):
        self.assertEqual('', self.wrapper.actual_console())

        self.console.display_bye()

        self.assertEqual('Bye\n', self.wrapper.actual_console())

    def test_should_display_computer_turn(self):
        self.assertEqual('', self.wrapper.actual_console())

        self.console.display_computer_turn('test')

        self.assertEqual('Computer turn [test]\n', self.wrapper.actual_console())

    def test_should_display_draw(self):
        self.assertEqual('', self.wrapper.actual_console())

        self.console.display_draw()

        self.assertEqual('DRAW!\n', self.wrapper.actual_console())

    def test_should_display_empty_line(self):
        self.assertEqual('', self.wrapper.actual_console())

        self.console.display_empty_line()

        self.assertEqual('\n', self.wrapper.actual_console())

    def test_should_display_human_turn(self):
        self.assertEqual('', self.wrapper.actual_console())

        self.console.display_human_turn('test')

        self.assertEqual('Human turn [test]\n', self.wrapper.actual_console())

    def test_should_display_line(self):
        self.assertEqual('', self.wrapper.actual_console())

        self.console.display_line()

        self.assertEqual('\n---------------\n', self.wrapper.actual_console())

    def test_should_display_lose(self):
        self.assertEqual('', self.wrapper.actual_console())

        self.console.display_lose()

        self.assertEqual('YOU LOSE!\n', self.wrapper.actual_console())

    def test_should_request_move(self):
        self.wrapper = StubBuiltInsWrapper([1])
        self.console = Console(self.wrapper)
        self.assertEqual('', self.wrapper.actual_console())

        output = self.console.request_move()

        self.assertEqual(1, output)
        self.assertEqual('Use numpad (1..9): 1\n', self.wrapper.actual_console())

    def test_should_player_order_when_lower_case_letter_provided(self):
        self.wrapper = StubBuiltInsWrapper(['y'])
        self.console = Console(self.wrapper)
        self.assertEqual('', self.wrapper.actual_console())

        output = self.console.request_player_order()

        self.assertEqual('Y', output)
        self.assertEqual('First to start?[y/n]: y\n', self.wrapper.actual_console())

    def test_should_player_order_when_upper_case_letter_provided(self):
        self.wrapper = StubBuiltInsWrapper(['Y'])
        self.console = Console(self.wrapper)
        self.assertEqual('', self.wrapper.actual_console())

        output = self.console.request_player_order()

        self.assertEqual('Y', output)
        self.assertEqual('First to start?[y/n]: Y\n', self.wrapper.actual_console())

    def test_should_player_piece_when_lower_case_letter_provided(self):
        self.wrapper = StubBuiltInsWrapper(['x'])
        self.console = Console(self.wrapper)
        self.assertEqual('', self.wrapper.actual_console())

        output = self.console.request_player_piece()

        self.assertEqual('X', output)
        self.assertEqual('Choose X or O\nChosen: x\n', self.wrapper.actual_console())

    def test_should_player_piece_when_upper_case_letter_provided(self):
        self.wrapper = StubBuiltInsWrapper(['X'])
        self.console = Console(self.wrapper)
        self.assertEqual('', self.wrapper.actual_console())

        output = self.console.request_player_piece()

        self.assertEqual('X', output)
        self.assertEqual('Choose X or O\nChosen: X\n', self.wrapper.actual_console())

    def test_should_display_square_with(self):
        self.assertEqual('', self.wrapper.actual_console())

        self.console.display_square_with('X')

        self.assertEqual('| X |', self.wrapper.actual_console())

    def test_should_display_win(self):
        self.assertEqual('', self.wrapper.actual_console())

        self.console.display_win()

        self.assertEqual('YOU WIN!\n', self.wrapper.actual_console())


if __name__ == '__main__':
    unittest.main()
