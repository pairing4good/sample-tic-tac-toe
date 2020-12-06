from com.pairgood.game.TicTacToe import TicTacToe


class Game:
    tic_tac_toe: TicTacToe

    def __init__(self, tic_tac_toe):
        self.tic_tac_toe = tic_tac_toe

    def play(self):
        self.tic_tac_toe.select_human_piece()
        self.tic_tac_toe.select_computer_piece()
        first = self.tic_tac_toe.select_player_order()

        self.tic_tac_toe.play_game(first)

        self.tic_tac_toe.display_game_over_message()
