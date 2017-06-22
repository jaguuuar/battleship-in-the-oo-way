from hotseat import Hotseat
from ocean import Ocean
import os


def main():
    print('\nWelcome to the Battleship game!')
    name = input("\nName of player no.1: ")
    name2 = input("Name of player no.2: ")
    game = Hotseat(name, name2)
    player1 = game.player
    player2 = game.player2

    # Filling boards
    print(game.board)
    player1.insert_ships(game.board)
    for item in game.board.board:
        for square in item:
            square.change_square_look()
    os.system("clear")

    input("{}, press key to continue".format(name2))
    print(game.board)
    player2.insert_ships(game.board2)
    for item in game.board2.board:
        for square in item:
            square.change_square_look()

    os.system("clear")

    while not player1.is_winner or not player2.is_winner:
        os.system("clear")
        hit = True

        while hit:
            sunk_ships1 = player2.sunk_ships_count()

            print_before_shot_info(name, name2)
            print(game.board2)
            row, col = get_shot_coordinates()
            hit = make_a_shot_player1(row, col, game, player1)

            if hit:

                sunk_ships1_check = player2.sunk_ships_count()

                if sunk_ships1_check > sunk_ships1:
                    print('\nYou destroyed whole ship!')
                else:
                    print("\nYou hit a ship!")
                player2.check_is_winner()

                if player2.is_winner:
                    print("{} win".format(name))
                    exit()
        os.system('clear')
        print("You've missed")
        input('{} has to play now. Press any key'.format(name2))
        hit = True

        while hit:
            sunk_ships2 = player1.sunk_ships_count()
            print_before_shot_info(name2, name)
            print(game.board)
            row, col = get_shot_coordinates()
            hit = make_a_shot_player2(row, col, game, player2)

            if hit:

                sunk_ships2_check = player1.sunk_ships_count()

                if sunk_ships2_check > sunk_ships2:
                    print('\nYou destroyed whole ship!')
                else:
                    print("\nYou hit a ship!")
                player1.check_is_winner()

                player1.check_is_winner()

                if player1.is_winner:
                    print("{} win".format(name2))
                    exit()

        print("You've missed")
        input('{} has to play now. Press any key'.format(name))
        hit = True


def make_a_shot_player1(row, col, game, player):

    coordinates = player.convert_coordinates((row, col))
    hit = game.board2.make_hit(coordinates[0], coordinates[1])

    return hit


def make_a_shot_player2(row, col, game, player):

    coordinates = player.convert_coordinates((row, col))
    hit = game.board.make_hit(coordinates[0], coordinates[1])

    return hit


def print_before_shot_info(player1_name, player2_name):
    print("{} has to make a shot now!\n".format(player1_name))


def get_shot_coordinates():
    row = get_shot_row()
    col = get_shot_col()

    return row, col


def get_shot_row():
    POSSIBLE_ROWS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')
    row = ''

    while row not in POSSIBLE_ROWS:
        row = input("ROW: ").upper()

        while(len(row) == 0):
            row = input("Bad input, ROW: ").upper()

            while(ord(row) > 74):
                row = input("Bad input, ROW: ").upper()
    return row


def get_shot_col():
    POSSIBLE_COLUMNS = range(10)
    col = ''

    while col not in POSSIBLE_COLUMNS:

        try:
            col = int(input("COLUMN: "))
        except ValueError:
            print('Wrong column!')

    while(int(col) > 9):
        col = input("Bad input, COLUMN: ")

    return col


if __name__ == '__main__':
    main()
