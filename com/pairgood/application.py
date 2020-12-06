from com.pairgood.game.Board import Board
from com.pairgood.game.Console import Console
from com.pairgood.game.Game import Game
from com.pairgood.game.TicTacToe import TicTacToe
from com.pairgood.game.player.Human import Human
from com.pairgood.wrapper.BuiltInsWrapper import BuiltInsWrapper


def main():
    wrapper = BuiltInsWrapper()
    console = Console(wrapper)
    game = Game(TicTacToe(console, Board(console), Human(), wrapper))
    game.play()
    exit()


if __name__ == '__main__':
    main()
