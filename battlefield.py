class BattleField:
    """Chcę, żeby były tutaj metody z playera : insert ship, get_ship_direction i get_ship_coordinates"""
    POSSIBLE_ROWS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')
    POSSIBLE_COLUMNS = range(10)

    def __init__(self):
        self.player_one = None
        self.player_two = None
        self.boards = None
        self.turn = None

    def start_pvp_game(self):
        self.player_one = self.createHumanPlayer(1)

    def get_opponent(self, current_player):
        if current_player == self.player_one:
            return self.player_two
        return self.player_one
        

    def insert_ships(self, ocean):

        print('{} place your ships!\n'.format(self.name))
        for ship, size in Ship.ship_types.items():
            succesful_adding = False
            while not succesful_adding:
                print(("Place {}, it has {} squares.\n").format(ship, size))
                direction = self.get_ship_direction(ship)
                coordinates = self.get_ship_coordinates()
                converted_coordinates = self.convert_coordinates(coordinates)
                ship_to_insert = Ship(ship, direction, converted_coordinates[0], converted_coordinates[1])
                succesful_adding = ocean.insert_ship(ship_to_insert)
                if succesful_adding:
                    self.ships.append(ship_to_insert)
                os.system("clear")
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
        row = coordinates[0].upper()
        col = coordinates[1]

        coordinates_values = {
                            'A': 0, 'B': 1, 'C': 2, 'D': 3,
                            'E': 4, 'F': 5, 'G': 6,
                            'H': 7, 'I': 8, 'J': 9
                            }

        row = coordinates_values[row]
        converted_coordinates = (int(row), int(col))

        return converted_coordinates


    def createHumanPlayer(self, player_number):
        """"TUTAJ CHCĘ ŻEBY TWORZYŁ SIĘ PLAYER NA PODSTAWIE PRZENIESIONYCH METOD"""


    # @staticmethod
    # def get_ship_coordinates(cls):
    #     row = ''
    #     col = ''
    #     while row not in cls.POSSIBLE_ROWS:
    #         row = input('Choose row (A - J): ').upper()
    #
    #     while col not in cls.POSSIBLE_COLUMNS:
    #         try:
    #             col = (int(input('Choose column (1-10): '))) - 1
    #         except ValueError:
    #             print("It's not a number!")
    #
    #     return (row, col)
    #
