from com.pairgood.game.Console import Console
from com.pairgood.game.Game import Game
from com.pairgood.game.TicTacToe import TicTacToe
from com.pairgood.wrapper.BuiltInsWrapper import BuiltInsWrapper


def main():
    wrapper = BuiltInsWrapper()
    game = Game(TicTacToe(wrapper, Console(wrapper)))
    game.play()
    exit()


if __name__ == '__main__':
    main()
