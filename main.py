from square import Square
from ship import Ship
from ocean import Ocean


def main():
    ship = Ship(5, True, 0, 0)
    print(ship)

    ocean = Ocean()
    #ocean.make_hit(0,0)
    ocean.build_board()
    ocean.make_hit(1,0)
    print(ocean)


if __name__ == '__main__':
    main()
