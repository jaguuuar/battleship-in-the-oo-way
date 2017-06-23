from hotseat import Hotseat
from ocean import Ocean
import os
from battlefield import BattleField


def main():
    battlefield = BattleField()
    print('\nWelcome to the Battleship game!')
    choice = ''
    possible_choices = [1, 2, 3, 0]
    while choice not in possible_choices:
        print('1) for 2 Players\n2) for 1 Player\n3) for PC vs PC\n0) Exit')
        try:
            choice = int(input("Choose game mode: "))
        except ValueError:
            print("Wrong choice!")
    if choice == 1:
        battlefield.start_pvp_game()
    elif choice == 2:
        battlefield.start_pvc_game()
    elif choice == 3:
        battlefield.start_cvc_game()
    elif choice == 0:
        exit()

if __name__ == '__main__':
    main()
