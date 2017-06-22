from player import Player
from ocean import Ocean

class Hotseat:

    def __init__(self, name, name2):
        self.player = Player(name)
        self.player2 = Player(name2)
        self.board = Ocean()
        self.board2 = Ocean()


    