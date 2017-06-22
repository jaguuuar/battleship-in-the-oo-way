from square import Square


class Ship:

    ship_types = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}

    def __init__(self, ship_type, is_vertical, start_row, start_column, is_sunk=False):
        self.ship_type = ship_type
        self.size = Ship.ship_types[ship_type]
        self.is_vertical = is_vertical
        self.starting_point = (start_row, start_column)
        self.ending_point = self.calculate_ending_point()
        self.squares = []
        self.is_sunk = is_sunk
        self.build_ship(self.size)

    def build_ship(self, size):
        '''
        Basing on provided size, construct a ship, by appending Square objects
        to self.squares list

        Parameters
        ----------
        size = int

        Returns
        -------
        None

        '''
        for i in range(size):
            square = Square(self, False)
            self.squares.append(square)

    def check_if_sunk(self):
        '''
        Check if every Square object that Ship consists of has
        is_hit attribute set to True, if that happens, is_sunk attribute
        of Ship is marked as True
        '''
        temp_list = []
        for square in self.squares:
            if square.is_hit:
                temp_list.append('Hit')
        if len(temp_list) == self.size:
                self.is_sunk = True

    def calculate_ending_point(self):
        '''
        Basing on Ship.starting_point (tuple of 2 ints), calculates its ending
        point and returns it

        Parameters
        ---------
        None

        Returns
        -------
        ending_point = tuple of 2 ints
        '''
        if self.is_vertical:
            ending_row = self.starting_point[0] + self.size - 1
            ending_point = (ending_row, self.starting_point[1])
        else:
            ending_column = self.starting_point[1] + self.size - 1
            ending_point = (self.starting_point[0], ending_column)

        return ending_point
