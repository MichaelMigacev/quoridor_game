class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [['E' for _ in range(width)] for _ in range(height)]
    def valid_position(self, number):
        if number < self.width and number >= 0:
            return True
        else:
            return False
    def clear_board(self):
        for i in range(self.width):
            for j in range(self.width):
                if self.cells[i][j] == 'V':
                    self.cells[i][j] = 'E'
    
    


