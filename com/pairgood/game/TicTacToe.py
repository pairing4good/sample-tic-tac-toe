from math import inf as infinity
import time

from com.pairgood.game.Board import Board
from com.pairgood.game.Console import Console
from com.pairgood.game.player.Computer import Computer
from com.pairgood.game.player.Human import Human
from com.pairgood.wrapper.BuiltInsWrapper import BuiltInsWrapper
from com.pairgood.wrapper.choice_wrapper import ChoiceWrapper


class TicTacToe:
    console: Console
    board: Board
    human: Human
    built_ins_wrapper: BuiltInsWrapper
    choice_wrapper: ChoiceWrapper

    def __init__(self, console, board, human, built_ins_wrapper, choice_wrapper):
        self.console = console
        self.board = board
        self.human = human
        self.built_ins_wrapper = built_ins_wrapper
        self.choice_wrapper = choice_wrapper

    def play_game(self, c_choice, first, h_choice):
        while len(self.board.empty_cells()) > 0 and not self.board.game_over():
            if first == 'N':
                self.ai_turn(c_choice, h_choice)
                first = ''

            self.human_turn(c_choice, h_choice)
            self.ai_turn(c_choice, h_choice)

    def display_game_over_message(self, c_choice, h_choice):

        if self.board.wins(Human.HUMAN):
            self.console.display_human_turn(h_choice)
            self.board.render(c_choice, h_choice)
            self.console.display_win()
        elif self.board.wins(Computer.COMP):
            self.console.display_computer_turn(c_choice)
            self.board.render(c_choice, h_choice)
            self.console.display_lose()
        else:
            self.console.display_board(self.board.get_board(), c_choice, h_choice)
            self.console.display_draw()

    def select_player_order(self):
        first = ''
        while first != 'Y' and first != 'N':
            try:
                first = self.console.request_player_order()
            except (EOFError, KeyboardInterrupt):
                self.console.display_bye()
                self.built_ins_wrapper.wrapped_exit()
            except (KeyError, ValueError):
                self.console.display_bad_choice()
        return first

    def select_human_piece(self):
        h_choice = ''
        while h_choice != 'O' and h_choice != 'X':
            try:
                self.console.display_empty_line()
                h_choice = self.console.request_player_piece()
            except (EOFError, KeyboardInterrupt):
                self.console.display_bye()
                self.built_ins_wrapper.wrapped_exit()
            except (KeyError, ValueError):
                self.console.display_bad_choice()
        return h_choice

    def select_computer_piece(self, h_choice):
        if h_choice == 'X':
            c_choice = 'O'
        else:
            c_choice = 'X'
        return c_choice

    def ai_turn(self, c_choice, h_choice):
        """
        It calls the minimax function if the depth < 9,
        else it choices a random coordinate.
        :param c_choice: computer's choice X or O
        :param h_choice: human's choice X or O
        :return:
        """
        depth = len(self.board.empty_cells())
        if depth == 0 or self.board.game_over():
            return

        self.console.display_computer_turn(c_choice)
        self.console.display_board(self.board.get_board(), c_choice, h_choice)

        if depth == 9:
            x = self.choice_wrapper.choice([0, 1, 2])
            y = self.choice_wrapper.choice([0, 1, 2])
        else:
            move = self.minimax(depth, Computer.COMP)
            x, y = move[0], move[1]

        self.board.set_move(x, y, Computer.COMP)
        time.sleep(1)

    def evaluate(self):
        """
        Function to heuristic evaluation of state.
        :param state: the state of the current board
        :return: +1 if the computer wins; -1 if the human wins; 0 draw
        """
        if self.board.wins(Computer.COMP):
            score = +1
        elif self.board.wins(Human.HUMAN):
            score = -1
        else:
            score = 0

        return score

    def minimax(self, depth, player):
        """
        AI function that choice the best move
        :param state: current state of the board
        :param depth: node index in the tree (0 <= depth <= 9),
        but never nine in this case (see iaturn() function)
        :param player: an human or a computer
        :return: a list with [the best row, best col, best score]
        """
        if player == Computer.COMP:
            best = [-1, -1, -infinity]
        else:
            best = [-1, -1, +infinity]

        if depth == 0 or self.board.game_over():
            score = self.evaluate()
            return [-1, -1, score]

        for cell in self.board.empty_cells():
            x, y = cell[0], cell[1]
            self.board.place_piece(x, y, player)
            score = self.minimax(depth - 1, -player)
            self.board.place_piece(x, y, 0)
            score[0], score[1] = x, y

            if player == Computer.COMP:
                if score[2] > best[2]:
                    best = score  # max value
            else:
                if score[2] < best[2]:
                    best = score  # min value

        return best

    def human_turn(self, c_choice, h_choice):
        """
        The Human plays choosing a valid move.
        :param c_choice: computer's choice X or O
        :param h_choice: human's choice X or O
        :return:
        """
        depth = len(self.board.empty_cells())
        if depth == 0 or self.board.game_over():
            return

        # Dictionary of valid moves
        move = -1
        moves = {
            1: [0, 0], 2: [0, 1], 3: [0, 2],
            4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1], 9: [2, 2],
        }

        self.console.display_human_turn(h_choice)
        self.console.display_board(self.board.get_board(), c_choice, h_choice)

        while move < 1 or move > 9:
            try:
                move = self.console.request_move()
                coord = moves[move]
                can_move = self.board.set_move(coord[0], coord[1], Human.HUMAN)

                if not can_move:
                    self.console.display_bad_move()
                    move = -1
            except (EOFError, KeyboardInterrupt):
                self.console.display_bye()
                self.built_ins_wrapper.wrapped_exit()
            except (KeyError, ValueError):
                self.console.display_bad_choice()
