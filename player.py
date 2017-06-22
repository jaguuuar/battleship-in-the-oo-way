from ocean import Ocean
from ship import Ship


class Player:

    def __init__(self, name):
        self.name = name
        self.is_winner = False
        self.ships = []
        self.enemy_sunk_ships = 0

    def insert_ships(self, ocean):

        for ship, size in Ship.ship_types.items():
            succesful_adding = False
            while not succesful_adding:
                print(("Place {}, it has {} squares.").format(ship, size))
                direction = self.get_ship_direction(ship)
                coordinates = self.get_ship_coordinates()
                converted_coordinates = convert_coordinates(coordinates)
                ship_to_insert = Ship(ship, direction, converted_coordinates[0], converted_coordinates[1])
                succesful_adding = ocean.insert_ship(ship_to_insert)
                if succesful_adding:
                    self.ships.append(ship_to_insert)
                print(ocean)

    def get_ship_direction(self, ship_name):
        possible_choices = ['V', 'H']
        direction_values = {'V': True, 'H': False}

        print("Choose 'H' for Horizontal or 'V' for Vertical.")
        direction = 0

        while direction not in possible_choices:
                direction = input(("Choose {} direction: ").format(ship_name)).upper()

                if direction not in possible_choices:
                    print("Wrong choice!")

        return direction_values[direction]

    def get_ship_coordinates(self):
        row = ''
        col = ''



        POSSIBLE_ROWS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')
        POSSIBLE_COLUMNS = range(10)

        while row not in POSSIBLE_ROWS:
            row = input('Choose row (A - J): ').upper()

        while col not in POSSIBLE_COLUMNS:
            try:
                col = (int(input('Choose column (1-10): '))) - 1
            except ValueError:
                print("It's not a number!")

        return (row, col)

    def convert_coordinates(self, coordinates):
        '''
        Parameters
        ----------
        coordinates = tuple

        Returns
        -------
        converted_coordinates = tuple of ints (2)
        '''
        row = coordinates[0]
        col = coordinates[1]

        coordinates_values = {
                            'A': 0, 'B': 1, 'C': 2, 'D': 3,
                            'E': 4, 'F': 5, 'G': 6,
                            'H': 7, 'I': 8, 'J': 9
                            }

        row = coordinates_values[row]
        converted_coordinates = (row, col)

        return converted_coordinates


    def sunk_ships_count(self):
        for ship in self.ships:
            if ship.is_sunk:
                self.enemy_sunk_ships += 1

    def check_is_winner(self):
        if self.enemy_sunk_ships == 2:
            self.is_winner = True

    def add_ship(self, ship):
        self.ships.append(ship)

    def remove_ship(self):
        for ship in self.ships:
            if ship.is_sunk:
                self.ships.remove(ship)

    def __str__(self):
        if self.is_winner:
            return "you win"
        else:
            return "try again"
