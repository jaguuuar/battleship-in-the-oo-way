from ship import Ship
from square import Square
from ocean import Ocean
from player import Player

def main():


    ocean = Ocean()
    print(ocean)
    player = Player('Mati')
    player.insert_ships(ocean)
    ocean.make_hit(1, 8)
    print(ocean)


if __name__ == '__main__':
    main()
