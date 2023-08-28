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
        gui.display_valid_moves(game_state.current_player, board, game_state)
        current_player = game_state.get_current_player()
        current_player.get_valid_moves()
            # Display the current game state on the GUI
        gui.display_game_state(game_state)
        gui.get_input(current_player)

                # Check if the move is valid
        if game_state.is_valid_move(current_player, gui.input):
                    # Update game state based on the move
            game_state.update_game_state(gui.input)
        else:
            print('Oopsie Whoopsie, we have done a fucky wucky! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧')
            # Switch turns for the next iteration
        game_state.switch_turns()
        gui.draw_board(board, game_state)
        if turns == 3:
            break
            
    return


        # Game over: Determine and display the winner
    winner = game_state.get_winner()
    gui.display_winner(winner)

        #kriege input von gui spieler 2 """

if __name__ == "__main__":
    main()




