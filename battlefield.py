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

