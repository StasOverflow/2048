import random
import getch


def receive_character():
    try:
        ch = getch.getch()
    except OverflowError:
        print("Please use EN Layout")
        ch = None
    return ch


class GameBoard:
    cell_row_list = []
    dimension = 0
    number_of_the_game = 3
    arrow = False

    moves = {
        'w': 'Up',
        'W': 'Up',
        'd': 'Right',
        'D': 'Right',
        's': 'Down',
        'S': 'Down',
        'a': 'Left',
        'A': 'Left',
        '\n': 'Enter',
        'q': 'Quit',
        'Q': 'Quit',
        # '\r': "Enter",
    }

    def __init__(self, dimension):
        self.dimension = dimension
        self.cell_row_list = [[self.Cell() for x in range(dimension)] for y in range(dimension)]

    def __repr__(self):
        row_list = []
        for x in self.cell_row_list:
            row = '|\t' + '\t|\t'.join(str(e) for e in x) + '\t|'
            row_list.append(row)
        row_list = ('\n'.join(row_list))
        return row_list

    def _get_random_number(self):
        num = self.number_of_the_game
        seed_1 = random.randint(0, 5)
        seed_2 = random.randint(0, 5)
        if seed_2 == seed_1:
            num = num * num
        return num

    def _fill_random_with_random(self):
        index_list = list()
        for x in range(self.dimension):
            for y in range(self.dimension):
                if self.cell_row_list[x][y].value == 0:
                    index_list.append([x, y])
        print(index_list)
        if index_list:
            print("not yet out")
            rand_cell_index = random.randint(0, len(index_list) - 1)
            value = self._get_random_number()
            x_coord = index_list[rand_cell_index][0]
            y_coord = index_list[rand_cell_index][1]
            self.cell_row_list[x_coord][y_coord].value = value
        else:
            print("vse, net vsobodnih")
        return index_list      # going to be false in case the list will be empty

    def shift_lines(self, array):
        # first, delete all empty elements to shift cells to a border
        print("before ", array)
        new_array = [x for x in array if x.value != 0]
        new_array.extend([self.Cell(0) for x in range(self.dimension - len(new_array))])
        print("after ", new_array)

        # then check for similar cells to multiply
        for x in range(self.dimension):
            if new_array[x].value:
                print("in cell ", x)
                if new_array[x].value == new_array[x+1].value:
                    new_array[x+1].value = new_array[x].value * GameBoard.number_of_the_game
                    new_array.pop(x)
                    new_array.append(self.Cell(0))
                    print("after multiplying", new_array)

        return new_array

    def shift_to_direction(self, move):
        shift_list = [list() for _ in range(self.dimension)]
        if move == 'Up':
            for x in range(self.dimension):
                for y in range(self.dimension):
                    shift_list[x].append(self.cell_row_list[y][x])
            # print("before l ", self.cell_row_list)
            # print("row_list ", shift_list)
            print("moving up")
        elif move == 'Down':
            for y in range(self.dimension):
                for x in reversed(range(self.dimension)):
                    shift_list[y].append(self.cell_row_list[x][y])
            print("moving down")
        elif move == 'Right':
            print("moving right")
        elif move == 'Left':
            print("moving left")
        print("before shifting", shift_list)
        print(self.__repr__())

        shift_row = list()

        for x in range(self.dimension):
            shift_row.append(self.shift_lines(shift_list[x]))

        print("after shifting", shift_row)

        if move == 'Up':
            for y in range(self.dimension):
                for x in range(self.dimension):
                    self.cell_row_list[x][y] = shift_row[y][x]
            # print("before l ", self.cell_row_list)
            # print("row_list ", shift_list)
            print("moving up")
        elif move == 'Down':
            for y in range(self.dimension):
                for x in reversed(range(self.dimension)):
                    self.cell_row_list[(self.dimension-1)-x][y] = shift_row[y][x]
            print(self.cell_row_list)
            print("moving down")
        elif move == 'Right':
            print("moving right")
        elif move == 'Left':
            print("moving left")
                # new_list[x].append(self.cell_row_list[y][x])
        # for x in range(self.dimension):
        #     self.cell_row_list[x][0] = shift_list[x]


    def _proceed_move(self, move):
        if move in self.moves.values():
            if move == 'Enter':
                print("Entering something")
            elif move == 'Quit':
                print("Exiting")
                return 0
            else:
                self.shift_to_direction(move)


    def receive_move(self, ch):
        if ch is not None:
            if ch.encode() == b'[':
                self.arrow = True
            if ch in self.moves:
                if not self.arrow:
                    self._proceed_move(self.moves[ch])
                    self.arrow = False
                    return True
                else:
                    self.arrow = False
        return False


    class Cell:
        value = 0

        def __init__(self, value=0):
            self.value = value

        def __repr__(self):
            return str(self.value)

        def compare(self, cell):
            if self.value == cell.value:
                return True
            else:
                return False

        def merge_with(self, cell):
            # print("comparing ", self.value, "with ", cell.value)
            merged = False
            if self.compare(cell):
                if self.value != 0:
                    self.value = self.value * GameBoard.number_of_the_game
                    merged = True
            elif self.value == 0:
                if cell.value != 0:
                    self.value = cell.value
                    merged = True
            # print("as a result ", self.value)
            return merged


#
# def make_a_move(game_board):
#     game_board.receive_move(receive_character())


def game_session(board_dimension=2):
    board = GameBoard(board_dimension)
    board._fill_random_with_random()
    board._fill_random_with_random()
    playing = True
    while 1:
        if board.receive_move(receive_character()):
            board._fill_random_with_random()
    # while board.shift_to_direction(1):
            print("--------------------------------\nadded random")
            # board._fill_random_with_random()
            print(board)
            # char = getch.getche() # also displayed on the screen
            # x = board.shift_cells(1)
            # print(x)
            # print("after all")
            # print(board)
            print("--------------------------------\n")
    # print("ENDGAME")
    # board.receive_character()

def main():
    game_session(4)


if __name__ == '__main__':
    main()
