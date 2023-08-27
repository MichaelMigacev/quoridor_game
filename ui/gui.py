import pygame
import sys
import time

class GUI:
    def __init__(self, board, gamestate):
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((1000, 1000))
        pygame.display.set_caption("Quoridor DX")

        self.grid_width = 800
        self.grid_height = 800
        self.cell_size = self.grid_height / 9

        self.grid = pygame.Surface((self.grid_width, self.grid_height))
        self.grid_rect = self.grid.get_rect(topleft=(0, 50))

        self.draw_board(board, gamestate)

    def draw_board(self, board, gamestate):
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
                    button_rect = pygame.Rect(j * self.cell_size + self.cell_size * 0.6, i * self.cell_size + self.cell_size * 0.6, self.cell_size * 0.5, self.cell_size * 0.5)
                    
                    pygame.draw.rect(self.grid, (0, 0, 255), button_rect)
                    font = pygame.font.Font(None, 36)
                    text_surface = font.render('W', True, (0, 0, 0))
                    text_rect = text_surface.get_rect(center=button_rect.center)
                    self.grid.blit(text_surface, text_rect)

        self.screen.fill((0, 0, 0))  # Fill screen with black
        self.screen.blit(self.grid, self.grid_rect)
        pygame.display.flip()

    def update_gui(self, board, game_state):
        self.draw_board(board, game_state)

    def get_input(self, current):
        print('input wait')
        time.sleep(2)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:  # Example: react to SPACE key
                        self.input = (7, 4)
                        return
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    def display_game_state(self, game_state):
        print(f'Current Player is: Player {game_state.current_player.handle}')

    def display_valid_moves(self, player, board, gamestate):
        print(f'Valid moves: {player.get_valid_moves()}')
        for length in range(len(player.get_valid_moves())):
            board.cells[player.get_valid_moves()[length][0]][player.get_valid_moves()[length][1]] = 'V'
        self.draw_board(board, gamestate)

class Wall_Button():
    def __init__(self, rect, color):
        self.rect = pygame.Rect(rect)
        self.color = color
        self.hover_effect = False

    def check_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.on_click(event)

    def on_click(self):
        self.function()

    def function(self):
        pass

class Move_Button():
    def __init__(self, rect, color):
        self.rect = pygame.Rect(rect)
        self.color = color
        self.hover_effect = True

    def check_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.on_click(event)

    def on_click(self):
        self.function()

    def check_hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if self.hover_effect:
                pass

    def function(self):
        pass

class Submit_Button():
    def __init__(self, rect, color):
        self.rect = pygame.Rect(rect)
        self.color = color
        self.hover_effect = True

    def check_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.on_release(event)

    def on_release(self):
        self.function()

    def check_hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if self.hover_effect:
                pass
    
    def function(self):
        pass
