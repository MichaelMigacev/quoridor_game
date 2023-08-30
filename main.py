from ui.gui import GUI
from ai.ai import *
from game_logic.board import Board
from game_logic.game_state import *
import time


def main():
    board = Board(width=9, height=9)
    game_state = GameState(board)
    gui = GUI(board, game_state)
    play(board, game_state, gui)
def play(board, game_state, gui):
    turns = 0
    while not game_state.is_game_over():
        turns += 1
        print(f'It is now the turn number: {turns}')
        current_player = game_state.get_current_player()
        current_player.get_valid_moves(board, game_state)

        gui.display_game_state(game_state)
        gui.get_input(current_player)

        while not game_state.is_valid_move(current_player, gui.input):
            print('Oopsie Whoopsie, we have done a fucky wucky! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧')
            print('Please repeat your input.')
            gui.get_input(current_player)
        game_state.update_game_state(gui.input)
            # Switch turns for the next iteration
        if game_state.is_game_over():
            break
        game_state.switch_turns()
        gui.draw_board(board, game_state)
        board.clear_board()
        if game_state.is_game_over():
            break
    
    board.clear_board()
    gui.display_winner(current_player)

        #kriege input von gui spieler 2 """

if __name__ == "__main__":
    main()




