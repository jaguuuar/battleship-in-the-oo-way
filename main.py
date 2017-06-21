from square import Square
from ship import Ship
from ocean import Ocean
from player import Player


def main():

    shipxD = Ship('Carrier', False, 0, 4)
    ocean = Ocean()
    player1 = Player("Tomek")
    #ocean.make_hit(0,0)
    ocean.build_board()

    ocean.insert_ship(shipxD)
    print(ocean)
    row = int(input("ROW: "))
    col = int(input("COL: "))
    ship2 = Ship('Cruiser', True, row, col)
    ocean.check_if_fits(ship2)
    if ocean.check_horizontal_ship(ship2) and ocean.check_if_fits(ship2):
        ocean.insert_ship(ship2)

    ocean.make_hit(0,6)
    ocean.make_hit(5,5)
    ocean.make_hit(6,5)
    ocean.make_hit(7,5)
    ship2.check_if_sunk()
    print(ship2.squares)
    print(ship2.is_sunk)
    player1.check_is_winner()
    print(ocean)
    print(player1.sunk_ships)
    print(player1)



if __name__ == '__main__':
    main()
