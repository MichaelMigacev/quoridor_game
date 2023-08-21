class GameState():
    def __init__(self, board):
        self.board = board
        self.player1 = Player(handle=1, position=(8, 4), board=self.board)
        self.player2 = Player(handle=2, position=(0, 4), board=self.board) # change later to Bot class once available
        self.list_of_walls = []
        self.current_player = self.player1
    def is_game_over(self):
        return False
    def get_current_player(self):
        return self.current_player
    def switch_turns(self):
        if self.get_current_player() == self.player1:
            self.current_player = self.player2
        elif self.get_current_player() == self.player2:
            self.current_player = self.player1
    def is_valid_move(self, current_player, move):
        return True
    def update_game_state(self, move):
        self.current_player.move(move)
        pass
class Player:
    def __init__(self, handle, position, board):
        self.board = board
        self.handle = handle
        self.position = position
        self.board.cells[self.position[0]][self.position[1]] = self.handle
    def move(self, input):
        self.input = input
        print(input)
        self.board.cells[self.position[0]][self.position[1]] = 'E'
        self.position = input
        self.board.cells[self.input[0]][self.input[1]] = self.handle
        

    