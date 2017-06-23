from ocean import Ocean
from ship import Ship
import os


class Player:

    def __init__(self, name):
        self.name = name
        self.ocean = Ocean()


    def add_ship(self, ship):
        return self.ocean.insert_ship(ship)

    def has_lost(self):
        if not self.ocean.ships:
            return True
        return False

    def take_damage(self, row, column):
        return self.ocean.make_hit(row, column)

    def __str__(self):
        return "Player: " + self.name
