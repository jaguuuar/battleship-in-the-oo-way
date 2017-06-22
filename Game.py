from hotseat import Hotseat
from ocean import Ocean
import os


def Game():
    print("Choose game type:\n 1: Hotseat\n 2: With PC\n")
    game_type = input("Enter game type: ")
    ## 1 - > Hot-Seat, ##
    if game_type == "1":
        name = input("Name of player no.1: ")
        name2 = input("Name of player no.2: ")
        game = Hotseat(name, name2)
        player1 = game.player
        player2 = game.player2

        ## Filling boards ##
        print(game.board)
        player1.insert_ships(game.board)

        for item in game.board.board:
            for square in item:
                square.change_square_look()
        os.system("clear")

        print("Tura gracza nr 2")
        input("Press key to continue")
        player2.insert_ships(game.board2)
        for item in game.board2.board:
            for square in item:
                square.change_square_look()

        os.system("clear")

        while (not player1.is_winner or not player2.is_winner):
            hit = True

            while(hit == True):
                print("Player 1 turn")
                input("Press key to continue")
                print(game.board2)
                row = input("ROW: ").upper()
                while(len(row) == 0):
                    row = input("Bad input, ROW: ").upper()
                    while(ord(row) > 74):
                        row = input("Bad input, ROW: ").upper()
                col = input("COLUMN: ")
                while(int(col) > 9 or len(col) == 0):
                    col = input("Bad input, COLUMN: ")
                coordinates = player1.convert_coordinates((row, col))
                hit = game.board2.make_hit(coordinates[0], coordinates[1])
                os.system("clear")
                print(game.board2)

            hit = True
            while(hit == True):
                print("Player 2 turn")
                input("Press key to continue")
                print(game.board)
                row = input("ROW: ").upper()
                while(len(row) == 0):
                    row = input("Bad input, ROW: ").upper()
                    while(ord(row) > 74):
                        row = input("Bad input, ROW: ").upper()
                col = input("COLUMN: ")
                while(int(col) > 9):
                    col = input("Bad input, COLUMN: ")
                coordinates = player2.convert_coordinates((row, col))
                hit = game.board.make_hit(coordinates[0], coordinates[1])
                os.system("clear")
                print(game.board)
        if(player1.is_winner):
            print("{} win".format(name))
        else:
            print("{} win".format(name2))


if __name__ == '__main__':
    Game()