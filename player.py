from ocean import Ocean
from ship import Ship


class Player:

    def __init__(self, name):
        self.name = name
        self.is_winner = False
        self.sunk_ships = 0
        self.player_ships = []


    def sunk_ships_count(self, ship):
        if ship.is_sunk == True:
            self.sunk_ships += 1

    def check_is_winner(self):
        if self.sunk_ships == 2:
            self.is_winner = True

    def add_ship(self, ship):
        self.player_ships.append(ship)


    def __str__(self):
        if self.is_winner:
            return "you win"
        else:
            return "try again"
