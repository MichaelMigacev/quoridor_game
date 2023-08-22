import tkinter as tk

class GUI:
    def __init__(self, board, gamestate):
        # Create a new window
        self.window = tk.Tk()
        self.window.geometry('1000x1000')
        # Set the window title
        self.window.title("Quoridor DX")

        # Set the window size
        self.canvas_width = 800
        self.canvas_height = 800
        self.cell_size = self.canvas_height/9

        # Create a canvas widget
        self.canvas = tk.Canvas(self.window, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack(pady=50)
        # Draw the game board on the canvas++
        self.draw_board(self.canvas, board)
        
        
        #window.mainloop()

    def draw_board(self, canvas, board):
        self.canvas.delete("all")  # Clear the canvas

    # Draw the board lines
        for i in range(1, board.width):
            canvas.create_line(0, i * self.cell_size, self.canvas_width, i * self.cell_size)
            canvas.create_line(i * self.cell_size, 0, i * self.cell_size, self.canvas_height)

        # Draw the board cells
        for i in range(board.width):
            for j in range(len(board.cells[i])):
                x = j * self.cell_size
                y = i * self.cell_size
                canvas.create_text(x + self.cell_size // 2, y + self.cell_size // 2, text=board.cells[i][j])
        self.canvas.pack()

    def get_input(self, current):
        self.input = (7, 4)
        return

    def update_gui(self, board, game_state):
        self.draw_board(self.canvas, board)
        
    def display_game_state(self, game_state):
        print(f'Current Player is: Player {game_state.current_player.handle}')
    def display_valid_moves(self, player):
        print(f'Valid moves: {player.get_valid_moves()}')
        