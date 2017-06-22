class Square:

    def __init__(self, ship=None, is_hit=False, in_game_look=False):
        self.ship = ship
        self.is_hit = is_hit
        self.in_game_look = in_game_look

    def hit(self):
        '''
        Marks attribute is_hit of Square object as True
        '''
        self.is_hit = True
        return self.is_ship()

    def change_square_look(self):
        self.in_game_look = True

    def is_ship(self):
        '''
        If Square object is a part of Ship - return True,
        otherwise return false
        '''
        if self.ship is not None:
            return True
        else:
            return False

    def __str__(self):
        '''
        During inserting *Ship* objects
        Returns 'X' if is_hit attribute of Square object is True,
        otherwise returns ' ' (empty string)
        '''
        if self.in_game_look:
            if self.is_hit:
                if self.ship is not None:
                    return 'X'
                else:
                    return 'O'
            else:
                return ' '
        else:
            if self.ship is not None:
                return 'X'
            else:
                return ' '
