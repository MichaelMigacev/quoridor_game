import pygame
import sys
import time

class GUI:
    def __init__(self, board, gamestate):
        pygame.init()
        self.running = True
        self.grid_width = 800
        self.grid_height = 800
        self.cell_size = self.grid_height / 9
        self.border = self.cell_size * 0.2

        self.screen = pygame.display.set_mode((800 - self.border, 900 - self.border))
        pygame.display.set_caption("Quoridor DX")

        self.board = board
        self.gamestate = gamestate

        self.grid = pygame.Surface((self.grid_width - self.border, self.grid_height - self.border))
        self.grid_rect = self.grid.get_rect(topleft=(0, 0))

        self.draw_board(board, gamestate)
        self.draw_buttons()
        self.submit_button = Submit_Button(self.screen, (0, 800 - self.border, 800 - self.border, 100), (186, 52, 63))


    def draw_board(self, board, gamestate):
        self.grid.fill((135, 137, 153))  # Fill grid with white
        for i in range(board.width):
            for j in range(board.width):
                cell_rect = pygame.Rect(j * self.cell_size, i * self.cell_size, self.cell_size * 0.8, self.cell_size * 0.8)
                if board.cells[i][j] == 'E':
                    pygame.draw.rect(self.grid, (202, 204, 219), cell_rect)
                    """ font = pygame.font.Font(None, 36)
                    text_surface = font.render('E', True, (0, 0, 0))
                    text_rect = text_surface.get_rect(center=cell_rect.center)
                    self.grid.blit(text_surface, text_rect) """
                elif board.cells[i][j] == 'V':
                    pygame.draw.rect(self.grid, (163, 194, 163), cell_rect)
                    """ font = pygame.font.Font(None, 36)
                    text_surface = font.render('V', True, (0, 0, 0))
                    text_rect = text_surface.get_rect(center=cell_rect.center)
                    self.grid.blit(text_surface, text_rect) """
                elif isinstance(board.cells[i][j], int):
                    pygame.draw.rect(self.grid, (166* (board.cells[i][j] - 1), 90, 161 ), cell_rect)
                    """ font = pygame.font.Font(None, 36)
                    text_surface = font.render(str(board.cells[i][j]), True, (0, 0, 0))
                    text_rect = text_surface.get_rect(center=cell_rect.center)
                    self.grid.blit(text_surface, text_rect) """
                
        
        
        self.screen.blit(self.grid, self.grid_rect)
        pygame.display.flip()

    def draw_buttons(self):
        self.buttons = []
        for i in range(self.board.width):
            for j in range(self.board.width):
                if i <= 7 and j <= 7:
                    wall_button = Wall_Button(self.grid, (j * self.cell_size + self.cell_size * 0.6, i * self.cell_size + self.cell_size * 0.6, self.cell_size * 0.5, self.cell_size * 0.5), (0, 0, 255), (i, j))
                    self.buttons.append(wall_button)
                if self.board.cells[i][j] == 'V':
                    move_button = Move_Button(self.grid, (j * self.cell_size, i * self.cell_size, self.cell_size * 0.8, self.cell_size * 0.8), (30, 30, 100), (i, j))
                    self.buttons.append(move_button)
        self.screen.blit(self.grid, self.grid_rect)
        pygame.display.flip()

    def update_gui(self, board, game_state):
        buttons_on_2 = 0
        buttons_with_input = 0
        for button in self.buttons:
            if button.output == 2:
                buttons_on_2 += 1
            if button.output == 1 or button.output == 0:
                buttons_with_input += 1
            button.update()
        if buttons_on_2 == len(self.buttons) or buttons_with_input > 1:
            self.draw_board(board, game_state)
            self.draw_buttons()
        self.submit_button.update()

        self.screen.blit(self.grid, self.grid_rect)
        pygame.display.flip()

    def get_input(self, current):
        self.draw_buttons()
        while True:
            for event in pygame.event.get():
                for button in self.buttons:
                    button.check_event(event)
                self.submit_button.check_event(event)
                if self.submit_button.output == 'submit':
                    self.input = []
                    for button in self.buttons:
                        if button.output != 2:
                            self.input = [button.place, button.output, button.type]
                    print(self.input)
                    self.submit_button.reset()
                    if self.input == []:
                        print('There was no input')
                        continue
                    return
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.update_gui(self.board, self.gamestate)
    
    def display_game_state(self, game_state):
        print(f'Current Player is: Player {game_state.current_player.handle}')


class Wall_Button():
    def __init__(self, grid, rect, color, place):
        self.grid = grid
        self.rect = pygame.Rect(rect)
        self.color = color
        self.place = place
        self.output = 2
        self.type = 'wall'

    def check_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.on_click()

    def on_click(self):
        self.function()

    def function(self):
        self.output = (self.output + 1) % 3
        print(self.output)
        
    def update(self):
        if self.output == 0:
            self.color = (0, 0, 255)
            pygame.draw.rect(self.grid, self.color, self.rect)
        elif self.output == 1:
            self.color = (255, 0, 0)
            pygame.draw.rect(self.grid, self.color, self.rect)


class Move_Button():
    def __init__(self, grid, rect, color, place):
        self.grid = grid
        self.rect = pygame.Rect(rect)
        self.color = color
        self.output = 2
        self.place = place
        self.type = 'move'


    def check_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.on_click()

    def on_click(self):
        self.function()

    def function(self):
        if self.output == 2:
            self.output = 1
        else:
            self.output = 2

    def update(self):
        if self.output == 1:
            self.color = (30, 100, 30)
            pygame.draw.rect(self.grid, self.color, self.rect)

    

class Submit_Button():
    def __init__(self, screen, rect, color):
        self.rect = pygame.Rect(rect)
        self.color = color
        self.screen = screen
        pygame.draw.rect(screen, color, rect)
        self.output = ''

    def check_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.on_release()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.on_click()

    def on_release(self):
        self.function()

    def on_click(self):
        self.color = (130, 40, 48)
    
    def function(self):
        self.output = 'submit'
        print('submit')

    def reset(self):
        self.color = (186, 52, 63)
        self.output = ''

    def update(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        
