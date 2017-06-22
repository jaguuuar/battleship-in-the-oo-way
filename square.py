class Square:

    def __init__(self, ship=None, is_hit=False):
        self.ship = ship
        self.is_hit = is_hit

    def hit(self):
        '''
        Marks attribute is_hit of Square object as True
        '''
        self.is_hit = True

    def __str__(self):
        # TODO:
        '''
        Returns 'X' if is_hit attribute of Square object is True,
        otherwise returns ' ' (empty string)
        '''
        if self.is_hit:
            if self.ship is not None:
                return 'Z'
            else:
                return 'O'
        else:
            if self.ship is not None:
                return 'S'
            else:
                return ' '
