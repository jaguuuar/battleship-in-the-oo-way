from square import Square
from ship import Ship
from ocean import Ocean


def main():

    shipxD = Ship('Carrier', False, 0, 4)
    ocean = Ocean()
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
    #ocean.make_hit(0,0)
    #ocean.make_hit(4,0)
    #ocean.make_hit(1,9)

    print(ocean)


if __name__ == '__main__':
    main()
