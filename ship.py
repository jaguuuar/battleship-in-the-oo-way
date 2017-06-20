from square import Square

class Ship:

    def __init__(self, size, is_vertical, start_row, start_column, is_sunk=False):
        self.size = size
        self.is_vertical = is_vertical
        self.start_row = start_row
        self.start_column = start_column
        self.squares = []
        self.is_sunk = is_sunk

    def build_ship(self, size):
        square = Square()
        for i in range(size):
            self.squares.append(square(True))

    def check_if_sunk(self):
        for square in self.squares:
            if square.is_hit == False:
                return False
            else:
                return True

    def __str__(self):
        pass
