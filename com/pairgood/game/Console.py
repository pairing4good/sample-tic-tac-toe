from com.pairgood.game.player.Computer import Computer
from com.pairgood.game.player.Human import Human
from com.pairgood.wrapper.BuiltInsWrapper import BuiltInsWrapper


class Console:
    built_ins_wrapper: BuiltInsWrapper

    def __init__(self, built_ins_wrapper):
        self.built_ins_wrapper = built_ins_wrapper

    def display_bad_choice(self):
        self.built_ins_wrapper.wrapped_print('Bad choice')

    def display_bad_move(self):
        self.built_ins_wrapper.wrapped_print('Bad move')

    def display_bye(self):
        self.built_ins_wrapper.wrapped_print('Bye')

    def display_computer_turn(self, c_choice):
        self.built_ins_wrapper.wrapped_print(f'Computer turn [{c_choice}]')

    def display_draw(self):
        self.built_ins_wrapper.wrapped_print('DRAW!')

    def display_empty_line(self):
        self.built_ins_wrapper.wrapped_print('')

    def display_human_turn(self, h_choice):
        self.built_ins_wrapper.wrapped_print(f'Human turn [{h_choice}]')

    def display_line(self):
        self.built_ins_wrapper.wrapped_print('\n' + '---------------')

    def display_lose(self):
        self.built_ins_wrapper.wrapped_print('YOU LOSE!')

    def display_square_with(self, symbol):
        self.built_ins_wrapper.wrapped_print_no_return(f'| {symbol} |')

    def display_win(self):
        self.built_ins_wrapper.wrapped_print('YOU WIN!')

    def request_move(self):
        return int(self.built_ins_wrapper.wrapped_input('Use numpad (1..9): '))

    def request_player_order(self):
        return self.built_ins_wrapper.wrapped_input('First to start?[y/n]: ').upper()

    def request_player_piece(self):
        return self.built_ins_wrapper.wrapped_input('Choose X or O\nChosen: ').upper()

    def display_board(self, board, c_choice, h_choice):
        chars = {
            Human.HUMAN: h_choice,
            Computer.COMP: c_choice,
            0: ' '
        }
        self.display_line()
        for row in board:
            for cell in row:
                symbol = chars[cell]
                self.display_square_with(symbol)
            self.display_line()

    def display_game_over_message(self, board, human, computer):

        if board.wins(Human.HUMAN):
            self.display_human_turn(human.get_piece())
            self.display_board(board.get_board(), computer.get_piece(), human.get_piece())
            self.display_win()
        elif board.wins(Computer.COMP):
            self.display_computer_turn(computer.get_piece())
            self.display_board(board.get_board(), computer.get_piece(), human.get_piece())
            self.display_lose()
        else:
            self.display_board(board.get_board(), computer.get_piece(), human.get_piece())
            self.display_draw()
