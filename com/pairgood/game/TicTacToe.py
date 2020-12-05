from math import inf as infinity
from random import choice
import platform
import time
from os import system

from com.pairgood.game.Console import Console
from com.pairgood.wrapper.BuiltInsWrapper import BuiltInsWrapper


class TicTacToe:

    built_ins_wrapper: BuiltInsWrapper
    console: Console

    def __init__(self, built_ins_wrapper, console):
        self.built_ins_wrapper = built_ins_wrapper
        self.console = console

    HUMAN = -1
    COMP = +1
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    def display_game_over_message(self, c_choice, h_choice):

        if self.wins(self.board, self.HUMAN):
            self.clean()
            self.console.display_human_turn(h_choice)
            self.render(self.board, c_choice, h_choice)
            self.built_ins_wrapper.wrapped_print('YOU WIN!')
        elif self.wins(self.board, self.COMP):
            self.clean()
            self.console.display_computer_turn(c_choice)
            self.render(self.board, c_choice, h_choice)
            self.built_ins_wrapper.wrapped_print('YOU LOSE!')
        else:
            self.clean()
            self.render(self.board, c_choice, h_choice)
            self.built_ins_wrapper.wrapped_print('DRAW!')

    def select_player_order(self):
        first = ''
        self.clean()
        while first != 'Y' and first != 'N':
            try:
                first = self.built_ins_wrapper.wrapped_input('First to start?[y/n]: ').upper()
            except (EOFError, KeyboardInterrupt):
                self.built_ins_wrapper.wrapped_print('Bye')
                self.built_ins_wrapper.wrapped_exit()
            except (KeyError, ValueError):
                self.built_ins_wrapper.wrapped_print('Bad choice')
        return first

    def select_human_piece(self):
        h_choice = ''
        while h_choice != 'O' and h_choice != 'X':
            try:
                self.built_ins_wrapper.wrapped_print('')
                h_choice = self.built_ins_wrapper.wrapped_input('Choose X or O\nChosen: ').upper()
            except (EOFError, KeyboardInterrupt):
                self.built_ins_wrapper.wrapped_print('Bye')
                self.built_ins_wrapper.wrapped_exit()
            except (KeyError, ValueError):
                self.built_ins_wrapper.wrapped_print('Bad choice')
        return h_choice

    def render(self, state, c_choice, h_choice):
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
        str_line = '---------------'

        self.built_ins_wrapper.wrapped_print('\n' + str_line)
        for row in state:
            for cell in row:
                symbol = chars[cell]
                self.built_ins_wrapper.wrapped_print_no_return(f'| {symbol} |')
            self.built_ins_wrapper.wrapped_print('\n' + str_line)

    def human_turn(self, c_choice, h_choice):
        """
        The Human plays choosing a valid move.
        :param c_choice: computer's choice X or O
        :param h_choice: human's choice X or O
        :return:
        """
        depth = len(self.empty_cells(self.board))
        if depth == 0 or self.game_over(self.board):
            return

        # Dictionary of valid moves
        move = -1
        moves = {
            1: [0, 0], 2: [0, 1], 3: [0, 2],
            4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1], 9: [2, 2],
        }

        self.clean()
        self.console.display_human_turn(h_choice)
        self.render(self.board, c_choice, h_choice)

        while move < 1 or move > 9:
            try:
                move = int(self.built_ins_wrapper.wrapped_input('Use numpad (1..9): '))
                coord = moves[move]
                can_move = self.set_move(coord[0], coord[1], self.HUMAN)

                if not can_move:
                    self.built_ins_wrapper.wrapped_print('Bad move')
                    move = -1
            except (EOFError, KeyboardInterrupt):
                self.built_ins_wrapper.wrapped_print('Bye')
                self.built_ins_wrapper.wrapped_exit()
            except (KeyError, ValueError):
                self.built_ins_wrapper.wrapped_print('Bad choice')

    def play_game(self, c_choice, first, h_choice):
        while len(self.empty_cells(self.board)) > 0 and not self.game_over(self.board):
            if first == 'N':
                self.ai_turn(c_choice, h_choice)
                first = ''

            self.human_turn(c_choice, h_choice)
            self.ai_turn(c_choice, h_choice)

    def select_computer_piece(self, h_choice):
        if h_choice == 'X':
            c_choice = 'O'
        else:
            c_choice = 'X'
        return c_choice

    def evaluate(self, state):
        """
        Function to heuristic evaluation of state.
        :param state: the state of the current board
        :return: +1 if the computer wins; -1 if the human wins; 0 draw
        """
        if self.wins(state, self.COMP):
            score = +1
        elif self.wins(state, self.HUMAN):
            score = -1
        else:
            score = 0

        return score

    def wins(self, state, player):
        """
        This function tests if a specific player wins. Possibilities:
        * Three rows    [X X X] or [O O O]
        * Three cols    [X X X] or [O O O]
        * Two diagonals [X X X] or [O O O]
        :param state: the state of the current board
        :param player: a human or a computer
        :return: True if the player wins
        """
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

    def game_over(self, state):
        """
        This function test if the human or computer wins
        :param state: the state of the current board
        :return: True if the human or computer wins
        """
        return self.wins(state, self.HUMAN) or self.wins(state, self.COMP)

    def empty_cells(self, state):
        """
        Each empty cell will be added into cells' list
        :param state: the state of the current board
        :return: a list of empty cells
        """
        cells = []

        for x, row in enumerate(state):
            for y, cell in enumerate(row):
                if cell == 0:
                    cells.append([x, y])

        return cells

    def valid_move(self, x, y):
        """
        A move is valid if the chosen cell is empty
        :param x: X coordinate
        :param y: Y coordinate
        :return: True if the board[x][y] is empty
        """
        if [x, y] in self.empty_cells(self.board):
            return True
        else:
            return False

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

    def minimax(self, state, depth, player):
        """
        AI function that choice the best move
        :param state: current state of the board
        :param depth: node index in the tree (0 <= depth <= 9),
        but never nine in this case (see iaturn() function)
        :param player: an human or a computer
        :return: a list with [the best row, best col, best score]
        """
        if player == self.COMP:
            best = [-1, -1, -infinity]
        else:
            best = [-1, -1, +infinity]

        if depth == 0 or self.game_over(state):
            score = self.evaluate(state)
            return [-1, -1, score]

        for cell in self.empty_cells(state):
            x, y = cell[0], cell[1]
            state[x][y] = player
            score = self.minimax(state, depth - 1, -player)
            state[x][y] = 0
            score[0], score[1] = x, y

            if player == self.COMP:
                if score[2] > best[2]:
                    best = score  # max value
            else:
                if score[2] < best[2]:
                    best = score  # min value

        return best

    def clean(self):
        """
        Clears the console
        """
        os_name = platform.system().lower()
        if 'windows' in os_name:
            system('cls')
        else:
            system('clear')

    def ai_turn(self, c_choice, h_choice):
        """
        It calls the minimax function if the depth < 9,
        else it choices a random coordinate.
        :param c_choice: computer's choice X or O
        :param h_choice: human's choice X or O
        :return:
        """
        depth = len(self.empty_cells(self.board))
        if depth == 0 or self.game_over(self.board):
            return

        self.clean()
        self.console.display_computer_turn(c_choice)
        self.render(self.board, c_choice, h_choice)

        if depth == 9:
            x = choice([0, 1, 2])
            y = choice([0, 1, 2])
        else:
            move = self.minimax(self.board, depth, self.COMP)
            x, y = move[0], move[1]

        self.set_move(x, y, self.COMP)
        time.sleep(1)
