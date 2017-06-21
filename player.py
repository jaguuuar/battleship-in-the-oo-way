from ocean import Ocean
from ship import Ship


class Player:

    def __init__(self, name):
        self.name = name
        self.is_winner = False

    def insert_ships(self):
        ocean = Ocean()

        for ship, size in Ship.ship_types.items():
            print(("Place {}, it has {} squares.").format(ship, size))
            direction = get_ship_direction(ship)
            row, col = get_ship_coordinates()
            ship_to_insert = Ship(ship, direction, row, col)
            ocean.insert_ship(ship_to_insert)

    def get_ship_direction(self, ship_name):
        possible_choices = [1, 2]
        direction_values = {1: True, 2: False}

        print("Choose 1 for Horizontal or 2 for Vertical.")
        direction = 0

        while direction not in possible_choices:
            try:
                direction = int(input(("Choose {} direction: ").format(ship_name)))
            except ValueError:
                print("Wrong choice!")

        return direction_values[direction]

    def get_ship_coordinates(self):
        row = ''
        col = ''

        coordinates_values = {
                            'A': 0, 'B': 1, 'C': 2, 'D': 3,
                            'E': 4, 'F': 5, 'G': 6,
                            'H': 7, 'I': 8, 'J': 9
                            }

        POSSIBLE_ROWS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')
        POSSIBLE_COLUMNS = range(10)

        while row not in POSSIBLE_ROWS:
            row = input('Choose row (A - J): ')

        while col not in POSSIBLE_COLUMNS:
            try:
                col = (int(input('Choose column (1-10)'))) - 1
            except ValueError:
                print("It's not a number!")

        return row, col
