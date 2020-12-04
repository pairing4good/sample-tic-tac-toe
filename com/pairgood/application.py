from com.pairgood.game.TicTacToe import TicTacToe
from com.pairgood.wrapper.BuiltInsWrapper import BuiltInsWrapper


def main():
    tic_tac_toe = TicTacToe(BuiltInsWrapper())
    tic_tac_toe.clean()

    h_choice = tic_tac_toe.select_human_piece()
    c_choice = tic_tac_toe.select_computer_piece(h_choice)
    first = tic_tac_toe.select_player_order()

    tic_tac_toe.play_game(c_choice, first, h_choice)

    tic_tac_toe.display_game_over_message(c_choice, h_choice)

    exit()


if __name__ == '__main__':
    main()
