import unittest

from com.pairgood.game.Game import Game
from com.pairgood.game.TicTacToe import TicTacToe


class MyTestCase(unittest.TestCase):
    def test_something(self):
        expected = """
Human turn [X]

---------------
|   ||   ||   |
---------------
|   ||   ||   |
---------------
|   ||   ||   |
---------------
Computer turn [O]

---------------
|   ||   ||   |
---------------
|   || X ||   |
---------------
|   ||   ||   |
---------------
Human turn [X]

---------------
| O ||   ||   |
---------------
|   || X ||   |
---------------
|   ||   ||   |
---------------
Computer turn [O]

---------------
| O ||   ||   |
---------------
|   || X ||   |
---------------
| X ||   ||   |
---------------
Human turn [X]

---------------
| O ||   || O |
---------------
|   || X ||   |
---------------
| X ||   ||   |
---------------
Computer turn [O]

---------------
| O || X || O |
---------------
|   || X ||   |
---------------
| X ||   ||   |
---------------
Human turn [X]

---------------
| O || X || O |
---------------
|   || X ||   |
---------------
| X || O ||   |
---------------
Computer turn [O]

---------------
| O || X || O |
---------------
|   || X ||   |
---------------
| X || O || X |
---------------
Human turn [X]

---------------
| O || X || O |
---------------
| O || X ||   |
---------------
| X || O || X |
---------------

---------------
| O || X || O |
---------------
| O || X || X |
---------------
| X || O || X |
---------------
DRAW!
"""
        stub_built_ins_wrapper = StubBuiltInsWrapper()
        game = Game(TicTacToe(stub_built_ins_wrapper))

        game.play()

        self.assertEqual(expected, stub_built_ins_wrapper.actual_console())


if __name__ == '__main__':
    unittest.main()


class StubBuiltInsWrapper:
    prints = ''
    recorded_inputs = ['X', 'y', 5, 7, 2, 9, 6]

    def wrapped_print(self, value):
        self.prints += (value + '\n')

    def wrapped_print_no_return(self, value):
        self.prints += value

    def wrapped_input(self, value):
        return self.recorded_inputs.pop(0)

    def wrapped_exit(self):
        return

    def actual_console(self):
        return self.prints

