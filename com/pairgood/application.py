from com.pairgood.game.ticTacToe import clean, select_human_piece, select_computer_piece, select_player_order, play_game, \
    display_game_over_message


def main():
    clean()

    h_choice = select_human_piece()
    c_choice = select_computer_piece(h_choice)
    first = select_player_order()

    play_game(c_choice, first, h_choice)

    display_game_over_message(c_choice, h_choice)

    exit()


if __name__ == '__main__':
    main()
