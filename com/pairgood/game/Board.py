from com.pairgood.game.Console import Console
from com.pairgood.game.player.Computer import Computer
from com.pairgood.game.player.Human import Human


class Board:
    board: None
    console: Console

    def __init__(self, console):
        self.console = console
        self.board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    def empty_cells(self):
        cells = []

        for x, row in enumerate(self.board):
            for y, cell in enumerate(row):
                if cell == 0:
                    cells.append([x, y])

        return cells

    def game_over(self):
        return self.wins(Human.HUMAN) or self.wins(Computer.COMP)

    def set_move(self, x, y, player):
        if self.valid_move(x, y):
            self.board[x][y] = player
            return True
        else:
            return False

    def wins(self, player):
        state = self.board

        win_state = [
            [state[0][0], state[0][1], state[0][2]],
            [state[1][0], state[1][1], state[1][2]],
            [state[2][0], state[2][1], state[2][2]],
            [state[0][0], state[1][0], state[2][0]],
            [state[0][1], state[1][1], state[2][1]],
            [state[0][2], state[1][2], state[2][2]],
            [state[0][0], state[1][1], state[2][2]],
            [state[2][0], state[1][1], state[0][2]],
        ]
        if [player, player, player] in win_state:
            return True
        else:
            return False

    def valid_move(self, x, y):
        if [x, y] in self.empty_cells():
            return True
        else:
            return False

    def get_board(self):
        return self.board

    def place_piece(self, x, y, player):
        self.board[x][y] = player
