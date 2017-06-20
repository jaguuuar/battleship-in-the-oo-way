from ship import Ship
from square import Square

class Ocean:

    def __init__(self):
        self.board = []

    def build_board(self):
        board_row = []
        for i in range(10):
            for j in range(10):
                square = Square()
                board_row.append(square)

            self.board.append(board_row)
            board_row = []


    def insert_ships(self, start_row, start_column, ship):
        pass

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
        # print("-" * len(label_vertical))
        string_to_return += line_between
        for i in range(len(a)):
            string_to_return += "| " + label_horizonal[i] + " | " + " | ".join(a[i]) + "  |\n"
            string_to_return += line_between

        return (string_to_return)
