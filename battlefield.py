from player import Player
from ship import Ship
from ocean import Ocean
from computer import Computer
import random
import os

class BattleField:

    def __init__(self):
        self.player_one = None
        self.player_two = None
        self.current_player = None

    def start_pvp_game(self):
        self.player_one = self.createHumanPlayer(1)
        self.player_two = self.createHumanPlayer(2)
        self.start_game()

    def start_pvc_game(self):
        self.player_one = self.createHumanPlayer(1)
        self.player_two = self.createComputerPlayer(2)
        self.start_game()

    def start_cvc_game(self):
        self.player_one = self.createComputerPlayer(1)
        self.player_two = self.createComputerPlayer(2)
        self.start_game()

    def start_game(self):
        self.current_player = self.player_one
        input("Player's {} turn".format(self.current_player.name))
        game_finished = False
        while not game_finished:
            game_finished = self.play_turn()

        print(self.display_battlefield())
        print(self.current_player.name + " has won the game!")


    def play_turn(self):
        if isinstance(self.current_player, Computer):
            return self.computer_turn()
        else:
            return self.human_turn()

    def human_turn(self):
        opponent = self.get_opponent()
        opponents_ships = len(opponent.ocean.ships)
        self.display_battlefield()
        print("Take the shot!")
        coords = self.get_coordinates()
        ship_was_hit = opponent.take_damage(coords[0], coords[1])
        if ship_was_hit:
            current_opponents_ships = len(opponent.ocean.ships)
            print("\nYou hit a ship!")
            if opponents_ships != current_opponents_ships:
                print('And you destroyed it!')
                if opponent.has_lost():
                    return True
        else:
            print("\nYou've missed")
            self.current_player = opponent
            print("Player's {} turn".format(opponent.name))

        input("Press enter to continue")
        return False

    def computer_turn(self):
        print(self.display_battlefield())
        opponent = self.get_opponent()
        opponents_ships = len(opponent.ocean.ships)
        coords = self.current_player.get_coords()
        coords_to_print = "{} {}".format(Ocean.POSSIBLE_ROWS[coords[0]], coords[1])
        print("\n{} has chosen point {}!".format(self.current_player.name, coords_to_print))
        ship_was_hit = opponent.take_damage(coords[0], coords[1])
        if ship_was_hit:
            self.current_player.opponent_was_hit()
            self.current_player.del_current_coord()
            current_opponents_ships = len(opponent.ocean.ships)
            print("\n{} has hit a ship!".format(self.current_player.name))
            if opponents_ships != current_opponents_ships:
                self.current_player.opponent_was_sunk()
                print('And destroyed it!')
                if opponent.has_lost():
                    return True
        else:
            self.current_player.del_current_coord()
            print("\n{} missed".format(self.current_player.name))
            self.current_player = opponent
            print("Player's {} turn".format(opponent.name))

        # input("Press enter to continue")
        return False

    def get_opponent(self):
        if self.current_player == self.player_one:
            return self.player_two
        return self.player_one
        
    def createHumanPlayer(self, player_number, debug=False):
        if not debug:
            name = input("\nName of player no.{}: ".format(player_number))
            player = Player(name)
            self.insert_ships(player)
            return player

        player = Player("debugPlayer")
        player.ocean = self.generateOcean()
        return player

    def createComputerPlayer(self, player_number, mode="EASY"):
        player = Computer("Computer player {}".format(player_number), mode)
        player.ocean = self.generateOcean()
        return player

    def generateOcean(self):
        ocean = Ocean()
        for shipTuple in sorted(Ship.ship_types.items(), key=lambda x: x[1], reverse=True):
            ship_added = False
            while not ship_added:
                chosenY = random.randint(0, 9)
                chosenX = random.randint(0, 9)
                isVertical = bool(random.getrandbits(1))
                ship = Ship(shipTuple[0], isVertical, chosenY, chosenX)
                ship_added = ocean.insert_ship(ship)
        return ocean

    def insert_ships(self, player):
        os.system("clear")
        print('{} place your ships!\n'.format(player.name))
        for ship, size in Ship.ship_types.items():
            successful_adding = False
            print(player.ocean)
            while not successful_adding:
                print(("Place {}, it has {} squares.\n").format(ship, size))
                direction = self.get_ship_direction(ship)
                coordinates = self.get_coordinates()
                ship_to_insert = Ship(ship, direction, coordinates[0], coordinates[1])
                successful_adding = player.add_ship(ship_to_insert)
                os.system("clear")
                print(player.ocean)
                if not successful_adding:
                    print("Sorry, but you can't put your ship here! ")

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

    def get_coordinates(self):
        row = ''
        col = ''

        while row not in Ocean.POSSIBLE_ROWS:
            row = input('Choose row (A - J): ').upper()

        while col not in Ocean.POSSIBLE_COLUMNS:
            try:
                col = (int(input('Choose column (1-10): '))) - 1
            except ValueError:
                print("It's not a number!")

        return self.convert_coordinates((row, col))

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

    def display_battlefield(self, debug=False):
        opponent =  self.get_opponent()
        players_board = self.current_player.ocean.get_display_str_list()
        if not debug:
            opponent_board = opponent.ocean.get_display_str_list(False)
        else:
            opponent_board = opponent.ocean.get_display_str_list()

        print("Opponent's ships         ".format(opponent.name) + " " * len(players_board) + "       Yours ships")
        for i in range(len(players_board)):
            print(opponent_board[i] + " " * 10 + players_board[i])


if __name__ == '__main__':
    BattleField().start_cvc_game()