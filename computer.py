from player import Player
import random

class Computer(Player):

    def __init__(self, name, difficulty):
        super().__init__(name)
        self.difficulty = difficulty
        self.seek_mode = True
        self.ship_position = None
        self.allowed_point_set = self.generate_allowed_points()
        self.current_coord = (-1, -1)

    @classmethod
    def generate_allowed_points(cls):
        set_of_points = set()
        for y in range(10):
            for x in range(10):
                set_of_points.add((y, x))
        return set_of_points

    def get_coords(self):
        if self.seek_mode:
            self.current_coord = random.choice(list(self.allowed_point_set))
            return self.current_coord

    def del_current_coord(self):
        self.allowed_point_set.discard(self.current_coord)
        print(len(self.allowed_point_set))

    def opponent_was_hit(self):
        if self.difficulty in ["MEDIUM", "HARD"] and self.seek_mode and self.ship_position is None:
            self.seek_mode = False

    def opponent_was_sunk(self):
        pass




