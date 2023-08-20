from ui.gui import GUI
from ai.ai import *
from game_logic.board import Board
from game_logic.game_state import *


def main():

    board = Board(width=9, height=9)
    gui = GUI(board)
    """ def play_game(board, game_state, gui):
        #kriege input von gui spieler 1
        #update game_state mit input
        gui.update(game_state)

        #kriege input von gui spieler 2 """

if __name__ == "__main__":
    main()




