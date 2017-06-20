from square import Square

class Ship:

    def __init__(self, size, is_vertical, start_row, start_column, is_sunk=False):
        self.size = size
        self.is_vertical = is_vertical
        self.start_row = start_row
        self.start_column = start_column
        self.squares = []
        self.is_sunk = is_sunk
        self.build_ship(size)

    def build_ship(self, size):
        square = Square(True, False)
        for i in range(size):
            self.squares.append(square)

    def check_if_sunk(self):
        for square in self.squares:
            if square.is_hit == False:
                return False
            else:
                return True

    def __str__(self):
        xd = ''
        for i in self.squares:
            if self.is_vertical:
                xd += str(i) + "|" "\n"
            else:
                xd += str(i) + "|"

        return xd
