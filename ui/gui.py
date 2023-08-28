import pygame
import sys
import time

class GUI:
    def __init__(self, board, gamestate):
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((800, 900))
        pygame.display.set_caption("Quoridor DX")

        self.grid_width = 800
        self.grid_height = 800
        self.cell_size = self.grid_height / 9

        self.board = board
        self.gamestate = gamestate

        self.grid = pygame.Surface((self.grid_width, self.grid_height))
        self.grid_rect = self.grid.get_rect(topleft=(0, 0))

        self.draw_board(board, gamestate)
        

    def draw_board(self, board, gamestate):
        self.buttons = []
        self.grid.fill((255, 255, 255))  # Fill grid with white
        for i in range(board.width):
            for j in range(board.width):
                cell_rect = pygame.Rect(j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size)
                if board.cells[i][j] == 'E':
                    pygame.draw.rect(self.grid, (0, 255, 0), cell_rect, 3)
                    font = pygame.font.Font(None, 36)
                    text_surface = font.render('E', True, (0, 0, 0))
                    text_rect = text_surface.get_rect(center=cell_rect.center)
                    self.grid.blit(text_surface, text_rect)
                elif board.cells[i][j] == 'V':
                    pygame.draw.rect(self.grid, (0, 255, 0), cell_rect, 3)
                    font = pygame.font.Font(None, 36)
                    text_surface = font.render('V', True, (0, 0, 0))
                    text_rect = text_surface.get_rect(center=cell_rect.center)
                    self.grid.blit(text_surface, text_rect)
                elif isinstance(board.cells[i][j], int):
                    pygame.draw.rect(self.grid, (0, 255, 0), cell_rect, 3)
                    font = pygame.font.Font(None, 36)
                    text_surface = font.render(str(board.cells[i][j]), True, (0, 0, 0))
                    text_rect = text_surface.get_rect(center=cell_rect.center)
                    self.grid.blit(text_surface, text_rect)
                if i <= 7 and j <= 7:
                    wall_button = Wall_Button(self.grid, (j * self.cell_size + self.cell_size * 0.6, i * self.cell_size + self.cell_size * 0.6, self.cell_size * 0.5, self.cell_size * 0.5), (0, 0, 255), (i, j))
                    self.buttons.append(wall_button)

        submit_button = Submit_Button(self.screen, (0, 800, 800, 100), (0, 255, 0))
        self.buttons.append(submit_button)

        #self.screen.fill((0, 0, 0))  # Fill screen with black
        self.screen.blit(self.grid, self.grid_rect)
        pygame.display.flip()

    def update_gui(self, board, game_state):
        for button in self.buttons:
            pygame.draw.rect(self.grid, button.color, button.rect)

        self.screen.blit(self.grid, self.grid_rect)
        pygame.display.flip()

    def get_input(self, current):
        print('input wait')
        while True:
            for event in pygame.event.get():
                for button in self.buttons:
                    button.check_event(event)
                    if button.output == 'submit':
                        self.input = (7,4)
                        print(self.input)
                        return
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.update_gui(self.board, self.gamestate)
    
    def display_game_state(self, game_state):
        print(f'Current Player is: Player {game_state.current_player.handle}')

    def display_valid_moves(self, player, board, gamestate):
        print(f'Valid moves: {player.get_valid_moves()}')
        for length in range(len(player.get_valid_moves())):
            board.cells[player.get_valid_moves()[length][0]][player.get_valid_moves()[length][1]] = 'V'
        self.draw_board(board, gamestate)

class Wall_Button():
    def __init__(self, grid, rect, color, place):
        self.grid = grid
        self.rect = pygame.Rect(rect)
        self.color = color
        self.hover_effect = False
        self.place = place
        self.output = ''
        pygame.draw.rect(grid, color, rect)

    def check_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.on_click()

    def on_click(self):
        self.function()

    def function(self):
        print(self.place)
        self.color = (255, 0, 0)

class Move_Button():
    def __init__(self, grid, rect, color):
        self.rect = pygame.Rect(rect)
        self.color = color
        self.hover_effect = True

    def check_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.on_click()

    def on_click(self):
        self.function()

    def check_hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if self.hover_effect:
                pass

    def function(self):
        pass

class Submit_Button():
    def __init__(self, screen, rect, color):
        self.rect = pygame.Rect(rect)
        self.color = color
        self.hover_effect = True
        self.screen = screen
        pygame.draw.rect(screen, color, rect)
        self.output = ''

    def check_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.on_release()

    def on_release(self):
        self.function()

    def check_hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if self.hover_effect:
                self.color = (10, 20, 10)
                time.sleep(0.1)
                self.color(0, 255, 0)
    
    def function(self):
        self.output = 'submit'
        print('submit')
