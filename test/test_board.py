import unittest

from com.pairgood.game.Board import Board


class TestBoard(unittest.TestCase):
    def test_should_return_all_nine_cells_for_a_default_board(self):
        board = Board(None)

        cells = board.empty_cells()

        self.assertEqual(9, len(cells))
        self.assertEqual([[0, 0], [0, 1], [0, 2],
                          [1, 0], [1, 1], [1, 2],
                          [2, 0], [2, 1], [2, 2]], cells)

    def test_should_return_all_empty_cells_for_a_board_containing_pieces(self):
        board = Board(None)

        board.board = [
            ['X', 0, 0],
            [0, 'O', 0],
            [0, 0, 'X'],
        ]

        cells = board.empty_cells()

        self.assertEqual(6, len(cells))
        self.assertEqual([[0, 1], [0, 2],
                          [1, 0], [1, 2],
                          [2, 0], [2, 1]], cells)

    def test_should_return_no_empty_cells_for_a_full_board(self):
        board = Board(None)

        board.board = [
            ['X', 'X', 'O'],
            ['O', 'O', 'X'],
            ['X', 'X', 'O'],
        ]

        cells = board.empty_cells()

        self.assertEqual(0, len(cells))


if __name__ == '__main__':
    unittest.main()
