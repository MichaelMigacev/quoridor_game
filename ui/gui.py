import tkinter as tk

class GUI:
    def __init__(self, board, gamestate):
        # Create a new window
        self.root = tk.Tk()
        self.root.geometry('1000x1000')
        # Set the window title
        self.root.title("Quoridor DX")

        # Set the window size
        self.grid_width = 800
        self.grid_height = 800
        self.cell_size = (self.grid_height/9)

        # Create a canvas widget
        self.grid = tk.Frame(self.root, width=self.grid_width, height=self.grid_height, highlightbackground='blue', highlightthickness=2)
        self.grid.pack(pady=50)
        # Draw the game board on the canvas++
        self.draw_board(board, gamestate)
        
        
        #window.mainloop()

    def draw_board(self, board, gamestate):
        for widget in self.grid.winfo_children():
            widget.destroy()
        for i in range(board.width):
            for j in range(board.width):
                cell_widget = tk.Frame(self.grid, width=self.cell_size, height=self.cell_size, borderwidth=3)
                cell_widget.grid(row=i, column=j)
                cell_widget.grid_propagate(False)
                if isinstance(board.cells[i][j], int):
                    button = tk.Button(cell_widget, text=str(board.cells[i][j]))
                    button.grid()
                elif board.cells[i][j] == 'E':
                    image_label = tk.Label(cell_widget, text='E')
                    image_label.grid()
                elif board.cells[i][j] == 'V':
                    button = tk.Button(cell_widget, text='V')
                    button.grid()

    def get_input(self, current):
        self.input = (7, 4)
        return

    def update_gui(self, board, game_state):
        self.draw_board(board, game_state)
        
    def display_game_state(self, game_state):
        print(f'Current Player is: Player {game_state.current_player.handle}')

    def display_valid_moves(self, player, board, gamestate):
        print(f'Valid moves: {player.get_valid_moves()}')
        for length in range(len(player.get_valid_moves())):
            board.cells[player.get_valid_moves()[length][0]][player.get_valid_moves()[length][1]] = 'V'
        self.draw_board(board, gamestate)
        