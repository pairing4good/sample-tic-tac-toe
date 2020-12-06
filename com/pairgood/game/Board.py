from com.pairgood.game.Console import Console
from com.pairgood.game.player.Computer import Computer
from com.pairgood.game.player.Human import Human


class Board:
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    console: Console

    def __init__(self, console):
        self.console = console

    def render(self, c_choice, h_choice):
        """
        Print the board on console
        :param h_choice:
        :param c_choice:
        :param state: current state of the board
        """

        chars = {
            -1: h_choice,
            +1: c_choice,
            0: ' '
        }
        self.console.display_line()
        for row in self.board:
            for cell in row:
                symbol = chars[cell]
                self.console.display_square_with(symbol)
            self.console.display_line()

    def empty_cells(self):
        """
        Each empty cell will be added into cells' list
        :param state: the state of the current board
        :return: a list of empty cells
        """
        cells = []

        for x, row in enumerate(self.board):
            for y, cell in enumerate(row):
                if cell == 0:
                    cells.append([x, y])

        return cells

    def game_over(self):
        """
        This function test if the human or computer wins
        :param state: the state of the current board
        :return: True if the human or computer wins
        """
        return self.wins(Human.HUMAN) or self.wins(Computer.COMP)

    def set_move(self, x, y, player):
        """
        Set the move on board, if the coordinates are valid
        :param x: X coordinate
        :param y: Y coordinate
        :param player: the current player
        """
        if self.valid_move(x, y):
            self.board[x][y] = player
            return True
        else:
            return False

    def wins(self, player):
        """
        This function tests if a specific player wins. Possibilities:
        * Three rows    [X X X] or [O O O]
        * Three cols    [X X X] or [O O O]
        * Two diagonals [X X X] or [O O O]
        :param state: the state of the current board
        :param player: a human or a computer
        :return: True if the player wins
        """
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
        """
        A move is valid if the chosen cell is empty
        :param x: X coordinate
        :param y: Y coordinate
        :return: True if the board[x][y] is empty
        """
        if [x, y] in self.empty_cells():
            return True
        else:
            return False

    def get_board(self):
        return self.board

    def place_piece(self, x, y, player):
        self.board[x][y] = player
