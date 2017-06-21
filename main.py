from square import Square
from ship import Ship
from ocean import Ocean
from player import Player


def main():

    shipxD = Ship('Carrier', False, 0, 4)
    ocean = Ocean()
    player1 = Player("Tomek")
    ocean.build_board()

    ocean.insert_ship(shipxD)
    print(ocean)
    #row = int(input("ROW: "))
    #col = int(input("COL: "))
    ship1 = Ship('Carrier', False, int(input("ROW: ")) , int(input("COL: ")))
    ocean.check_if_fits(ship1)
    if ocean.check_horizontal_ship(ship1) and ocean.check_if_fits(ship1):
        ocean.insert_ship(ship1)

    ship2 = Ship('Cruiser', True, int(input("ROW: ")), int(input("COL: ")))
    ocean.check_if_fits(ship2)
    if ocean.check_horizontal_ship(ship2) and ocean.check_if_fits(ship2):
        ocean.insert_ship(ship2)
    print(ocean)
    player1.add_ship(ship1)
    player1.add_ship(ship2)

    print(player1.player_ships)
    print(player1.sunk_ships)


    while not player1.is_winner:
        print("Make a hit!")
        row = int(input("ROW: "))
        col = int(input("COL: "))
        ocean.make_hit(row, col)
        print(ocean)
        for ship in player1.player_ships:
            ship.check_if_sunk()
            player1.sunk_ships_count(ship)
            print(ship.is_sunk)
            player1.check_is_winner()
            print(ocean)
            print(player1.sunk_ships)
            print(player1)




if __name__ == '__main__':
    main()
