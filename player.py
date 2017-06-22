from ocean import Ocean
from ship import Ship
import os


class Player:

    def __init__(self, name):
        self.name = name
        self.ocean = Ocean()


    def add_ship(self, ship):
        return self.ocean.insert_ship(ship)

    def hasLost(self):
        if not self.ocean.ships:
            return True

    def __str__(self):
        return "Player: " + self.name
