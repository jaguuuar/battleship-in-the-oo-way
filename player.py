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
            directions = get_ship_direction(ship)


    def get_ship_direction(self, ship_name):
        possible_choices = [1, 2]
        print("Choose 1 for Horizontal or 2 for Vertical.")
        direction = 0

        while direction not in possible_choices:
            try:
                direction = int(input(("Choose {} direction: ").format(ship_name)))
            except ValueError:
                print("Wrong choice!")

        if direction == 1:
            return False
        else:
            return True
