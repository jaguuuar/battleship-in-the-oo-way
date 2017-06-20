class Square:

    def __init__(self, is_ship_part, is_hit=False):
        self.is_ship_part = is_ship_part
        self.is_hit = is_hit


    def hit(self):
        self.is_hit = True

    def __str__(self):
        if self.is_hit:
            if self.is_ship_part:
                return 'X'
            else:
                return 'O'
        else:
            return ' '
