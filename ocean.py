from ship import Ship
from square import Square
from player import Player


class Ocean:

    def __init__(self):
        self.board = []
        Ocean.build_board(self)

    def build_board(self):

        board_row = []

        for i in range(10):
            for j in range(10):
                square = Square()
                board_row.append(square)

            self.board.append(board_row)
            board_row = []


    def insert_ship(self, ship):
        ship_fits = self.check_if_fits(ship)

        ship_squares = ship.squares
        square_index = 0
        if ship_fits:
            if ship.is_vertical:
                if self.check_vertical_ship(ship):
                # INSERTING ON BOARD
                    for i in range(ship.starting_point[0], ship.starting_point[0] + ship.size):
                        self.board[i][ship.starting_point[1]] = ship_squares[square_index]
                        square_index += 1
                else:
                    return False

            else:
                if self.check_horizontal_ship(ship):
                # INSERTING ON BOARD
                    for i in range(ship.starting_point[1], ship.starting_point[1] + ship.size):
                        self.board[ship.starting_point[0]][i] = ship_squares[square_index]
                        square_index += 1
                else:
                    return False
            return True


    def check_if_fits(self, ship):
        if int(ship.ending_point[0]) > 9 or int(ship.ending_point[1]) > 9:
            print("Sadly, the ship won't fit here, place it again.")
            return False

        return True

    def check_horizontal_ship(self, ship):

        check_from_col = ship.starting_point[1] - 1
        check_to_col = check_from_col + ship.size + 1

        check_from_row = ship.starting_point[0] - 1
        check_to_row = check_from_row + 2


        for index in range(check_from_col, check_to_col + 1):
            try:
                if self.board[ship.starting_point[0]][index].ship is not None:
                    print("You can't place a ship here, it touches other ship!")
                    return False
                elif self.board[check_from_row][index].ship is not None:
                    print("You can't place a ship here, it touches other ship!")
                    return False
                elif self.board[check_to_row][index].ship is not None:
                    print("You can't place a ship here, it touches other ship!")
                    return False
            except IndexError:
                a=1

        return True

    def check_vertical_ship(self, ship):

        check_from_col = ship.starting_point[1] - 1
        check_to_col = check_from_col  + 2

        check_from_row = ship.starting_point[0] - 1
        check_to_row = check_from_row + ship.size + 1


        for index in range(check_from_row, check_to_row + 1):
            try:
                if self.board[index][ship.starting_point[1]].ship is not None:
                    print("Tu leży statek")
                    return False
                elif self.board[index][check_from_col].ship is not None:
                    print("Tu leży statek")
                    return False
                elif self.board[index][check_to_col].ship is not None:
                    print("Tu leży statek")
                    return False
            except IndexError:
                a = 1

        return True


    def make_hit(self, row, column):
        self.board[row][column].hit()

    def __str__(self):
        string_to_return = ""

        a = [ [str(Square) for Square in self.board[y]] for y in range(len(self.board))]
        label_horizonal = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "h"]
        label_vertical = "|   | " + " | ".join([str(x) for x in range(1,11)]) + " |"

        joined_text = " | ".join(label_horizonal) + "   | "
        line_between = "|" + "".join([ "+" if x%4 == 0  else "-" for x in range(1,len( joined_text)-1)]) +"|\n"
        string_to_return += "-" * len(label_vertical) + "\n"
        string_to_return += label_vertical + "\n"
        string_to_return += line_between
        for i in range(len(a)):
            string_to_return += "| " + label_horizonal[i] + " | " + " | ".join(a[i]) + "  |\n"
            string_to_return += line_between

        return (string_to_return)
