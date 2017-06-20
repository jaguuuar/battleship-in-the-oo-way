class Square:

    def __init__(self, ship=None, is_hit=False):
        #self.row = row
        #self.column = column
        self.ship = ship
        self.is_hit = is_hit


    def hit(self):
        self.is_hit = True

    def __str__(self):
        if self.is_hit:
            if self.ship is not None:
                return 'X'
            else:
                return 'O'
        else:
            return ' '
