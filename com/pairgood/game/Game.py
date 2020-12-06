from com.pairgood.game.TicTacToe import TicTacToe


class Game:
    tic_tac_toe: TicTacToe

    def __init__(self, tic_tac_toe):
        self.tic_tac_toe = tic_tac_toe

    def play(self):
        self.tic_tac_toe.clean()

        h_choice = self.tic_tac_toe.select_human_piece()
        c_choice = self.tic_tac_toe.select_computer_piece(h_choice)
        first = self.tic_tac_toe.select_player_order()

        self.tic_tac_toe.play_game(c_choice, first, h_choice)

        self.tic_tac_toe.display_game_over_message(c_choice, h_choice)
