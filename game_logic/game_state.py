class GameState():
    def __init__(self, board):
        self.board = board
        self.player1 = Player(handle=1, position=(8, 4), board=self.board)
        self.player2 = Player(handle=2, position=(0, 4), board=self.board) # change later to Bot class once available
        self.list_of_walls = []
        self.list_of_blocked_moves = []
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
        if move[2] == 'move':
            return True
        elif move[2] == 'wall':
            wall = Wall(move[0], move[1])
            if wall.is_valid(self) == True:
                return True
            else:
                return False
    def update_game_state(self, move):
        if move[2] == 'move':
            self.current_player.move(move)
        elif move[2] == 'wall':
            wall = Wall(move[0], move[1])
            self.list_of_walls.append(wall)
            for move in wall.blocking_moves:
                self.list_of_blocked_moves.append(move)
            print(wall.alignement)
            print(self.list_of_blocked_moves)
            
    
class Player:
    def __init__(self, handle, position, board):
        self.board = board
        self.handle = handle
        self.position = position
        self.board.cells[self.position[0]][self.position[1]] = self.handle
        self.walls = 10
    def move(self, input):
        self.input = input
        self.board.cells[self.position[0]][self.position[1]] = 'E'
        self.position = input[0]
        self.board.cells[self.input[0][0]][self.input[0][1]] = self.handle
    def get_valid_moves(self, board, gamestate):
        self.valid_moves = []
        hypothetical_moves = [(self.position[0]-1, self.position[1]),(self.position[0]+1, self.position[1]),\
                              (self.position[0], self.position[1]-1),(self.position[0], self.position[1]+1)]
        for move in hypothetical_moves:
            if self.board.valid_position(move[0]) and self.board.valid_position(move[1]) and (self.position, move) not in gamestate.list_of_blocked_moves:
                self.valid_moves.append(move)
        for moves in self.valid_moves:
            board.cells[moves[0]][moves[1]] = 'V'
        return self.valid_moves

class Wall:
    def __init__(self, position, alignement):
        self.position = position
        #True is vertical alignement
        self.alignement = alignement
        self.blocking_moves = self.blocks_moves()
    def blocks_moves(self):
        self.blocking_moves = []
        if self.alignement:
            self.blocking_moves.append(((self.position),(self.position[0], self.position[1]+1)))
            self.blocking_moves.append(((self.position[0], self.position[1]+1),(self.position)))
            self.blocking_moves.append(((self.position[0]+1, self.position[1]),(self.position[0]+1, self.position[1]+1)))
            self.blocking_moves.append(((self.position[0]+1, self.position[1]+1),(self.position[0]+1, self.position[1])))
        else:
            self.blocking_moves.append(((self.position),(self.position[0]+1, self.position[1])))
            self.blocking_moves.append(((self.position[0]+1, self.position[1]),(self.position)))
            self.blocking_moves.append(((self.position[0], self.position[1]+1),(self.position[0]+1, self.position[1]+1)))
            self.blocking_moves.append(((self.position[0]+1, self.position[1]+1),(self.position[0], self.position[1]+1)))
        return self.blocking_moves
    def is_valid(self, gamestate):
        self.validity = True
        for wall in gamestate.list_of_walls:
            if self.position == wall.position:
                self.validity = False
        for blocked_move in self.blocking_moves:
            if blocked_move in gamestate.list_of_blocked_moves:
                self.validity = False
        return self.validity
            