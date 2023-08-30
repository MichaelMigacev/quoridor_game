from collections import deque
class GameState():
    def __init__(self, board):
        self.board = board
        self.player1 = Player(handle=1, position=(8, 4), board=self.board)
        self.player2 = Player(handle=2, position=(0, 4), board=self.board) # change later to Bot class once available
        self.list_of_walls = []
        self.list_of_blocked_moves = []
        self.current_player = self.player1
        self.other_player = self.player2
    def is_game_over(self):
        if self.current_player.handle == 1:
            if self.current_player.position[0] == 0:
                return True
        elif self.current_player.handle == 2:
            if self.current_player.position[0] == 8:
                return True
        else:
            return False
    def get_current_player(self):
        return self.current_player
    def switch_turns(self):
        if self.get_current_player() == self.player1:
            self.current_player = self.player2
            self.other_player = self.player1
        elif self.get_current_player() == self.player2:
            self.current_player = self.player1
            self.other_player = self.player2
    def is_valid_move(self, current_player, move):
        if move[2] == 'move':
            return True
        elif move[2] == 'wall':
            wall = Wall(move[0], move[1])
            if wall.is_valid(self) == True and self.check_reachability(current_player, wall) and self.check_reachability(self.other_player, wall):
                return True
            else:
                return False
    def check_reachability(self, player, wall):
        start_row = 0 if player.handle == 2 else 8
        visited = set()
        queue = deque([(start_row, col) for col in range(self.board.width)])
        while queue:
            row, col = queue.popleft()
            if (row, col) == player.position:
                return True
            if (row, col) not in visited:
                visited.add((row, col))
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if self.board.valid_position(new_row) and self.board.valid_position(new_col):
                        if ((row, col), (new_row, new_col)) not in self.list_of_blocked_moves and (new_row, new_col) not in visited and ((row, col), (new_row, new_col)) not in wall.blocking_moves:
                            queue.append((new_row, new_col))
        return False
    def update_game_state(self, move):
        if move[2] == 'move':
            self.current_player.move(move)
        elif move[2] == 'wall':
            wall = Wall(move[0], move[1])
            self.list_of_walls.append(wall)
            for move in wall.blocking_moves:
                self.list_of_blocked_moves.append(move)
            
    
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
        hypothetical_moves = [self.left(self.position),self.right(self.position),\
                              self.up(self.position),self.down(self.position)]
        for move in hypothetical_moves:
            if self.board.valid_position(move[0]) and self.board.valid_position(move[1]):
                if (self.position, move) not in gamestate.list_of_blocked_moves:
                    if self.board.cells[move[0]][move[1]] == 'E':
                        self.valid_moves.append(move)
                        continue
                    elif isinstance(self.board.cells[move[0]][move[1]], int):
                        directions = [self.left, self.right, self.up, self.down]
                        for direction in directions:
                            if move == direction(self.position):
                                if (move, direction(move)) not in gamestate.list_of_blocked_moves:
                                    self.valid_moves.append(direction(move))
                                    break
                                else:
                                    for direction2 in directions:
                                        if direction(move) != direction2(move) and direction2(move) != self.position and (move, direction2(move)) not in gamestate.list_of_blocked_moves:
                                            self.valid_moves.append(direction2(move))
        for moves in self.valid_moves:
            board.cells[moves[0]][moves[1]] = 'V'
        return self.valid_moves
    def left(self, position):
        left = (position[0], position[1] - 1)
        return left
    def right(self, position):
        left = (position[0], position[1] + 1)
        return left
    def up(self, position):
        left = (position[0] - 1, position[1])
        return left
    def down(self, position):
        left = (position[0] + 1, position[1])
        return left

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
            