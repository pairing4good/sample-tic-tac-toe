from com.pairgood.game.Game import Game
from com.pairgood.game.TicTacToe import TicTacToe
from com.pairgood.wrapper.BuiltInsWrapper import BuiltInsWrapper


def main():
    game = Game(TicTacToe(BuiltInsWrapper()))
    game.play()
    exit()


if __name__ == '__main__':
    main()
