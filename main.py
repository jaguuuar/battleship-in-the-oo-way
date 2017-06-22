from square import Square
from ship import Ship
from ocean import Ocean
from player import Player


def main():


    ocean = Ocean()
    print(ocean)
    player = Player('Mati')
    player.insert_ships(ocean)

    while not player.is_winner:
        print("Make a hit!")
        row = int(input("ROW: "))
        col = int(input("COL: "))
        ocean.make_hit(row, col)
        for ship in player.ships:
            ship.check_if_sunk()
        player.sunk_ships_count()
        print(player.ships)
        print(player.enemy_sunk_ships)
        player.check_is_winner()
        print(ocean)
    print(ocean)



if __name__ == '__main__':
    main()
